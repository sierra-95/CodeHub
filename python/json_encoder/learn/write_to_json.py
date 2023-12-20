#!/usr/bin/env python3
"""write to json"""
import json

# Serializing Python data to JSON
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
with open('test.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file)