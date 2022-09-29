

from settings import Settings

settings = Settings()

def return_homepage(request, user: str, data_list: list):
    msg =  f'Github Repositories from user: {user}'
    new_data_list = []
    for item in data_list:
        temp = {
            'id': item.get('id', -1),
            'name': item.get('name', 'error'),
            'description': item.get('description', 'empy'),
            'visibility': item.get('visibility', 'error'),
            'language': item.get('language', 'empy'),
            'created_at': item.get('created_at', 'error').replace('Z', ''),
            'updated_at': item.get('updated_at', 'error').replace('Z', ''),
            'url': item.get('url', 'empy').replace('api.', '').replace('/repos', '')
        }
        new_data_list.append(temp)

    data = {
            'request': request, 
            'title': 'searcher', 
            'msg': msg, 
            'data': new_data_list
            }
    return settings.template.TemplateResponse(name='homepage.html', context=data)
