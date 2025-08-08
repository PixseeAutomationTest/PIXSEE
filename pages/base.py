import unittest
from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import re
import os
from selenium.common import NoSuchElementException
import csv
import subprocess
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.support.wait import WebDriverWait


class BaseTestCase(unittest.TestCase):
    def setUp(self, no_reset=True):
        capabilities = UiAutomator2Options()
        capabilities.platform_name = "Android"
        capabilities.device_name = "emulator-5554"
        capabilities.language = "en-us text"  # Chinese (Taiwan): "tw text", English: "en-us text"
        # capabilities.device_name = "emulator-5554"

        # adb devices
        capabilities.app_package = "com.compal.bioslab.pixsee.pixm01"
        capabilities.app_activity = "com.compal.bioslab.pixsee.pixm01.activities.SplashActivity"
        capabilities.no_reset = no_reset
        capabilities.auto_grant_permissions = True
        capabilities.new_command_timeout = 300
        # subprocess.run([
        #     "adb", "shell", "cmd", "notification", "suspend_package",
        #     "com.compal.bioslab.pixsee.pixm01"
        # ])
        self.tutor_id = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
        self.driver = webdriver.Remote("http://localhost:4723", options=capabilities)
        self.driver.update_settings({"waitForIdleTimeout": 100})
    def open_app(self):
        self.driver.activate_app(self.driver.capabilities.get("appPackage"))
        time.sleep(10)
    def shutdown_app(self):
        self.driver.terminate_app(self.driver.capabilities.get("appPackage"))
        time.sleep(5)
    # from right to left
    def left_wipe(self):
        time.sleep(0.5)
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(1)'
        )
    # from left to right
    def right_wipe(self):
        time.sleep(0.5)
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToBeginning(1)'
        )
    # from top to bottom
    def down_scroll(self):
        time.sleep(0.5)
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(1)'
        )
    # from bottom to top
    def up_scroll(self):
        time.sleep(0.5)
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(1)'
        )
    def click_middle(self):
        size = self.driver.get_window_size()
        x = size['width'] // 2
        y = size['height'] // 7 * 6

        self.driver.execute_script("mobile: clickGesture", {
            "x": x,
            "y": y
        })
        time.sleep(1)

    def go_to_home_screen(self):
        self.driver.press_keycode(AndroidKey.HOME)
        time.sleep(1)

    def go_back(self):
        self.driver.press_keycode(AndroidKey.BACK)
        time.sleep(1)
    def skip_first_four_tutor(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.tutor_id))
        )
        for i in range(4):
            self.click_middle()
            time.sleep(1)

    def get_string(self, key="", language = None):
        if language is None:
            language = self.driver.capabilities.get("language")
        if not language:
            raise ValueError(f"Unsupported language code: {language}")
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 取得專案根目錄
        csv_path = os.path.join(base_dir, "Pixsee App translations - master_202403.csv")
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["Identifier Android"] == key:
                    return re.sub(r'</?[^>]+>', '', row.get(language, f"[Missing:{key}]"))
        return f"[NotFound:{key}]"
    def check_switch_and_content(self, expected_on: bool, itemid):
        if expected_on:
            try:
                is_visible = len(self.driver.find_elements(AppiumBy.ID, itemid)) > 0
                assert is_visible
                print("switch on success")
            except AssertionError:
                raise AssertionError("switch on failed")
        else:
            try:
                # check findable
                is_visible =  len(self.driver.find_elements(AppiumBy.ID, itemid)) > 0
                assert not is_visible
                print("switch off success")
            except AssertionError:
                raise AssertionError("switch off failed")
    def tap_on_visibility(self, itemid, name, should_be_visible=True):
        try:
            is_visible = len(self.driver.find_elements(AppiumBy.ID, itemid)) > 0
            if should_be_visible:
                assert is_visible
            else:
                assert not is_visible
            print(f"tap on {name} success")
        except AssertionError:
            raise AssertionError(f"tap on {name} failed")
    def account(self):
        return "amypixsee03@gmail.com"
    def password(self):
        return "@Aa12345"
    def tearDown(self):
            self.driver.quit()

