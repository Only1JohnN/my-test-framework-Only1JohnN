# tests/test_popups_page.py
import pytest
from selenium import webdriver
from pages.popups_page import PopupsPage
from config.settings import Config
from utils.logger import setup_logger

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

    # Test alert popup
    logger.info("Triggering alert popup")
    popups_page.alert_popup()
    popups_page.verify_alert_message(expected_message="Hi there, pal!")

    # Test confirm popup
    logger.info("Triggering confirm popup")
    popups_page.confirm_popup()

    # Test prompt popup
    logger.info("Triggering prompt popup")
    popups_page.prompt_popup()

    # Test tooltip
    logger.info("Triggering tooltip")
    popups_page.tooltip()

    # Optionally add asserts or additional verification here
