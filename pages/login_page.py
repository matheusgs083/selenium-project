import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_btn_press = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//h3[@data-test='error']")
        self.sucess_message = (By.XPATH, '//*[@id="inventory_filter_container"]/div')

    def login(self, user, password):

        self.write(self.username_field, user)
        self.write(self.password_field, password)
        self.click(self.login_btn_press)

    def login_error(self):
        self.is_displayed(self.error_message_login)

    def login_sucess(self):
        self.is_displayed(self.sucess_message)

    def check_text(self, text):
        text_finded = self.check_text(self.error_message_login)
        assert text_finded == text, f"Expected text '{text}' not found, found '{text_finded}'"