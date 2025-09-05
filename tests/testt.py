from appium.options.android import UiAutomator2Options
from appium import webdriver
import unittest
import time

from pages.base import BaseTestCase
from pages.menu_pages.pixsee_friends_pages.pixsee_friends_page import PixseeFriendsPage



class TestCase(BaseTestCase):
    def __init__(self, methodName='runTest', language="zh", locale="CN"):
        super().__init__(methodName)
        self.language = language
        self.locale = locale
    def setUp(self):
        super().setUp(language=self.language, locale=self.locale)
    def test_test(self):
        pixsee_friends_page = PixseeFriendsPage(self.driver)
        pixsee_friends_page.scroll_up_dolls_list()
        time.sleep(2)
        pixsee_friends_page.scroll_down_dolls_list()