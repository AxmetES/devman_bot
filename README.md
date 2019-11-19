## Synopsis

this project adds notification functionality to the bot created in the telegram messenger by [Pyhton 3.6], added packages  (requests, telegram, os, proxybroker, asyncio)

## Code Example

telegram - a package that allows you to interact with the telegram messenger using the token that is specified in the module
'''
    import telegram
    bot = telegram.Bot(token=os.environ.get('BOT_TOKEN')
    [more information on python-telegram-bot ](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API)
'''

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
for the project to work, you need to configure environment variables in python, and name it [environment.env]
you write secret variables into it, and with the help of
    [BOT_TOKEN='your token'
     DEVMAN_TOKEN='your token'
     DEVMAN_API = 'your API']
 you extract it in the code with package
 [import os] [more info](https://gist.github.com/dvmn-tasks/22b18aafb24a6be5213eb5c6532eaef8)
     '''
        import os

        bot = telegram.Bot(token=os.environ.get('BOT_TOKEN'))
        # in module devman_bot.py
            devman_token = os.getenv('DEVMAN_TOKEN')

        # in module const.py
            headers = {'Authorization': f'Token {devman_token}'}
     '''

## Installation

set by launching telegram bot

## License

You may copy, distribute and modify the software
