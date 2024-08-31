# test_javascript_delays.py
import pytest
from selenium import webdriver
from javascript_delays_page import JavaScriptDelaysPage
from config.settings import Config

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH)
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_javascript_delays(driver):
    js_delays_page = JavaScriptDelaysPage(driver)
    
    js_delays_page.navigate_to_delays()
    js_delays_page.start_countdown()
    js_delays_page.verify_liftoff()
