from config.config import Config
from applications.api.github_api import GitHubApi
import pytest

@pytest.fixture(scope='session')
def github_api_client():
    github_api_client = GitHubApi(Config.base_url)
    
    yield github_api_client

    print("END-UP TEST")