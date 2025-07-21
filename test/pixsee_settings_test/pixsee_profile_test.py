from pages.base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_page import MenuPage
from pages.pixsee_settings.pixsee_settings_page import PixseeSettingsPage
from pages.pixsee_settings.pixsee_profile_page import PixseeProfilePage

import re

class PixseeProfileTest(BaseTestCase):
    def test_select_location(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            pixsee_profile_page = PixseeProfilePage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Pixsee Profile Page'''
            pixsee_settings_page.click_PixseeProfile()
            self.assertTrue(pixsee_profile_page.is_in_pixsee_profile_page(), "Can't go to Pixsee Profile Page")

            '''Verify Pixsee Profile Page'''
            self.assertEqual(pixsee_profile_page.get_page_title_text(), self.get_string("profile_settings"), "Text \"FFI00 profile\" is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_unbind_device_button_text(), self.get_string("unbind"), "button \"Unbind\" is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_info_text(), self.get_string("device_info_title"), "button \"Device info\" is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_location_title_text(), self.get_string("device_location"), "Text \"Device location\" is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_time_zone_title_text(), self.get_string("timezone"), "Text \"Timezone\" is not properly displayed")
            self.assertEqual(re.search(r'([^\d]*?\s*)(\d+(?:\.\d+)+)', pixsee_profile_page.get_current_version_text()).group(1), self.get_string("firmware_current_version").split('%')[0], "version display is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_check_update_button_text(), self.get_string("check_fw_upgrade"), "button \"Update\" is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_reboot_device_button_text(), self.get_string("device_reboot"), "button \"Device Reboot\" is not properly displayed")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

