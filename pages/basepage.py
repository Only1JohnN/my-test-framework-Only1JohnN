# base_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import Config
from utils.logger import setup_logger

logger = setup_logger()

class BasePage:
    def __init__(self, driver):
        self.driver = driver






    # Element Interaction Methods
    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()
        logger.info(f"Clicked on element: {locator}")

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
        logger.info(f"Entered text '{text}' in element: {locator}")

    def verify_text(self, locator, expected_text):
        element = self.wait_for_element(locator)
        self.assert_element_text(element, expected_text)

    def verify_visibility(self, locator):
        element = self.wait_for_element(locator)
        self.assert_element_visible(element)






    # Wait Methods
    def wait_for_element(self, locator, timeout=Config.TIMEOUT):
        """
        Waits for an element to be visible on the page.
        
        :param locator: Locator tuple (By, value)
        :param timeout: Maximum wait time in seconds
        :return: WebElement if found
        """
        try:
            logger.info(f"Waiting for element: {locator}")
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            logger.info(f"Element located: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Timed out waiting for element: {locator}")
            raise

    def wait_for_element_clickable(self, locator, timeout=Config.TIMEOUT):
        """
        Waits for an element to be clickable.
        
        :param locator: Locator tuple (By, value)
        :param timeout: Maximum wait time in seconds
        :return: WebElement if clickable
        """
        try:
            logger.info(f"Waiting for element to be clickable: {locator}")
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            logger.info(f"Element is clickable: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Timed out waiting for element to be clickable: {locator}")
            raise

    def wait_for_ajax(self, timeout=Config.TIMEOUT):
        """
        Waits for all AJAX requests to complete on the page.
        
        :param timeout: Maximum wait time in seconds
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script('return jQuery.active') == 0
            )
            logger.info("All AJAX requests have completed.")
        except TimeoutException:
            logger.error("Timed out waiting for AJAX requests to complete.")
            raise

    def wait_for_attribute(self, locator, attribute, value, timeout=Config.TIMEOUT):
        """
        Waits for an element's attribute to match the specified value.
        
        :param locator: Locator tuple (By, value)
        :param attribute: The attribute to check
        :param value: The expected attribute value
        :param timeout: Maximum wait time in seconds
        """
        try:
            logger.info(f"Waiting for element: {locator}")
            WebDriverWait(self.driver, timeout).until(
                EC.attribute_to_be(locator, attribute, value)
            )
            logger.info(f"Element {locator} has attribute '{attribute}' with value '{value}'")
            return self.driver.find_element(*locator)  # Return the element for further operations
        except TimeoutException:
            logger.error(f"Timeout waiting for attribute '{attribute}' to be '{value}' on element {locator}")
            raise

    def wait_for_text_to_be_present(self, locator, text, timeout=Config.TIMEOUT):
        """
        Waits for a specific text to be present in an element.
        
        :param locator: Locator tuple (By, value)
        :param text: Expected text to be present in the element
        :param timeout: Maximum wait time in seconds
        """
        try:
            logger.info(f"Waiting for text '{text}' to be present in element: {locator}")
            WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            logger.info(f"Text '{text}' is present in element {locator}")
        except TimeoutException:
            logger.error(f"Timed out waiting for text '{text}' in element {locator}")
            raise






    # Assertion Methods
    def assert_element_text(self, element, expected_text):
        """
        Asserts that the element's text matches the expected text.
        Logs success or raises an AssertionError if the assertion fails.
        
        :param element: WebElement
        :param expected_text: Expected text value
        """
        try:
            assert element.text == expected_text, f"Expected text '{expected_text}', but got '{element.text}'"
            logger.info(f"Assertion passed: Element text is '{expected_text}'")
        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            raise

    def assert_element_visible(self, element):
        """
        Asserts that the element is visible on the page.
        Logs success or raises an AssertionError if the element is not visible.
        
        :param element: WebElement
        """
        try:
            assert element.is_displayed(), "Element is not visible on the page"
            logger.info("Assertion passed: Element is visible")
        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            raise

    def assert_url_matches(self, expected_url):
        """
        Asserts that the current URL matches the expected URL.
        Logs success or raises an AssertionError if the URLs do not match.
        
        :param expected_url: Expected URL string
        """
        try:
            assert self.driver.current_url == expected_url, f"Expected URL '{expected_url}', but got '{self.driver.current_url}'"
            logger.info(f"Assertion passed: URL matches '{expected_url}'")
        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            raise
