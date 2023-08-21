import requests

def test_http_status_code_200():
    resp = requests.get('https://api.github.com/users/se1t4r')
    assert resp.json()['login'] == 'se1t4r'
    assert resp.json()['id'] == 102989181

def test_user_exists():
    resp = requests.get('https://api.github.com/users/se1t4r')
    assert resp.status_code == 200

def test_user_non_exists():
    resp = requests.get('https://api.github.com/users/asklfj12412asdkl')
    assert resp.status_code == 404
    assert resp.json()['message'] == 'Not Found'