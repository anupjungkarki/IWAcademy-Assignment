# Write a Python program to print the even numbers from a given list.
def check_even(number):
    even_data = []
    for data in number:
        if data % 2 == 0:
            even_data.append(data)
    return even_data


result = check_even([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)
