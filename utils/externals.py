import requests

def get_github_repos(user: str) -> dict:
    url = f'https://api.github.com/users/{user}/repos'

    res = {}
    try:
        consult = requests.get(url=url)
        res['status_code'] = consult.status_code
        res['repos'] = consult.json()
    except Exception as e:
        res['status_code'] = 500
        res['repos'] = [{'error': str(e)}]

    return res
