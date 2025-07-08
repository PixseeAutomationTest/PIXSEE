import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


class Function :
    def __init__(self,driver):
        self.driver=driver

    def login_email_input(self,text):
        time.sleep(3)
        element = self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/signInEmailField")
        element.click()
        element.send_keys(text)
    def login_password_input(self,text):
        element = self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/signInPasswordField")
        element.click()
        element.send_keys(text)
    def click_btn(self,btn):
        # sign-in
        element = self.driver.find_element(AppiumBy.ID, btn);
        element.click()
        time.sleep(2)
    def test_text(self,expected_text,hint_text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.ID, hint_text))
            )
            if element.is_displayed():
                if element.text == expected_text:
                    print("----success: hint right")
                else:
                    print("----failed: 文字不符")
            else:
                print("----failed")
        except TimeoutException:
            print("----error:time out")
    def click(self):  #點螢幕中間
        size = self.driver.get_window_size()
        x = size['width'] // 2
        y = size['height'] // 2

        self.driver.execute_script("mobile: clickGesture", {
            "x": x,
            "y": y
        })
    def login_check(self):
        baby_monitor = "com.compal.bioslab.pixsee.pixm01:id/videoTextureView"
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, baby_monitor))
            )
            if element.is_displayed():
                print("----Login success")
            else:
                print("----Login failed")
        except TimeoutException:
            print("----Login failed:time out")