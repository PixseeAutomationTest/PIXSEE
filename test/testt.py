import time

from pages.base import BaseTestCase
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_page import MenuPage
from appium.options.android import UiAutomator2Options
from appium import webdriver
from pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_friends_detection_page import  PixseeFriendsDetPage


class reset(BaseTestCase):
        def setUp(self):
                super().setUp(no_reset=True)


        def test_wipe(self):
                pixsee_friends_page = PixseeFriendsDetPage(self.driver)
                try:
                        title = pixsee_friends_page.title()
                        hint = self.get_string("pixsee_friends_detection_title")
                        self.assertEqual(title, hint)
                        print("Friends detection title right")
                except AssertionError:
                        print("Friends detection title wrong")
                        raise AssertionError("Friends detection title mismatch")


