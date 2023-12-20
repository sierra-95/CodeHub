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