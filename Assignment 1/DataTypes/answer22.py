# Write a Python program to remove duplicates from a list
list_data = [5, 6, 7, 5, 8, 4, 9, 7]
print('Before:', list_data)
empty_list = []
for item in list_data:
    if item not in empty_list:
        empty_list.append(item)
list_data = empty_list
print('After:', list_data)
