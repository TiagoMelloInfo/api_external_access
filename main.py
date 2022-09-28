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

order_by_accepts = '<h2>order_by</h2><b>Accepts:</b> id, node_id, name, full_name, private, owner, description, \
    fork, created_at, updated_at, pushed_at, homepage, size, stargazers_count, watchers_count, \
        language, has_issues, has_project, has_downloads, has_wiki, has_pages, forks_count, archived,\
             disabled, open_issues_count, license, allow_forking, is_template, web_commit_signoff_required, \
                topics, visibility, forks, open_issues, watchers, default_branch \
                    <br><b>Default value</b> = "name"'


filter_list_accepts = '<h2>filter_list</h2><b>Accepts:</b> private, fork, has_issues, has_projects, has_downloads, \
    has_wiki, has_pages, archived, disabled, allow_forking, is_template, web_commit_signoff_required \
        <br><b>Default value</b> = []'

description = f'{order_by_accepts}<br><br>{filter_list_accepts}'

@app.middleware('http')
async def intermediador(request: Request, call_next):
    return await call_next(request) if autenticador(request) else JSONResponse(
                    status_code=403, content={'msg': 'Authentication failed'})
    
    
@app.post(path=f'/{settings.api_name}', response_model=Payload_response, 
          description=description)
async def main(payload: Payload_request):
    return verifica_cache(payload)


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', 
    port=8000, log_level='info', reload=True,
    debug=True)

