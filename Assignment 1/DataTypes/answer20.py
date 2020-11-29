# Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.
def match_words(words):
    char = 0
    for word in words:
        if len(word) > 1:
            if word[0] == word[-1]:
                char += 1
    return char


input_data = match_words(["aba", "pqp", '232', 'ads', 'drf'])
print(input_data)