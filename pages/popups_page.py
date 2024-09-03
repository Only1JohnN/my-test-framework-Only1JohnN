# pages/popups_page.py
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from pages.basepage import BasePage
from utils.screenshot import take_screenshot
from utils.waits import wait_for_element_clickable
from utils.logger import setup_logger
logger = setup_logger()

class PopupsPage(BasePage):
    ALERT_POPUP = (By.XPATH, "//b[normalize-space()='Alert Popup']")
    CONFIRM_POPUP = (By.XPATH, "//b[normalize-space()='Confirm Popup']")
    CONFIRM_POPUP_RESULT = (By.ID, "confirmResult")
    PROMPT_POPUP = (By.ID, "prompt")
    PROMPT_POPUP_RESULT = (By.ID, "promptResult")
    CLICK_ME_TO_SEE_A_TOOLTIP = (By.CLASS_NAME, "tooltip_1")
    CLICK_ME_TO_SEE_A_TOOLTIP_RESULT = (By.ID, "myTooltip")
    
    def alert_popup(self):
        try:
            wait_for_element_clickable(self.driver, self.ALERT_POPUP)
            self.click(self.ALERT_POPUP)
        except TimeoutException:
            logger.error("Element not found or not clickable within timeout")
            take_screenshot(self.driver, folder='screenshots', filename='alert_popup')
        except NoSuchElementException:
            logger.error("Element not found on the page")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            traceback.print_exc()
    
    
    def confirm_popup(self):
        try:
            wait_for_element_clickable(self.driver, self.CONFIRM_POPUP)
            self.click(self.CONFIRM_POPUP)
        except TimeoutException:
            logger.error("Element not found or not clickable within timeout")
            take_screenshot(self.driver, folder='screenshots', filename='confirm_popup')
        except NoSuchElementException:
            logger.error("Element not found on the page")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            traceback.print_exc()


    def prompt_popup(self):
        try:
            wait_for_element_clickable(self.driver, self.PROMPT_POPUP)
            self.click(self.PROMPT_POPUP)
        except TimeoutException:
            logger.error("Element not found or not clickable within timeout")
            take_screenshot(self.driver, folder='screenshots', filename='confirm_popup')
        except NoSuchElementException:
            logger.error("Element not found on the page")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            traceback.print_exc()
            

    def tooltip(self):
        try:
            wait_for_element_clickable(self.driver, self.CLICK_ME_TO_SEE_A_TOOLTIP)
            self.click(self.CLICK_ME_TO_SEE_A_TOOLTIP)
        except TimeoutException:
            logger.error("Element not found or not clickable within timeout")
            take_screenshot(self.driver, folder='screenshots', filename='tooltip_popup')
        except NoSuchElementException:
            logger.error("Element not found on the page")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            traceback.print_exc()
            
    def verify_alert_message(self, expected_message):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            assert alert_text == expected_message, f"Expected '{expected_message}', but got '{alert_text}'"
        except NoAlertPresentException:
            raise AssertionError("Alert is not present after the form submission.")
    
    
