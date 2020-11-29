# Write a Python function that takes a list of words and returns the length of the longest one.
def list_word():
    text = input('Enter the text here:')
    longest = 0
    for words in text.split():
        if len(words) > longest:
            longest = len(words)
    print("The longest words is:", words, "With  length", longest)


list_word()
