# base_page.py
from selenium.webdriver.common.by import By
from utils.waits import wait_for_element, wait_for_element_clickable
from utils.assertion import assert_element_text, assert_element_visible
from utils.logger import js_delays_logger as logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):
        element = wait_for_element_clickable(self.driver, locator)
        element.click()
        logger.info(f"Clicked on element: {locator}")

    def enter_text(self, locator, text):
        element = wait_for_element(self.driver, locator)
        element.clear()
        element.send_keys(text)
        logger.info(f"Entered text '{text}' in element: {locator}")

    def verify_text(self, locator, expected_text):
        element = wait_for_element(self.driver, locator)
        assert_element_text(element, expected_text)
    
    def verify_visibility(self, locator):
        element = wait_for_element(self.driver, locator)
        assert_element_visible(element)
