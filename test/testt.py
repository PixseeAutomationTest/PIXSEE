import time

from pages.base import BaseTestCase
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_page import MenuPage
from appium.options.android import UiAutomator2Options
from appium import webdriver
from pages.photo_page import PhotoPage



class reset(BaseTestCase):
        def setUp(self):
                super().setUp(no_reset=False)


        def test_wipe(self):
                photo_page = PhotoPage(self.driver)
                photo_page.scroll_down_photo()
