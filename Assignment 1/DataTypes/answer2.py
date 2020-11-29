# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.
def get_two_string(str):
    if len(str) < 2:
        return 'Empty String'
    else:
        return str[0:2] + str[-2:]


print(get_two_string('Python'))
print(get_two_string('Py'))
print(get_two_string('W'))
