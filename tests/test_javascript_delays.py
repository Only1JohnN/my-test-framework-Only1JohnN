# test_javascript_delays.py
import pytest
from selenium import webdriver
from pages.javascript_delays_page import JavaScriptDelaysPage
from config.settings import Config
from selenium.webdriver.common.by import By
from time import sleep
from utils.logger import js_delays_logger
from utils.waits import wait_for_text_to_be_present
from utils.assertion import assert_url_matches

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_javascript_delays(driver):
    js_delays_logger.info("Opened the Website")
    js_delays_page = JavaScriptDelaysPage(driver)
    sleep(3)
    
    # driver.execute_script("window.scrollTo(0, 250)")

    # js_delays_logger.info("Attempting to click the JavaScript Delays button")
    # js_delays_page.navigate_to_delays()
    # sleep(10)
    
    # wait_for_text_to_be_present(driver, (By.LINK_TEXT, "Home"), "Home")
    
    assert_url_matches(driver, "https://practice-automation.com/javascript-delays/")
    
    js_delays_logger.info("Attempting to start countdown")
    js_delays_page.start_countdown()
    sleep(3)

    js_delays_logger.info("Verifying liftoff")
    js_delays_page.verify_liftoff()
    sleep(3)
