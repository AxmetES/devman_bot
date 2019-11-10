import requests
import pprint
import telegram

from const import *

bot = telegram.Bot(token=TOKEN)

# bot.send_message(chat_id=421935954, text=' Извини, Дэйв, боюсь, я не могу этого сделать')
while True:
    response = requests.get(dev_long_URL, headers=headers)
    for message in response:
        bot.send_message(chat_id=421935954, text=response.json())
