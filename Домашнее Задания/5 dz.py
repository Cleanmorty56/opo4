import csv

file_name = 'employees.csv'

name = input('Введите имя сотрудника: ')
pay = input('Введите зарплату сотрудника: ')
job = input('Введите должность сотрудника: ')

with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow([name, pay, job])
print(f'Сотрудник: {name} успешно добавлен в файл: {file_name}')