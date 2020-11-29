#  Write a Python function to insert a string in the middle of a string.
def insert_string_in_middle(str, word):
    return str[:2] + word + str[2:]


print(insert_string_in_middle('[[]]', 'JavaScript'))
print(insert_string_in_middle('{{}}', 'Python'))
