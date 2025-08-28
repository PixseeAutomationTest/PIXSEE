from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.area_detection_page import AreaDetectionPage


class AreaDetectionCase1(BaseTestCase):
    def __init__(self, methodName='runTest', language="zh", locale="TW"):
        super().__init__(methodName)
        self.language = language
        self.locale = locale

    def setUp(self):
        super().setUp(language=self.language, locale=self.locale, no_reset=False)

    def test_01_area_detection_tutor_skip_1(self):
        area_detection_page = AreaDetectionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(), self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        # ensure is connected to machine
        baby_monitor_page = BabyMonitorPage(self.driver)
        if not baby_monitor_page.is_connected():
            self.skipTest("not online，skip all test")

        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()

        menu_page.click_settings()

        pixsee_settings_page.click_area_detection()
        # check first tutor title
        try:
            title = area_detection_page.tutor_first_title_text()
            hint = self.get_string("safe_area_tutorial_title")
            self.assertEqual(title, hint)
            print("first tutor  title right")
        except AssertionError :
            raise AssertionError("first tutor  title wrong")
        # check first tutor indicator
        try:
            self.assertTrue(area_detection_page.is_in_tutor_first_page())
            print("first tutor indicator displayed")
        except AssertionError :
            raise AssertionError("first tutor indicator doesn't displayed")
        # check skip
        try:
            skip = area_detection_page.skip_text()
            hint = self.get_string("skip")
            self.assertEqual(skip, hint)
            print("skip display right")
        except AssertionError :
            raise AssertionError("skip display wrong")
        area_detection_page.click_skip()
        # check in area area_detection_page
        try:
            self.assertTrue(area_detection_page.is_in_area_detection_page())
            print("skip first tutor successfully")
        except AssertionError :
            raise AssertionError("skip first tutor unsuccessfully")
    def test_02_area_detection_tutor_skip_2(self):
        area_detection_page = AreaDetectionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(), self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        # ensure is connected to machine
        baby_monitor_page = BabyMonitorPage(self.driver)
        if not baby_monitor_page.is_connected():
            self.skipTest("not online，skip all test")

        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()

        menu_page.click_settings()

        pixsee_settings_page.click_area_detection()
        self.left_wipe()
        # check second tutor title
        try:
            title = area_detection_page.tutor_second_title_text()
            hint = self.get_string("caution_area_tutorial_title")
            self.assertEqual(title, hint)
            print("second tutor  title right")
        except AssertionError :
            raise AssertionError("second tutor  title wrong")
        # check second tutor indicator
        try:
            self.assertTrue(area_detection_page.is_in_tutor_second_page())
            print("second tutor indicator displayed")
        except AssertionError :
            raise AssertionError("second tutor indicator doesn't displayed")
        # check skip
        try:
            skip = area_detection_page.skip_text()
            hint = self.get_string("skip")
            self.assertEqual(skip, hint)
            print("skip display right")
        except AssertionError :
            raise AssertionError("skip display wrong")

        area_detection_page.click_skip()
        # check in area area_detection_page
        try:
            self.assertTrue(area_detection_page.is_in_area_detection_page())
            print("skip second tutor successfully")
        except AssertionError :
            raise AssertionError("skip second tutor unsuccessfully")
    def test_03_area_detection_tutor_skip_121(self):
        area_detection_page = AreaDetectionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(), self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        # ensure is connected to machine
        baby_monitor_page = BabyMonitorPage(self.driver)
        if not baby_monitor_page.is_connected():
            self.skipTest("not online，skip all test")

        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()

        menu_page.click_settings()

        pixsee_settings_page.click_area_detection()

        # check first tutor page
        try:
            self.assertTrue(area_detection_page.is_in_tutor_first_page())
            print("first tutor displayed")
        except AssertionError :
            raise AssertionError("first tutor doesn't displayed")

        self.left_wipe()
        # check second tutor page
        try:
            self.assertTrue(area_detection_page.is_in_tutor_second_page())
            print("second tutor indicator displayed")
        except AssertionError :
            raise AssertionError("second tutor indicator doesn't displayed")

        self.right_wipe()
        # check first tutor page
        try:
            self.assertTrue(area_detection_page.is_in_tutor_first_page())
            print("first tutor displayed")
        except AssertionError :
            raise AssertionError("first tutor doesn't displayed")

        area_detection_page.click_skip()
        # check in area area_detection_page
        try:
            self.assertTrue(area_detection_page.is_in_area_detection_page())
            print("skip second tutor successfully")
        except AssertionError :
            raise AssertionError("skip second tutor unsuccessfully")