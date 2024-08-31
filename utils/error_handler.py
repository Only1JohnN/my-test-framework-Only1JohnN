# utils/error_handler.py
from utils.logger import js_delays_logger as logger

def log_exception(exception, context):
    """
    Logs an exception with context information.
    :param exception: Exception instance
    :param context: Additional context about where the exception occurred
    """
    logger.error(f"Exception in {context}: {exception}")

def handle_selenium_exception(func):
    """
    Handles Selenium-related exceptions.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_exception(e, f"Function {func.__name__}")
            raise
    return wrapper
