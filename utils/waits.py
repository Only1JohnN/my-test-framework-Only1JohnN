from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import Config
from utils.logger import js_delays_logger as logger

def wait_for_element(driver, locator, timeout=Config.TIMEOUT):
    """
    Waits for an element to be visible on the page.
    
    :param driver: WebDriver instance
    :param locator: Locator tuple (By, value)
    :param timeout: Maximum wait time in seconds
    :return: WebElement if found
    """
    try:
        logger.info(f"Waiting for element: {locator}")
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        logger.info(f"Element located: {locator}")
        return element
    except TimeoutException:
        logger.error(f"Timed out waiting for element: {locator}")
        raise

def wait_for_ajax(driver):
    """
    Waits for all AJAX requests to complete on the page.
    
    :param driver: WebDriver instance
    """
    try:
        WebDriverWait(driver, Config.TIMEOUT).until(
            lambda driver: driver.execute_script('return jQuery.active') == 0
        )
        logger.info("All AJAX requests have completed.")
    except TimeoutException:
        logger.error("Timed out waiting for AJAX requests to complete.")
        raise

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

def wait_for_element_clickable(driver, locator, timeout=Config.TIMEOUT):
    """
    Waits for an element to be clickable.
    
    :param driver: WebDriver instance
    :param locator: Locator tuple (By, value)
    :param timeout: Maximum wait time in seconds
    :return: WebElement if clickable
    """
    try:
        logger.info(f"Waiting for element to be clickable: {locator}")
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        logger.info(f"Element is clickable: {locator}")
        return element
    except TimeoutException:
        logger.error(f"Timed out waiting for element to be clickable: {locator}")
        raise

def wait_for_text_to_be_present(driver, locator, text, timeout=Config.TIMEOUT):
    """
    Waits for a specific text to be present in an element.
    
    :param driver: WebDriver instance
    :param locator: Locator tuple (By, value)
    :param text: Expected text to be present in the element
    :param timeout: Maximum wait time in seconds
    """
    try:
        logger.info(f"Waiting for element to be present: {locator}")
        WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
        logger.info(f"Text '{text}' is present in element {locator}")
    except TimeoutException:
        logger.error(f"Timed out waiting for text '{text}' in element {locator}")
        raise
