import pytest
import requests


def test_user_exists(github_api_client):
    user = github_api_client.get_user('se1t4r')

    assert user['login'] == 'se1t4r'
    assert user['id'] == 102989181

def test_user_not_exists(github_api_client):
    with pytest.raises(requests.exceptions.HTTPError):
        user = github_api_client.get_user('se1tsssss4r')