import unittest

from pages.base import BaseTestCase

from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages import menu_page
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.user_profile_pages.user_profile_page import UserProfilePage
from pages.menu_pages.user_profile_pages.change_password_page import ChangePasswordPage
from pages.menu_pages.user_profile_pages.add_backup_email import AddBackupEmailPage

class UserProfileTest(BaseTestCase):
    def setUp(self):
        super().setUp()

        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        user_profile_page = UserProfilePage(self.driver)
        try:
            while self.driver.current_package != self.driver.capabilities.get("appPackage"):
                self.driver.terminate_app(self.driver.current_package)
                self.open_app()
            if user_profile_page.is_in_user_profile_page():
                return
            elif not baby_monitor_page.is_in_baby_monitor_page():
                self.shutdown_app()
                self.open_app()
            baby_monitor_page.click_home()
            menu_page.click_profile()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
    def test_change_password_success(self):
        try:
            login_page = LoginPage(self.driver)
            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Change Password Page and verify contents'''
            user_profile_page.click_change_password()
            self.assertTrue(change_password_page.is_in_change_password_page(), "Can't go to Change Password Page")
            self.assertEqual(change_password_page.get_page_title(), self.get_string("change_password_title"), "Text \"Change Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_current_password_hint(), self.get_string("current_password_field"), "Hint \"Current Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_hint(), self.get_string("new_password_field"), "Hint \"New Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_hint(), self.get_string("reset_password_confirm_field"), "Hint \"Confirm Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(change_password_page.get_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")

            '''Change Password and click Done Button'''
            change_password_page.input_current_password("@Aa12345")
            change_password_page.input_new_password("@Aa123456")
            change_password_page.input_confirm_password("@Aa123456")
            change_password_page.click_done()
            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't return to Change Password Page after clicking \"Done\" button in Change Password Page")

            '''Log out to verify the change password'''
            user_profile_page.click_return()
            menu_page.click_logout()
            login_page.login("amypixsee03@gmail.com", "@Aa123456")
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page(), "Can't go to Baby Monitor Page after logging in with new password")

            '''Change Password back to original password to avoid affecting other tests'''
            baby_monitor_page.click_home()
            menu_page.click_profile()
            user_profile_page.click_change_password()
            change_password_page.input_current_password("@Aa123456")
            change_password_page.input_new_password("@Aa12345")
            change_password_page.input_confirm_password("@Aa12345")
            change_password_page.click_done()

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    @unittest.skip("Spec doesn't mention about what error messages should be. Please wait for the spec to be updated and modify this test case.")
    def test_change_password_with_empty(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Change Password Page and verify contents'''
            user_profile_page.click_change_password()
            self.assertTrue(change_password_page.is_in_change_password_page(), "Can't go to Change Password Page")
            self.assertEqual(change_password_page.get_page_title(), self.get_string("change_password_title"), "Text \"Change Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_current_password_hint(), self.get_string("current_password_field"), "Hint \"Current Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_hint(), self.get_string("new_password_field"), "Hint \"New Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_hint(), self.get_string("reset_password_confirm_field"), "Hint \"Confirm Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(change_password_page.get_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")

            '''Change Password and click Done Button'''
            change_password_page.click_done()
            self.assertEqual(change_password_page.get_current_password_error(), self.get_string("sign_up_error_empty_password"), "Current password error message \"Required field\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_error() ,self.get_string("sign_up_error_empty_password"), "New password error message \"Required field\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_error(), self.get_string("sign_up_error_empty_password"), "Confirm password error message \"Required field\" is not properly displayed")
            change_password_page.click_cancel()

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    @unittest.skip("Spec doesn't mention about what error messages should be. Please wait for the spec to be updated and modify this test case.")
    def test_change_password_with_less_words(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Change Password Page and verify contents'''
            user_profile_page.click_change_password()
            self.assertTrue(change_password_page.is_in_change_password_page(), "Can't go to Change Password Page")
            self.assertEqual(change_password_page.get_page_title(), self.get_string("change_password_title"), "Text \"Change Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_current_password_hint(), self.get_string("current_password_field"), "Hint \"Current Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_hint(), self.get_string("new_password_field"), "Hint \"New Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_hint(), self.get_string("reset_password_confirm_field"), "Hint \"Confirm Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(change_password_page.get_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")
            '''Change Password and click Done Button'''
            password = "123456789"
            for i in range(1, len(password) + 1):
                change_password_page.input_current_password(password[:i])
                change_password_page.input_new_password(password[:i])
                change_password_page.input_confirm_password(password[:i])
                change_password_page.click_done()
                if i < 8:
                    self.assertEqual(change_password_page.get_current_password_error(), self.get_string("form_password_error_characters"), "Current password error message \"- 8 or more characters\" is not properly displayed")
                    self.assertEqual(change_password_page.get_new_password_error() ,self.get_string("form_password_error_characters"), "New password error message \"- 8 or more characters\"is not properly displayed")
                    self.assertEqual(change_password_page.get_confirm_password_error(), self.get_string("form_password_error_characters"), "Confirm password error message \"- 8 or more characters\"is not properly displayed")
                else:
                    self.assertNotEqual(change_password_page.get_current_password_error(), self.get_string("form_password_error_characters"), "Current password error message \"- 8 or more characters\" should not display")
                    self.assertNotEqual(change_password_page.get_new_password_error(), self.get_string("form_password_error_characters"), "New password error message \"- 8 or more characters\"should not display")
                    self.assertNotEqual(change_password_page.get_confirm_password_error(), self.get_string("form_password_error_characters"), "Confirm password error message \"- 8 or more characters\"should not display")
            change_password_page.click_cancel()

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    @unittest.skip("Spec doesn't mention about what error messages should be. Please wait for the spec to be updated and modify this test case.")
    def test_change_password_with_no_lowercase_letter(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Change Password Page and verify contents'''
            user_profile_page.click_change_password()
            self.assertTrue(change_password_page.is_in_change_password_page(), "Can't go to Change Password Page")
            self.assertEqual(change_password_page.get_page_title(), self.get_string("change_password_title"), "Text \"Change Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_current_password_hint(), self.get_string("current_password_field"), "Hint \"Current Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_hint(), self.get_string("new_password_field"), "Hint \"New Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_hint(), self.get_string("reset_password_confirm_field"), "Hint \"Confirm Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(change_password_page.get_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")
            '''Change Password and click Done Button'''
            change_password_page.input_current_password("@A12345678")
            change_password_page.input_new_password("@A12345678")
            change_password_page.input_confirm_password("@A12345678")
            change_password_page.click_done()
            self.assertEqual(change_password_page.get_current_password_error(), self.get_string("form_password_error_lowercase"), "Current password error message \"- At least one lowercase letter\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_error() ,self.get_string("form_password_error_lowercase"), "New password error message \"- At least one lowercase letter\"is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_error(), self.get_string("form_password_error_lowercase"), "Confirm password error message \"- At least one lowercase letter\"is not properly displayed")
            change_password_page.click_cancel()

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    @unittest.skip("Spec doesn't mention about what error messages should be. Please wait for the spec to be updated and modify this test case.")
    def test_change_password_with_no_uppercase_letter(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Change Password Page and verify contents'''
            user_profile_page.click_change_password()
            self.assertTrue(change_password_page.is_in_change_password_page(), "Can't go to Change Password Page")
            self.assertEqual(change_password_page.get_page_title(), self.get_string("change_password_title"), "Text \"Change Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_current_password_hint(), self.get_string("current_password_field"), "Hint \"Current Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_hint(), self.get_string("new_password_field"), "Hint \"New Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_hint(), self.get_string("reset_password_confirm_field"), "Hint \"Confirm Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(change_password_page.get_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")
            '''Change Password and click Done Button'''
            change_password_page.input_current_password("@a12345678")
            change_password_page.input_new_password("@a12345678")
            change_password_page.input_confirm_password("@a12345678")
            change_password_page.click_done()
            self.assertEqual(change_password_page.get_current_password_error(), self.get_string("form_password_error_uppercase"), "Current password error message \"- At least one uppercase letter\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_error() ,self.get_string("form_password_error_uppercase"), "New password error message \"- At least one uppercase letter\"is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_error(), self.get_string("form_password_error_uppercase"), "Confirm password error message \"- At least one uppercase letter\"is not properly displayed")
            change_password_page.click_cancel()

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    @unittest.skip("Spec doesn't mention about what error messages should be. Please wait for the spec to be updated and modify this test case.")
    def test_change_password_with_no_number(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Change Password Page and verify contents'''
            user_profile_page.click_change_password()
            self.assertTrue(change_password_page.is_in_change_password_page(), "Can't go to Change Password Page")
            self.assertEqual(change_password_page.get_page_title(), self.get_string("change_password_title"), "Text \"Change Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_current_password_hint(), self.get_string("current_password_field"), "Hint \"Current Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_hint(), self.get_string("new_password_field"), "Hint \"New Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_hint(), self.get_string("reset_password_confirm_field"), "Hint \"Confirm Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(change_password_page.get_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")
            '''Change Password and click Done Button'''
            change_password_page.input_current_password("@Aabcdefgh")
            change_password_page.input_new_password("@@Aabcdefgh")
            change_password_page.input_confirm_password("@@Aabcdefgh")
            change_password_page.click_done()
            self.assertEqual(change_password_page.get_current_password_error(), self.get_string("form_password_error_number"), "Current password error message \"- At least one number\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_error() ,self.get_string("form_password_error_number"), "New password error message \"- At least one number\"is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_error(), self.get_string("form_password_error_number"), "Confirm password error message \"- At least one number\"is not properly displayed")
            change_password_page.click_cancel()

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    @unittest.skip("Spec doesn't mention about what error messages should be. Please wait for the spec to be updated and modify this test case.")
    def test_change_password_with_no_special_character(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Change Password Page and verify contents'''
            user_profile_page.click_change_password()
            self.assertTrue(change_password_page.is_in_change_password_page(), "Can't go to Change Password Page")
            self.assertEqual(change_password_page.get_page_title(), self.get_string("change_password_title"), "Text \"Change Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_current_password_hint(), self.get_string("current_password_field"), "Hint \"Current Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_hint(), self.get_string("new_password_field"), "Hint \"New Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_hint(), self.get_string("reset_password_confirm_field"), "Hint \"Confirm Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(change_password_page.get_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")
            '''Change Password and click Done Button'''
            change_password_page.input_current_password("Aa123456")
            change_password_page.input_new_password("Aa123456")
            change_password_page.input_confirm_password("Aa123456")
            change_password_page.click_done()
            self.assertEqual(change_password_page.get_current_password_error(), self.get_string("form_password_special_character"), "Current password error message \"- At least one special character\"is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_error() ,self.get_string("form_password_special_character"), "New password error message \"- At least one special character\"is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_error(), self.get_string("form_password_special_character"), "Confirm password error message \"- At least one special character\"is not properly displayed")
            change_password_page.click_cancel()

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    @unittest.skip("Spec doesn't mention about what error messages should be. Please wait for the spec to be updated and modify this test case.")
    def test_change_password_with_inconsistent_input(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Change Password Page and verify contents'''
            user_profile_page.click_change_password()
            self.assertTrue(change_password_page.is_in_change_password_page(), "Can't go to Change Password Page")
            self.assertEqual(change_password_page.get_page_title(), self.get_string("change_password_title"), "Text \"Change Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_current_password_hint(), self.get_string("current_password_field"), "Hint \"Current Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_hint(), self.get_string("new_password_field"), "Hint \"New Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_hint(), self.get_string("reset_password_confirm_field"), "Hint \"Confirm Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(change_password_page.get_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")
            '''Change Password and click Done Button'''
            change_password_page.input_current_password("@Aa12345")
            change_password_page.input_new_password("@Aa123456")
            change_password_page.input_confirm_password("@Aa12345")
            change_password_page.click_done()
            self.assertEqual(change_password_page.get_confirm_password_error(), self.get_string("form_password_error_do_not_match"), "Confirm password error message \"Wrong password\"is not properly displayed")
            change_password_page.click_cancel()

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    @unittest.skip("Spec doesn't mention about what error messages should be. Please wait for the spec to be updated and modify this test case.")
    def test_change_password_with_wrong_current_password(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Change Password Page and verify contents'''
            user_profile_page.click_change_password()
            self.assertTrue(change_password_page.is_in_change_password_page(), "Can't go to Change Password Page")
            self.assertEqual(change_password_page.get_page_title(), self.get_string("change_password_title"), "Text \"Change Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_current_password_hint(), self.get_string("current_password_field"), "Hint \"Current Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_hint(), self.get_string("new_password_field"), "Hint \"New Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_hint(), self.get_string("reset_password_confirm_field"), "Hint \"Confirm Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(change_password_page.get_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")
            '''Change Password and click Done Button'''
            change_password_page.input_current_password("@Aa123456")
            change_password_page.input_new_password("@Aa12345")
            change_password_page.input_confirm_password("@Aa12345")
            change_password_page.click_done()
            self.assertEqual(change_password_page.get_wrong_bar_text(), self.get_string("something_went_error"), "\"Something went wrong! Please try again later.\"is not properly displayed")
            change_password_page.click_cancel()

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_change_password_with_cancel(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Change Password Page and verify contents'''
            user_profile_page.click_change_password()
            self.assertTrue(change_password_page.is_in_change_password_page(), "Can't go to Change Password Page")
            self.assertEqual(change_password_page.get_page_title(), self.get_string("change_password_title"), "Text \"Change Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_current_password_hint(), self.get_string("current_password_field"), "Hint \"Current Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_new_password_hint(), self.get_string("new_password_field"), "Hint \"New Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_confirm_password_hint(), self.get_string("reset_password_confirm_field"), "Hint \"Confirm Password\" is not properly displayed")
            self.assertEqual(change_password_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(change_password_page.get_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")

            '''Click Cancel Button'''
            change_password_page.click_cancel()
            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't return to Change Password Page after clicking \"Cancel\" button in Change Password Page")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_change_user_profile_success(self):
        try:
            menu_page = MenuPage(self.driver)
            user_profile_page = UserProfilePage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Change user avatar, name and birthday'''
            user_profile_page.select_avatar()
            user_profile_page.input_user_name()
            user_profile_page.select_birthday()
            new_user_name = user_profile_page.get_user_name_text()
            new_user_birthday = user_profile_page.get_user_birthday_text()

            '''Save changes and verify that changes are saved'''
            user_profile_page.click_done()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't return to Menu Page after clicking \"Done\" button in User Profile Page")
            menu_page.click_profile()
            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't return to User Profile Page")
            self.assertEqual(user_profile_page.get_user_name_text(), new_user_name, "User name should be changed")
            self.assertEqual(user_profile_page.get_user_birthday_text(), new_user_birthday, "User birthday should be changed")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_change_user_profile_with_cancel(self):
        try:
            menu_page = MenuPage(self.driver)
            user_profile_page = UserProfilePage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            old_user_name = user_profile_page.get_user_name_text()
            old_user_birthday = user_profile_page.get_user_birthday_text()

            '''Change user avatar, name and birthday'''
            user_profile_page.select_avatar()
            user_profile_page.input_user_name()
            user_profile_page.select_birthday()

            '''Save changes and verify that changes are saved'''
            user_profile_page.click_return()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't return to Menu Page after clicking \"Return\" button in User Profile Page")
            menu_page.click_profile()
            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't return to User Profile Page")
            self.assertEqual(user_profile_page.get_user_name_text(), old_user_name, "User name should not be changed")
            self.assertEqual(user_profile_page.get_user_birthday_text(), old_user_birthday, "User birthday should not be changed")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    # Please check the account has no backup email before run this test
    def test_add_backup_email_dialog_with_cancel(self):
        try:
            user_profile_page = UserProfilePage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
                self.skipTest("Backup email already exists, skipping this test")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Click Add Backup Email Button and verify the dialog'''
            user_profile_page.click_add_backup_email()
            self.assertTrue(user_profile_page.has_add_backup_email_dialog(), "\"Help us protect your account\" window isn't displayed")
            self.assertEqual(user_profile_page.get_add_backup_email_dialog_title_text(), self.get_string("backup_email_title_dialog"), "Text \"Help us protect your account\" is properly displayed")
            self.assertEqual(user_profile_page.get_add_backup_email_dialog_info_text(), self.get_string("backup_email_description_dialog"), "Text \"Add backup information to enhance your account security.\" is not properly displayed")
            self.assertEqual(user_profile_page.get_add_backup_email_dialog_ok_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add a backup email\" is not properly displayed")
            self.assertEqual(user_profile_page.get_add_backup_email_dialog_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")

            '''Click Cancel Button and verify that dialog is closed'''
            user_profile_page.click_add_backup_email_dialog_cancel()
            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't return to User Profile Page after clicking \"Cancel\" button in Add Backup Email Dialog")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    # Please check the account has no backup email before run this test
    def test_add_or_change_backup_email_with_close(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            add_backup_email_page = AddBackupEmailPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Add Backup Email page'''
            if user_profile_page.has_backup_email():
                user_profile_page.click_change_backup_email()
            else:
                user_profile_page.click_add_backup_email()
                self.assertTrue(user_profile_page.has_add_backup_email_dialog(), "\"Help us protect your account\" window isn't displayed")
                self.assertEqual(user_profile_page.get_add_backup_email_dialog_title_text(), self.get_string("backup_email_title_dialog"), "Text \"Help us protect your account\" is properly displayed")
                self.assertEqual(user_profile_page.get_add_backup_email_dialog_info_text(), self.get_string("backup_email_description_dialog"), "Text \"Add backup information to enhance your account security.\" is not properly displayed")
                self.assertEqual(user_profile_page.get_add_backup_email_dialog_ok_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add a backup email\" is not properly displayed")
                self.assertEqual(user_profile_page.get_add_backup_email_dialog_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")
                user_profile_page.click_add_backup_email_dialog_ok()
            self.assertEqual(add_backup_email_page.get_title_text(), self.get_string("backup_email_screen_title"), "Can't go to Add Backup Email Page")

            '''Click close button'''
            add_backup_email_page.click_close()
            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't returb to User Profile Page after clicking \"Close\" button in Add Backup Email Page")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_add_or_change_backup_email_with_invalid_email(self):
        try:
            user_profile_page = UserProfilePage(self.driver)
            add_backup_email_page = AddBackupEmailPage(self.driver)

            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
            else:
                self.assertEqual(user_profile_page.get_add_backup_email_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add backup mail\" is properly displayed")
                self.skipTest("Backup email doesn't exist, skipping this test")
            self.assertEqual(user_profile_page.get_delete_account_button_text(), self.get_string("account_profile_btn_delete"), "Button \"Delete account\" is properly displayed")

            '''Go to Add Backup Email page'''
            if user_profile_page.has_backup_email():
                user_profile_page.click_change_backup_email()
            else:
                user_profile_page.click_add_backup_email()
                self.assertTrue(user_profile_page.has_add_backup_email_dialog(), "\"Help us protect your account\" window isn't displayed")
                self.assertEqual(user_profile_page.get_add_backup_email_dialog_title_text(), self.get_string("backup_email_title_dialog"), "Text \"Help us protect your account\" is properly displayed")
                self.assertEqual(user_profile_page.get_add_backup_email_dialog_info_text(), self.get_string("backup_email_description_dialog"), "Text \"Add backup information to enhance your account security.\" is not properly displayed")
                self.assertEqual(user_profile_page.get_add_backup_email_dialog_ok_button_text(), self.get_string("add_backup_email_button_title"), "Button \"Add a backup email\" is not properly displayed")
                self.assertEqual(user_profile_page.get_add_backup_email_dialog_cancel_button_text(), self.get_string("cancel"), "Button \"Cancel\" is not properly displayed")
                user_profile_page.click_add_backup_email_dialog_ok()
            self.assertEqual(add_backup_email_page.get_title_text(), self.get_string("backup_email_screen_title"), "Can't go to Add Backup Email Page")

            '''Input invalid email and click next button'''
            add_backup_email_page.input_email("amypixsee@")
            add_backup_email_page.click_next()
            self.assertTrue(add_backup_email_page.has_error_message_text(), "Text \"Please enter a valid email address\" is not properly displayed.")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e