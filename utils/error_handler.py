from utils.logger import js_delays_logger as logger
import traceback

def handle_error(error_message):
    """
    Handles errors by logging the error message and stack trace.
    Optionally, you can add custom recovery or fallback steps within this function.

    :param error_message: A custom error message to log.
    """
    try:
        logger.error(f"Error occurred: {error_message}")
        logger.error("Stack trace:\n" + traceback.format_exc())
        # Optional: Implement error recovery steps or notifications here
    except Exception as e:
        logger.critical(f"Failed to handle error: {e}")
        logger.critical("Handling failed:\n" + traceback.format_exc())
        # Optional: Further action if error handling fails, like sending alerts
