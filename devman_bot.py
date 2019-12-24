import requests
import telegram
import os
from const import headers, dev_long_URL
from proxy_broker import get_proxy


def get_time_stamp(resp_dect):
    if resp_dect['status'] == 'found':
        element_of_response = resp_dect.get('last_attempt_timestamp')
        request_params = {'timestamp_to_request': {f'{element_of_response}'}}
        return request_params
    else:
        element_of_response = resp_dect.get('timestamp_to_request')
        request_params = {'timestamp_to_request': {f'{element_of_response}'}}
        return request_params


def send_message(response, chat_id, bot):
    url_devman = 'https://dvmn.org'
    message = ''
    result_check = response['new_attempts'][0]['is_negative']
    lesson_title = response['new_attempts'][0]['lesson_title']
    lesson_url = response['new_attempts'][0]['lesson_url']

    if response['status'] == 'timeout':
        pass
    elif response['status'] == 'found':
        if not result_check:
            message = 'Преподавателю все понравилось, можно приступать к следующему уроку!'
        elif result_check:
            message = 'К сожалению в работе нашлись ошибки'

        url_devman = url_devman + lesson_url

        full_message = f'''{lesson_title}, {message}  Ссылка на урок: {url_devman}'''
        bot.send_message(chat_id=chat_id, text=full_message)


def request_devman_api(url, headers, params):
    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    response_data = response.json()

    if 'error' in response.text:
        raise requests.exceptions.HTTPError(response_data['error'])
    return response_data


def main():
    proxy = get_proxy()
    pp = telegram.utils.request.Request(proxy_url=proxy)

    bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'), request=pp)
    chat_id = os.environ.get('CHAT_ID')

    request_params = {}
    while True:
        try:
            response = request_devman_api(dev_long_URL, headers, request_params)

            request_params = get_time_stamp(response)

            send_message(response, chat_id, bot)

        except requests.exceptions.ConnectionError as error:
            print(f'{error}')
        except requests.exceptions.Timeout as error:
            print(f'{error}')
        except requests.exceptions.HTTPError as error:
            print('Cant get data from server:\n{0}'.format(error))


if __name__ == '__main__':
    main()
