# Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.
from collections import Counter

paragraph = "The cat and dog play tac game in an god level act"
data = paragraph.split(' ')
str = 'act'
result = list(filter(lambda x: (Counter(str) == Counter(x)), data))
print('The anagrams from the paragraph of test is:')
print(result)
