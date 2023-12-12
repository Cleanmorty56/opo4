import csv

file_name = 'employees.csv'


target_letter = 'Д'

with open(file_name, encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    for item in reader:
        employ_name = item[0]
        if employ_name and employ_name.startswith(target_letter):
            print(employ_name)

