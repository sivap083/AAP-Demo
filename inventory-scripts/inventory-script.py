import json

# Read the JSON data from the file
with open('json_payload.json', 'r') as json_file:
    inventory_data = json.load(json_file)

# Print the JSON data
print(json.dumps(inventory_data))
