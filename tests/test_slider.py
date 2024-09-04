# tests/test_slider_page.py
import pytest
from selenium import webdriver
from pages.slider_page import SliderPage
from config.settings import Config
from time import sleep
from utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL + "slider/")
    yield driver
    driver.quit()

def test_slider_page(driver):
    slider_page = SliderPage(driver)

    logger.info("Opened the Slider page of the Website")


    # Move the slider to the desired value
    slider_page.move_slider_to_value(50)
    sleep(2)

    # Get the current slider value
    current_value = slider_page.get_slider_value()

    # Verify that the slider value is correct
    assert current_value == '50', f"Expected slider value to be '50', but got '{current_value}'"
    print(f"Slider is set to the correct value: {current_value}")
