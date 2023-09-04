from config.config import Config
from applications.api.github_api import GitHubApi
from applications.api.github_api import PupLicapis
import pytest

@pytest.fixture(scope='session')
def github_api_client():
    github_api_client = GitHubApi(Config.base_url)
    
    yield github_api_client

@pytest.fixture(scope='session')
def service_api_client():
    service_api_client = PupLicapis(Config.bese_url_2)

    yield service_api_client


#comment for testing pull request