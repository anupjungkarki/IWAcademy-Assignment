# Write a Python program to sort a list of tuples using Lambda.
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('anup', 15)]
print('Before Sort:', tup)
tup.sort(key=lambda x: x[1])
print('After Sort:', tup)
