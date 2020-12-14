# Create a list of tuples of first name, last name, and age for your friends and colleagues. If you don't know the age,
# put in None. Calculate the average age, skipping over any None values. Print out each name, followed by old or young
# if they are above or below the average age.
list_of_tuples = [('Anup', 'Karki', 23), ('Jit', 'Magar', 22), ('Sajan', 'Rai', 25), ('Aayan', 'Karki', 34)]
print(list_of_tuples)
age_list = []
for data in list_of_tuples:
    if data is not None:
        age_list.append(data[2])
print(age_list)
sum = 0
count = 0
for value in range(len(age_list)):
    if type(age_list[value]) == int:
        sum = sum + age_list[value]
        count = count + 1
average = sum / count
final_list = []
final_name = []
for i in list_of_tuples:
    if i is not None:
        final_list.append(i[2])
        final_name.append(i[0])
for data in final_list:
    if average > data:
        print("The below Average Age With Name is :", final_name[0], data)
    if average < data:
        print("The below Above Age With Name is :", final_name[3], data)

