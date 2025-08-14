from pages.base import BaseTestCase

from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage


class LoginCase(BaseTestCase):
        def __init__(self, methodName='runTest', language="zh", locale="TW"):
                super().__init__(methodName)
                self.language = language
                self.locale = locale

        def setUp(self):
                super().setUp(language=self.language, locale=self.locale, no_reset=False)


        def test_01_login_wrong_email_failure(self):
                login_page = LoginPage(self.driver)

                login_page.login("amypixsee03", "@Aa12345")
                hint = self.get_string("field_validation_invalid_email")
                # hint = "Please enter a valid email address"
                try:
                        self.assertEqual(login_page.get_email_error_text(), hint)
                        print("Wrong email test success")
                except AssertionError:
                        print("Wrong email test failed")
                        raise AssertionError("Wrong email test failed, expected error message not found")

        def test_02_login_wrong_password_failure(self):
                login_page = LoginPage(self.driver)

                login_page.login("amypixsee03@gmail.com", "aiwu464")
                hint = self.get_string("e10016")
                # hint = "Wrong password"
                try:
                        self.assertEqual(login_page.get_password_error_text(), hint)
                        print("Wrong password test success")
                except AssertionError:
                        print("Wrong password test failed")
                        raise AssertionError("Wrong password test failed, expected error message not found")

        def test_03_login_empty_email_failure(self):
                login_page = LoginPage(self.driver)

                login_page.login("", "@Aa12345")
                # hint = self.strings["e10001"]
                hint = self.get_string("e10001")

                # hint = "Please enter an email"
                try:
                        self.assertEqual(login_page.get_email_error_text(), hint)
                        print("Empty email test success")
                except AssertionError:
                        print("Empty email test failed")
                        raise AssertionError("Empty email test failed, expected error message not found")

        def test_04_login_empty_password_failure(self):
                login_page = LoginPage(self.driver)

                login_page.login("amypixsee03@gmail.com", "")
                hint = self.get_string("e10002")
                # hint = "Please enter password"
                try:
                        self.assertEqual(login_page.get_password_error_text(), hint)
                        print("Empty password test success")
                except AssertionError:
                        print("Empty password test failed")
                        raise AssertionError("Empty password test failed, expected error message not found")

        def test_05_login_success(self):
                login_page = LoginPage(self.driver)
                baby_monitor_page = BabyMonitorPage(self.driver)

                login_page.login("amypixsee03@gmail.com", "@Aa12345")
                try:
                        self.assertTrue(baby_monitor_page.is_in_baby_monitor_page())
                        print("Login test success")
                except:
                        print("Login test failed")
                        raise AssertionError("Login failed, not in baby monitor page")