import conftest
from selenium.webdriver.common.by import By
from selenium import webdriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_btn_press = (By.ID, "login-button")

    def login(self, user, password):

        self.write(self.username_field, user)
        self.write(self.password_field, password)
        self.click(self.login_btn_press)


