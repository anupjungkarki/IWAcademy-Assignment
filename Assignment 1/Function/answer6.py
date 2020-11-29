# Write a Python function to check whether a number is in a given range.
def check_number_range(num):
    if num in range(2, 7):
        print(num, 'is in range')
    else:
        print(num, 'is out of range')


check_number_range(4)
