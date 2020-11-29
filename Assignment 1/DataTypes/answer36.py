# Write a Python program to sum all the items in a dictionary.
def sum_dic(dic_data):
    sum = 0
    for data in dic_data:
        sum = sum + dic_data[data]
    return sum


dict_data = {'1': 12, '2': 34, '3': 37, '4': 39, '5': 44}
print('Total:', sum_dic(dict_data))

# or
total = sum(dict_data.values())
print('Total:', total)
