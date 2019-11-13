import requests
from requests import Timeout, ConnectionError
import pprint
import telegram

from const import *

pp = telegram.utils.request.Request(proxy_url='socks5h://95.141.130.122:9999')
bot = telegram.Bot(token=TOKEN, request=pp)

bot.send_message(chat_id=421935954, text=' Извини, Дэйв, боюсь, я не могу этого сделать')

# requesr-respons function
# timestamp = {'timestamp_to_request': 0}
#
# while True:
#     if timestamp.get('timestamp_to_request') == 0:
#         try:
#             response = requests.get(dev_long_URL, headers=headers)
#             dict_resp = response.json()
#
#             if dict_resp.get('status') == 'found':
#                 timestamp['timestamp_to_request'] = dict_resp.get('last_attempt_timestamp')
#                 pprint.pprint(dict_resp)
#                 print(timestamp)
#             else:
#                 timestamp['timestamp_to_request'] = dict_resp.get('timestamp_to_request')
#         except ConnectionError:
#             continue
#     else:
#         try:
#             response = requests.get(dev_long_URL, headers=headers, params=timestamp)
#             dict_resp = response.json()
#
#             if dict_resp.get('status') == 'found':
#                 timestamp['timestamp_to_request'] = dict_resp.get('last_attempt_timestamp')
#                 pprint.pprint(dict_resp)
#                 print(timestamp)
#             else:
#                 timestamp['timestamp_to_request'] = dict_resp.get('timestamp_to_request')
#         except ConnectionError:
#             continue

# respons  - example
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
