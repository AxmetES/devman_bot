import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    tg_token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    devman_token = os.getenv('DEVMAN_TOKEN')


settings = Settings()
