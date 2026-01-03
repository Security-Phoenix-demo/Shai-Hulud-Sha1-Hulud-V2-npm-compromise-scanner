#!/usr/bin/env python3
"""
5TH WAVE: Process versioned package list with granular version detection.
This creates version-specific compromised package entries instead of "all versions".
"""

import json
import re
import sys
from datetime import datetime
from collections import defaultdict

def parse_package_line(line):
    """Parse: 'package-name (v1.0.0, v1.0.1)' or 'package-name'"""
    line = line.strip()
    if not line or line.startswith('#'):
        return None, []
    
    # Match: package-name (v1.0.0, v1.0.1)
    match = re.match(r'(.+?)\s*\((.+?)\)\s*$', line)
    if match:
        package_name = match.group(1).strip()
        versions_str = match.group(2)
        # Extract versions (handle v prefix, spaces, commas)
        versions = re.findall(r'v?([\d.]+)', versions_str)
        return package_name, versions
    else:
        # Package without version - potentially compromised
        return line, []

def calculate_safe_version(versions):
    """Calculate safe version (one before first compromised)"""
    if not versions:
        return "unknown - check release history"
    
    try:
        first_ver = versions[0]
        parts = first_ver.split('.')
        
        if len(parts) >= 3:
            major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
            if patch > 0:
                return f"{major}.{minor}.{patch-1}"
            elif minor > 0:
                return f"{major}.{minor-1}.99"  
            elif major > 0:
                return f"{major-1}.99.99"
            return "0.0.0 or avoid"
        elif len(parts) == 2:
            major, minor = int(parts[0]), int(parts[1])
            if minor > 0:
                return f"{major}.{minor-1}"
            elif major > 0:
                return f"{major-1}.99"
            return "0.0 or avoid"
        else:
            major = int(parts[0])
            if major > 0:
                return f"{major-1}"
            return "avoid - no safe version"
    except:
        return "check release history manually"

def main():
    print("="*80)
    print("5TH WAVE UPDATE: Granular Version Processing")
    print("="*80)
    print()
    
    # Check for input file
    input_file = 'versioned_packages_input.txt'
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    
    print(f"📂 Reading from: {input_file}")
    
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ Error: {input_file} not found")
        print(f"   Please create it and paste your package list")
        return
    
    # Load existing database
    print("📂 Loading current database...")
    try:
        with open('compromised_packages_2025.json', 'r') as f:
            db = json.load(f)
    except Exception as e:
        print(f"❌ Error loading database: {e}")
        return
    
    print(f"   Current: {len(db['compromised_packages'])} confirmed")
    print(f"   Current: {len(db.get('potentially_compromised_packages', []))} potentially")
    print()
    
    # Process new package list
    print("🔍 Processing versioned package list...")
    new_confirmed = {}
    new_potentially = []
    
    for line in lines:
        pkg_name, versions = parse_package_line(line)
        if pkg_name:
            if versions:
                # Has versions - confirmed compromised
                safe_ver = calculate_safe_version(versions)
                new_confirmed[pkg_name] = {
                    "compromised_versions": versions,
                    "safe_version": safe_ver
                }
            else:
                # No versions - potentially compromised (severity 3)
                new_potentially.append(pkg_name)
    
    print(f"✅ Parsed {len(lines)} lines")
    print(f"   Confirmed (with versions): {len(new_confirmed)}")
    print(f"   Potentially (no versions): {len(new_potentially)}")
    print()
    
    if not new_confirmed and not new_potentially:
        print("⚠️  No packages found in input file")
        print("   Please paste your package list into:", input_file)
        return
    
    # Update database
    print("📝 Updating database...")
    
    # Replace with new data
    db['compromised_packages'] = new_confirmed
    db['potentially_compromised_packages'] = new_potentially
    
    # Update metadata
    db['incident_metadata']['total_packages_confirmed'] = len(new_confirmed)
    db['incident_metadata']['total_packages_potentially_compromised'] = len(new_potentially)
    db['incident_metadata']['total_packages'] = len(new_confirmed) + len(new_potentially)
    db['incident_metadata']['last_update'] = datetime.now().strftime('%Y-%m-%d')
    db['incident_metadata']['version'] = "5.0.0"
    db['incident_metadata']['note'] = "5th Wave: Granular version-specific detection. Packages with specific compromised versions. Potentially compromised packages report as severity 3."
    
    # Save updated database
    print("💾 Saving updated database...")
    with open('compromised_packages_2025.json', 'w') as f:
        json.dump(db, f, indent=2)
    
    print("✅ Database updated successfully!")
    print()
    
    # Generate report
    print("📊 Summary Report:")
    print(f"   Total packages: {db['incident_metadata']['total_packages']}")
    print(f"   Confirmed with versions: {len(new_confirmed)}")
    print(f"   Potentially (no version): {len(new_potentially)}")
    print()
    
    # Show examples
    print("📋 Sample Confirmed Packages:")
    for i, (pkg, data) in enumerate(list(new_confirmed.items())[:5]):
        print(f"\n   {i+1}. {pkg}")
        print(f"      Compromised: {', '.join(data['compromised_versions'])}")
        print(f"      Safe: {data['safe_version']}")
    
    if new_potentially:
        print(f"\n📋 Sample Potentially Compromised (severity 3):")
        for i, pkg in enumerate(new_potentially[:5]):
            print(f"   {i+1}. {pkg}")
    
    print()
    print("="*80)
    print("✅ 5TH WAVE UPDATE COMPLETE")
    print("="*80)
    print()
    print("Next steps:")
    print("1. Review compromised_packages_2025.json")
    print("2. Test scanner: python3 enhanced_npm_compromise_detector_phoenix.py test_variations/")
    print("3. Update documentation with new statistics")
    print("4. Commit changes")

if __name__ == '__main__':
    main()





