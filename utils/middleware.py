import json

from fastapi import Request

from settings import Settings
from utils.telebot import Telebot

settings = Settings()
def autenticador(request: Request):
    token = request.headers.get('token', '')
    user = request.headers.get('user', '')
    endpoint = str(request.url).split('/')[3]
    auth_res = token == settings.token

    telebot = Telebot()
    msg = json.dumps({'auth_res': auth_res,'endpoint_access': endpoint, 'user': user})
    telebot.enviar(log_type='auth', msg=msg)

    if endpoint in settings.endpoints_permitidos:
        return True
    else:
        return auth_res
    