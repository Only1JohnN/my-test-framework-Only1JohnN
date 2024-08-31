# retry.py
from decorators import retry_on_exception
from selenium.common.exceptions import NoSuchElementException, TimeoutException

@retry_on_exception(NoSuchElementException, retries=3, delay=2)
def click_element(driver, locator):
    """
    Click an element with retry logic.
    
    :param driver: WebDriver instance
    :param locator: Locator of the element to click
    """
    element = driver.find_element(*locator)
    element.click()
