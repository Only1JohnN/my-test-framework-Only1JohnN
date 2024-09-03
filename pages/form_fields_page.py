# pages/form_fields_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from pages.basepage import BasePage

class FormFieldsPage(BasePage):
    NAME_INPUT = (By.ID, "name-input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    DRINK_CHECKBOX = (By.CSS_SELECTOR, 'label[for="drink2"]')
    COLOR_CHECKBOX = (By.CSS_SELECTOR, 'label[for="color2"]')
    AUTOMATION_DROPDOWN = (By.NAME, "automation")
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_BOX = (By.ID, "message")
    SUBMIT_BUTTON = (By.CLASS_NAME, "custom_btn")

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def select_favourite_drink(self):
        self.driver.find_element(*self.DRINK_CHECKBOX).click()

    def select_favourite_color(self):
        self.driver.find_element(*self.COLOR_CHECKBOX).click()

    def select_automation(self, option):
        select = Select(self.driver.find_element(*self.AUTOMATION_DROPDOWN))
        select.select_by_visible_text(option)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def enter_message(self, message):
        self.driver.find_element(*self.MESSAGE_BOX).send_keys(message)

    def submit_form(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def verify_alert_message(self, expected_message):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            assert alert_text == expected_message, f"Expected '{expected_message}', but got '{alert_text}'"
        except NoAlertPresentException:
            raise AssertionError("Alert is not present after the form submission.")
