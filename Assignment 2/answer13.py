# Write a function to write a comma-separated value (CSV) file. It should accept a filename and a list of tuples as
# parameters. The  tuples should have a name, address, and age. The file should create a header row followed by a row
# for each tuple. If the following list of tuples was passed in: [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
# 21)] it should write the following in the file:
import csv


def csv_func(filename, tuple_list):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'address', 'age'])
        writer.writerow(tuple_list[0])
        writer.writerow(tuple_list[1])
        writer.writerow(tuple_list[2])


filename = 'my_csv.csv'
tuple_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21) ,('Anup', '23 Pepsicola', 22)]
print(csv_func(filename, tuple_list))
