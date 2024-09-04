# pages/form_fields_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, ElementNotInteractableException
from pages.basepage import BasePage
from utils.logger import setup_logger

logger = setup_logger('form_fields_page')
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

    def scroll_to_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        except Exception as e:
            logger.error(f"Error scrolling to element: {element}. Exception: {e}")

    def enter_name(self, name):
        element = self.wait_for_element_visible(self.NAME_INPUT)
        element.send_keys(name)
        self.logger.info(f"Entered name: {name}")

    def enter_password(self, password):
        element = self.wait_for_element_visible(self.PASSWORD_INPUT)
        element.send_keys(password)
        self.logger.info("Entered password")

    def select_favourite_drink(self):
        element = self.wait_for_element_clickable(self.DRINK_CHECKBOX)
        element.click()
        self.logger.info("Selected favourite drink")

    def select_favourite_color(self):
        element = self.wait_for_element_clickable(self.COLOR_CHECKBOX)
        element.click()
        self.logger.info("Selected favourite color")

    def select_automation(self, option):
        element = self.wait_for_element_visible(self.AUTOMATION_DROPDOWN)
        select = Select(element)
        select.select_by_visible_text(option)
        self.logger.info(f"Selected automation option: {option}")

    def enter_email(self, email):
        element = self.wait_for_element_visible(self.EMAIL_INPUT)
        element.send_keys(email)
        self.logger.info(f"Entered email: {email}")

    def enter_message(self, message):
        element = self.wait_for_element_visible(self.MESSAGE_BOX)
        element.send_keys(message)
        self.logger.info(f"Entered message: {message}")

    def submit_form(self):
        element = self.wait_for_element_clickable(self.SUBMIT_BUTTON)
        element.click()
        self.logger.info("Form submitted")

    def verify_alert_message(self, expected_message):
        try:
            alert = self.wait_for_alert_present()
            alert_text = alert.text
            self.wait_for_text_to_be_present(alert_text, expected_message)
            assert alert_text == expected_message, f"Expected '{expected_message}', but got '{alert_text}'"
            self.logger.info(f"Alert message verification passed: '{expected_message}'")
        except NoAlertPresentException:
            self.logger.error("Alert is not present after form submission.")
            raise
        except AssertionError as e:
            self.logger.error(f"Assertion failed: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Error verifying alert message. Exception: {e}")
            raise