import uuid

# Generate a random UUID (UUID version 4)
random_uuid = uuid.uuid4()
print("Random UUID:", random_uuid)

# Convert UUID to string representation
uuid_str = str(random_uuid)
print("String representation:", uuid_str)

# Convert UUID back to UUID object
uuid_obj = uuid.UUID(uuid_str)
print("UUID object:", uuid_obj)

# Access attributes of UUID object
print("UUID fields:", uuid_obj.fields)
