import csv

with open("file.csv", "r") as person_data:
    reader = csv.reader(person_data)
    next(reader)
    for line in reader:
        print(line[0] + " is " + line[2] + " and " + line[1] + " years old")
