# javascript_delays_page.py
import traceback
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utils.logger import setup_logger
from utils.screenshot import take_screenshot

logger = setup_logger('javascript_delays_page')
logger.info("Test started")

class JavaScriptDelaysPage(BasePage):
    JAVASCRIPT_DELAYS_BUTTON = (By.LINK_TEXT, "JavaScript Delays")
    START_BUTTON = (By.XPATH, "//button[@id='start']")
    DELAY_FIELD = (By.CSS_SELECTOR, "#delay")

    def navigate_to_delays(self):
        try:
            self.wait_for_element_clickable(self.JAVASCRIPT_DELAYS_BUTTON)
            self.click(self.JAVASCRIPT_DELAYS_BUTTON)
            logger.info("Navigated to JavaScript Delays page")
        except TimeoutException:
            logger.error("Element not found or not clickable within timeout")
            self.take_screenshot('navigate_to_delays_error')
        except NoSuchElementException:
            logger.error("Element not found on the page")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise
        

    def start_countdown(self):
        try:
            self.wait_for_element_clickable(self.START_BUTTON)
            self.click(self.START_BUTTON)
            logger.info("Started countdown")
        except TimeoutException:
            logger.error("Element not found or not clickable within timeout")
            self.take_screenshot('start_countdown')
        except NoSuchElementException:
            logger.error("Element not found on the page")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise


    def verify_liftoff(self):
        try:
            element = self.wait_for_attribute(self.DELAY_FIELD, attribute="value", value="Liftoff!")
            self.assert_element_text(element, "Liftoff!")
            logger.info("Liftoff verification successful")
        except AssertionError:
            logger.error("Liftoff message did not match the expected value")
            raise
        except Exception as e:
            logger.error(f"Error verifying liftoff message. Exception: {e}")
            raise
