# javascript_delays_page.py
import traceback
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utils.assertion import assert_element_text
from utils.waits import wait_for_element, wait_for_element_clickable
from utils.logger import js_delays_logger
from utils.screenshot import take_screenshot

class JavaScriptDelaysPage(BasePage):
    JAVASCRIPT_DELAYS_BUTTON = (By.LINK_TEXT, "JavaScript Delays")
    START_BUTTON = (By.XPATH, "//button[@id='start']")
    DELAY_FIELD = (By.CSS_SELECTOR, "#delay")

    def navigate_to_delays(self):
        try:
            wait_for_element_clickable(self.driver, self.JAVASCRIPT_DELAYS_BUTTON)
            self.click(self.JAVASCRIPT_DELAYS_BUTTON)
        except TimeoutException:
            js_delays_logger.error("Element not found or not clickable within timeout")
            take_screenshot(self.driver, folder='screenshots', filename='navigate_to_delays_error')
        except NoSuchElementException:
            js_delays_logger.error("Element not found on the page")
        except Exception as e:
            js_delays_logger.error(f"An unexpected error occurred: {e}")
            traceback.print_exc()
        

    def start_countdown(self):
        try:
            wait_for_element_clickable(self.driver, self.START_BUTTON)
            self.click(self.START_BUTTON)
        except TimeoutException:
            js_delays_logger.error("Element not found or not clickable within timeout")
            take_screenshot(self.driver, folder='screenshots', filename='start_countdown')
        except NoSuchElementException:
            js_delays_logger.error("Element not found on the page")
        except Exception as e:
            js_delays_logger.error(f"An unexpected error occurred: {e}")
            traceback.print_exc()

    def verify_liftoff(self):
        element = wait_for_element(self.driver, self.DELAY_FIELD)
        assert_element_text(element, "Liftoff!")
