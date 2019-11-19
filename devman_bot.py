import requests
from requests import ConnectionError
import telegram
import os
from const import headers, dev_long_URL
from proxy_broker import get_proxy

proxy = get_proxy()
pp = telegram.utils.request.Request(proxy_url=proxy)

bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'), request=pp)
get_chat_id = os.environ.get('CHAT_ID')

timestamp = {}
devman_lesson_url = ''

while True:
    try:
        response = requests.get(dev_long_URL, headers=headers, params=timestamp)
        dict_resp = response.json()
        if dict_resp.get('status') == 'found':
            last_timestamp = dict_resp.get('last_attempt_timestamp')
            timestamp = {'timestamp_to_request': {last_timestamp}}
            devman_lesson_url = 'https://dvmn.org'
            devman_lesson_url = devman_lesson_url + dict_resp['new_attempts'][0]['lesson_url']

            if dict_resp['new_attempts'][0]['is_negative'] == False:
                teach_str = 'Преподавателю все понравилось, можно приступать к следующему уроку!'
            else:
                teach_str = 'К сожелению в работе нашлись ошибки'
            bot.send_message(
                chat_id=get_chat_id,
                text=f'У вас проверили работу "Отправляем уведомление о проверке работ"\n{teach_str}\n Ссылка на урок: {devman_lesson_url}')
        else:
            last_timestamp = dict_resp.get('timestamp_to_request')
            timestamp = {'timestamp_to_request': {last_timestamp}}
    except ConnectionError:
        continue
