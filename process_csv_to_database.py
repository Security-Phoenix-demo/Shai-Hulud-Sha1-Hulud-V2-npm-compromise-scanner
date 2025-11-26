#!/usr/bin/env python3
"""
5TH WAVE: Process CSV file with all versioned packages.
Parse Book3.csv and update compromised_packages_2025.json with granular versions.
"""

import csv
import json
import re
from datetime import datetime
from collections import defaultdict

def parse_package_version(full_package_str):
    """
    Parse '@package/name@v1.0.0' or 'package@v1.0.0' format
    Returns: (package_name, version)
    """
    if not full_package_str or full_package_str == 'N/A':
        return None, None
    
    # Match: @scope/package@v1.0.0 or package@v1.0.0
    match = re.match(r'(.+?)@v?([\d.]+)', full_package_str)
    if match:
        package_name = match.group(1)
        version = match.group(2)
        return package_name, version
    
    return None, None

def safe_version_sort_key(version):
    """Create a sortable key from version string, handling malformed versions"""
    try:
        parts = version.split('.')
        return [int(x) if x else 0 for x in parts]
    except:
        # For malformed versions, put them at the end
        return [999999, 999999, 999999]

def calculate_safe_version(versions):
    """Calculate safe version (one before first compromised)"""
    if not versions:
        return "unknown - check release history"
    
    # Sort versions to find the earliest
    try:
        sorted_versions = sorted(versions, key=safe_version_sort_key)
        first_ver = sorted_versions[0]
        parts = first_ver.split('.')
        
        if len(parts) >= 3:
            major = int(parts[0]) if parts[0] else 0
            minor = int(parts[1]) if parts[1] else 0
            patch = int(parts[2]) if parts[2] else 0
            
            if patch > 0:
                return f"{major}.{minor}.{patch-1}"
            elif minor > 0:
                return f"{major}.{minor-1}.99"
            elif major > 0:
                return f"{major-1}.99.99"
            return "0.0.0 or avoid"
        elif len(parts) == 2:
            major = int(parts[0]) if parts[0] else 0
            minor = int(parts[1]) if parts[1] else 0
            
            if minor > 0:
                return f"{major}.{minor-1}"
            elif major > 0:
                return f"{major-1}.99"
            return "0.0 or avoid"
        else:
            major = int(parts[0]) if parts[0] else 0
            if major > 0:
                return f"{major-1}"
            return "avoid - no safe version"
    except Exception as e:
        return "check release history manually"

def main():
    print("="*80)
    print("5TH WAVE: Processing CSV with Versioned Packages")
    print("="*80)
    print()
    
    # Load CSV file
    csv_file = 'database-findings/Book3.csv'
    print(f"📂 Reading CSV: {csv_file}")
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return
    
    print(f"   Loaded {len(rows)} rows")
    print()
    
    # Process rows and group by package
    print("🔍 Processing packages and versions...")
    package_versions = defaultdict(list)
    packages_no_version = set()
    
    processed = 0
    skipped = 0
    
    for row in rows:
        # Get package@version from second column
        full_package = None
        for key in row.keys():
            if '@' in row[key] and 'v' in row[key]:
                full_package = row[key]
                break
        
        if not full_package:
            skipped += 1
            continue
        
        package_name, version = parse_package_version(full_package)
        
        if package_name and version:
            package_versions[package_name].append(version)
            processed += 1
        elif package_name:
            packages_no_version.add(package_name)
            processed += 1
        else:
            skipped += 1
    
    print(f"   Processed: {processed} entries")
    print(f"   Skipped: {skipped} entries")
    print(f"   Unique packages with versions: {len(package_versions)}")
    print(f"   Packages without versions: {len(packages_no_version)}")
    print()
    
    # Load existing database
    print("📂 Loading current database...")
    try:
        with open('compromised_packages_2025.json', 'r') as f:
            db = json.load(f)
    except Exception as e:
        print(f"❌ Error loading database: {e}")
        return
    
    print(f"   Current confirmed: {len(db.get('compromised_packages', {}))}")
    print(f"   Current potentially: {len(db.get('potentially_compromised_packages', []))}")
    print()
    
    # Build new database entries
    print("🏗️  Building new database structure...")
    new_confirmed = {}
    
    for package_name, versions in package_versions.items():
        # Remove duplicates and sort
        unique_versions = sorted(set(versions), key=safe_version_sort_key)
        safe_ver = calculate_safe_version(unique_versions)
        
        new_confirmed[package_name] = {
            "compromised_versions": unique_versions,
            "safe_version": safe_ver
        }
    
    new_potentially = sorted(list(packages_no_version))
    
    print(f"   Built {len(new_confirmed)} confirmed entries")
    print(f"   Built {len(new_potentially)} potentially entries")
    print()
    
    # Update database
    print("📝 Updating database structure...")
    db['compromised_packages'] = new_confirmed
    db['potentially_compromised_packages'] = new_potentially
    
    # Update metadata
    db['incident_metadata']['total_packages_confirmed'] = len(new_confirmed)
    db['incident_metadata']['total_packages_potentially_compromised'] = len(new_potentially)
    db['incident_metadata']['total_packages'] = len(new_confirmed) + len(new_potentially)
    db['incident_metadata']['last_update'] = datetime.now().strftime('%Y-%m-%d')
    db['incident_metadata']['version'] = "5.0.0"
    db['incident_metadata']['date'] = datetime.now().strftime('%Y-%m-%d')
    db['incident_metadata']['note'] = "5th Wave: Granular version-specific detection from CSV import. Specific compromised versions with safe version recommendations."
    
    # Save
    print("💾 Saving updated database...")
    with open('compromised_packages_2025.json', 'w') as f:
        json.dump(db, f, indent=2)
    
    print("✅ Database updated successfully!")
    print()
    
    # Generate report
    print("="*80)
    print("📊 5TH WAVE UPDATE COMPLETE")
    print("="*80)
    print()
    print(f"Total packages: {db['incident_metadata']['total_packages']}")
    print(f"Confirmed with specific versions: {len(new_confirmed)}")
    print(f"Potentially (no version info): {len(new_potentially)}")
    print()
    
    # Show examples
    print("📋 Sample Confirmed Packages (with specific versions):")
    for i, (pkg, data) in enumerate(list(new_confirmed.items())[:10]):
        versions_str = ', '.join(data['compromised_versions'][:5])
        if len(data['compromised_versions']) > 5:
            versions_str += f" ... (+{len(data['compromised_versions'])-5} more)"
        print(f"   {i+1}. {pkg}")
        print(f"      Compromised: {versions_str}")
        print(f"      Safe: {data['safe_version']}")
    
    if new_potentially:
        print(f"\n📋 Sample Potentially Compromised (severity 3 - no version):")
        for i, pkg in enumerate(new_potentially[:5]):
            print(f"   {i+1}. {pkg}")
    
    print()
    print("="*80)
    print("🎯 NEXT STEPS")
    print("="*80)
    print()
    print("1. Review compromised_packages_2025.json")
    print("2. Test scanner:")
    print("   python3 enhanced_npm_compromise_detector_phoenix.py test_variations/")
    print()
    print("3. Verify expected behavior:")
    print("   • CRITICAL: Exact version matches")
    print("   • CLEAN (severity 1): Non-compromised versions")
    print("   • POTENTIALLY (severity 3): No version info")
    print()
    print("4. Update documentation with final statistics")
    print()

if __name__ == '__main__':
    main()

