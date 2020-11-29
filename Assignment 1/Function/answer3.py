#  Write a Python function to multiply all the numbers in a list.
def multiply(list_data):
    total = 1
    for i in list_data:
        total *= i
    return total


result = multiply((3, 4, 5))
print(result)
