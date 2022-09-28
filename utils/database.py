import sqlite3
import json

from datetime import datetime

from Schema.payload import Payload_request

from settings import Settings
settings = Settings()


class Database:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(settings.database)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS data_lake (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                created_at TEXT NOT NULL,
                                user TEXT NOT NULL,
                                status_code_response INT NOT NULL,
                                api_bureau TEXT NOT NULL,
                                filters TEXT NOT NULL,
                                order_by TEXT NOT NULL,
                                data TEXT NOT NULL)'''
                            )    
    

    def fechar(self) -> None:
        self.conn.close()


    def inserir(self, payload_request: Payload_request, external_response: dict) -> dict:
        data = external_response.get('repos', [{}])
        status_code = external_response.get('status_code', 500)

        texto = 'INSERT INTO data_lake (created_at, user, status_code_response, api_bureau, filters, order_by, data) VALUES (?,?,?,?,?,?,?)'
        parametros = (
            str(datetime.today()).split('.')[0],
            payload_request.user,
            status_code,
            settings.api_name,
            str(payload_request.filter_list),
            payload_request.order_by,
            json.dumps(data)
        )

        try:
            res = self.cursor.execute(texto, parametros)
            cache_id = res.lastrowid
            self.conn.commit()
            res = {
                'cache_id': cache_id,
                'status_code': status_code,
                'msg': 'Sucesso', 
                'data': data,
                'from_cache': False,
                'msg': 'ok'
            }
        except Exception as e:
            res = {'error': str(e), 'cache_id': -1}
        
        return res
        

    def buscar(self, user: str, days_in_cache: int) -> dict:
        hoje = str(datetime.now()).split('.')[0]
        texto = f'''SELECT 
                        id,
                        status_code_response,
                        data
                    FROM 
                        data_lake 
                    WHERE 
                        user = "{user}" 
                        AND status_code_response = 200
                        AND ABS(JULIANDAY(created_at) - JULIANDAY("{hoje}")) <= {days_in_cache}
                    ORDER BY created_at DESC
                    LIMIT 1'''
        try:
            cache = self.cursor.execute(texto).fetchone()
            if cache:
                res = {
                    'cache_id': cache[0],
                    'status_code': cache[1],
                    'data': json.loads(cache[2]),
                    'from_cache': True,
                    'msg': 'ok'
                }
            else:
                res = {'cache_id': -1}
        except Exception as e:
            res = {'msg': str(e), 'cache_id': -1}
        
        return res
