# Create a tuple with your first name, last name, and age. Create a list,people, and append your tuple to it. Make more
# tuples with the corresponding information from your friends and append them to the list. Sort the list. When you learn
# about sort method, you can use the key parameter to sort by any field in the tuple, first name, last name,or age.
tuples_data = ('Znup', 'Karki', 22)
people = []
people.append(tuples_data)
tuples_data1 = ('Hari', 'Karki', 20)
tuples_data2 = ('Ram', 'Karki', 19)
people.append(tuples_data1)
people.append(tuples_data2)
print(people)
people.sort(key=lambda x: x[0][2])
print(people)

