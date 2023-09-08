from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys


class PageLogin:
    def __init__(self, driver, base_url) -> None:
        self.driver = driver
        self.login_url = base_url + "/login"

    @property
    def login_field(self):
        # step1: wait and find
        # step2: validate field
        return self.driver.find_element(By.ID, "login_field")

    @property
    def pass_field(self):
        return self.driver.find_element(By.ID, "password")

    @property
    def login_btn(self):
        return self.driver.find_element(By.NAME, "commit")

    @property
    def signup_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Create an account")

    def navigate(self):
        self.driver.get(self.login_url)

    def login(self, username, password):
        self.navigate()

        self.login_field.send_keys(username)
        self.pass_field.send_keys(password)

        self.login_btn.click()

        if self.is_login_ok():
            return True

        return False

    def forgot_password(self):
        pass

    def proceed_to_signup_page(self):
        self.signup_link.click()
        # return PageSignUP()
        return True

    def is_login_ok(self):
        # should be validated if user logged in or not
        return True
