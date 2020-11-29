#  Write a Python program to add an item in a tuple
my_tuple = (1, 3, 4, 6, 2, 9, 10)
print(my_tuple)
convert_to_list = list(my_tuple)
convert_to_list.append(12)
my_tuple = tuple(convert_to_list)
print(my_tuple)
