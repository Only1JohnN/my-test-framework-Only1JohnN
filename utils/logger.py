# utils/logger.py
import logging
import os
from config.settings import Config

def setup_logger():
    """
    Sets up a logger that dynamically creates a log file based on the script name.
    """
    # Get the name of the script being run
    script_name = os.path.basename(__file__).replace('.py', '')

    # Create the log path based on the script name
    log_file = f"{script_name}.log"
    log_path = os.path.join(Config.LOG_DIR, log_file)

    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger(script_name)
    logger.setLevel(logging.INFO)

    # File Handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers if they are not already added
    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = setup_logger()
logger.info("Test started")