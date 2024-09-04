# tests/test_form_fields.py
import pytest
from selenium import webdriver
from pages.form_fields_page import FormFieldsPage
from config.settings import Config
from utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL + "form-fields/")
    yield driver
    driver.quit()

def test_form_fields(driver):
    form_fields_page = FormFieldsPage(driver)
    
    logger.info("Opened the Form fields page of the Website")
    
    form_fields_page.enter_name("Adeniyi John")
    form_fields_page.enter_password("password123")
    
    form_fields_page.select_favourite_drink()
    form_fields_page.select_favourite_color()
    
    form_fields_page.select_automation("Yes")
    form_fields_page.enter_email("sample@mail.com")
    form_fields_page.enter_message("This is just a basic flow for automation testing")
    
    form_fields_page.submit_form()
    
    form_fields_page.verify_alert_message("Message received!")
