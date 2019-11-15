import os

dev_URL = 'https://dvmn.org/api/user_reviews/'
dev_long_URL = 'https://dvmn.org/api/long_polling/'
devman_token = os.getenv('DEVMAN_TOKEN')
headers = {'Authorization': f'Token {devman_token}'}
