# tests/test_popups_page.py
import pytest
from selenium import webdriver
from pages.popups_page import PopupsPage
from config.settings import Config
from time import sleep
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
    
    sleep(2)
    popups_page.verify_alert_message(expected_message="Hi there, pal!")
    popups_page.accept_alert()






    # Test confirm popup
    logger.info("Triggering confirm popup")
    confirm_popup_result = popups_page.find_element(popups_page.CONFIRM_POPUP_RESULT)
    

    
    #Scenario-1 : Click Ok
    popups_page.confirm_popup()
    popups_page.verify_alert_message(expected_message="OK or Cancel, which will it be?")
    popups_page.accept_alert()
    sleep(2)
    popups_page.assert_element_text(element=confirm_popup_result, expected_text="OK it is!")
    
    #Scenario-2 : Click Cancel
    popups_page.confirm_popup()
    popups_page.verify_alert_message(expected_message="OK or Cancel, which will it be?")
    popups_page.dismiss_alert()
    sleep(2)
    popups_page.assert_element_text(element=confirm_popup_result, expected_text="Cancel it is!")






    # Test prompt popup
    logger.info("Triggering prompt popup")
    prompt_popup_result = popups_page.find_element(popups_page.PROMPT_POPUP_RESULT)
    
    #Scenario-1 : Click Cancel without entering text    
    popups_page.prompt_popup()
    popups_page.verify_alert_message(expected_message="Hi there, what's your name?")
    popups_page.dismiss_alert()
    logger.info("Clicked Cancel without entering text")
    sleep(2)
    popups_page.assert_element_text(element=prompt_popup_result, expected_text="Fine, be that way...")
    
    
    #Scenario-2 : Click Ok without entering text
    popups_page.prompt_popup()
    popups_page.verify_alert_message(expected_message="Hi there, what's your name?")
    popups_page.accept_alert()
    logger.info("Clicked Ok without entering text")
    sleep(2)
    popups_page.assert_element_text(element=prompt_popup_result, expected_text="Fine, be that way...")
    
    
    #Scenario-3 : Click Cancel after entering text
    popups_page.prompt_popup()
    popups_page.verify_alert_message(expected_message="Hi there, what's your name?")
    entered_text = "Only1JohnN"
    popups_page.send_text_to_alert(entered_text)
    popups_page.dismiss_alert()
    logger.info("Clicked Cancel after entering text")
    sleep(2)
    popups_page.assert_element_text(element=prompt_popup_result, expected_text="Fine, be that way...")
    
    
    #Scenario-4 : Click Ok after entering text
    popups_page.prompt_popup()
    popups_page.verify_alert_message(expected_message="Hi there, what's your name?")
    entered_text = "Only1JohnN"
    popups_page.send_text_to_alert(entered_text)
    popups_page.accept_alert()
    logger.info("Clicked Ok after entering text")
    sleep(2)
    popups_page.assert_element_text(element=prompt_popup_result, expected_text=f"Nice to meet you,{entered_text}")






    # Test tooltip
    logger.info("Triggering tooltip")
    popups_page.tooltip()

    sleep(5)
