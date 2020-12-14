# Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator. Gracefully deal
# with input that doesn't cleanly convert to numbers. Deal with division by zero errors.
def calculator(num1, num2):
    try:
        res = num1 / num2
        return res
    except ZeroDivisionError:
        return "Division By Zero is Not Allowed"


num1 = int(input("Enter  Number for Calculation:"))
num2 = int(input("Enter  Number for Calculation:"))
print(calculator(num1, num2))
