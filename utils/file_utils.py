# file_utils.py
import os
from datetime import datetime
from utils.logger import js_delays_logger as logger

def ensure_directory_exists(directory):
    """
    Ensure the specified directory exists. Create it if it doesn't.
    
    :param directory: Directory path
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")
    except Exception as e:
        logger.error(f"Failed to create directory {directory}: {e}")
        raise

def get_timestamped_filename(base_filename, extension):
    """
    Generate a timestamped filename.
    
    :param base_filename: Base name of the file
    :param extension: File extension
    :return: Timestamped filename
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{base_filename}_{timestamp}.{extension}"
