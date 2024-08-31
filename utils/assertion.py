from selenium.common.exceptions import NoSuchElementException
from utils.logger import js_delays_logger as logger

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