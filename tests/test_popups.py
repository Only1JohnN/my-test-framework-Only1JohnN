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
    