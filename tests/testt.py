from appium.options.android import UiAutomator2Options
from appium import webdriver
import unittest
import time

from pages.base import BaseTestCase
from pages.menu_pages.edit_baby_profile_page import EditBabyProfilePage




class TestCase(BaseTestCase):
    def __init__(self, methodName='runTest', language="zh", locale="CN"):
        super().__init__(methodName)
        self.language = language
        self.locale = locale
    def setUp(self):
        super().setUp(language=self.language, locale=self.locale)
    def test_test(self):
        edit_baby_profile_page = EditBabyProfilePage(self.driver)
        edit_baby_profile_page.select_baby_birthday(self.locale, 2020, 5, 31)
        edit_baby_profile_page.select_baby_birthday(self.locale)
        edit_baby_profile_page.select_baby_birthday(self.locale, 2025, 8, 15)
