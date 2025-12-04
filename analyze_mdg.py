#!/usr/bin/env python3
"""
Analyze NAF v4 MDG file to extract viewpoints, diagram types, stereotypes, and relationship types.
"""

import xml.etree.ElementTree as ET
import json
from collections import defaultdict

def analyze_mdg(file_path):
    """Parse and analyze the MDG XML file."""

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    results = {
        'diagram_profiles': [],
        'stereotypes': defaultdict(list),
        'viewpoints': [],
        'uml_profiles': []
    }

    # Find all DiagramProfile elements
    for diagram_profile in root.findall('.//DiagramProfile'):
        name = diagram_profile.get('name', '')
        notes = diagram_profile.get('notes', '')
        diagram_type = diagram_profile.get('type', '')

        if name:
            results['diagram_profiles'].append({
                'name': name,
                'notes': notes,
                'type': diagram_type
            })

    # Find all Stereotype elements
    for stereotype in root.findall('.//Stereotype'):
        name = stereotype.get('name', '')
        notes = stereotype.get('notes', '')
        base_class = stereotype.get('baseClass', '')

        if name:
            results['stereotypes'][base_class].append({
                'name': name,
                'notes': notes
            })

    # Find all UMLProfile elements
    for profile in root.findall('.//UMLProfile'):
        name = profile.get('name', '')
        notes = profile.get('notes', '')

        if name:
            results['uml_profiles'].append({
                'name': name,
                'notes': notes
            })

    # Look for viewpoint information in notes
    for elem in root.iter():
        notes = elem.get('notes', '')
        if 'viewpoint' in notes.lower():
            name = elem.get('name', '')
            if name and name not in [vp['name'] for vp in results['viewpoints']]:
                results['viewpoints'].append({
                    'name': name,
                    'notes': notes[:200]  # First 200 chars
                })

    return results

def main():
    mdg_file = '/home/user/naf4_admbw_claudeskill/mdg/NAFv4-ADMBw-MDG-2024.06.xml'

    print("Analyzing NAF v4 MDG file...")
    results = analyze_mdg(mdg_file)

    print(f"\n=== DIAGRAM PROFILES (Total: {len(results['diagram_profiles'])}) ===")
    for dp in sorted(results['diagram_profiles'], key=lambda x: x['name']):
        print(f"\n{dp['name']}")
        if dp['type']:
            print(f"  Type: {dp['type']}")
        if dp['notes']:
            print(f"  Notes: {dp['notes'][:150]}...")

    print(f"\n\n=== UML PROFILES (Total: {len(results['uml_profiles'])}) ===")
    for profile in results['uml_profiles']:
        print(f"\n{profile['name']}")
        if profile['notes']:
            print(f"  Notes: {profile['notes'][:150]}...")

    print(f"\n\n=== STEREOTYPES BY BASE CLASS (Total base classes: {len(results['stereotypes'])}) ===")
    for base_class, stereotypes in sorted(results['stereotypes'].items()):
        print(f"\n{base_class} ({len(stereotypes)} stereotypes):")
        for st in stereotypes[:10]:  # Show first 10
            print(f"  - {st['name']}")
        if len(stereotypes) > 10:
            print(f"  ... and {len(stereotypes) - 10} more")

    print(f"\n\n=== VIEWPOINT REFERENCES (Total: {len(results['viewpoints'])}) ===")
    for vp in results['viewpoints'][:20]:  # Show first 20
        print(f"\n{vp['name']}")
        print(f"  {vp['notes']}")

    # Save detailed results to JSON
    output_file = '/home/user/naf4_admbw_claudeskill/mdg_analysis.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        # Convert defaultdict to dict for JSON serialization
        results['stereotypes'] = dict(results['stereotypes'])
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n\nDetailed results saved to: {output_file}")

if __name__ == '__main__':
    main()
