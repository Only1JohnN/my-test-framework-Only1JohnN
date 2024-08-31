# screenshot.py
import os
from selenium.webdriver.common.by import By
from file_utils import ensure_directory_exists, get_timestamped_filename
from utils.logger import js_delays_logger as logger

def take_screenshot(driver, folder='screenshots', filename='screenshot'):
    """
    Take a screenshot and save it to the specified folder with a timestamped filename.
    
    :param driver: WebDriver instance
    :param folder: Directory to save the screenshot
    :param filename: Base name for the screenshot file
    """
    ensure_directory_exists(folder)
    screenshot_filename = get_timestamped_filename(filename, 'png')
    filepath = os.path.join(folder, screenshot_filename)
    
    try:
        driver.save_screenshot(filepath)
        logger.info(f"Screenshot saved to {filepath}")
    except Exception as e:
        logger.error(f"Failed to save screenshot to {filepath}: {e}")
        raise
