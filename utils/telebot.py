import requests

from datetime import datetime

from settings import Settings

settings = Settings()

class Telebot:
    def __init__(self):
        token = settings.telegram_token
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def enviar(self, log_type: str, msg: str):
        msg_envio = f'created_at={str(datetime.now()).split(".")[0]}--log_type={log_type}--{msg}'
        endpoint = f'{self.url_base}sendMessage?chat_id={settings.telegram_group}&text={msg_envio}'
        requests.get(endpoint)
