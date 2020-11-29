# Write a Python program to iterate over dictionaries using for loops.
dict_data = {
    'name': 'example',
    'address': 'kathmandu',
    'age': 22,
    'phone': '9842123523'
}
for key, value in dict_data.items():
    print(key, '=', value)
