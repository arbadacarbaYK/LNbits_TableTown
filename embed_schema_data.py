#!/usr/bin/env python3

import json

# Read the JSON data
with open('lnbits_extensions_data.json', 'r') as f:
    schema_data = json.load(f)

# Read the HTML file
with open('lnbits_schema_interactive.html', 'r') as f:
    html_content = f.read()

# Find the position to insert the data
start_marker = "const embeddedSchemaData = {"
end_marker = "// Initialize the visualization"

# Find the start position
start_pos = html_content.find(start_marker)
if start_pos == -1:
    print("Could not find start marker")
    exit(1)

# Find the end position
end_pos = html_content.find(end_marker)
if end_pos == -1:
    print("Could not find end marker")
    exit(1)

# Create the embedded data string (as JavaScript object, not JSON string)
# Remove quotes to make it a JavaScript object instead of a string
embedded_data = json.dumps(schema_data, indent=2)

# Replace the content
new_content = (
    html_content[:start_pos + len(start_marker)] + 
    "\n" + embedded_data + "\n        };\n        \n        // Set schemaData to embedded data\n        schemaData = embeddedSchemaData;\n        \n        " +
    html_content[end_pos:]
)

# Write the updated HTML file
with open('lnbits_schema_interactive.html', 'w') as f:
    f.write(new_content)

print("Successfully embedded schema data into HTML file")