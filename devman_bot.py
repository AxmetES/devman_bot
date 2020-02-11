import time

import requests
import telegram
from proxy_broker import get_proxy
import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger('bot logger')


def get_time_stamp(response):
    if response['status'] == 'found':
        timestamp = response.get('last_attempt_timestamp')
        request_params = {'timestamp_to_request': timestamp}
        return request_params
    else:
        timestamp = response.get('timestamp_to_request')
        request_params = {'timestamp_to_request': timestamp}
        return request_params


def send_message(response, chat_id, bot):
    url_devman = 'https://dvmn.org'
    message = ''

    if response['status'] == 'found':
        attempt = response['new_attempts'][0]

        if not attempt['is_negative']:
            message = 'Преподавателю все понравилось, можно приступать к следующему уроку!'
        elif attempt['is_negative']:
            message = 'К сожалению в работе нашлись ошибки'

        url_devman = url_devman + attempt['lesson_url']

        full_message = f'''{attempt['lesson_title']}, {message}  Ссылка на урок: {url_devman}'''
        bot.send_message(chat_id=chat_id, text=full_message)


def request_devman_api(url, headers, params):
    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    response_data = response.json()

    if 'error' in response.text:
        raise requests.exceptions.HTTPError(response_data['error'])
    return response_data


def main():
    load_dotenv(verbose=True)
    long_polling_url = 'https://dvmn.org/api/long_polling/'
    devman_token = os.getenv('DEVMAN_TOKEN')
    headers = {'Authorization': f'Token {devman_token}'}

    proxy = get_proxy()
    pp = telegram.utils.request.Request(proxy_url=proxy)
    bot = telegram.Bot(token=os.getenv('BOT_TOKEN'), request=pp)
    chat_id = os.getenv('CHAT_ID')

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    handler = BotLoggerHandler(bot=bot, chat_id=chat_id)
    logger.addHandler(handler)

    logger.info('bot is started')
    request_params = {}
    while True:
        try:
            response = request_devman_api(long_polling_url, headers, request_params)
            request_params = get_time_stamp(response)
            send_message(response, chat_id, bot)
        except requests.exceptions.ConnectionError as error:
            logger.debug(f'{error}')
            time.sleep(30)
        except requests.exceptions.Timeout as error:
            logger.debug(f'{error}')
        except requests.exceptions.HTTPError as error:
            logger.error(f'{error}')
            time.sleep(30)
        except Exception:
            logger.exception('Bot is crashed')


class BotLoggerHandler(logging.Handler):
    def __init__(self, bot, chat_id):
        super().__init__()
        self.bot = bot
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(self.chat_id, text=log_entry)


if __name__ == '__main__':
    main()
