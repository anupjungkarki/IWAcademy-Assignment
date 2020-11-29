# Write a Python program to check whether all dictionaries in a list are empty or not.
list_data1 = [{}, {}, {}]
list_data2 = [{1, 2}, {}, {}]
print(all(len(d) == 0 for d in list_data1))
print(all(len(d) == 0 for d in list_data2))
