# Write a function that reads a CSV file. It should return a list of dictionaries, using the first row as key names,
# and each subsequent row as values for those keys.
import csv


def read_csv(filename):
    result = []
    with open(filename) as file:
        first = True
        for line in file:
            if first:
                keys = "".join(line.split()).split(',')
                first = False
            else:
                values = "".join(line.split()).split(',')
                result.append({keys[n]: values[n] for n in range(0, len(keys))})
        print(result)


read_csv('my_csv.csv')
