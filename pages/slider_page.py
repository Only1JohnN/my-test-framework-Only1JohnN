# pages/slider_page.py
import traceback
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, MoveTargetOutOfBoundsException
from pages.basepage import BasePage
from utils.screenshot import take_screenshot
from utils.logger import setup_logger

logger = setup_logger()
logger.info("Test started")

class SliderPage(BasePage):
    SLIDER = (By.ID, 'slideMe')

    def move_slider_to_value(self, value):
        """
        Moves the slider to the desired value.
        :param value: Desired value to set on the slider
        """
        try:
            slider = self.find_element(self.SLIDER)
            current_value = int(slider.get_attribute('value'))
            logger.info(f"Current slider value: {current_value}, target: {value}")

            # Ensure the target value is within bounds
            if value < 0 or value > 100:  # Assuming slider range is 0-100; adjust if different
                logger.error(f"Target value {value} is out of bounds.")
                return

            # Attempt to move the slider
            self.move_slider(slider, value)
            new_value = int(slider.get_attribute('value'))
            logger.info(f"Slider moved to value: {new_value}")

            # Verify the slider has reached the desired value
            if new_value != value:
                logger.warning(f"Slider did not reach the desired value. Current: {new_value}, Expected: {value}")
                # Optionally retry or adjust further

        except (NoSuchElementException, StaleElementReferenceException) as e:
            logger.error(f"Failed to find slider element: {str(e)}")
        except MoveTargetOutOfBoundsException as e:
            logger.error(f"Move target out of bounds: {str(e)} - Retrying with smaller movements.")
            # Implement retry logic with smaller steps if necessary
            self.move_slider(slider, value, use_small_steps=True)
        except Exception as e:
            logger.error(f"An unexpected error occurred while moving the slider: {str(e)}")
            raise

    def get_slider_value(self):
        """
        Gets the current value of the slider.
        :return: Current value of the slider as a string
        """
        try:
            slider = self.find_element(self.SLIDER)
            value = slider.get_attribute('value')
            logger.info(f"Retrieved slider value: {value}")
            return value
        except NoSuchElementException as e:
            logger.error(f"Slider element not found: {str(e)}")
            return None
        except StaleElementReferenceException as e:
            logger.error(f"Slider element is no longer attached to the DOM: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"An unexpected error occurred while retrieving the slider value: {str(e)}")
            return None