import requests
from requests import Timeout, ConnectionError
import pprint
import telegram

from const import *

#
# bot = telegram.Bot(token=TOKEN)
# timestamp = {'timestamp_to_request': 0}

# bot.send_message(chat_id=421935954, text=' Извини, Дэйв, боюсь, я не могу этого сделать')

timestamp = {'timestamp_to_request': 0}

while True:
    if timestamp.get('timestamp_to_request') == 0:
        try:
            response = requests.get(dev_long_URL, headers=headers)
            dict_resp = response.json()
            if dict_resp.get('status') == 'timeout':
                pprint.pprint(dict_resp)
        except ConnectionError:
            continue

# while True:
#     if timestamp['timestamp_to_request'] == 0:
#         response = requests.get(dev_long_URL, headers=headers)
#         dict_resp = response.json()
#         if dict_resp.get('status') == 'timeout':
#             timestamp['timestamp_to_request'] = dict_resp['timestamp_to_request']
#         else:
#             print(dict_resp)
#     else:
#         response = requests.get(dev_long_URL, headers=headers, params=timestamp)
#         dict_resp = response.json()
#         if dict_resp.get('status') == 'timeout':
#             timestamp['timestamp_to_request'] = dict_resp['timestamp_to_request']
#         else:
#             print(dict_resp)

# {'last_attempt_timestamp': 1573572410.077114,
#  'new_attempts': [{'is_negative': True,
#                    'lesson_title': 'Отправляем уведомления о проверке работ',
#                    'lesson_url': '/modules/chat-bots/lesson/devman-bot/',
#                    'submitted_at': '2019-11-12T18:26:50.077114+03:00',
#                    'timestamp': 1573572410.077114}],
#  'request_query': [],
#  'status': 'found'}

# {'request_query': [],
#  'status': 'timeout',
#  'timestamp_to_request': 1573581788.6642153}