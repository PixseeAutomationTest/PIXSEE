import unittest

from pages.base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.baby_timeline_page import BabyTimelinePage
from pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.menu_pages.pixsee_settings_pages.pixsee_profile_page import PixseeProfilePage
from pages.device_unbind_page import DeviceUnbindPage

import random
import time
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
            pixsee_settings_page.click_pixsee_profile()
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

            '''Select Location'''
            pixsee_profile_page.select_location(random.randint(0, 9)) # 10 locations available
            self.assertTrue(pixsee_profile_page.is_in_pixsee_profile_page(), "Can't close the list of locations")
            select_location = pixsee_profile_page.get_current_location_text()

            '''Go back to Pixsee Settings Page and check if the selected location is displayed correctly'''
            pixsee_profile_page.click_back()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't return to Pixsee Settings Page from Pixsee Profile Page")
            self.assertEqual(select_location, pixsee_settings_page.location_name_text(), "Selected location is not displayed correctly in Pixsee Settings Page")

            '''Go back to Baby Monitor Page and check if the selected location is displayed correctly'''
            pixsee_settings_page.click_back()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't return to Menu Page from Pixsee Settings Page")
            menu_page.click_home()
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page(), "Can't return to Baby Monitor Page from Menu Page")
            self.assertEqual(select_location, baby_monitor_page.get_stream_title(), "Selected location is not displayed correctly in Baby Monitor Page")


        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    # FIXME: No checking the time in Baby Monitor Page because Android doesn't support Daylight Saving Time (DST).
    def test_select_time_zone(self):
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
            pixsee_settings_page.click_pixsee_profile()
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

            '''Select Time Zone'''
            pixsee_profile_page.select_time_zone(random.randint(0, 72)) # 73 time zones available
            self.assertTrue(pixsee_profile_page.is_in_pixsee_profile_page(), "Can't close the list of time zone")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_check_device_info(self):
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
            pixsee_settings_page.click_pixsee_profile()
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

            '''Click Device Info and verify the device info dialog'''
            pixsee_profile_page.click_device_info()
            self.assertTrue(pixsee_profile_page.has_device_info_dialog(), "Device info dialog is not displayed")
            self.assertEqual(pixsee_profile_page.get_device_info_dialog_title_text(), self.get_string("device_info_title"), "Text \"Device info.\" is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_product_name_title_text(), self.get_string("device_info_product_name"), "Text \"Product name:\" is not properly displayed")
            self.assertNotEqual(pixsee_profile_page.get_product_name_text(), "", "Product name is not displayed")
            self.assertEqual(pixsee_profile_page.get_product_model_title_text(), self.get_string("device_info_product_model"), "Text \"Product model:\" is not properly displayed")
            self.assertNotEqual(pixsee_profile_page.get_product_model_text(), "", "Product model is not displayed")
            self.assertEqual(pixsee_profile_page.get_product_serial_number_title_text(), self.get_string("device_info_serial_number"), "Text \"Serial number:\" is not properly displayed")
            self.assertNotEqual(pixsee_profile_page.get_product_serial_number_text(), "", "Product serial number is not displayed")
            self.assertEqual(pixsee_profile_page.get_warranty_period_title_text(), self.get_string("device_info_warranty_period"), "Text \"Warranty period:\" is not properly displayed")
            self.assertNotEqual(pixsee_profile_page.get_warranty_period_text(), "", "Warranty period is not displayed")
            self.assertEqual(pixsee_profile_page.get_device_info_dialog_ok_button_text(), self.get_string("ok"), "button \"Ok\" is not properly displayed")

            '''Close Device Info dialog'''
            pixsee_profile_page.click_device_info_dialog_ok()
            self.assertTrue(pixsee_profile_page.is_in_pixsee_profile_page(), "Can't return to Pixsee Profile Page after closing Device Info dialog")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_reboot_device(self):
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
            pixsee_settings_page.click_pixsee_profile()
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

            '''Reboot Device'''
            pixsee_profile_page.click_reboot_device()
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page(), "Can't automatically return to Baby Monitor Page")
            self.assertEqual(baby_monitor_page.get_connecting_status_text(), self.get_string("stream_connecting_status"), "Text \"Connecting\" is not properly displayed")
            time.sleep(10)  # Wait for the device to reboot

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_rotate_screen(self):
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
            pixsee_settings_page.click_pixsee_profile()
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

            '''Click rotate'''
            pixsee_profile_page.click_rotate()
            self.assertEqual(pixsee_profile_page.get_syncing_text(), self.get_string("device_setting_camera_iq_rotate_toast_sync"), "Text \"Server data is syncing. Thank you for your patience.\" is not properly displayed")
            time.sleep(5)
            self.assertFalse(pixsee_profile_page.has_syncing_toast(), "Syncing toast is still displayed after 5 seconds")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_IQ_setting_with_no_changing(self):
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
            pixsee_settings_page.click_pixsee_profile()
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

            '''No changing IQ setting level and verify contents'''
            pixsee_profile_page.click_IQ_setting()
            self.assertTrue(pixsee_profile_page.has_IQ_setting_bar(), "Doesn't show IQ setting menu")
            self.assertEqual(pixsee_profile_page.get_IQ_setting_bar_len(), 4, "IQ setting menu should have 4 levels")
            pixsee_profile_page.click_IQ_option(pixsee_profile_page.get_IQ_setting_current_level())
            self.assertFalse(pixsee_profile_page.has_syncing_toast(), "Syncing toast shouldn't be displayed after no changing IQ setting level")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_IQ_setting_with_changing(self):
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
            pixsee_settings_page.click_pixsee_profile()
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

            '''Choose IQ setting level and verify contents'''
            pixsee_profile_page.click_IQ_setting()
            self.assertTrue(pixsee_profile_page.has_IQ_setting_bar(), "Doesn't show IQ setting menu")
            self.assertEqual(pixsee_profile_page.get_IQ_setting_bar_len(), 4, "IQ setting menu should have 4 levels")
            candidates = [i for i in range(4) if i != pixsee_profile_page.get_IQ_setting_current_level()]
            pixsee_profile_page.click_IQ_option(random.choice(candidates))
            self.assertEqual(pixsee_profile_page.get_syncing_text(), self.get_string("device_setting_camera_iq_rotate_toast_sync"), "Text \"Server data is syncing. Thank you for your patience.\" is not properly displayed")
            time.sleep(5)
            self.assertFalse(pixsee_profile_page.has_syncing_toast(), "Syncing toast is still displayed after 5 seconds")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_check_update(self):
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
            pixsee_settings_page.click_pixsee_profile()
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

            '''Click Check Update and verify contents'''
            pixsee_profile_page.click_check_update()
            time.sleep(5)
            self.assertEqual(pixsee_profile_page.get_firmware_release_text(), self.get_string("firmware_up_to_date"), "Text \"The camera is up to date.\" is not properly displayed")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_device_unbind_dialog_with_no(self):
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
            pixsee_settings_page.click_pixsee_profile()
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

            '''Click Unbind and verify the device unbind dialog'''
            pixsee_profile_page.click_unbind_device()
            self.assertTrue(pixsee_profile_page.has_device_unbind_dialog(), "Device unbind dialog is not displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_title_text(), self.get_string("user_profile_delete_device_dialog_title"), "Text \"Are you sure you want to unbind the FFI00 device?\" is properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_description_text().replace('\n', '\\n'), self.get_string("user_profile_delete_device_dialog_message"), "Unbind message is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_yes_button_text(), self.get_string("yes"), "button \"Yes\" is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_no_button_text(), self.get_string("cancel"), "button \"No\" is not properly displayed")

            '''Click No in Device Unbind dialog'''
            pixsee_profile_page.click_device_unbind_dialog_no()
            self.assertTrue(pixsee_profile_page.is_in_pixsee_profile_page(), "Can't return to Pixsee Profile Page after canceling unbind device")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_device_unbind_page_with_close(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            pixsee_profile_page = PixseeProfilePage(self.driver)
            device_unbind_page = DeviceUnbindPage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Pixsee Profile Page'''
            pixsee_settings_page.click_pixsee_profile()
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

            '''Click Unbind and verify the device unbind dialog'''
            pixsee_profile_page.click_unbind_device()
            self.assertTrue(pixsee_profile_page.has_device_unbind_dialog(), "Device unbind dialog is not displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_title_text(), self.get_string("user_profile_delete_device_dialog_title"), "Text \"Are you sure you want to unbind the FFI00 device?\" is properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_description_text().replace('\n', '\\n'), self.get_string("user_profile_delete_device_dialog_message"), "Unbind message is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_yes_button_text(), self.get_string("yes"), "button \"Yes\" is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_no_button_text(), self.get_string("cancel"), "button \"No\" is not properly displayed")

            '''Click Yes in Device Unbind dialog and go to Device Unbind Page'''
            pixsee_profile_page.click_device_unbind_dialog_yes()
            self.assertTrue(device_unbind_page.is_in_device_unbind_page(), "Can't automatically go to Device Unbind Page from Pixsee Profile Page")

            '''Verify Device Unbind Page'''
            self.assertEqual(device_unbind_page.get_page_title_text(), self.get_string("delete_device_title"), "Text \"Initiate unbind\" is not properly displayed")
            self.assertEqual(device_unbind_page.get_message_text(), self.get_string("long_press_volume_white"), "Unbind message(ITC8) is not properly displayed")
            self.assertEqual(device_unbind_page.get_seen_flash_light_button_text(), self.get_string("delete_device_positive_button_white"), "button \"Blink white light\" is not properly displayed")
            self.assertEqual(device_unbind_page.get_cancel_button_text(), self.get_string("cancel"), "button \"Cancel\" is not properly displayed")

            '''Click Close in Device Unbind Page'''
            device_unbind_page.click_close()
            self.assertTrue(pixsee_profile_page.is_in_pixsee_profile_page(), "Can't return to Pixsee Profile Page after clicking close Device Unbind Page")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_device_unbind_page_with_cancel(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            pixsee_profile_page = PixseeProfilePage(self.driver)
            device_unbind_page = DeviceUnbindPage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Pixsee Profile Page'''
            pixsee_settings_page.click_pixsee_profile()
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

            '''Click Unbind and verify the device unbind dialog'''
            pixsee_profile_page.click_unbind_device()
            self.assertTrue(pixsee_profile_page.has_device_unbind_dialog(), "Device unbind dialog is not displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_title_text(), self.get_string("user_profile_delete_device_dialog_title"), "Text \"Are you sure you want to unbind the FFI00 device?\" is properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_description_text().replace('\n', '\\n'), self.get_string("user_profile_delete_device_dialog_message"), "Unbind message is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_yes_button_text(), self.get_string("yes"), "button \"Yes\" is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_no_button_text(), self.get_string("cancel"), "button \"No\" is not properly displayed")

            '''Click Yes in Device Unbind dialog and go to Device Unbind Page'''
            pixsee_profile_page.click_device_unbind_dialog_yes()
            self.assertTrue(device_unbind_page.is_in_device_unbind_page(), "Can't automatically go to Device Unbind Page from Pixsee Profile Page")

            '''Verify Device Unbind Page'''
            self.assertEqual(device_unbind_page.get_page_title_text(), self.get_string("delete_device_title"), "Text \"Initiate unbind\" is not properly displayed")
            self.assertEqual(device_unbind_page.get_message_text(), self.get_string("long_press_volume_white"), "Unbind message(ITC8) is not properly displayed")
            self.assertEqual(device_unbind_page.get_seen_flash_light_button_text(), self.get_string("delete_device_positive_button_white"), "button \"Blink white light\" is not properly displayed")
            self.assertEqual(device_unbind_page.get_cancel_button_text(), self.get_string("cancel"), "button \"Cancel\" is not properly displayed")

            '''Click Cancel in Device Unbind Page'''
            device_unbind_page.click_cancel()
            self.assertTrue(pixsee_profile_page.is_in_pixsee_profile_page(), "Can't return to Pixsee Profile Page after clicking close Device Unbind Page")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    @unittest.skip("Important: This test will unbind the device. If you want to run other tests after this, you may need to bind the device manually.")
    def test_device_unbind_success(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            baby_timeline_page = BabyTimelinePage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            pixsee_profile_page = PixseeProfilePage(self.driver)
            device_unbind_page = DeviceUnbindPage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Pixsee Profile Page'''
            pixsee_settings_page.click_pixsee_profile()
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

            '''Click Unbind and verify the device unbind dialog'''
            pixsee_profile_page.click_unbind_device()
            self.assertTrue(pixsee_profile_page.has_device_unbind_dialog(), "Device unbind dialog is not displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_title_text(), self.get_string("user_profile_delete_device_dialog_title"), "Text \"Are you sure you want to unbind the FFI00 device?\" is properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_description_text().replace('\n', '\\n'), self.get_string("user_profile_delete_device_dialog_message"), "Unbind message is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_yes_button_text(), self.get_string("yes"), "button \"Yes\" is not properly displayed")
            self.assertEqual(pixsee_profile_page.get_device_unbind_dialog_no_button_text(), self.get_string("cancel"), "button \"No\" is not properly displayed")

            '''Click Yes in Device Unbind dialog and go to Device Unbind Page'''
            pixsee_profile_page.click_device_unbind_dialog_yes()
            self.assertTrue(device_unbind_page.is_in_device_unbind_page(), "Can't automatically go to Device Unbind Page from Pixsee Profile Page")

            '''Verify Device Unbind Page'''
            self.assertEqual(device_unbind_page.get_page_title_text(), self.get_string("delete_device_title"), "Text \"Initiate unbind\" is not properly displayed")
            self.assertEqual(device_unbind_page.get_message_text(), self.get_string("long_press_volume_white"), "Unbind message(ITC8) is not properly displayed")
            self.assertEqual(device_unbind_page.get_seen_flash_light_button_text(), self.get_string("delete_device_positive_button_white"), "button \"Blink white light\" is not properly displayed")
            self.assertEqual(device_unbind_page.get_cancel_button_text(), self.get_string("cancel"), "button \"Cancel\" is not properly displayed")

            '''Click "Blink white light" in Device Unbind Page'''
            device_unbind_page.click_seen_flash_light()
            self.assertTrue(device_unbind_page.has_unbind_complete_dialog(), "Unbind complete dialog is not properly displayed")
            self.assertEqual(device_unbind_page.get_unbind_complete_dialog_title_text(), self.get_string("delete_device_dialog_title"), "Text \"Unbind complete\" is properly displayed")
            self.assertEqual(device_unbind_page.get_unbind_complete_dialog_ok_button_text(), self.get_string("ok"), "button \"Ok\" is not properly displayed")

            '''Click Ok in Unbind Complete dialog and check if the device is deleted'''
            device_unbind_page.click_unbind_complete_dialog_ok()
            self.assertTrue(baby_timeline_page.is_in_baby_timeline_page(), "Can't automatically return to Baby Timeline Page after unbinding device")
            baby_timeline_page.click_menu()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page from Baby Timeline Page")
            self.assertEqual(menu_page.get_settings_button_text(),self.get_string("home_initialization_menu_add_device"), "button \"Add device\" is not properly displayed")


        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()
