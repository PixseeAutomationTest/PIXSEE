from pages.base import BaseTestCase
import unittest
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage


class LoginCase(BaseTestCase):
        def setUp(self):
                super().setUp(no_reset=False)

        def test_login_success(self):
                login_page = LoginPage(self.driver)
                baby_monitor_page = BabyMonitorPage(self.driver)

                login_page.login("jackypixsee02@gmail.com", "@Aa12345")

                self.assertTrue(baby_monitor_page.is_in_baby_monitor_page())

        def test_login_wrong_email_failure(self):
                login_page = LoginPage(self.driver)

                login_page.login("jackypixsee02", "@Aa12345")
                self.assertEqual(login_page.get_email_error_text(),"Please enter a valid email address")

        def test_login_wrong_password_failure(self):
                login_page = LoginPage(self.driver)

                login_page.login("jackypixsee02@gmail.com", "aiwu464")
                self.assertEqual(login_page.get_password_error_text(), "Wrong password")

        def test_login_empty_email_failure(self):
                login_page = LoginPage(self.driver)

                login_page.login("", "@Aa12345")
                self.assertEqual(login_page.get_email_error_text(), "Please enter an email")

        def test_login_empty_password_failure(self):
                login_page = LoginPage(self.driver)

                login_page.login("jackypixsee02@gmail.com", "")
                self.assertEqual(login_page.get_password_error_text(), "Please enter password.")

if __name__ == "__main__":
    unittest.main()