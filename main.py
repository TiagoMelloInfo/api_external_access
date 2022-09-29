import os

from fastapi import FastAPI
from fastapi import Request

from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse

from utils.middleware import autenticador
from utils.cache import verifica_cache
from utils.homepage import return_homepage

from Schema.payload import Payload_request
from Schema.payload import Payload_response

from settings import Settings

settings = Settings()
app = FastAPI(title=settings.api_name, version=settings.api_version)

post_description = f'{settings.order_by_accepts}<br><br>{settings.filter_list_accepts}'

@app.middleware('http')
async def intermediador(request: Request, call_next):
    return await call_next(request) if autenticador(request) else JSONResponse(
                    status_code=403, content={'msg': 'Authentication failed'})
    
    
@app.post(path=f'/{settings.api_name}', response_model=Payload_response, description=post_description)
async def main(payload: Payload_request):
    return verifica_cache(payload)


@app.get('/pesquisar/{user}', response_class=HTMLResponse)
async def homepage(request: Request, user: str):
    payload = Payload_request(user=user)
    data_list = verifica_cache(payload).data
    return return_homepage(request=request, user=user, data_list=data_list)


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', 
    port=8000, log_level='info', reload=True,
    debug=True)

