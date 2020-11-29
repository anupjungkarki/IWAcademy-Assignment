# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
input_data = int(input("Enter the number="))
result = {i: i * i for i in range(1, input_data + 1)}
print(result)
