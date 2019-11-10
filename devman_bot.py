import requests
import telebot

from const import *

# bot = telebot.TeleBot(TOKEN)

response = requests.get('https://dvmn.org/api/user_reviews/')
print(response.json())
# bot.send_message(r.json())

# bot.polling(timeout=60)
