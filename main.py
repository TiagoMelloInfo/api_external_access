from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from utils.middleware import autenticador
from utils.cache import verifica_cache
from Schema.payload import Payload_request
from Schema.payload import Payload_response

from settings import Settings

app = FastAPI()
settings = Settings()

@app.middleware('http')
async def intermediador(request: Request, call_next):
    return await call_next(request) if autenticador(request) else JSONResponse(
                    status_code=403, content={'msg': 'Authentication failed'})
    
    
@app.post(f'/{settings.api_name}', response_model=Payload_response)
async def main(payload: Payload_request):
    return verifica_cache(payload)


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', 
    port=8000, log_level='info', reload=True,
    debug=True)

