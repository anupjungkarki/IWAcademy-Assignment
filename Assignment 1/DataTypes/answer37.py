# Write a Python program to multiply all the items in a dictionary.
dict_data = {'1': 2, '2': 4, '3': 3, '4': 9, '5': 6}
mul = 1
for values in dict_data:
    mul = values * dict_data[values]
print('Total:', mul)
