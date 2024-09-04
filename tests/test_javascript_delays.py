# test_javascript_delays.py
import pytest
from selenium import webdriver
from pages.javascript_delays_page import JavaScriptDelaysPage
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

    # Navigate to the JavaScript Delays page if necessary
    # js_delays_page.navigate_to_delays()

    # Validate the current URL
    assert js_delays_page.get_current_url() == "https://practice-automation.com/javascript-delays/"
    logger.info("URL verification successful")

    # Start the countdown
    logger.info("Attempting to start countdown")
    js_delays_page.start_countdown()

    # Wait for countdown to complete
    sleep(15)

    # Verify the liftoff message
    logger.info("Verifying liftoff")
    js_delays_page.verify_liftoff()

    # Optional sleep to ensure all operations are completed
    sleep(3)
