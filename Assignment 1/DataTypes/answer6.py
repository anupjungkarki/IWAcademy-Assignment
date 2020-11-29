# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
def find_not_poor(str):
    string_not = str.find('not')
    string_bad = str.find('poor')

    if string_bad > string_not > 0 and string_bad > 0:
        str = str.replace(str[string_not:(string_bad + 4)], 'good')
        return str
    else:
        return str


print(find_not_poor('The lyrics is not that poor!'))
print(find_not_poor('This lyrics is poor!'))
