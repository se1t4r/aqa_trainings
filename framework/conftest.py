from config.config import Config
from applications.api.github_api import GitHubApi
from applications.ui.github_ui import GitHubUI
from applications.api.github_api import PupLicapis
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture(scope='session')
def github_api_client():
    github_api_client = GitHubApi(Config.base_url_api)
    
    yield github_api_client

@pytest.fixture(scope='session')
def service_api_client():
    service_api_client = PupLicapis(Config.bese_url_2)

    yield service_api_client


@pytest.fixture(scope='session')
def github_ui_client():
    driver = webdriver.Chrome(
        service = Service(r"/home/liza/Desktop/Serik/aqa/framework/chromedriver")
    )
    github_ui_client = GitHubUI(Config.base_url_ui, driver)

    yield github_ui_client

    github_ui_client.close_browser()