import os

class Config:
    BASE_URL = "https://practice-automation.com/"
    TIMEOUT = 20
    SCREENSHOT_DIR = os.path.join(os.getcwd(), "screenshots")
    LOG_DIR = os.path.join(os.getcwd(), 'logs')
    LOG_FILE = os.path.join(LOG_DIR, 'javascript_delays.log')
    
    # Create necessary directories if they don't exist
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    
