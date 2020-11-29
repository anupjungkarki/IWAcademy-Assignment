# Write a Python function to find the Max of three numbers.
def findMax(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


max_num = findMax(40, 32, 45)
print(max_num)
