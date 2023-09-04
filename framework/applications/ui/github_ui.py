from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GitHubUI:
    
    def __init__(self, base_url, path, driver) -> None:
        self.base_url = base_url
        self.path = path
        self.driver = driver

    def login(self, username, userpassword):
        self.driver.get(f"{self.base_url}{self.path}")
        
        elem = self.driver.find_element(By.ID, "login_field")
        elem.send_keys(username)

        elem = self.driver.find_element(By.ID, "password")
        elem.send_keys(userpassword)

        elem.send_keys(Keys.RETURN)

        return True
    
    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title