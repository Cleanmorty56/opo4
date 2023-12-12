import csv

file_name = 'employees.csv'

new_employees = [
    {'Имя': 'Валерия', 'Зарплата': 25000, 'Должность': 'Фотограф'},
    {'Имя': 'Артем', 'Зарплата': 15000, 'Должность': 'Уборщик'}]

with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for employ in new_employees:
        writer.writerow([employ['Имя'], employ['Зарплата'], employ['Должность']])
print(f'Данные успешно записаны в файл:{file_name}')