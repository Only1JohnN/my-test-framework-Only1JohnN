# pages/form_fields_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from pages.basepage import BasePage
from utils.logger import setup_logger

logger = setup_logger()
logger.info("Test started")

class FormFieldsPage(BasePage):
    NAME_INPUT = (By.ID, "name-input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    DRINK_CHECKBOX = (By.CSS_SELECTOR, 'label[for="drink2"]')
    COLOR_CHECKBOX = (By.CSS_SELECTOR, 'label[for="color2"]')
    AUTOMATION_DROPDOWN = (By.NAME, "automation")
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_BOX = (By.ID, "message")
    SUBMIT_BUTTON = (By.CLASS_NAME, "custom_btn")

    
    def enter_name(self, name):
        element = self.wait_for_element_visible(self.NAME_INPUT)
        element.send_keys(name)
        logger.info(f"Entered name: {name}")

    def enter_password(self, password):
        element = self.wait_for_element_visible(self.PASSWORD_INPUT)
        element.send_keys(password)
        logger.info("Entered password")

    def select_favourite_drink(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.DRINK_CHECKBOX))
        )
        element.click()
        logger.info("Selected favourite drink")

    def select_favourite_color(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.COLOR_CHECKBOX))
        )
        element.click()
        logger.info("Selected favourite color")

    def select_automation(self, option):
        element = self.wait_for_element_visible(self.AUTOMATION_DROPDOWN)
        select = Select(element)
        select.select_by_visible_text(option)
        logger.info(f"Selected automation option: {option}")

    def enter_email(self, email):
        element = self.wait_for_element_visible(self.EMAIL_INPUT)
        element.send_keys(email)
        logger.info(f"Entered email: {email}")

    def enter_message(self, message):
        element = self.wait_for_element_visible(self.MESSAGE_BOX)
        element.send_keys(message)
        logger.info(f"Entered message: {message}")

    def submit_form(self):
        element = self.wait_for_element_clickable(self.SUBMIT_BUTTON)
        element.click()
        logger.info("Form submitted")

    def verify_alert_message(self, expected_message):
        try:
            alert = self.wait_for_alert_present()
            alert_text = alert.text
            assert alert_text == expected_message, f"Expected '{expected_message}', but got '{alert_text}'"
            logger.info(f"Alert message verification passed: '{expected_message}'")
        except NoAlertPresentException:
            logger.error("Alert is not present after form submission.")
            raise
        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            raise
        except Exception as e:
            logger.error(f"Error verifying alert message. Exception: {e}")
            raise