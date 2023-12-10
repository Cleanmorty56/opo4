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
                     'use /todos for get random task')


@bot.message_handler(commands=['todos'])
def handle_todos(message):
    url = f"https://jsonplaceholder.typicode.com/todos/{random.randint(1, 200)}"
    response = requests.get(url)
    if response.status_code == 200:
        todos = response.json()
        idx = todos['id']
        title = todos['title']
        userid = todos['userId']
        completed = todos['completed']
        bot.send_message(message.chat.id, f"task: {todos['title']}\nStatus: {completed}")
        with open('todos.csv', 'a', newline='',  encoding='utf-8') as file:
            filenames = ['id', 'title', 'user', 'status']
            writer = csv.DictWriter(file, fieldnames=filenames)
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({
                'id': idx,
                'title': title,
                'user': userid,
                'status': completed
            })
    else:
        bot.send_message(message.chat.id, "task not found")

bot.polling(none_stop=True)