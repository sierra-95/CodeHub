import json

# Custom data type
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object with custom data types
person = Person("Bob", 35)

# Defining a custom JSON encoder class
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age}
        return super().default(obj)

# Serializing the custom object using the custom encoder
json_string = json.dumps(person, cls=CustomEncoder)
print(json_string)

# Now, let's deserialize it using an object_hook
def custom_object_hook(obj):
    if 'name' in obj and 'age' in obj:
        return Person(obj['name'], obj['age'])
    return obj

json_data = '{"name": "Alice", "age": 28}'
custom_person = json.loads(json_data, object_hook=custom_object_hook)
print(custom_person.name, custom_person.age)

