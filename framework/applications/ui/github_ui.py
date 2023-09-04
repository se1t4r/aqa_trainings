from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GitHubUI:
    
    def __init__(self, base_url, driver) -> None:
        self.base_url = base_url
        self.driver = driver

    def login(self, username, userpassword):
        self.driver.get(f"{self.base_url}/login")
        
        elem = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )
        elem.send_keys(username)

        elem = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        elem.send_keys(userpassword)

        elem.send_keys(Keys.RETURN)

        return True
    
    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title
    
    def login_alert_popup(self):
        try:
            alert_popup = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "js-flash-alert"))
            )
            print("Alert is shown")
        except TimeoutException:
            print("Alert NOT been shown")
            pass

    def logout(self):
        self.driver.get(f"{self.base_url}/logout")