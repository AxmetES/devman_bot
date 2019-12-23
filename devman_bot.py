import requests
import telegram
import os
from const import headers, dev_long_URL
from proxy_broker import get_proxy


def get_time_stump(json):
    if json['status'] == 'found':
        element_of_response = json.get('last_attempt_timestamp')
        request_params = {'timestamp_to_request': {f'{element_of_response}'}}
        print(request_params)
        return request_params
    else:
        element_of_response = json.get('timestamp_to_request')
        request_params = {'timestamp_to_request': {f'{element_of_response}'}}
        print(request_params)
        return request_params


def get_message(json, chat_id, bot):
    url_devman = 'https://dvmn.org'
    message = ''

    if json['status'] == 'timeout':
        pass
    elif json['status'] == 'found':
        if not json['new_attempts'][0]['is_negative']:
            message = 'Преподавателю все понравилось, можно приступать к следующему уроку!'
        elif json['new_attempts'][0]['is_negative']:
            message = 'К сожалению в работе нашлись ошибки'
        url_lesson = json['new_attempts'][0]['lesson_url']

        url_devman = url_devman + url_lesson
        lesson_title = json['new_attempts'][0]['lesson_title']
        full_message = f'''{lesson_title}, {message}  Ссылка на урок: {url_devman}'''
        bot.send_message(chat_id=chat_id, text=full_message)


def get_request(url, headers, params):
    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    dict_resp = response.json()

    if 'error' in response.text:
        raise requests.exceptions.HTTPError(dict_resp['error'])
    return dict_resp


def main():
    proxy = get_proxy()
    pp = telegram.utils.request.Request(proxy_url=proxy)

    bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'), request=pp)
    chat_id = os.environ.get('CHAT_ID')

    request_params = {}
    while True:
        try:
            dict_resp = get_request(dev_long_URL, headers, request_params)

            request_params = get_time_stump(dict_resp)

            get_message(dict_resp, chat_id, bot)

        except requests.exceptions.ConnectionError as error:
            print(f'{error}')
        except requests.exceptions.Timeout as error:
            print(f'{error}')
        except requests.exceptions.HTTPError as error:
            print('Cant get data from server:\n{0}'.format(error))


if __name__ == '__main__':
    main()
