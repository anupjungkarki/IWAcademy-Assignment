# Write a Python program to check whether a given string is number or not using Lambda.
is_number = lambda q: q.replace('.', '', 1).isdigit()
print(is_number('26587'))
print(is_number('hello'))
