# decorators.py
from functools import wraps
import time
from utils.logger import js_delays_logger as logger

def retry_on_exception(exception, retries=3, delay=2, logger=None):
    """
    Decorator to retry a function call on specific exception.
    
    :param exception: Exception type to catch and retry
    :param retries: Number of retry attempts
    :param delay: Delay between retries in seconds
    :param logger: Optional logger for logging retry attempts
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    attempt += 1
                    message = f"Attempt {attempt} failed: {e}. Retrying in {delay} seconds..."
                    if logger:
                        logger.warning(message)
                    else:
                        print(message)  # Fallback logging
                    time.sleep(delay)
            final_message = f"All {retries} attempts failed."
            if logger:
                logger.error(final_message)
            else:
                print(final_message)  # Fallback logging
            raise
        return wrapper
    return decorator
