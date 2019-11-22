## Telegram bot notifications

project of a bot notifying via telegram a messenger about the status of homework at Devman courses

## Getting Started

telegram - a package that allows you to interact with the telegram messenger using the token that is specified in the module
[more information on python-telegram-bot ](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API)

 `import telegram 
 bot = telegram.Bot(token=os.environ.get('BOT_TOKEN')`

ProxyBroker - ProxyBroker is an open source tool that asynchronously finds public proxies from multiple sources and concurrently checks them.
[Documentation](https://proxybroker.readthedocs.io/)

    '''
        To install last stable release from pypi:
        .. code-block:: bash
        $ pip install proxybroker

        import asyncio
        from proxybroker import Broker

                async def show(proxies):
                while True:
                proxy = await proxies.get()
                if proxy is None: break
                print('Found proxy: %s' % proxy)

                proxies = asyncio.Queue()
                broker = Broker(proxies)
                tasks = asyncio.gather(
                broker.find(types=['HTTP', 'HTTPS'], limit=10),
                show(proxies))

                loop = asyncio.get_event_loop()
                loop.run_until_complete(tasks)
    '''

## Motivation

the project is an assignment in online courses [Devman](https://dvmn.org/modules/)

## Using
for the project to work, you need to configure environment variables in python, and name it environment.env
you write secret variables into it, and with the help of

    '''
         BOT_TOKEN='your token'
         DEVMAN_TOKEN='your token'
         DEVMAN_API = 'your API'
         CHAT_ID ='input youre chat id from telegram'
    '''
you extract it in the code with package
import os [more info](https://gist.github.com/dvmn-tasks/22b18aafb24a6be5213eb5c6532eaef8)
#### in module devman_bot.py

    '''
        import os

        bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'))
        devman_token = os.getenv('DEVMAN_TOKEN')
        get_chat_id = os.environ.get('CHAT_ID')
    '''

#### in module const.py

    '''
        import os

        headers = {'Authorization': f'Token {devman_token}'}
    '''

## Installation

set by launching telegram bot

## License

You may copy, distribute and modify the software
