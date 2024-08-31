import logging
import os
from config.settings import Config

def setup_logger(name, log_file):
    """
    Sets up a logger with a specified name and log file.
    """
    log_path = os.path.join(Config.LOG_DIR, log_file)
    
    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # File Handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)
    
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Add handlers
    if not logger.hasHandlers():
        logger.addHandler(file_handler)
    
    return logger

# JavaScript Delays specific logger
js_delays_logger = setup_logger(
    name="javascript_delays",
    log_file="javascript_delays.log"  # Path to logs folder and javascript_delays.log file
)
