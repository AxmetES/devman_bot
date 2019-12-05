## Telegram bot notifications

project of a bot notifying via telegram a messenger about the status of homework at Devman courses

## Getting Started

for the project to work, install all necessary packages 

```python
 pip install -r requirements.txt
```
than you need to configure environment variables in python, and name it environment.env
you write secret variables into it, and with the help of

```python
 BOT_TOKEN='your token'
 DEVMAN_TOKEN='your token'
 DEVMAN_API = 'your API'
 CHAT_ID ='input youre chat id from telegram'
```
you extract it in the code with package
import os [more info](https://gist.github.com/dvmn-tasks/22b18aafb24a6be5213eb5c6532eaef8)
#### in module devman_bot.py

```python
 import os

 bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'))
 devman_token = os.getenv('DEVMAN_TOKEN')
 get_chat_id = os.environ.get('CHAT_ID')
```

#### in module const.py

```python
 import os

 headers = {'Authorization': f'Token {devman_token}'}
```

## Motivation

the project is an assignment in online courses [Devman](https://dvmn.org/modules/)

## Using


## Installation

set by launching telegram bot

## Running

```python
 python devman_bot.py
```

## License

You may copy, distribute and modify the software
