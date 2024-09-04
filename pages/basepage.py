# base_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException, NoSuchElementException
from config.settings import Config
from utils.logger import setup_logger
from selenium.webdriver.common.alert import Alert
from utils.screenshot import take_screenshot

logger = setup_logger()

class BasePage:
    def __init__(self, driver):
        self.driver = driver






    # Element Interaction Methods
    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            logger.error(f"Element not found: {locator}")
            raise
        except Exception as e:
            logger.error(f"Error finding element: {locator}. Exception: {e}")
            raise
    
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
        
    
    # SCROLLING TO ELEMENTS BEFORE PERFORMING ACTIONS
    def scroll_to_element_and_perform_action(self, locator, action, *args, timeout=Config.TIMEOUT):
        """
        Scrolls to an element and performs a specified action on it.

        :param locator: Locator tuple (By, value)
        :param action: The action to perform (e.g., 'click', 'send_keys')
        :param args: Arguments for the action (e.g., text for send_keys)
        :param timeout: Maximum wait time in seconds
        """
        try:
            # Wait for the element to be present
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            
            # Scroll to the element
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            logger.info(f"Scrolled to element: {locator}")

            # Perform the action
            if action == 'click':
                element.click()
                logger.info(f"Clicked on element: {locator}")
            elif action == 'send_keys':
                if args:
                    element.send_keys(*args)
                    logger.info(f"Sent keys '{args[0]}' to element: {locator}")
                else:
                    logger.error(f"No keys provided for send_keys action")
                    raise ValueError("No keys provided for send_keys action")
            else:
                logger.error(f"Unsupported action '{action}'")
                raise ValueError(f"Unsupported action '{action}'")

        except TimeoutException:
            logger.error(f"Timed out waiting for element {locator}")
            raise
        except Exception as e:
            logger.error(f"An error occurred while performing action '{action}' on element {locator}: {e}")
            raise






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
        
    def wait_for_element_visible(self, locator, timeout=Config.TIMEOUT):
        """
        Waits for an element to be visible.

        :param locator: Locator tuple (By, value)
        :param timeout: Maximum wait time in seconds
        :return: WebElement if visible
        """
        try:
            logger.info(f"Waiting for element to be visible: {locator}")
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            logger.info(f"Element is visible: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Timed out waiting for element to be visible: {locator}")
            take_screenshot(self.driver, folder='screenshots', filename='element_visible_timeout')
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
            # Wait until the element is present
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            
            # Wait until the attribute value matches the expected value
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.find_element(*locator).get_attribute(attribute) == value
            )
            
            # Optionally retrieve the element if needed
            element = self.driver.find_element(*locator)
            
            logger.info(f"Element's attribute '{attribute}' has the expected value '{value}'")
            return element
        except TimeoutException:
            logger.error(f"Timed out waiting for element's attribute '{attribute}' to be '{value}'")
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
            element = WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            logger.info(f"Text '{text}' is present in element {locator}")
            return element
        except TimeoutException:
            logger.error(f"Timed out waiting for text '{text}' in element {locator}")
            raise
        
    def wait_for_alert_present(self, timeout=Config.TIMEOUT):
        """
        Waits for an alert to be present.
        
        :param timeout: Maximum wait time in seconds
        :return: The alert object if present
        """
        try:
            logger.info(f"Waiting for alert to be present")
            alert = WebDriverWait(self.driver, timeout).until(
                EC.alert_is_present()
            )
            logger.info("Alert is present")
            return alert
        except TimeoutException:
            logger.error("Timed out waiting for alert to be present")
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
        
        
        
        
        
    # Handling Alert Methods
    def verify_alert_message(self, expected_message):
        try:
            alert = self.wait_for_alert_present()
            alert_text = alert.text
            assert alert_text == expected_message, f"Expected '{expected_message}', but got '{alert_text}'"
            logger.info(f"Alert message verification passed: '{expected_message}'")
        except NoAlertPresentException:
            logger.error("Alert is not present after form submission.")
            raise
        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            raise
        except Exception as e:
            logger.error(f"Error verifying alert message. Exception: {e}")
            raise
    
    def accept_alert(self):
        try:
            alert = self.wait_for_alert_present()
            alert.accept()  # Clicks "OK" on the alert
            logger.info("Alert accepted.")
        except NoAlertPresentException:
            logger.error("No alert present to accept.")
            raise

    def dismiss_alert(self):
        try:
            alert = self.wait_for_alert_present()
            alert.dismiss()  # Clicks "Cancel" on the alert
            logger.info("Alert dismissed.")
        except NoAlertPresentException:
            logger.error("No alert present to dismiss.")
            raise
        
    def send_text_to_alert(self, text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = Alert(self.driver)
            alert.send_keys(text)
            logger.info(f"Text '{text}' sent to alert.")
        except TimeoutException:
            logger.error("Alert did not appear within the timeout period.")
            raise

