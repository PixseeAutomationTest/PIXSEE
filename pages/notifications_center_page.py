from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages.base as base

class NotificationsCenterPage():
    def __init__(self, driver):
        self.driver = driver

