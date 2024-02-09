#!/usr/bin/python3
class Example:
    def __init__(self, name, age, data):
        self.name = name
        self.age = age
        self.data = data

# Create an instance of the class
obj = Example("John", 25, {"key": "value", "nested_list": [1, 2, 3], "is_student": True})

# Convert the instance to a JSON-serializable dictionary
result = class_to_json(obj)

print(result)
