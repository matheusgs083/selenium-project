import conftest
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self):
        self.driver = conftest.driver

    def login(self, user, password):
        self.login_box = driver.find_element(By.XPATH, '//input[@id="user-name"]')
        self.pasword_box = driver.find_element(By.XPATH, '//input[@id="password"]')
        self.login_btn = driver.find_element(By.XPATH, '//input[@id="login-button"]')

        self.login_box.send_keys(user)
        self.password_box.send_keys(password)
        self.login_btn.click()


