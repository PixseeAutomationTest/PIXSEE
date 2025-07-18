from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TimeLapseVideoPage():
    def __init__(self, driver):
        self.driver = driver
        self.Header = "com.compal.bioslab.pixsee.pixm01:id/textView5"

    def is_in_timelapse_video_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Header))
            )
            return True
        except:
            return False

