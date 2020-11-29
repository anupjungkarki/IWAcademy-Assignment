#  Write a Python function that takes a list and returns a new list with unique elements of the first list.
def get_unique_list(list_data):
    result = []
    unique_list = set(list_data)
    for list_data in unique_list:
        result.append(list_data)
    return result


print(get_unique_list(list_data=[1, 2, 2, 3, 3, 4, 4, 5]))
