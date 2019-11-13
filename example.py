timestamp = {'timestamp_to_request': 0}
dict_resp = {'last_attempt_timestamp': 1573572410.077114,
             'new_attempts': [{'is_negative': False,
                               'lesson_title': 'Отправляем уведомления о проверке работ',
                               'lesson_url': '/modules/chat-bots/lesson/devman-bot/',
                               'submitted_at': '2019-11-12T18:26:50.077114+03:00',
                               'timestamp': 1573572410.077114}],
             'request_query': [],
             'status': 'found'}

answer_list = dict_resp.get('new_attempts')[0]
# dic_attempts = answer_list[0]
if answer_list.get('is_negative') == False:
    print('test in')
