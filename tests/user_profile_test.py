from pages.base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.user_profile_pages.user_profile_page import UserProfilePage
from pages.menu_pages.user_profile_pages.change_password_page import ChangePasswordPage

class UserProfileTest(BaseTestCase):
    def test_change_password_success(self):
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
            change_password_page.input_new_password("@Aa12345")
            change_password_page.input_confirm_password("@Aa12345")
            change_password_page.click_done()
            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't return to Change Password Page after clicking \"Done\" button in Change Password Page")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_change_password_with_cancel(self):
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
        finally:
            self.shutdown_app()

    def test_change_user_profile_success(self):
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
        finally:
            self.shutdown_app()

    def test_change_user_profile_with_cancel(self):
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
        finally:
            self.shutdown_app()

    # Please check the account has no backup email before run this test
    def test_add_backup_email_dialog_with_cancel(self):
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
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
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
        finally:
            self.shutdown_app()

    # Please check the account has no backup email before run this test
    def test_add_backup_email_dialog_with_yes(self):
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
            self.assertEqual(user_profile_page.get_done_button_text(), self.get_string("done"), "Button \"Done\" is not properly displayed")
            self.assertEqual(user_profile_page.get_change_password_button_text(), self.get_string("user_profile_change_password_button"), "Button \"Change password\" is properly displayed")
            if user_profile_page.has_backup_email():
                self.assertEqual(user_profile_page.get_change_backup_email_button_text(), self.get_string("backup_email_change_backup_email"), "Button \"Change backup email\" is properly displayed")
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

            '''Click ok Button and verify add backup email page contents'''
            user_profile_page.click_add_backup_email_dialog_ok()
            self.assertTrue(user_profile_page.is_in_user_profile_page(), "Can't return to User Profile Page after clicking \"Cancel\" button in Add Backup Email Dialog")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()