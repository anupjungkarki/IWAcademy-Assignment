# Create a function, is_palindrome, to determine if a supplied word is the same if the letters are reversed.
def is_palindrome(str):
    revers = ''.join(reversed(str))
    if str == revers:
        return True
    else:
        return False


str = 'anna'
res = is_palindrome(str)
if res:
    print('Yes')
else:
    print('No')
