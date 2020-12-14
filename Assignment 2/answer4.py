# Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list.
# What is the first item on the list? What is the second item on the list?
empty_list = []
print(id(empty_list))
empty_list.append('Anup Karki')
empty_list.append('Jit Rana Magar')
empty_list.append('Patrick Sharma')
empty_list.append('Hari Bijok Tharu')
print(id(empty_list))
print(empty_list)
# No id is not changed after appending the value to list.
empty_list.sort()
print(empty_list)
print('The First Item on list is: {} and the second item on list is: {}'.format(empty_list[0], empty_list[1]))
