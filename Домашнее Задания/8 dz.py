import csv

file_name = 'employees.csv'


with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    employees_data = list(reader)

    for item in employees_data:
        print(item[0], '-', item[1])

    name_remove = input('Введите имя сотрудника для удаления: ')

    remove_employ = [item for item in employees_data if item[0] != name_remove ]

    with open(file_name, 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        fieldnames = ['Имя', 'Зарплата', 'Должность']
        writer.writerow(fieldnames)
        writer.writerows(remove_employ)
    print(f'Сотрудник ({name_remove}) успешно удален из файла: {file_name}')