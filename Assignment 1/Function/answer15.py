# Write a Python program to filter a list of integers using Lambda.
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, 60]
print(my_list)
result = list(filter(lambda x: (x % 13 == 0), my_list))
print(result)
