# javascript_delays_page.py
from selenium.webdriver.common.by import By
from base_page import BasePage
from utils.waits import wait_for_element

class JavaScriptDelaysPage(BasePage):
    JAVASCRIPT_DELAYS_BUTTON = (By.LINK_TEXT, "JavaScript Delays")
    START_BUTTON = (By.ID, "start")
    DELAY_FIELD = (By.ID, "delay")

    def navigate_to_delays(self):
        self.click(self.JAVASCRIPT_DELAYS_BUTTON)

    def start_countdown(self):
        self.click(self.START_BUTTON)

    def verify_liftoff(self):
        element = wait_for_element(self.driver, self.DELAY_FIELD)
        assert_element_text(element, "Liftoff!")
