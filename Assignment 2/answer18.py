# Find a package in the Python standard library for dealing with JSON.Import the library module and inspect the attributes
# of the module. Use the help function to learn more about how to use the module.Serialize a dictionary mapping 'name' to
# your name and 'age' to your age, to a JSON string. Deserialize the JSON back into Python.
import json
my_data = {}
my_data["name"] = "Anup Karki"
my_data["age"] = 21
print("Mero dictionary:", my_data)

json_string = json.dumps(my_data)
print("Serialize dictionary JSON string:", json_string)

deserialized_person = json.loads(json_string)
print("Deserialized dictionary from JSON string:", deserialized_person)
