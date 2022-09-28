import json

from Schema.payload import Payload_response
from Schema.payload import Payload_request

from utils.database import Database
from utils.telebot import Telebot
from utils.validators import order_list
from utils.validators import filters
from utils.externals import get_github_repos


def verifica_cache(payload_request: Payload_request):
    payload_response = Payload_response()
    database = Database()

    try:
        cache = database.buscar(payload_request.user, payload_request.days_in_cache)
        if cache.get('cache_id') == -1:
            external_response = get_github_repos(payload_request.user)
            cache = database.inserir(payload_request, external_response)     
            database.fechar()       
    except Exception as e:
        cache = {
                'cache_id': -1,
                'status_code': 500,
                'data': [str(e)],
                'from_cache': False,
                'msg': 'cache error'
        }

    data = cache.get('data', [{}])

    data = order_list(
                        lista = filters(lista = data, filter_list = payload_request.filter_list),
                        ordem = payload_request.order_by,
                        text_field = payload_request.text_field
                    )

    payload_response.cache_id = cache.get('cache_id', -1)
    payload_response.status_code = cache.get('status_code', 500)
    payload_response.data = data
    payload_response.from_cache = cache.get('from_cache', False)
    payload_response.msg = cache.get('msg', 'full error')

    cache.pop('data', None)
    cache.pop('cache_id', None)

    log_msg = json.dumps(cache)

    telebot = Telebot()
    telebot.enviar(log_type='cache_response', msg=log_msg)

    return payload_response
