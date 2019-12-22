import logging
import requests
import telegram
import os
from const import headers, dev_long_URL
from proxy_broker import get_proxy

URL_DEVMAN_LESSON = 'https://dvmn.org/modules/'


def get_time_stump(json):
    if 'found' in json:
        element_of_response = json.get('last_attempt_timestamp')
        request_params = {'timestamp_to_request': {f'{element_of_response}'}}
        return request_params
    else:
        element_of_response = json.get('timestamp_to_request')
        request_params = {'timestamp_to_request': {f'{element_of_response}'}}
        return request_params


def get_message(json):
    if not json['new_attempts'][0]['is_negative']:
        message = 'Преподавателю все понравилось, можно приступать к следующему уроку!'
    else:
        message = 'К сожалению в работе нашлись ошибки'

    full_message = f'''У вас проверили работу, отправляем уведомление о проверке работ,
                        {message}  Ссылка на урок: {URL_DEVMAN_LESSON}'''
    return full_message


def main():
    proxy = get_proxy()
    pp = telegram.utils.request.Request(proxy_url=proxy)

    bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'), request=pp)
    chat_id = os.environ.get('CHAT_ID')

    request_params = {}
    while True:
        try:
            response = requests.get(dev_long_URL, headers=headers, params=request_params)
            response.raise_for_status()
            dict_resp = response.json()
            if 'error' in dict_resp:
                raise requests.exceptions.HTTPError(dict_resp['error'])

            request_params = get_time_stump(dict_resp)

            user_message = get_message(dict_resp)

            bot.send_message(chat_id=chat_id, text=user_message)

        except requests.exceptions.ConnectionError as error:
            print(f'{error}')
        except requests.exceptions.Timeout as error:
            print(f'{error}')
        except requests.exceptions.HTTPError as error:
            print('Cant get data from server:\n{0}'.format(error))


if __name__ == '__main__':
    main()
