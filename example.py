response = {'request_query': [],
            'status': 'timeout',
            'timestamp_to_request': 1573446633.184347}
for message in response:
    if 'timeout' in response:
        print('test in')
        break
#
# print([val for key, val in response.items() if key = 'status'])
