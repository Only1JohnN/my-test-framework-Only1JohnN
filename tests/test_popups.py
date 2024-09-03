# tests/test_popups_page.py
import pytest
from selenium import webdriver
from pages.popups_page import PopupsPage
from config.settings import Config
from utils.logger import setup_logger
from time import sleep
logger = setup_logger()

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL + "popups/")
    yield driver
    driver.quit()
    
def test_popups_page(driver):
    popups_page = PopupsPage(driver)
    
    logger.info("Opened the Popups page of the Website")
    popups_page.alert_popup()
    popups_page.verify_alert_message("Hi there, pal!")
    popups_page.confirm_popup
    