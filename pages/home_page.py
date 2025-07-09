import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")

    def login_sucessful(self):
        self.is_displayed(self.page_title)