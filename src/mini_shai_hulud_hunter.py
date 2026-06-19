#!/usr/bin/env python3
"""
Mini Shai-Hulud Hunter
======================

Searches GitHub for the "A Mini Shai-Hulud has Appeared" indicator-of-compromise
(IOC) left behind by the 6th-wave "Mini" Shai-Hulud npm supply-chain worm, then
cross-references the compromised GitHub accounts/repos against package managers
(npm) and the local compromised-package database.

The Mini Shai-Hulud worm creates Dune-themed exfiltration repositories on a
victim's GitHub account (e.g. `victim/kralizec-sietch-906`) whose description /
content is "A Mini Shai-Hulud has Appeared". The *owner* of such a repo is the
compromised account; this tool finds those accounts and asks: do they publish
npm packages, and are any of those packages already in our compromised DB?

Cross-reference confidence levels
---------------------------------
  confirmed : the npm package name appears in compromised_packages_2025.json
  strong    : npm package discovered via a found repo's package.json `repository`
  weak      : npm package found by matching GitHub login == npm maintainer name
              (heuristic - logins and npm handles often differ)

Auth
----
GitHub token is resolved in priority order (token value is never printed/saved):
  1. GITHUB_TOKEN / GH_TOKEN environment variable
  2. [phoenix] github_token in the .config file
  3. `gh auth token` (GitHub CLI), if installed and logged in
Description/commit search works unauthenticated (low rate limit); code search
*requires* authentication.

Stdlib only - no external dependencies (urllib, configparser, json).
"""

import argparse
import base64
import configparser
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

DEFAULT_MARKER = "A Mini Shai-Hulud has Appeared"
DEFAULT_SINCE = "2025-09-01"  # First Shai-Hulud wave; nothing meaningful before this.
GITHUB_API = "https://api.github.com"
NPM_REGISTRY = "https://registry.npmjs.org"
USER_AGENT = "Shai-Halud-Mini-Hunter/1.0"
SEARCH_RESULT_CAP = 1000  # Hard GitHub Search API cap, per query.


# --------------------------------------------------------------------------- #
# Auth / config
# --------------------------------------------------------------------------- #
def _validate_token(token):
    """Return True if the token authenticates against the GitHub API."""
    if not token or token == "your_github_token_here":
        return False
    try:
        req = urllib.request.Request(
            f"{GITHUB_API}/rate_limit",
            headers={"Authorization": f"token {token}", "User-Agent": USER_AGENT},
        )
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except urllib.error.HTTPError:
        return False
    except Exception:
        return False


def resolve_github_token(config_path):
    """Resolve a working GitHub token, never printing its value."""
    # 1. Environment
    for env in ("GITHUB_TOKEN", "GH_TOKEN"):
        tok = os.getenv(env)
        if tok and _validate_token(tok.strip()):
            print(f"🔗 Using GitHub token from ${env}")
            return tok.strip()
        if tok:
            print(f"⚠️  ${env} is set but failed authentication - trying next source")

    # 2. .config [phoenix] github_token
    if os.path.exists(config_path):
        try:
            parser = configparser.ConfigParser()
            parser.read(config_path)
            if "phoenix" in parser:
                sec = parser["phoenix"]
                tok = (sec.get("github_token") or sec.get("Github_token")
                       or sec.get("GITHUB_TOKEN") or "").strip()
                if tok and _validate_token(tok):
                    print(f"🔗 Using GitHub token from {config_path}")
                    return tok
                if tok:
                    print(f"⚠️  github_token in {config_path} failed auth "
                          "(expired/revoked?) - trying GitHub CLI")
        except Exception as e:
            print(f"⚠️  Could not read {config_path}: {e}")

    # 3. gh CLI
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True,
                             text=True, timeout=15)
        tok = out.stdout.strip()
        if out.returncode == 0 and tok and _validate_token(tok):
            print("🔗 Using GitHub token from `gh auth token`")
            return tok
    except (FileNotFoundError, subprocess.SubprocessError):
        pass

    print("💡 No working GitHub token found. Description/commit search will run "
          "unauthenticated (low rate limit); code search will be skipped.")
    return None


# --------------------------------------------------------------------------- #
# HTTP helpers (with rate-limit handling)
# --------------------------------------------------------------------------- #
class GitHub:
    def __init__(self, token, verbose=False):
        self.token = token
        self.verbose = verbose

    def _headers(self, accept="application/vnd.github+json"):
        h = {"Accept": accept, "User-Agent": USER_AGENT}
        if self.token:
            h["Authorization"] = f"token {self.token}"
        return h

    def get(self, url, accept="application/vnd.github+json", _retries=4):
        """GET with primary/secondary rate-limit backoff. Returns (status, headers, body)."""
        for attempt in range(_retries):
            try:
                req = urllib.request.Request(url, headers=self._headers(accept))
                with urllib.request.urlopen(req, timeout=30) as r:
                    return r.status, dict(r.headers), json.load(r)
            except urllib.error.HTTPError as e:
                hdr = dict(e.headers)
                # Secondary rate limit
                if e.code in (403, 429):
                    retry_after = hdr.get("Retry-After")
                    remaining = hdr.get("X-RateLimit-Remaining")
                    if retry_after:
                        wait = int(retry_after) + 1
                    elif remaining == "0":
                        reset = int(hdr.get("X-RateLimit-Reset", "0"))
                        wait = max(1, reset - int(time.time()) + 1)
                    else:
                        wait = 2 ** attempt + 1
                    wait = min(wait, 90)
                    if self.verbose:
                        print(f"   ⏳ rate limited ({e.code}); sleeping {wait}s")
                    time.sleep(wait)
                    continue
                try:
                    body = json.loads(e.read().decode())
                except Exception:
                    body = {}
                return e.code, hdr, body
            except Exception as e:
                if attempt == _retries - 1:
                    return 0, {}, {"message": str(e)}
                time.sleep(2 ** attempt)
        return 0, {}, {"message": "exhausted retries"}

    def _respect_remaining(self, headers):
        """Sleep if we're about to hit the search rate limit (search resets per-minute)."""
        try:
            remaining = int(headers.get("X-RateLimit-Remaining", "99"))
            reset = int(headers.get("X-RateLimit-Reset", "0"))
        except (TypeError, ValueError):
            return
        if remaining <= 1 and reset:
            wait = max(1, reset - int(time.time()) + 1)
            if self.verbose:
                print(f"   ⏳ search budget exhausted; sleeping {wait}s")
            time.sleep(min(wait, 90))

    def search_paged(self, endpoint, query, accept="application/vnd.github+json",
                     label=""):
        """Page through a search endpoint up to the 1000-result cap.

        Returns (items, total_count). Logs loudly if total_count > cap.
        """
        items = []
        page = 1
        total_count = None
        while True:
            q = urllib.parse.quote(query)
            url = f"{GITHUB_API}/search/{endpoint}?q={q}&per_page=100&page={page}"
            status, headers, body = self.get(url, accept=accept)
            if status != 200:
                msg = body.get("message", "") if isinstance(body, dict) else body
                print(f"   ⚠️  {label} search error {status}: {msg}")
                break
            total_count = body.get("total_count", 0)
            batch = body.get("items", [])
            items.extend(batch)
            if len(items) >= total_count or not batch or len(items) >= SEARCH_RESULT_CAP:
                break
            page += 1
            self._respect_remaining(headers)
        return items, (total_count or 0)


# --------------------------------------------------------------------------- #
# Search strategies
# --------------------------------------------------------------------------- #
def _date_ranges_bisect(gh, marker, start, end, label, verbose):
    """Recursively split [start, end] created-date ranges so each query stays
    under the 1000-result cap, returning all repository items."""
    query = f'"{marker}" in:description created:{start}..{end}'
    # Cheap count probe (per_page=1)
    q = urllib.parse.quote(query)
    status, headers, body = gh.get(f"{GITHUB_API}/search/repositories?q={q}&per_page=1")
    if status != 200:
        print(f"   ⚠️  range {start}..{end} probe error {status}")
        return []
    total = body.get("total_count", 0)
    if total == 0:
        return []
    if total <= SEARCH_RESULT_CAP:
        items, _ = gh.search_paged("repositories", query, label=f"{label} {start}..{end}")
        if verbose:
            print(f"   • {start}..{end}: {len(items)} repos")
        return items
    # Too many - bisect by date
    sd = datetime.strptime(start, "%Y-%m-%d")
    ed = datetime.strptime(end, "%Y-%m-%d")
    if (ed - sd).days <= 1:
        # Cannot split further; take what we can and warn.
        items, _ = gh.search_paged("repositories", query, label=f"{label} {start}..{end}")
        print(f"   ⚠️  {start}..{end} has {total} results but day is indivisible; "
              f"capturing first {len(items)} (UNDERCOUNT).")
        return items
    mid = sd + (ed - sd) / 2
    mid_s = mid.strftime("%Y-%m-%d")
    next_day = (datetime.strptime(mid_s, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
    left = _date_ranges_bisect(gh, marker, start, mid_s, label, verbose)
    right = _date_ranges_bisect(gh, marker, next_day, end, label, verbose)
    return left + right


def search_descriptions(gh, marker, since, verbose):
    """Primary signal: repos whose description contains the marker.
    Partitions by created-date to defeat the 1000-result cap."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"🔎 [descriptions] searching repos with description ~ {marker!r} "
          f"(created {since}..{today})")
    items = _date_ranges_bisect(gh, marker, since, today, "descriptions", verbose)
    out = []
    for it in items:
        owner = it.get("owner", {}) or {}
        out.append({
            "full_name": it.get("full_name"),
            "owner": owner.get("login"),
            "owner_type": owner.get("type"),
            "html_url": it.get("html_url"),
            "description": it.get("description"),
            "default_branch": it.get("default_branch"),
            "created_at": it.get("created_at"),
            "source": "description",
        })
    print(f"   ✅ {len(out)} IOC repositories via description")
    return out


def search_code(gh, marker, verbose):
    """Secondary (noisy) signal: the marker string inside files. Requires auth.
    NOTE: also matches detection tools / research repos that merely *mention* the
    string, so these are lower confidence and flagged is_possible_research."""
    if not gh.token:
        print("⚠️  [code] skipped - requires authentication")
        return []
    print(f"🔎 [code] searching file contents for {marker!r}")
    items, total = gh.search_paged("code", f'"{marker}"', label="code")
    if total > len(items):
        print(f"   ⚠️  retrieved {len(items)} of {total} (cap/limit)")
    out = []
    for it in items:
        repo = it.get("repository", {}) or {}
        owner = repo.get("owner", {}) or {}
        name = (repo.get("full_name") or "").lower()
        out.append({
            "full_name": repo.get("full_name"),
            "owner": owner.get("login"),
            "owner_type": owner.get("type"),
            "html_url": it.get("html_url"),
            "path": it.get("path"),
            "source": "code",
            "is_possible_research": any(k in name for k in
                                        ("detect", "scan", "guard", "shai-hulud",
                                         "security", "hunter", "verifier", "ioc")),
        })
    print(f"   ✅ {len(out)} code hits (some may be detection/research repos)")
    return out


def search_commits(gh, marker, verbose):
    """Secondary signal: marker in commit messages."""
    print(f"🔎 [commits] searching commit messages for {marker!r}")
    items, total = gh.search_paged(
        "commits", f'"{marker}"',
        accept="application/vnd.github.cloak-preview+json", label="commits")
    out = []
    for it in items:
        repo = it.get("repository", {}) or {}
        owner = repo.get("owner", {}) or {}
        name = (repo.get("full_name") or "").lower()
        out.append({
            "full_name": repo.get("full_name"),
            "owner": owner.get("login"),
            "owner_type": owner.get("type"),
            "html_url": it.get("html_url"),
            "source": "commit",
            "is_possible_research": any(k in name for k in
                                        ("detect", "scan", "guard", "shai-hulud",
                                         "security", "hunter", "verifier", "ioc")),
        })
    print(f"   ✅ {len(out)} commit hits")
    return out


# --------------------------------------------------------------------------- #
# Cross-reference
# --------------------------------------------------------------------------- #
def load_compromised_db(path):
    if not os.path.exists(path):
        print(f"⚠️  compromised DB not found at {path}; skipping DB match")
        return {}, []
    try:
        with open(path) as f:
            data = json.load(f)
        comp = data.get("compromised_packages", {}) or {}
        pot = data.get("potentially_compromised_packages", []) or []
        pot_names = [p.get("name") if isinstance(p, dict) else p for p in pot]
        print(f"📚 Loaded compromised DB: {len(comp)} confirmed, {len(pot_names)} potential")
        return comp, pot_names
    except Exception as e:
        print(f"⚠️  Could not parse compromised DB: {e}")
        return {}, []


def npm_get(path, retries=3):
    """GET JSON from the npm registry, retrying transient failures."""
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(f"{NPM_REGISTRY}{path}",
                                         headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None  # genuinely absent; don't retry
            last = e
        except Exception as e:
            last = e
        time.sleep(1.5 * (attempt + 1))
    return None


def npm_packages_for_maintainer(login):
    """Weak-confidence: npm packages whose maintainer handle == GitHub login."""
    data = npm_get(f"/-/v1/search?text=maintainer:{urllib.parse.quote(login)}&size=250")
    if not data:
        return []
    pkgs = []
    for obj in data.get("objects", []):
        pkg = obj.get("package", {})
        maints = [m.get("username") for m in pkg.get("maintainers", []) if isinstance(m, dict)]
        if login.lower() in [m.lower() for m in maints if m]:
            pkgs.append(pkg.get("name"))
    return sorted(set(p for p in pkgs if p))


def fetch_package_json(gh, full_name, default_branch):
    """Strong-confidence: read package.json from the IOC repo (often absent)."""
    branch = default_branch or "main"
    status, _, body = gh.get(
        f"{GITHUB_API}/repos/{full_name}/contents/package.json?ref={branch}")
    if status != 200 or not isinstance(body, dict):
        return None
    try:
        content = base64.b64decode(body.get("content", "")).decode("utf-8", "replace")
        pkg = json.loads(content)
        return {"name": pkg.get("name"), "version": pkg.get("version")}
    except Exception:
        return None


def cross_reference(gh, repos, comp_db, pot_names, do_npm, do_scan,
                    npm_limit, verbose):
    """Build the per-account cross-reference."""
    # Dedup owners (keeping each owner's repos)
    accounts = {}
    for r in repos:
        login = r.get("owner")
        if not login:
            continue
        acc = accounts.setdefault(login, {
            "login": login, "type": r.get("owner_type"),
            "repos": [], "npm_packages": [],
        })
        acc["repos"].append({"full_name": r.get("full_name"),
                             "source": r.get("source"),
                             "html_url": r.get("html_url"),
                             "is_possible_research": r.get("is_possible_research", False)})

    comp_lower = {k.lower(): k for k in comp_db}
    pot_lower = {p.lower(): p for p in pot_names if p}

    def classify(pkg_name):
        ln = (pkg_name or "").lower()
        if ln in comp_lower:
            return "confirmed_compromised", comp_db[comp_lower[ln]]
        if ln in pot_lower:
            return "potentially_compromised", None
        return "not_in_db", None

    # 2. Scan IOC repos' package.json (strong link)
    if do_scan:
        print(f"🔬 Scanning {len(repos)} IOC repos for package.json ...")
        seen = set()
        for r in repos:
            fn = r.get("full_name")
            if not fn or fn in seen:
                continue
            seen.add(fn)
            pj = fetch_package_json(gh, fn, r.get("default_branch"))
            if pj and pj.get("name"):
                status, db = classify(pj["name"])
                accounts[r["owner"]]["npm_packages"].append({
                    "name": pj["name"], "confidence": "strong",
                    "source": "repo package.json", "db_status": status,
                    "db_detail": db,
                })

    # 3. npm maintainer lookup (weak link)
    if do_npm:
        logins = list(accounts.keys())
        if npm_limit and len(logins) > npm_limit:
            print(f"⚠️  {len(logins)} unique accounts; npm-checking first {npm_limit} "
                  f"(use --npm-limit 0 for all). {len(logins) - npm_limit} skipped.")
            logins = logins[:npm_limit]
        print(f"📦 npm maintainer lookup for {len(logins)} accounts ...")
        for i, login in enumerate(logins, 1):
            for name in npm_packages_for_maintainer(login):
                existing = [p["name"] for p in accounts[login]["npm_packages"]]
                if name in existing:
                    continue
                status, db = classify(name)
                accounts[login]["npm_packages"].append({
                    "name": name, "confidence": "weak",
                    "source": f"npm maintainer:{login}", "db_status": status,
                    "db_detail": db,
                })
            if verbose and i % 25 == 0:
                print(f"   ... {i}/{len(logins)}")
            time.sleep(0.1)  # be polite to npm registry

    return accounts


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #
def build_report(marker, accounts, repos):
    confirmed, potential = [], []
    for acc in accounts.values():
        for p in acc["npm_packages"]:
            row = {"account": acc["login"], "package": p["name"],
                   "confidence": p["confidence"], "source": p["source"],
                   "db_detail": p.get("db_detail")}
            if p["db_status"] == "confirmed_compromised":
                confirmed.append(row)
            elif p["db_status"] == "potentially_compromised":
                potential.append(row)
    sources = {}
    for r in repos:
        sources[r["source"]] = sources.get(r["source"], 0) + 1
    return {
        "metadata": {
            "tool": "mini_shai_hulud_hunter",
            "marker": marker,
            "generated_at": datetime.now(timezone.utc).isoformat(),
        },
        "summary": {
            "ioc_repositories": len(repos),
            "unique_accounts": len(accounts),
            "results_by_source": sources,
            "npm_packages_linked": sum(len(a["npm_packages"]) for a in accounts.values()),
            "confirmed_compromised_packages": len(confirmed),
            "potentially_compromised_packages": len(potential),
        },
        "confirmed_db_matches": confirmed,
        "potential_db_matches": potential,
        "accounts": list(accounts.values()),
        "ioc_repositories": repos,
    }


def print_summary(report):
    s = report["summary"]
    print("\n" + "=" * 64)
    print("🐛  MINI SHAI-HULUD HUNT - SUMMARY")
    print("=" * 64)
    print(f"  IOC repositories found      : {s['ioc_repositories']}")
    print(f"  Unique GitHub accounts      : {s['unique_accounts']}")
    print(f"  Results by source           : {s['results_by_source']}")
    print(f"  npm packages linked         : {s['npm_packages_linked']}")
    print(f"  ⚠️  CONFIRMED compromised pkgs : {s['confirmed_compromised_packages']}")
    print(f"  ⚠️  Potentially compromised    : {s['potentially_compromised_packages']}")
    if report["confirmed_db_matches"]:
        print("\n  🔴 CONFIRMED matches (package in compromised DB):")
        for m in report["confirmed_db_matches"][:50]:
            print(f"     - {m['package']}  (account {m['account']}, "
                  f"{m['confidence']} link via {m['source']})")
    print("=" * 64)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(
        description="Hunt the 'A Mini Shai-Hulud has Appeared' IOC and cross-"
                    "reference compromised GitHub accounts to npm packages.")
    ap.add_argument("--config", default=".config", help="Path to .config (default: .config)")
    ap.add_argument("--marker", default=DEFAULT_MARKER, help="IOC marker string to search")
    ap.add_argument("--since", default=DEFAULT_SINCE,
                    help="Earliest repo created-date for description partitioning")
    ap.add_argument("--sources", default="description,code,commits",
                    help="Comma list: description,code,commits")
    ap.add_argument("--db", default="compromised_packages_2025.json",
                    help="Path to compromised-package database")
    ap.add_argument("--output", default="results/mini-shai-hulud",
                    help="Output directory for the JSON report")
    ap.add_argument("--no-npm", action="store_true", help="Skip npm maintainer lookups")
    ap.add_argument("--no-scan", action="store_true", help="Skip scanning repo package.json")
    ap.add_argument("--no-db", action="store_true", help="Skip local DB cross-reference")
    ap.add_argument("--npm-limit", type=int, default=250,
                    help="Max unique accounts for npm lookup (0 = unlimited)")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    # Resolve config path relative to repo root if not found as-is.
    config_path = args.config
    if not os.path.exists(config_path):
        alt = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           args.config)
        if os.path.exists(alt):
            config_path = alt

    token = resolve_github_token(config_path)
    gh = GitHub(token, verbose=args.verbose)
    sources = [s.strip() for s in args.sources.split(",") if s.strip()]

    repos = []
    if "description" in sources:
        repos += search_descriptions(gh, args.marker, args.since, args.verbose)
    if "code" in sources:
        repos += search_code(gh, args.marker, args.verbose)
    if "commits" in sources:
        repos += search_commits(gh, args.marker, args.verbose)

    if not repos:
        print("\n❌ No IOC results found (check token / marker / network).")
        return 1

    comp_db, pot_names = ({}, [])
    if not args.no_db:
        db_path = args.db if os.path.exists(args.db) else os.path.join(
            os.path.dirname(config_path), args.db)
        comp_db, pot_names = load_compromised_db(db_path)

    accounts = cross_reference(
        gh, repos, comp_db, pot_names,
        do_npm=not args.no_npm, do_scan=not args.no_scan,
        npm_limit=(None if args.npm_limit == 0 else args.npm_limit),
        verbose=args.verbose)

    report = build_report(args.marker, accounts, repos)
    print_summary(report)

    os.makedirs(args.output, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    out_path = os.path.join(args.output, f"mini_shai_hulud_hunt_{stamp}.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\n💾 Report written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
