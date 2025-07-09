import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.base import BaseTestCase
from pages.music_tutorial_page import MusicTutorial
from pages.login_page import LoginPage
import datetime
from pages.baby_monitor_page import BabyMonitorPage
class MusicTutorialTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base = BaseTestCase()
        self.base.setUp(no_reset=False)

        login = LoginPage(self.base.driver)
        login.login("amypixsee03@gmail.com", "@Aa12345")

        self.base.skip_SD()# 跳過SD卡確認(可註解掉)
        for _ in range(4):  # 跳過教程
            self.base.click()
            time.sleep(0.8)

        home = BabyMonitorPage(self.base.driver)
        home.click_music()# 點擊音樂按鈕
        time.sleep(3)

    def tearDown(self):
        self.base.driver.quit()  # 結束 session，釋放資源

    def test_first_skip(self):
        print("測試第一張進入音樂教程時點擊跳過")
        music_tutorial = MusicTutorial(self.base.driver)
        music_tutorial.click_skip()
        music_tutorial.success_check()
    def test_second_skip(self):
        print("測試第二張進入音樂教程時點擊跳過")
        music_tutorial = MusicTutorial(self.base.driver)
        self.base.right_wipe()
        time.sleep(1)
        music_tutorial.click_skip()
        music_tutorial.success_check()
    def test_third_skip(self):
        print("測試第三張進入音樂教程時點擊跳過")
        music_tutorial = MusicTutorial(self.base.driver)
        self.base.right_wipe()
        time.sleep(1)
        self.base.right_wipe()
        time.sleep(1)
        music_tutorial.click_skip()
        music_tutorial.success_check()
    def test_fourth_skip(self):
        print("測試第四張進入音樂教程時點擊跳過")
        music_tutorial = MusicTutorial(self.base.driver)
        self.base.right_wipe()
        time.sleep(1)
        self.base.right_wipe()
        time.sleep(1)
        self.base.right_wipe()
        time.sleep(1)
        music_tutorial.click_skip()
        music_tutorial.success_check()
    def test_first_close(self):
        print("測試第一張進入音樂教程時點擊關閉")
        music_tutorial = MusicTutorial(self.base.driver)
        music_tutorial.click_close()
        music_tutorial.success_check()
    def test_second_close(self):
        print("測試第二張進入音樂教程時點擊關閉")
        music_tutorial = MusicTutorial(self.base.driver)
        self.base.right_wipe()
        time.sleep(1)
        music_tutorial.click_close()
        music_tutorial.success_check()
    def test_third_close(self):
        print("測試第三張進入音樂教程時點擊關閉")
        music_tutorial = MusicTutorial(self.base.driver)
        self.base.right_wipe()
        time.sleep(1)
        self.base.right_wipe()
        time.sleep(1)
        music_tutorial.click_close()
        music_tutorial.success_check()
    def test_fourth_close(self):
        print("測試第四張進入音樂教程時點擊關閉")
        music_tutorial = MusicTutorial(self.base.driver)
        self.base.right_wipe()
        time.sleep(1)
        self.base.right_wipe()
        time.sleep(1)
        self.base.right_wipe()
        time.sleep(1)
        music_tutorial.click_close()
        music_tutorial.success_check()


if __name__ == "__main__":
    unittest.main()
