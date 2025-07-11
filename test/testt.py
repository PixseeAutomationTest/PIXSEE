import time

from pages.base import BaseTestCase
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_page import MenuPage
from appium.options.android import UiAutomator2Options
from appium import webdriver



class reset(BaseTestCase):
        def setUp(self):
                super().setUp(no_reset=True)

        def test_wipe(self):
                self.open_app()

                login_page = LoginPage(self.driver)
                baby_monitor_page = BabyMonitorPage(self.driver)
                menu_page = MenuPage(self.driver)


                login_page.login("amypixsee03@gmail.com", "@Aa12345")
                time.sleep(5)
                self.assertTrue(baby_monitor_page.is_in_baby_monitor_page())
                self.shutdown_app()