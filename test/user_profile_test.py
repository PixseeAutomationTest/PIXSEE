from pages.base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_page import MenuPage
from pages.menu_pages.user_profile_page import UserProfilePage
from pages.menu_pages.user_profile_pages.change_password_page import ChangePasswordPage

import re

class UserProfileTest(BaseTestCase):
    def test_change_password(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            user_profile_page = UserProfilePage(self.driver)
            change_password_page = ChangePasswordPage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")

            '''Go to User Profile Page'''
            menu_page.click_profile()
            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't go to User Profile Page")

            '''Verify User Profile Page'''
            self.assertEqual(user_profile_page.get_page_title(), self.get_string("user_profile_title"), "Text \"User Profile\" is not properly displayed")
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

            #TODO: Incomplete test case





        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()
