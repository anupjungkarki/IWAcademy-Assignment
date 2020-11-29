# Write a Python program to reverse a string.
def reverse_string(string):
    string = "".join(reversed(string))
    return string


s = "Python"
print("The original string : ", end="")
print(s)
print("The reversed string: ", end="")
print(reverse_string(s))