from pages.base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.baby_timeline_page import BabyTimelinePage
from pages.menu_page import MenuPage
from pages.menu_pages.add_baby_profile_page import AddBabyProfilePage
from pages.menu_pages.edit_baby_profile_page import EditBabyProfilePage
from pages.menu_pages.edit_baby_profile_pages.delete_baby_profile import DeleteBabyProfilePage
class EditBabyTest(BaseTestCase):
    def test_delete_baby_profile(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            add_baby_profile_page = AddBabyProfilePage(self.driver)
            baby_timeline_page = BabyTimelinePage(self.driver)
            edit_baby_profile_page = EditBabyProfilePage(self.driver)
            delete_baby_profile_page = DeleteBabyProfilePage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")

            '''Go to Add Baby Profile Page and add a new baby profile'''
            menu_page.click_baby_add()
            self.assertTrue(add_baby_profile_page.is_in_add_baby_profile_page(), "Can't go to Add Baby Profile Page")
            add_baby_profile_page.add_new_baby()

            '''Go to Baby Timeline Page'''
            self.assertTrue(baby_timeline_page.is_in_baby_timeline_page(), "Can't automatically go to Baby Timeline Page after adding a new baby profile")

            '''Go to Menu Page'''
            baby_timeline_page.click_menu()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page from Baby Timeline Page")

            '''Go to Edit Baby Profile Page'''
            menu_page.click_baby_edit()
            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")

            '''Verify Edit Baby Profile Page'''
            self.assertEqual(edit_baby_profile_page.get_page_title(), self.get_string("baby_profile_title"), "Text \"Baby profile\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_done_button_text(), self.get_string("done"), "\"Done\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_baby_profile_button_text(), self.get_string("baby_profile_btn_delete_profile"), "\"Delete baby's profile\" Button is not properly displayed")

            '''Click Delete Baby Profile Button and verify the confirmation dialog'''
            edit_baby_profile_page.click_delete_baby_profile()
            self.assertTrue(edit_baby_profile_page.has_delete_dialog(), "\"Delete confirmation window\" is not displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_dialog_title(), self.get_string("delete_baby_dialog_baby_title"), "Text \" Are you sure you want to delete baby’s profile?\" is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_dialog_message(), self.get_string("delete_baby_dialog_info"), "Hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_dialog_warning_message(), self.get_string("delete_baby_dialog_warning"), "Warning hint is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_dialog_no_button_text(), self.get_string("delete_baby_dialog_btn_backup"), "\"Go to backup\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_dialog_yes_button_text(), self.get_string("delete_baby_dialog_btn_delete_baby"), "\"Yes, delete baby's profile\" Button is not properly displayed")
            self.assertEqual(edit_baby_profile_page.get_delete_dialog_cancel_button_text(), self.get_string("cancel"), "\"Cancel\" Button is not properly displayed")

            '''Go to Delete Baby Profile and verify content'''
            edit_baby_profile_page.click_delete_dialog_yes()
            self.assertTrue(delete_baby_profile_page.is_in_delete_baby_profile_page(), "Can't automatically go to Delete Baby Profile Page from Edit Baby Profile Page")
            self.assertEqual(delete_baby_profile_page.get_page_title(), self.get_string("delete_baby_title"), "Text \"Delete baby’s profile\" is not properly displayed")
            self.assertEqual(delete_baby_profile_page.get_warning_text(), (self.get_string("delete_baby_warning") + " " + self.get_string("delete_warning_instruction")).replace("\\n", "\n"), "Warning Hint is not properly displayed")
            self.assertEqual(delete_baby_profile_page.get_check_info_text(), self.get_string("delete_baby_check"), "Text \"Your baby’s data will be gone forever and cannot be recovered.\" is not properly displayed")
            self.assertEqual(delete_baby_profile_page.get_delete_baby_profile_button_text(), self.get_string("delete_baby_btn_delete"), "\"Delete baby's profile\" Button is not properly displayed")
            self.assertEqual(delete_baby_profile_page.get_cancel_button_text(), self.get_string("cancel"), "\"Cancel\" Button is not properly displayed")

            '''Click Delete Baby Profile Button'''
            delete_baby_profile_page.click_check()
            delete_baby_profile_page.click_delete_baby_profile()

            '''Go to Baby monitor page'''
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page(), "Can't automatically go to Baby Monitor Page after deleting a baby profile")


        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()
