# Write a Python program to remove an item from a tuple.
tuple_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_data)
list_data = list(tuple_data)
list_data.remove(10)
tuple_data = tuple(list_data)
print(tuple_data)