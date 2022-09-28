from decouple import config

class Settings:
    api_name = config('API_NAME')
    token = config('TOKEN')
    endpoints_permitidos = ('docs', 'redoc', 'openapi.json')
    database = config('DATABASE')
    
    telegram_token = config('TELEGRAM_TOKEN')
    telegram_group = config('TELEGRAM_GROUP')
