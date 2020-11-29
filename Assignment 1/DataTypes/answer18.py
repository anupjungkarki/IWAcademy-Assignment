# Write a Python program to get the largest number from a list.
def my_max_number(list_data_next):
    max_number = list_data_next[0]
    for data in list_data_next:
        if data > max_number:
            max_number = data
    return max_number


result = my_max_number([1, 3, 5, 20, 45, 2, 4, 7, 13])
print('The largest number is:', result)

# or we can   also
list_data = [1, 4, 5, 18, 2, 3, 7, 9, 13, 12, 11]
list_data.sort()
if list_data:
    print('The Largest number is:', list_data[-1])
else:
    print('No data found in list')