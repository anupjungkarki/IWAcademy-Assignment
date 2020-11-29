# Write a Python program to sort a list of dictionaries using Lambda
data = [{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Rajesh'}, {'age': 20, 'name': 'Jonny'}]
print('Before sort:', data)
sorted_data = sorted(data, key=lambda x: x['name'])
print('After sort:', sorted_data)
