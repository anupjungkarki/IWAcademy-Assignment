# Write a Python program to remove the characters which have odd index values of a given string.
def remove_character(str):
    final = ""
    for i in range(len(str)):
        if i % 2 == 0:
            final = final + str[i]
    return final


str = input("Enter the string:")
print(remove_character(str))
