from base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.baby_timeline_page import BabyTimelinePage
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.add_baby_profile_page import AddBabyProfilePage
from pages.menu_pages.edit_baby_profile_page import EditBabyProfilePage
from pages.delete_profile_page import DeleteProfilePage
from pages.download_account_data_page import DownloadAccountDataPage

import time
import random
import unittest
# The tests in this TestCase will add a new baby profile first..
class EditBabyTestWithAdding(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = getattr(cls, "language", "zh")
        cls.locale = getattr(cls, "locale", "TW")
        super().setUpClass()

    def setUp(self):
        super().setUp()

        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        add_baby_profile_page = AddBabyProfilePage(self.driver)
        baby_timeline_page = BabyTimelinePage(self.driver)
        try:
            while self.driver.current_package != self.driver.capabilities.get("appPackage"):
                self.driver.terminate_app(self.driver.current_package)
                self.open_app()
            if not baby_monitor_page.is_in_baby_monitor_page():
                self.shutdown_app()
                self.open_app()
            baby_monitor_page.click_home()
            menu_page.click_baby_add()
            add_baby_profile_page.add_new_baby(self.locale)
            if baby_timeline_page.has_frame_tutor():
                self.click_middle()
            baby_timeline_page.click_menu()
            menu_page.click_baby_edit()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
    def test_03_delete_baby_profile_success(self):
        try:
            baby_monitor_page = BabyMonitorPage(self.driver)
            edit_baby_profile_page = EditBabyProfilePage(self.driver)
            delete_profile_page = DeleteProfilePage(self.driver)

            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")

            '''Verify Edit Baby Profile Page'''
            self.assertEqual(edit_baby_profile_page.get_page_title(), self.get_string("baby_profile_title"), "Text \"Baby profile\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_done_button_text(), self.get_string("done"), "\"Done\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_baby_profile_button_text(), self.get_string("baby_profile_btn_delete_profile"), "\"Delete baby's profile\" Button is not properly displayed")

            '''Click Delete Baby Profile Button and verify the confirmation dialog'''
            edit_baby_profile_page.click_delete_baby_profile()
            self.assertTrue(edit_baby_profile_page.has_dialog(), "\"Delete confirmation window\" is not displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_title(), self.get_string("delete_baby_dialog_baby_title"), "Text \" Are you sure you want to delete baby’s profile?\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_message(), self.get_string("delete_baby_dialog_info"), "Hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_warning_message(), self.get_string("delete_baby_dialog_warning"), "Warning hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_no_button_text(), self.get_string("delete_baby_dialog_btn_backup"), "\"Go to backup\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_yes_button_text(), self.get_string("delete_baby_dialog_btn_delete_baby"), "\"Yes, delete baby's profile\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_cancel_button_text(), self.get_string("cancel"), "\"Cancel\" Button is not properly displayed")

            '''Go to Delete Profile and verify content'''
            edit_baby_profile_page.click_dialog_yes()
            self.assertTrue(delete_profile_page.is_in_delete_profile_page(), "Can't automatically go to Delete Baby Profile Page from Edit Baby Profile Page")
            self.assertEqual(delete_profile_page.get_page_title(), self.get_string("delete_baby_title"), "Text \"Delete baby’s profile\" is not properly displayed")
            self.assertEqual(delete_profile_page.get_warning_text().replace("\n", "\\n"), self.get_string("delete_baby_warning") + " " + self.get_string("delete_warning_instruction"), "Warning Hint is not properly displayed")
            self.assertEqual(delete_profile_page.get_check_info_text(), self.get_string("delete_baby_check"), "Text \"Your baby’s data will be gone forever and cannot be recovered.\" is not properly displayed")
            self.assertEqual(delete_profile_page.get_delete_profile_button_text(), self.get_string("delete_baby_btn_delete"), "\"Delete baby's profile\" Button is not properly displayed")
            self.assertEqual(delete_profile_page.get_cancel_button_text(), self.get_string("cancel"), "\"Cancel\" Button is not properly displayed")

            '''Click Delete Baby Profile Button'''
            delete_profile_page.click_check()
            delete_profile_page.click_delete_profile()

            '''Go to Baby monitor page'''
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page(), "Can't automatically go to Baby Monitor Page after deleting a baby profile")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_01_change_baby_profile_cancel(self):
        try:
            menu_page = MenuPage(self.driver)
            add_baby_profile_page = AddBabyProfilePage(self.driver)
            edit_baby_profile_page = EditBabyProfilePage(self.driver)
            delete_profile_page = DeleteProfilePage(self.driver)

            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")

            '''Verify Edit Baby Profile Page'''
            self.assertEqual(edit_baby_profile_page.get_page_title(), self.get_string("baby_profile_title"), "Text \"Baby profile\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_done_button_text(), self.get_string("done"), "\"Done\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_baby_profile_button_text(), self.get_string("baby_profile_btn_delete_profile"), "\"Delete baby's profile\" Button is not properly displayed")

            old_gender_boy_status = edit_baby_profile_page.get_gender_boy_status()
            old_gender_girl_status = edit_baby_profile_page.get_gender_girl_status()
            old_baby_name = edit_baby_profile_page.get_baby_name_text()
            old_baby_birthday = edit_baby_profile_page.get_baby_birthday_text()
            old_baby_nation = edit_baby_profile_page.get_nation_text()
            old_baby_relative = edit_baby_profile_page.get_relative_text()

            '''Select one gender and verify their status'''
            edit_baby_profile_page.click_gender_boy()
            self.assertTrue(edit_baby_profile_page.get_gender_boy_status(), "Gender boy should be selected after clicking gender boy")
            self.assertFalse(edit_baby_profile_page.get_gender_girl_status(), "Gender girl should not be selected after clicking gender boy")
            edit_baby_profile_page.click_gender_girl()
            self.assertFalse(edit_baby_profile_page.get_gender_boy_status(), "Gender boy should not be selected after clicking gender girl")
            self.assertTrue(edit_baby_profile_page.get_gender_girl_status(), "Gender girl should be selected after clicking gender girl")

            '''Change baby's profile contents'''
            add_baby_profile_page.select_avatar()
            if random.choice([True, False]):
                edit_baby_profile_page.click_gender_boy()
            else:
                edit_baby_profile_page.click_gender_girl()
            edit_baby_profile_page.input_baby_name()
            edit_baby_profile_page.select_baby_birthday(self.locale, 2024, 6, 30)
            edit_baby_profile_page.select_nation(random.randint(1, 58))
            edit_baby_profile_page.select_relative(random.randint(1, 10))

            '''Click cancel button and verify that the changes are not saved'''
            edit_baby_profile_page.click_cancel()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")
            menu_page.click_baby_edit()
            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")
            self.assertEqual(edit_baby_profile_page.get_gender_boy_status(), old_gender_boy_status, "Gender boy status should not be changed after canceling changing")
            self.assertEqual(edit_baby_profile_page.get_gender_girl_status(), old_gender_girl_status, "Gender girl status should not be changed after canceling changing")
            self.assertEqual(edit_baby_profile_page.get_baby_name_text(), old_baby_name, "Baby name should not be changed after canceling changing")
            self.assertEqual(edit_baby_profile_page.get_baby_birthday_text(), old_baby_birthday, "Baby birthday should not be changed after canceling changing")
            self.assertEqual(edit_baby_profile_page.get_nation_text(), old_baby_nation, "Baby nation should not be changed after canceling changing")
            self.assertEqual(edit_baby_profile_page.get_relative_text(), old_baby_relative, "Baby relative should not be changed after canceling changing")

            '''Delete the baby profile to let the next test can run properly'''
            edit_baby_profile_page.click_delete_baby_profile()
            edit_baby_profile_page.click_dialog_yes()
            delete_profile_page.click_check()
            delete_profile_page.click_delete_profile()
            time.sleep(5)

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_02_change_baby_profile_save(self):
        try:
            menu_page = MenuPage(self.driver)
            add_baby_profile_page = AddBabyProfilePage(self.driver)
            edit_baby_profile_page = EditBabyProfilePage(self.driver)
            delete_profile_page = DeleteProfilePage(self.driver)

            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")

            '''Verify Edit Baby Profile Page'''
            self.assertEqual(edit_baby_profile_page.get_page_title(), self.get_string("baby_profile_title"), "Text \"Baby profile\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_done_button_text(), self.get_string("done"), "\"Done\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_baby_profile_button_text(), self.get_string("baby_profile_btn_delete_profile"), "\"Delete baby's profile\" Button is not properly displayed")

            '''Select one gender and verify their status'''
            edit_baby_profile_page.click_gender_boy()
            self.assertTrue(edit_baby_profile_page.get_gender_boy_status(), "Gender boy should be selected after clicking gender boy")
            self.assertFalse(edit_baby_profile_page.get_gender_girl_status(), "Gender girl should not be selected after clicking gender boy")
            edit_baby_profile_page.click_gender_girl()
            self.assertFalse(edit_baby_profile_page.get_gender_boy_status(), "Gender boy should not be selected after clicking gender girl")
            self.assertTrue(edit_baby_profile_page.get_gender_girl_status(), "Gender girl should be selected after clicking gender girl")

            '''Change baby's profile contents'''
            add_baby_profile_page.select_avatar()
            if random.choice([True, False]):
                edit_baby_profile_page.click_gender_boy()
            else:
                edit_baby_profile_page.click_gender_girl()
            edit_baby_profile_page.input_baby_name()
            edit_baby_profile_page.select_baby_birthday(self.locale, 2024, 6, 30)
            edit_baby_profile_page.select_nation(random.randint(1, 58))
            edit_baby_profile_page.select_relative(random.randint(1, 10))

            new_gender_boy_status = edit_baby_profile_page.get_gender_boy_status()
            new_gender_girl_status = edit_baby_profile_page.get_gender_girl_status()
            new_baby_name = edit_baby_profile_page.get_baby_name_text()
            new_baby_birthday = edit_baby_profile_page.get_baby_birthday_text()
            new_baby_nation = edit_baby_profile_page.get_nation_text()
            new_baby_relative = edit_baby_profile_page.get_relative_text()

            '''Click done button and verify that the changes are saved'''
            edit_baby_profile_page.click_done()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page after saving changing baby profile")
            menu_page.click_baby_edit()
            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")
            self.assertEqual(edit_baby_profile_page.get_gender_boy_status(), new_gender_boy_status, "Gender boy status should be changed after saving changing")
            self.assertEqual(edit_baby_profile_page.get_gender_girl_status(), new_gender_girl_status, "Gender girl status should be changed after saving changing")
            self.assertEqual(edit_baby_profile_page.get_baby_name_text(), new_baby_name, "Baby name should be changed after saving changing")
            self.assertEqual(edit_baby_profile_page.get_baby_birthday_text(), new_baby_birthday, "Baby birthday should be changed after saving changing")
            self.assertEqual(edit_baby_profile_page.get_nation_text(), new_baby_nation, "Baby nation should be changed after saving changing")
            self.assertEqual(edit_baby_profile_page.get_relative_text(), new_baby_relative, "Baby relative should be changed after saving changing")

            '''Delete the baby profile to let the next test can run properly'''
            edit_baby_profile_page.click_delete_baby_profile()
            edit_baby_profile_page.click_dialog_yes()
            delete_profile_page.click_check()
            delete_profile_page.click_delete_profile()
            time.sleep(5)

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    # The tests in this TestCase will edit baby profile directly.
class EditBabyTestWithoutAdding(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = getattr(cls, "language", "zh")
        cls.locale = getattr(cls, "locale", "TW")
        super().setUpClass()

    def setUp(self):
        super().setUp()

        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        edit_baby_page = EditBabyProfilePage(self.driver)
        try:
            while self.driver.current_package != self.driver.capabilities.get("appPackage"):
                self.driver.terminate_app(self.driver.current_package)
                self.open_app()
            if edit_baby_page.is_in_edit_baby_profile_page():
                return
            elif not baby_monitor_page.is_in_baby_monitor_page():
                self.shutdown_app()
                self.open_app()
            baby_monitor_page.click_home()
            menu_page.click_baby_edit()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
    def test_05_delete_baby_profile_dialog_with_cancel(self):
        try:
            edit_baby_profile_page = EditBabyProfilePage(self.driver)

            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")

            '''Verify Edit Baby Profile Page'''
            self.assertEqual(edit_baby_profile_page.get_page_title(), self.get_string("baby_profile_title"), "Text \"Baby profile\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_done_button_text(), self.get_string("done"), "\"Done\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_baby_profile_button_text(), self.get_string("baby_profile_btn_delete_profile"), "\"Delete baby's profile\" Button is not properly displayed")

            '''Click Delete Baby Profile Button and verify the confirmation dialog'''
            edit_baby_profile_page.click_delete_baby_profile()
            self.assertTrue(edit_baby_profile_page.has_dialog(), "\"Delete confirmation window\" is not displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_title(), self.get_string("delete_baby_dialog_baby_title"), "Text \" Are you sure you want to delete baby’s profile?\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_message(), self.get_string("delete_baby_dialog_info"), "Hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_warning_message(), self.get_string("delete_baby_dialog_warning"), "Warning hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_no_button_text(), self.get_string("delete_baby_dialog_btn_backup"), "\"Go to backup\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_yes_button_text(), self.get_string("delete_baby_dialog_btn_delete_baby"), "\"Yes, delete baby's profile\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_cancel_button_text(), self.get_string("cancel"), "\"Cancel\" Button is not properly displayed")

            '''Go to Delete Baby Profile and verify content'''
            edit_baby_profile_page.click_dialog_cancel()
            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't return to Edit Baby Profile Page after clicking cancel in Delete Baby Profile dialog")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_06_delete_baby_profile_page_with_cancel(self):
        try:
            edit_baby_profile_page = EditBabyProfilePage(self.driver)
            delete_profile_page = DeleteProfilePage(self.driver)

            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")

            '''Verify Edit Baby Profile Page'''
            self.assertEqual(edit_baby_profile_page.get_page_title(), self.get_string("baby_profile_title"), "Text \"Baby profile\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_done_button_text(), self.get_string("done"), "\"Done\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_baby_profile_button_text(), self.get_string("baby_profile_btn_delete_profile"), "\"Delete baby's profile\" Button is not properly displayed")

            '''Click Delete Baby Profile Button and verify the confirmation dialog'''
            edit_baby_profile_page.click_delete_baby_profile()
            self.assertTrue(edit_baby_profile_page.has_dialog(), "\"Delete confirmation window\" is not displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_title(), self.get_string("delete_baby_dialog_baby_title"), "Text \" Are you sure you want to delete baby’s profile?\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_message(), self.get_string("delete_baby_dialog_info"), "Hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_warning_message(), self.get_string("delete_baby_dialog_warning"), "Warning hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_no_button_text(), self.get_string("delete_baby_dialog_btn_backup"), "\"Go to backup\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_yes_button_text(), self.get_string("delete_baby_dialog_btn_delete_baby"), "\"Yes, delete baby's profile\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_cancel_button_text(), self.get_string("cancel"), "\"Cancel\" Button is not properly displayed")

            '''Go to Delete Baby Profile and verify content'''
            edit_baby_profile_page.click_dialog_yes()
            self.assertTrue(delete_profile_page.is_in_delete_profile_page(), "Can't automatically go to Delete Baby Profile Page from Edit Baby Profile Page")
            self.assertEqual(delete_profile_page.get_page_title(), self.get_string("delete_baby_title"), "Text \"Delete baby’s profile\" is not properly displayed")
            self.assertEqual(delete_profile_page.get_warning_text().replace("\n", "\\n"), self.get_string("delete_baby_warning") + " " + self.get_string("delete_warning_instruction"), "Warning Hint is not properly displayed")
            self.assertEqual(delete_profile_page.get_check_info_text(), self.get_string("delete_baby_check"), "Text \"Your baby’s data will be gone forever and cannot be recovered.\" is not properly displayed")
            self.assertEqual(delete_profile_page.get_delete_profile_button_text(), self.get_string("delete_baby_btn_delete"), "\"Delete baby's profile\" Button is not properly displayed")
            self.assertEqual(delete_profile_page.get_cancel_button_text(), self.get_string("cancel"), "\"Cancel\" Button is not properly displayed")

            '''Click Cancel Button'''
            delete_profile_page.click_cancel()
            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't return to Edit Baby Profile Page after clicking cancel in Delete Baby Profile Page")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_02_backup_baby_profile_dialog_with_ok(self):
        try:
            edit_baby_profile_page = EditBabyProfilePage(self.driver)
            download_account_data_page = DownloadAccountDataPage(self.driver)

            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")

            '''Verify Edit Baby Profile Page'''
            self.assertEqual(edit_baby_profile_page.get_page_title(), self.get_string("baby_profile_title"), "Text \"Baby profile\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_done_button_text(), self.get_string("done"), "\"Done\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_baby_profile_button_text(), self.get_string("baby_profile_btn_delete_profile"), "\"Delete baby's profile\" Button is not properly displayed")

            '''Click Delete Baby Profile Button and verify the confirmation dialog'''
            edit_baby_profile_page.click_delete_baby_profile()
            self.assertTrue(edit_baby_profile_page.has_dialog(), "\"Delete confirmation window\" is not displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_title(), self.get_string("delete_baby_dialog_baby_title"), "Text \" Are you sure you want to delete baby’s profile?\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_message(), self.get_string("delete_baby_dialog_info"), "Hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_warning_message(), self.get_string("delete_baby_dialog_warning"), "Warning hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_no_button_text(), self.get_string("delete_baby_dialog_btn_backup"), "\"Go to backup\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_yes_button_text(), self.get_string("delete_baby_dialog_btn_delete_baby"), "\"Yes, delete baby's profile\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_cancel_button_text(), self.get_string("cancel"), "\"Cancel\" Button is not properly displayed")

            '''Go to Download Account Data Page'''
            edit_baby_profile_page.click_dialog_no()
            self.assertTrue(download_account_data_page.has_dialog(), "\"Download data list window\" is not displayed")
            download_account_data_page.click_all_data()
            download_account_data_page.click_dialog_ok()
            self.assertTrue(download_account_data_page.is_in_download_account_data_page(), "Can't go to Download Account Data Page from Edit Baby Profile Page")
            self.go_back()

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_01_backup_baby_profile_dialog_with_cancel(self):
        try:
            edit_baby_profile_page = EditBabyProfilePage(self.driver)
            download_account_data_page = DownloadAccountDataPage(self.driver)

            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")

            '''Verify Edit Baby Profile Page'''
            self.assertEqual(edit_baby_profile_page.get_page_title(), self.get_string("baby_profile_title"), "Text \"Baby profile\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_done_button_text(), self.get_string("done"), "\"Done\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_baby_profile_button_text(), self.get_string("baby_profile_btn_delete_profile"), "\"Delete baby's profile\" Button is not properly displayed")

            '''Click Delete Baby Profile Button and verify the confirmation dialog'''
            edit_baby_profile_page.click_delete_baby_profile()
            self.assertTrue(edit_baby_profile_page.has_dialog(), "\"Delete confirmation window\" is not displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_title(), self.get_string("delete_baby_dialog_baby_title"), "Text \" Are you sure you want to delete baby’s profile?\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_message(), self.get_string("delete_baby_dialog_info"), "Hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_warning_message(), self.get_string("delete_baby_dialog_warning"), "Warning hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_no_button_text(), self.get_string("delete_baby_dialog_btn_backup"), "\"Go to backup\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_yes_button_text(), self.get_string("delete_baby_dialog_btn_delete_baby"), "\"Yes, delete baby's profile\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_dialog_cancel_button_text(), self.get_string("cancel"), "\"Cancel\" Button is not properly displayed")

            '''Click Go to Backup Button in Delete Confirmation dialog and cancel button in Download Account Data dialog'''
            edit_baby_profile_page.click_dialog_no()
            self.assertTrue(download_account_data_page.has_dialog(), "\"Download data list window\" is not displayed")
            download_account_data_page.click_dialog_cancel()
            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't return to Edit Baby Profile Page after clicking cancel in Download Account Data dialog")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    # Please confirm the baby profile has photos from over 280 days ago before running this test.
    @unittest.skip("Incomplete test: Because the app bug found (2025/7/30).")
    def test_03_change_baby_birthday_dialog_cancel(self):
        pass

    # Please confirm the baby profile has photos from over 280 days ago before running this test.
    @unittest.skip("Incomplete test: Because the app bug found (2025/7/30).")
    def test_04_change_baby_birthday_dialog_ok(self):
        pass

