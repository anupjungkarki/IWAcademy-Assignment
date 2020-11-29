# Write a Python program to get the smallest number from a list.
def smallest_number(list_data):
    smaller_number = list_data[0]
    for data in list_data:
        if data < smaller_number:
            smaller_number = data
    return smaller_number


result = smallest_number([10, 2, 4, 5, 7, 1, 4, 12, 11])
print('The smallest number is:', result)
