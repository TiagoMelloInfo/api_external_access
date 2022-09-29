import requests

url = 'http://localhost:8000/github'

headers = {'user': 'tdd', 'token': 'abc'}
payload = {'user': 'TiagoMelloInfo'}

#Scene 2
res = requests.post(url=url, headers=headers, json=payload)

status_code = res.status_code
mock = res.json()
data = mock.get('data', [{}])

def test_has_id_cache():
    assert 'cache_id' in mock.keys()

def test_cache_id_response():
    assert mock.get('cache_id', -1) > 0

def test_has_status_code():
    assert 'status_code' in mock.keys()

def test_data_response():
    assert len(data) > 0

def test_has_data_id():
    assert 'id' in data[0].keys()

def test_data_id_response():
    assert data[0].get('id', -1) > 0

def test_user_in_fullname():
    assert payload.get('user', '') in data[0].get('full_name', '')
