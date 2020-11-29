# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
string1 = 'abc'
string2 = 'xyz'
x = string1[0:2]
y = string2[0:2]
string1 = string1.replace(x, y)
string2 = string2.replace(y, x)
print(string1, string2)

# or we ca also do it in following way
string1 = 'abc'
string2 = 'xyz'
y, x = string2[0:2], string1[2:]
result1 = y+x
x, y = string1[0:2], string2[2:]
result2 = x + y
print(result1, result2)
