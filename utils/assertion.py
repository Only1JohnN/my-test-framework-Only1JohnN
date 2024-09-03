from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import Config
from utils.logger import setup_logger
logger = setup_logger()

def assert_element_text(element, expected_text):
    
    try:
        assert element.text == expected_text, f"Expected text '{expected_text}', but got '{element.text}'"
        logger.info(f"Assertion passed: Element text is '{expected_text}'")
    except AssertionError as e:
        logger.error(f"Assertion failed: {e}")
        raise
    
    """
    Asserts that the element's text matches the expected text.
    Logs success or raises an AssertionError if the assertion fails.
    """


def wait_for_attribute(driver, locator, attribute, value, timeout=Config.TIMEOUT):
    """
    Waits for an element's attribute to match the specified value.
    
    :param driver: WebDriver instance
    :param locator: Locator tuple (By, value)
    :param attribute: The attribute to check
    :param value: The expected attribute value
    :param timeout: Maximum wait time in seconds
    """
    try:
        logger.info(f"Waiting for element: {locator}")
        WebDriverWait(driver, timeout).until(
            EC.attribute_to_be(locator, attribute, value)
        )
        logger.info(f"Element {locator} has attribute '{attribute}' with value '{value}'")
    except TimeoutException:
        logger.error(f"Timeout waiting for attribute '{attribute}' to be '{value}' on element {locator}")
        raise
    

def assert_element_visible(element):
    
    try:
        assert element.is_displayed(), "Element is not visible on the page"
        logger.info("Assertion passed: Element is visible")
    except AssertionError as e:
        logger.error(f"Assertion failed: {e}")
        raise
    
    """
    Asserts that the element is visible on the page.
    Logs success or raises an AssertionError if the element is not visible.
    """



def assert_url_matches(driver, expected_url):
    
    try:
        assert driver.current_url == expected_url, f"Expected URL '{expected_url}', but got '{driver.current_url}'"
        logger.info(f"Assertion passed: URL matches '{expected_url}'")
    except AssertionError as e:
        logger.error(f"Assertion failed: {e}")
        raise
    
    """
    Asserts that the current URL matches the expected URL.
    Logs success or raises an AssertionError if the URLs do not match.
    """