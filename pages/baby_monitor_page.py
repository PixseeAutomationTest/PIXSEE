from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BabyMonitorPage:
        def __init__(self, driver):
            self.driver = driver

            self.babyMonitorScreen = "com.compal.bioslab.pixsee.pixm01:id/clVideoStreamButtons"

        def is_in_baby_monitor_page(self):
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((AppiumBy.ID, self.babyMonitorScreen))
                )
                self.driver.find_element(AppiumBy.ID, self.babyMonitorScreen)
                return True

            except:
                return False

        def wait_for_tutor_by_id(self, tutor_id, timeout=20):
            """等待 tutor 元素出現，並回傳元素文字"""
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ID, tutor_id))
            )
            return self.driver.find_element(AppiumBy.ID, tutor_id).text

        def click_stream_title(self):
            """點擊畫面標題"""
            self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/tvStreamTitle").click()

        def click_home(self):
            self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome").click()






