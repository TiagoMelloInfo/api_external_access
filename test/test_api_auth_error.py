import requests

url = 'http://localhost:8000/github'

headers = {'user': 'tdd'}
payload = {}

res = requests.post(url=url, headers=headers, json=payload)
status_code = res.status_code
mock = res.json()

print(status_code)
print(mock)

def test_status_code_1():
    assert status_code == 403

def test_response_loc_1():
    assert mock.get('msg') == 'Authentication failed'


