from applications.ui.pages.page_login import PageLogin


class GitHubUI:
    def __init__(self, base_url, driver) -> None:
        self.base_url = base_url
        self.driver = driver

        self.login_page = PageLogin(self.driver, self.base_url)

    def login(self, username, userpassword):
        return self.login_page.login(username, userpassword)

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title

    # def login_alert_popup(self):
    #     try:
    #         alert_popup = WebDriverWait(self.driver, 1).until(
    #             EC.presence_of_element_located((By.CLASS_NAME, "js-flash-alert"))
    #         )
    #         print("Alert is shown")
    #     except TimeoutException:
    #         print("Alert NOT been shown")
    #         pass

    # def logout(self):
    #     self.driver.get(f"{self.base_url}/logout")
