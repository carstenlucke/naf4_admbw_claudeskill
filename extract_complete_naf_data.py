#!/usr/bin/env python3
"""
Complete extraction of NAF v4 / ADMBw viewpoints, diagram types, stereotypes, and relationships.
"""

import xml.etree.ElementTree as ET
import json
import re
from collections import defaultdict

def extract_viewpoint_code(name):
    """Extract NAF viewpoint code (e.g., 'C1', 'L4', 'P2', 'S1', 'A2', 'Ar')."""
    match = re.match(r'^([A-Z][0-9a-z]+)\s*[-–]\s*', name)
    return match.group(1) if match else None

def analyze_complete_mdg(file_path):
    """Complete analysis of NAF MDG file."""

    tree = ET.parse(file_path)
    root = tree.getroot()

    results = {
        'viewpoints': {},
        'viewpoint_categories': [],
        'toolboxes': {},
        'model_templates': [],
        'diagram_stereotypes': [],
        'all_stereotypes': defaultdict(list),
        'relationship_types': set(),
        'element_types': set()
    }

    # 1. Extract Diagram Stereotypes (Viewpoints as diagram types)
    for diagram_profile in root.findall('.//DiagramProfile'):
        for stereotype in diagram_profile.findall('.//Stereotype'):
            name = stereotype.get('name', '')
            notes = stereotype.get('notes', '')
            alias = stereotype.get('alias', '')

            # Check if this applies to a diagram
            apply_elem = stereotype.find('.//Apply[@type="Diagram_Custom"]')
            if apply_elem is not None:
                # Extract diagram properties
                props = {}
                for prop in apply_elem.findall('.//Property'):
                    prop_name = prop.get('name', '')
                    prop_value = prop.get('value', '')
                    props[prop_name] = prop_value

                viewpoint_code = extract_viewpoint_code(name)

                diagram_info = {
                    'name': name,
                    'alias': alias,
                    'notes': notes,
                    'code': viewpoint_code,
                    'diagramID': props.get('diagramID', ''),
                    'toolbox': props.get('toolbox', '')
                }

                results['diagram_stereotypes'].append(diagram_info)

                if viewpoint_code:
                    results['viewpoints'][viewpoint_code] = diagram_info

    # 2. Extract Model Templates
    for model in root.findall('.//Model'):
        name = model.get('name', '')
        description = model.get('description', '')
        location = model.get('location', '')
        group_name = model.get('groupName', '')

        viewpoint_code = extract_viewpoint_code(name)

        results['model_templates'].append({
            'name': name,
            'code': viewpoint_code,
            'description': description,
            'location': location,
            'group': group_name
        })

    # 3. Extract Toolboxes and their elements
    for profile in root.findall('.//UMLProfile'):
        doc = profile.find('Documentation')
        if doc is None:
            continue

        profile_name = doc.get('name', '')

        # Skip if not a toolbox profile
        if 'Toolbox' not in profile_name:
            continue

        # Extract viewpoint code from toolbox name (e.g., "NAFv4-ADMBw-A1-Toolbox" -> "A1")
        toolbox_match = re.search(r'-([A-Z][0-9a-z]+)-Toolbox', profile_name)
        if not toolbox_match:
            continue

        viewpoint_code = toolbox_match.group(1)

        toolbox_data = {
            'profile_name': profile_name,
            'pages': []
        }

        # Find all toolbox pages (stereotypes with type="ToolboxPage")
        for stereotype in profile.findall('.//Stereotype'):
            applies_to = stereotype.find('.//Apply[@type="ToolboxPage"]')
            if applies_to is not None:
                page_name = stereotype.get('name', '')
                elements = []

                # Extract all elements (tagged values)
                for tag in stereotype.findall('.//Tag'):
                    tag_name = tag.get('name', '')
                    if 'NAFv4-ADMBw::' in tag_name:
                        # Parse: NAFv4-ADMBw::ElementType(UML::BaseClass)
                        match = re.match(r'NAFv4-ADMBw::(\w+)\(UML::(\w+)\)', tag_name)
                        if match:
                            element_type = match.group(1)
                            uml_base = match.group(2)

                            elements.append({
                                'element_type': element_type,
                                'uml_base': uml_base
                            })

                            results['element_types'].add(element_type)

                            # Track relationships
                            if uml_base in ['Dependency', 'Realization', 'Association', 'Abstraction', 'Usage']:
                                results['relationship_types'].add(element_type)

                if elements:
                    toolbox_data['pages'].append({
                        'page_name': page_name,
                        'elements': elements
                    })

        if toolbox_data['pages']:
            results['toolboxes'][viewpoint_code] = toolbox_data

    # 4. Extract all stereotypes
    for stereotype in root.findall('.//Stereotype'):
        name = stereotype.get('name', '')
        notes = stereotype.get('notes', '')

        # Get base classes
        for apply in stereotype.findall('.//Apply'):
            base_class = apply.get('type', '')
            if base_class and base_class not in ['ToolboxPage', 'Diagram_Custom']:
                results['all_stereotypes'][base_class].append({
                    'name': name,
                    'notes': notes[:200] if notes else ''
                })

    # 5. Extract viewpoint categories
    for profile in root.findall('.//UMLProfile'):
        doc = profile.find('Documentation')
        if doc is None:
            continue

        name = doc.get('name', '')
        notes = doc.get('notes', '')

        if 'Viewpoints' in name and 'Toolbox' not in name and 'DiagramProfile' not in name:
            results['viewpoint_categories'].append({
                'name': name,
                'notes': notes
            })

    return results

def print_results(results):
    """Print comprehensive results."""

    print("=" * 100)
    print("NAF v4 / ADMBw MDG - COMPLETE ANALYSIS")
    print("=" * 100)

    # 1. Viewpoint Categories
    print(f"\n{'=' * 100}")
    print(f"1. VIEWPOINT CATEGORIES ({len(results['viewpoint_categories'])})")
    print(f"{'=' * 100}")
    for cat in results['viewpoint_categories']:
        print(f"\n• {cat['name']}")

    # 2. All Viewpoints (Diagram Types)
    print(f"\n{'=' * 100}")
    print(f"2. NAF v4 VIEWPOINTS / DIAGRAM TYPES ({len(results['viewpoints'])})")
    print(f"{'=' * 100}")

    # Group by prefix
    viewpoint_groups = defaultdict(list)
    for code, vp in results['viewpoints'].items():
        prefix = code[0]
        viewpoint_groups[prefix].append((code, vp))

    group_names = {
        'A': 'Architecture Foundation',
        'C': 'Concept',
        'S': 'Service Specification',
        'L': 'Logical Specification',
        'P': 'Physical Resource Specification',
        'R': 'Requirement'
    }

    for prefix in sorted(viewpoint_groups.keys()):
        print(f"\n{group_names.get(prefix, prefix)}-Series Viewpoints:")
        print("─" * 100)

        for code, vp in sorted(viewpoint_groups[prefix]):
            print(f"\n  {code}: {vp['name']}")
            print(f"      Diagram ID: {vp['diagramID']}")
            print(f"      Toolbox: {vp['toolbox']}")
            if vp['notes']:
                notes = vp['notes'][:150] + '...' if len(vp['notes']) > 150 else vp['notes']
                print(f"      Description: {notes}")

    # 3. Toolboxes and Elements
    print(f"\n{'=' * 100}")
    print(f"3. TOOLBOXES AND AVAILABLE ELEMENTS PER VIEWPOINT ({len(results['toolboxes'])})")
    print(f"{'=' * 100}")

    for code in sorted(results['toolboxes'].keys()):
        vp_name = results['viewpoints'].get(code, {}).get('name', code)
        toolbox = results['toolboxes'][code]

        print(f"\n{code}: {vp_name}")
        print("─" * 100)

        for page in toolbox['pages']:
            print(f"\n  Toolbox Page: {page['page_name']}")

            # Group by UML base
            by_uml = defaultdict(list)
            for elem in page['elements']:
                by_uml[elem['uml_base']].append(elem['element_type'])

            for uml_base in sorted(by_uml.keys()):
                elements = ', '.join(sorted(by_uml[uml_base]))
                print(f"    {uml_base}: {elements}")

    # 4. Summary Statistics
    print(f"\n{'=' * 100}")
    print(f"4. SUMMARY STATISTICS")
    print(f"{'=' * 100}")
    print(f"\nTotal Viewpoints: {len(results['viewpoints'])}")
    print(f"Total Element Types: {len(results['element_types'])}")
    print(f"Total Relationship Types: {len(results['relationship_types'])}")
    print(f"Total Model Templates: {len(results['model_templates'])}")

    # Count by category
    by_category = defaultdict(int)
    for mt in results['model_templates']:
        group = mt['group'].replace('NAFv4-ADMBw ', '')
        by_category[group] += 1

    print(f"\nViewpoints by Category:")
    for cat, count in sorted(by_category.items()):
        print(f"  {cat}: {count}")

    # 5. All Relationship Types
    print(f"\n{'=' * 100}")
    print(f"5. ALL RELATIONSHIP TYPES ({len(results['relationship_types'])})")
    print(f"{'=' * 100}")

    # Group relationships
    groups = defaultdict(list)
    for rel in sorted(results['relationship_types']):
        # Try to categorize
        if any(x in rel for x in ['To', 'For', 'In', 'By', 'From']):
            groups['Relationships'].append(rel)
        else:
            groups['Other'].append(rel)

    for group, rels in groups.items():
        print(f"\n{group}:")
        for rel in rels[:20]:  # Show first 20
            print(f"  - {rel}")
        if len(rels) > 20:
            print(f"  ... and {len(rels) - 20} more")

def main():
    mdg_file = '/home/user/naf4_admbw_claudeskill/mdg/NAFv4-ADMBw-MDG-2024.06.xml'

    results = analyze_complete_mdg(mdg_file)
    print_results(results)

    # Save to JSON
    output_file = '/home/user/naf4_admbw_claudeskill/naf_complete_analysis.json'

    # Convert sets to lists for JSON serialization
    results_json = {
        'viewpoints': results['viewpoints'],
        'viewpoint_categories': results['viewpoint_categories'],
        'toolboxes': results['toolboxes'],
        'model_templates': results['model_templates'],
        'diagram_stereotypes': results['diagram_stereotypes'],
        'all_stereotypes': {k: v[:50] for k, v in results['all_stereotypes'].items()},  # Limit to 50 per base class
        'element_types': sorted(list(results['element_types'])),
        'relationship_types': sorted(list(results['relationship_types']))
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results_json, f, indent=2, ensure_ascii=False)

    print(f"\n{'=' * 100}")
    print(f"Detailed results saved to: {output_file}")
    print(f"{'=' * 100}\n")

if __name__ == '__main__':
    main()
