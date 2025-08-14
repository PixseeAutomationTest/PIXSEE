from appium.options.android import UiAutomator2Options
from appium import webdriver
import unittest
import time




class BaseTestCase(unittest.TestCase):
    def setUp(self):
        driver = start_driver("en", "US")
        driver.activate_app(driver.capabilities.get("appPackage"))
        driver.quit()
        time.sleep(5)
    def test_test(self):
        print("test")
