# pages/calendars_page.py
import traceback
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, MoveTargetOutOfBoundsException
from pages.basepage import BasePage
from utils.screenshot import take_screenshot
from utils.logger import setup_logger

logger = setup_logger()
logger.info("Test started")

class CalendarsPage(BasePage):
    CALENDAR_FIELD = (By.ID, "g1065-selectorenteradate")
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='entry-content']//button[@type='submit'][normalize-space()='Submit']")