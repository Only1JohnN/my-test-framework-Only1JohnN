# pages/popups_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from pages.basepage import BasePage

class PopupsPage(BasePage):
    ALERT_POPUP = ""
    CONFIRM_POPUP = ""
    PROMPT_POPUP = ""
    CLICK_ME_TO_SEE_A_TOOLTIP = ""
    
