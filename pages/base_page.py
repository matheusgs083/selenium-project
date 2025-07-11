import conftest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def write(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def is_displayed(self, locator):
        assert self.find_element(locator).is_displayed(), f"element {locator}, not finded"

    def element_text(self, locator):
        self.find_element(locator).text

    def wait_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))
    
    def verify_existence(self, locator):
        assert self.find_element(locator), f"Element {locator} not found on the page, but it should be present."
    
    def not_verify_existence(self, locator):
        assert not self.find_element(locator), f"Element {locator} should not be present on the page, but it was found."

    def double_click(self, locator):
        element = self.find_element(locator)
        action = self.driver.action_chains.ActionChains(self.driver)
        action.double_click(element).perform()

    def right_click(self, locator):
        element = self.find_element(locator)
        action = self.driver.action_chains.ActionChains(self.driver)
        action.context_click(element).perform()
    
    def press_keys(self, locator, keys):
        element = self.find_element(locator)
        element.send_keys(keys)
