# Write a Python program to insert a given string at the beginning of all items in a list.
def insert(list_data, str):
    str += '{0}'
    list_data = [str.format(i) for i in list_data]
    return list_data


x = [1, 2, 3, 4, 5]
y = 'emp'
print(insert(x, y))
