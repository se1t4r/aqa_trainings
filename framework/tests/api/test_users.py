from providers.data.users_provider import UserProvider
from config.config import Config
import pytest
import requests


# def test_http_status_code200(github_api_client):
#     r = requests.get('https://api.github.com/zen')

#     assert r.status_code == 200

def test_list_code200():
    r = requests.get(Config.bese_url_2)

    assert r.status_code == 200

# def test_user_exists(github_api_client):
#     user = UserProvider.existing_user_from_env()

#     api_user = github_api_client.get_user(user['login'])

#     assert api_user['login'] == user['login']
#     assert api_user['id'] == user['id']

def test_get_list(service_api_client):
    l = service_api_client.get_service(Config.path_entries)

    assert l['count'] > 0
    print(l['count'])
    assert l['entries'] is not None

def test_check_category(service_api_client):
    c = service_api_client.get_service(Config.path_entries)

    assert c['entries'][0]['Category'] == 'Animals'
    print(c['entries'][0]['Category'])

def test_random(service_api_client):
    r = service_api_client.get_service(Config.path_random)

    assert r['count'] == 1
    print(r['count'])
    print(r['entries'])

def test_check_health(service_api_client):
    h = service_api_client.get_service(Config.path_health)

    assert h['alive'] is True
    print(h['alive'])

# def test_user_not_exists(github_api_client):
#     user = UserProvider.fake_user()

#     with pytest.raises(requests.exceptions.HTTPError):
#         user = github_api_client.get_user(user['login'])