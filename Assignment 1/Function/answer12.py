# Write a Python program to create a function that takes one argument, and that argument will be multiplied
# with an unknown given number.
def calculate(n):
    return lambda x: x * n


result = calculate(2)
print("Result:", result(15))
