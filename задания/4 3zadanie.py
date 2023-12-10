import csv
import os
import random
import requests
import telebot
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id,
                        'hi you tape me /start or /help.'
                     'use /infousers for get random task')


@bot.message_handler(commands=['infousers'])
def handle_todos(message):
    url = f"https://dummyjson.com/users/{random.randint(1, 200)}"
    response = requests.get(url)
    if response.status_code == 200:
        infousers = response.json()
        adress = infousers['adress']
        title = infousers['title']
        city = infousers['city']
        name = infousers['name']
        status = infousers['status']
        departament = infousers['departament']
        with open('infousers.csv', 'a', newline='',  encoding='utf-8') as file:
            filenames = ['adress', 'title', 'city', 'status', 'name', 'departament']
            writer = csv.DictWriter(file, fieldnames=filenames)
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({
                'adress': adress,
                'title': title,
                'city': city,
                'status': status,
                'name': name,
                'departament': departament

            })
    else:
        bot.send_message(message.chat.id, "task not found")

bot.polling(none_stop=True)