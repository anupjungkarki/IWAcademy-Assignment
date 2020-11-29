# Write a Python program to count the occurrences of each word in a given sentence.
def count_word(str):
    count = dict()
    words = str.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


str = input("Enter the sentence:")
print(count_word(str))
