import pytest   

from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.loginfailed
class TestLogin:
    def test_login(self, setup_teardown):
        login_page = LoginPage(setup_teardown)

        login_page.login("standard_user", "secret_saaaaauce")

        login_page.login_error()
