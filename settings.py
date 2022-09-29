from os import path
from decouple import config

from fastapi.templating import Jinja2Templates

class Settings:
    api_name = config('API_NAME')
    api_version = config('API_VERSION')
    token = config('TOKEN')
    endpoints_permitidos = ('docs', 'redoc', 'openapi.json', 'pesquisar')
    database = config('DATABASE')
    
    telegram_token = config('TELEGRAM_TOKEN')
    telegram_group = config('TELEGRAM_GROUP')

    dirname = path.dirname(__file__)
    template = Jinja2Templates(directory=path.join(dirname, 'templates'))

    order_by_accepts = '''<h2>order_by</h2>
                          <b>Accepts:</b> id, node_id, name, full_name, private, owner, description,
                          fork, created_at, updated_at, pushed_at, homepage, size, stargazers_count, watchers_count,
                          language, has_issues, has_project, has_downloads, has_wiki, has_pages, forks_count, archived
                          disabled, open_issues_count, license, allow_forking, is_template, web_commit_signoff_required,
                          topics, visibility, forks, open_issues, watchers, default_branch
                          <br><b>Default value</b> = "name"'''

    filter_list_accepts = '''<h2>filter_list</h2>
                             <b>Accepts:</b> private, fork, has_issues, has_projects, has_downloads, 
                             has_wiki, has_pages, archived, disabled, allow_forking, is_template, web_commit_signoff_required 
                             <br><b>Default value</b> = []'''

