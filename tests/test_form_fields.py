# tests/test_form_fields.py
import pytest
from selenium import webdriver
from pages.form_fields_page import FormFieldsPage
from time import sleep
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
    
    driver.execute_script("window.scrollTo(0, 400)")
    sleep(2)
    form_fields_page.select_favourite_drink()
    
    
    sleep(2)
    form_fields_page.select_favourite_color()
    
    
    driver.execute_script("window.scrollTo(0, 800)")
    sleep(2)
    form_fields_page.select_automation("Yes")
    form_fields_page.enter_email("sample@mail.com")
    
    
    driver.execute_script("window.scrollTo(0, 1200)")
    sleep(2)
    form_fields_page.enter_message("This is just a basic flow for automation testing")
    
    sleep(2)
    form_fields_page.submit_form()
    
    sleep(2)
    form_fields_page.verify_alert_message(expected_message="Message received!")
    sleep(3)
