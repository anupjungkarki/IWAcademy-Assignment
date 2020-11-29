# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
str = 'google.com'
frequencies = {}
for i in str:
    if i in frequencies:
        frequencies[i] += 1
    else:
        frequencies[i] = 1
print(frequencies)

# we can also do like this

frequencies = {}
for keys in str:
    frequencies[keys] = frequencies.get(keys, 0) + 1
print(frequencies)
