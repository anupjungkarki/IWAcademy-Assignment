# Write a Python script to check whether a given key already exists in a dictionary.
def check_key(dic, key):
    if key in dic.keys():
        print('Present', end='')
        print('Value=', dic[key])
    else:
        print('Not present')


dic = {'a': 100, 'b': 200, 'c': 300}
key = 'a'
check_key(dic, key)
