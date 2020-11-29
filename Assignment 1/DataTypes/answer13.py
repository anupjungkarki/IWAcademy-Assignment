# Write a Python program that accepts a comma separated sequence of words as input and prints the
# unique words in sorted form (alphanumerically)
data = [x for x in input("Enter comma separated sequence word:").split(',')]
data.sort()
print(",".join(data))
