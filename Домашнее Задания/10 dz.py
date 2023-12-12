import csv

file_name = 'employees.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    employees_data = list(reader)
    '''
    Имя - Максим
    Зарплата - 20000
    Должность - Преподаватель
    '''

    sorted_employees_data = sorted(employees_data, key=lambda x: int(x[1]))

    with open(file_name, 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        fieldnames = ['Имя', 'Зарплата', 'Должность']
        writer.writerow(fieldnames)
        writer.writerows(sorted_employees_data)