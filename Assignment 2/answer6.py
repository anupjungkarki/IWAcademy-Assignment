# Create a list with the names of friends and colleagues. Search for the name ‘John’ using a for a loop.
# Print ‘not found’ if you didn't find it.
list_data = ['Anup', 'Ram', 'Shyam', 'Hari']
if 'John' in list_data:
    print('John is Found in List')
else:
    print("Not Found")


# or

def search(list_data, name):
    for i in range(len(list_data)):
        if list_data[i] == name:
            return True
        else:
            return False


list_data = ['Anup', 'Ram', 'Shyam', 'Hari']
name = 'John'
if search(list_data, name):
    print('John is Found in List')
else:
    print('Not Found')
