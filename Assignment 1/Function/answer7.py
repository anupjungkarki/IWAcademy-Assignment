# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
def upper_lower(string):
    upper = 0
    lower = 0

    for i in range(len(string)):

        # For lower letters
        if 97 <= ord(string[i]) <= 122:
            lower += 1

        # For upper letters
        elif 65 <= ord(string[i]) <= 90:
            upper += 1

    print('Lower case characters = %s' % lower,
          'Upper case characters = %s' % upper)


# Driver Code
string = 'IWAcademy Software Engineering BootCamp'
upper_lower(string)
