# Write a Python program to remove a key from a dictionary.
dic_data = {'name': 'Anup', 'address': 'kathmandu', 'age': 21, 'occupation': 'programmer'}
print(dic_data)
if 'name' in dic_data:
    del dic_data['name']
print(dic_data)