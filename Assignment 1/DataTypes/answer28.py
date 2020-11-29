# Write a Python script to add a key to a dictionary.
dict_data = {0: 10, 1: 20}
print('Before:', dict_data)
next_dict = {2: 30, 4: 40}
dict_data.update(next_dict)
print('After:', dict_data)
