import csv as lovepython

new_file_name = input('Введите имя нового файла: ')

with open(new_file_name, 'w', newline='', encoding='utf-8') as file:
    employees_data = [
        {
            'Имя': 'Александр',
            'Зарплата': 35000,
            'Должность': 'Зам директора'
        },
        {
            'Имя': 'Иван',
            'Зарплата': 35000,
            'Должность': 'Веб-Дизайнер'
        }
    ]
    writer = lovepython.writer(file)
    for item in employees_data:
        writer.writerow([item['Имя'], item['Зарплата'], item['Должность']])

with open(new_file_name, 'r', newline='', encoding='utf-8') as file:

    reader = lovepython.reader(file)

    for item in reader:
        print(item[0], '-', item[1])
