#!/usr/bin/env python3
"""
Comprehensive analysis of NAF v4 MDG file to extract:
- All viewpoints and their descriptions
- Diagram types and toolboxes
- Stereotypes mapped to viewpoints
- Element types and relationships
"""

import xml.etree.ElementTree as ET
import json
import re
from collections import defaultdict

def extract_viewpoint_code(name):
    """Extract NAF viewpoint code (e.g., 'C1', 'L4', 'P2', 'S1', 'A2', 'Ar')."""
    match = re.match(r'^([A-Z][0-9a-z])\s*[-–]\s*', name)
    return match.group(1) if match else None

def analyze_naf_mdg(file_path):
    """Parse and comprehensively analyze the NAF MDG XML file."""

    tree = ET.parse(file_path)
    root = tree.getroot()

    results = {
        'viewpoints': {},
        'diagram_profiles': [],
        'toolboxes': defaultdict(list),
        'stereotypes_by_baseclass': defaultdict(list),
        'stereotypes_by_toolbox': defaultdict(list),
        'viewpoint_categories': [],
        'all_element_types': set(),
        'relationship_types': set()
    }

    # Extract viewpoint information from UMLProfile Documentation
    for profile in root.findall('.//UMLProfile'):
        doc = profile.find('Documentation')
        if doc is not None:
            name = doc.get('name', '')
            notes = doc.get('notes', '')

            # Check if this is a viewpoint category
            if 'Viewpoints' in name:
                results['viewpoint_categories'].append({
                    'name': name,
                    'notes': notes
                })

            # Check if this is a specific viewpoint toolbox
            viewpoint_code = extract_viewpoint_code(name)
            if viewpoint_code:
                # Find all toolbox pages (stereotypes with ToolboxPage)
                for stereotype in profile.findall('.//Stereotype'):
                    applies_to = stereotype.find('.//Apply[@type="ToolboxPage"]')
                    if applies_to is not None:
                        toolbox_name = stereotype.get('name', '')
                        tagged_values = []

                        # Extract all tagged values (element types and relationships)
                        for tag in stereotype.findall('.//Tag'):
                            tag_name = tag.get('name', '')
                            if 'NAFv4-ADMBw::' in tag_name:
                                # Parse the tag to extract element type and UML base
                                match = re.match(r'NAFv4-ADMBw::(\w+)\(UML::(\w+)\)', tag_name)
                                if match:
                                    element_type = match.group(1)
                                    uml_base = match.group(2)
                                    tagged_values.append({
                                        'element_type': element_type,
                                        'uml_base': uml_base
                                    })

                                    results['all_element_types'].add(element_type)

                                    # Identify relationships (Dependency, Realization, etc.)
                                    if uml_base in ['Dependency', 'Realization', 'Association', 'Abstraction']:
                                        results['relationship_types'].add(element_type)

                        if tagged_values:
                            results['toolboxes'][viewpoint_code].append({
                                'toolbox_name': toolbox_name,
                                'elements': tagged_values
                            })

                            # Also store stereotypes by toolbox
                            for tv in tagged_values:
                                results['stereotypes_by_toolbox'][viewpoint_code].append(tv['element_type'])

                # Store viewpoint info
                if viewpoint_code and viewpoint_code not in results['viewpoints']:
                    results['viewpoints'][viewpoint_code] = {
                        'code': viewpoint_code,
                        'full_name': name,
                        'notes': notes,
                        'profile_id': doc.get('id', ''),
                        'version': doc.get('version', '')
                    }

    # Extract all stereotypes
    for stereotype in root.findall('.//Stereotype'):
        name = stereotype.get('name', '')
        notes = stereotype.get('notes', '')

        # Get base class(es)
        for apply in stereotype.findall('.//Apply'):
            base_class = apply.get('type', '')
            if base_class and base_class != 'ToolboxPage':
                results['stereotypes_by_baseclass'][base_class].append({
                    'name': name,
                    'notes': notes
                })

    return results

def main():
    mdg_file = '/home/user/naf4_admbw_claudeskill/mdg/NAFv4-ADMBw-MDG-2024.06.xml'

    print("=" * 80)
    print("NAF v4 / ADMBw MDG COMPREHENSIVE ANALYSIS")
    print("=" * 80)

    results = analyze_naf_mdg(mdg_file)

    # 1. Viewpoint Categories
    print(f"\n{'='*80}")
    print(f"1. VIEWPOINT CATEGORIES (Total: {len(results['viewpoint_categories'])})")
    print(f"{'='*80}")
    for cat in results['viewpoint_categories']:
        print(f"\n{cat['name']}")
        if cat['notes']:
            print(f"  {cat['notes']}")

    # 2. All Viewpoints
    print(f"\n{'='*80}")
    print(f"2. NAF v4 VIEWPOINTS (Total: {len(results['viewpoints'])})")
    print(f"{'='*80}")

    # Group by prefix
    viewpoint_groups = defaultdict(list)
    for vp_code, vp_data in results['viewpoints'].items():
        prefix = vp_code[0]
        viewpoint_groups[prefix].append((vp_code, vp_data))

    for prefix in sorted(viewpoint_groups.keys()):
        print(f"\n{prefix}-Series Viewpoints:")
        for vp_code, vp_data in sorted(viewpoint_groups[prefix]):
            print(f"\n  {vp_code}: {vp_data['full_name']}")
            if vp_data['notes']:
                # Truncate long notes
                notes = vp_data['notes'][:200] + '...' if len(vp_data['notes']) > 200 else vp_data['notes']
                print(f"      {notes}")

    # 3. Toolboxes and Elements per Viewpoint
    print(f"\n{'='*80}")
    print(f"3. TOOLBOXES AND ELEMENTS PER VIEWPOINT")
    print(f"{'='*80}")

    for vp_code in sorted(results['toolboxes'].keys()):
        vp_name = results['viewpoints'].get(vp_code, {}).get('full_name', vp_code)
        print(f"\n{vp_code}: {vp_name}")
        print(f"{'─'*80}")

        for toolbox in results['toolboxes'][vp_code]:
            print(f"\n  Toolbox: {toolbox['toolbox_name']}")
            print(f"  Elements ({len(toolbox['elements'])}):")

            # Group by UML base
            by_uml_base = defaultdict(list)
            for elem in toolbox['elements']:
                by_uml_base[elem['uml_base']].append(elem['element_type'])

            for uml_base in sorted(by_uml_base.keys()):
                elements = ', '.join(sorted(by_uml_base[uml_base]))
                print(f"    {uml_base}: {elements}")

    # 4. Summary Statistics
    print(f"\n{'='*80}")
    print(f"4. SUMMARY STATISTICS")
    print(f"{'='*80}")
    print(f"\nTotal Viewpoints: {len(results['viewpoints'])}")
    print(f"Total Unique Element Types: {len(results['all_element_types'])}")
    print(f"Total Relationship Types: {len(results['relationship_types'])}")
    print(f"Total UML Base Classes with Stereotypes: {len(results['stereotypes_by_baseclass'])}")

    # 5. All Relationship Types
    print(f"\n{'='*80}")
    print(f"5. RELATIONSHIP TYPES (Total: {len(results['relationship_types'])})")
    print(f"{'='*80}")
    for rel_type in sorted(results['relationship_types']):
        print(f"  - {rel_type}")

    # Save detailed JSON
    output_file = '/home/user/naf4_admbw_claudeskill/naf_viewpoints_analysis.json'

    # Convert sets to lists for JSON serialization
    results_serializable = {
        'viewpoints': results['viewpoints'],
        'viewpoint_categories': results['viewpoint_categories'],
        'toolboxes': dict(results['toolboxes']),
        'stereotypes_by_baseclass': dict(results['stereotypes_by_baseclass']),
        'stereotypes_by_toolbox': dict(results['stereotypes_by_toolbox']),
        'all_element_types': sorted(list(results['all_element_types'])),
        'relationship_types': sorted(list(results['relationship_types']))
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results_serializable, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*80}")
    print(f"Detailed results saved to: {output_file}")
    print(f"{'='*80}\n")

if __name__ == '__main__':
    main()
