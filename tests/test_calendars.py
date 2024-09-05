# tests/test_calendars.py
import pytest
from selenium import webdriver
from pages.calendars_page import CalendarsPage
from config.settings import Config
from time import sleep
from utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL + "calendars/")
    yield driver
    driver.quit()

def test_calendars_page(driver):
    slider_page = CalendarsPage(driver)

    logger.info("Opened the Calendars page of the Website")