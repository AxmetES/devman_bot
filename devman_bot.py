import requests
import telegram
import os
from const import headers, dev_long_URL
from proxy_broker import get_proxy
import logging


def get_time_stamp(response):
    if response['status'] == 'found':
        timestamp = response.get('last_attempt_timestamp')
        request_params = {'timestamp_to_request': f'{timestamp}'}
        return request_params
    else:
        timestamp = response.get('timestamp_to_request')
        request_params = {'timestamp_to_request': f'{timestamp}'}
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
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    proxy = get_proxy()
    pp = telegram.utils.request.Request(proxy_url=proxy)

    bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'), request=pp)
    chat_id = os.environ.get('CHAT_ID')
    logging.info('bot is started')

    request_params = {}
    while True:
        try:
            response = request_devman_api(dev_long_URL, headers, request_params)

            request_params = get_time_stamp(response)

            send_message(response, chat_id, bot)

        except requests.exceptions.ConnectionError as error:
            logging.debug(f'{error}')
        except requests.exceptions.Timeout as error:
            logging.debug(f'{error}')
        except requests.exceptions.HTTPError as error:
            logging.error(f'{error}')


if __name__ == '__main__':
    main()
