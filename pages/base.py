import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseTestCase(unittest.TestCase):
    def setUp(self, no_reset=True):
        capabilities = UiAutomator2Options()
        capabilities.platform_name = "Android"
        capabilities.device_name = "38161FDJG00DXJ"
        # capabilities.device_name = "emulator-5554"


        # adb devices
        capabilities.app_package = "com.compal.bioslab.pixsee.pixm01"
        capabilities.app_activity = "com.compal.bioslab.pixsee.pixm01.activities.SplashActivity"
        capabilities.no_reset = no_reset
        capabilities.auto_grant_permissions = True
        capabilities.new_command_timeout = 300

        self.driver = webdriver.Remote("http://localhost:4723", options=capabilities)

    def verify_text_and_click(self, element_id, expected_text, name, timeout=20):
        """
        等待元素、比對文字、點擊另一個元素
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ID, element_id))
            )
            actual_text = self.driver.find_element(AppiumBy.ID, element_id).text
            assert actual_text == expected_text, f"Text mismatch! Expected: '{expected_text}', Got: '{actual_text}'"
            print(f"{name} tutor success")
        except AssertionError as ae:
            print(f"{name} tutor FAIL: {str(ae)}")
        except Exception as e:
            print(f"{name} tutor FAIL: Exception occurred - {str(e)}")


    # 向左滑
    def left_wipe(self):
        time.sleep(0.5)
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(1)'
        )
    # 向右滑動
    def right_wipe(self):
        time.sleep(0.5)
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToBeginning(1)'
        )
    #下拉
    def down_scroll(self):
        time.sleep(0.5)
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(1)'
        )
    #上拉
    def up_scroll(self):
        time.sleep(0.5)
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(1)'
        )

    def click_middle(self):
        size = self.driver.get_window_size()
        x = size['width'] // 2
        y = size['height'] // 2

        self.driver.execute_script("mobile: clickGesture", {
            "x": x,
            "y": y
        })
        time.sleep(1)

    def tearDown(self):
            pass

