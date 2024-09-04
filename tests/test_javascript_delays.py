# test_javascript_delays.py
import pytest
from selenium import webdriver
from pages.javascript_delays_page import JavaScriptDelaysPage
from pages.basepage import BasePage
from config.settings import Config
from time import sleep
from utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL + "javascript-delays/")
    yield driver
    driver.quit()

def test_javascript_delays(driver):
    logger.info("Opened the JavaScript Delays page of the Website")
    js_delays_page = JavaScriptDelaysPage(driver)

    # Optional sleep to ensure page load (consider replacing with more robust wait)
    sleep(3)

    # Scroll to ensure the button is in view
    driver.execute_script("window.scrollTo(0, 400)")


    js_delays_page.assert_url_matches(expected_url="https://practice-automation.com/javascript-delays/")
    logger.info("URL verification successful")

    # Start the countdown
    logger.info("Attempting to start countdown")
    js_delays_page.start_countdown()

    # Wait for countdown to complete
    sleep(15)

    # Verify the liftoff message
    # logger.info("Verifying liftoff")
    # js_delays_page.verify_liftoff()

    # Optional sleep to ensure all operations are completed
    sleep(3)
