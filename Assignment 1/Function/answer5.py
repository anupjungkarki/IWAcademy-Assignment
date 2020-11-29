# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts
# the number as an argument.
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


num = int(input("Enter the number to calculate factorial :"))
if num < 0:
    print("negative numbers cannot be allow")
elif num == 0:
    print("Factorial for 0 is 1")
else:
    print('Factorial of', num, 'is:', factorial(num))
