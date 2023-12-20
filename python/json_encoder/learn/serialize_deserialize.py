import json

# Serializing Python data to JSON
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
#converting dictionary to json string
json_string = json.dumps(data)
print(json_string)

# Writing JSON data to a file
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file)

# Deserializing JSON data from a file
#json string to python objects
with open('data.json', 'r', encoding='utf-8') as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)
