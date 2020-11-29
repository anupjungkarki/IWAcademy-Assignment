# Write a Python script to concatenate following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dic = dict()
for data in dic1, dic2, dic3:
    new_dic.update(data)
print(new_dic)

