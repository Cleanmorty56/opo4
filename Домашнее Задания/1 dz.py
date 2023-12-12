import csv

employees = [
    {'Имя': 'Алексей', 'Зарплата': 10000, 'Должность': 'Стажер-программист'},
    {'Имя': 'Дмитрий', 'Зарплата': 55000, 'Должность': 'Директор'},
    {'Имя': 'Юлия', 'Зарплата': 35000, 'Должность': 'Педагог-психолог'}
]

file_name = 'employees.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Имя', 'Зарплата', 'Должность']
    writer = csv.DictWriter(file, fieldnames)

    writer.writeheader()
    for employ in employees:
        writer.writerow(employ)