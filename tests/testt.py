from pages.base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.about_page import AboutPage

import time

class AboutTest(BaseTestCase):
    def setUp(self):
        super().setUp()

        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        about_page = AboutPage(self.driver)
        try:
            while self.driver.current_package != self.driver.capabilities.get("appPackage"):
                self.driver.terminate_app(self.driver.current_package)
                self.open_app()
            if about_page.is_in_about_page():
                return
            elif not baby_monitor_page.is_in_baby_monitor_page():
                self.shutdown_app()
                self.open_app()
            print("Finish opening app.")
            baby_monitor_page.click_home()
            menu_page.click_about()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
    def test_about_pixsee(self):
        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        about_page = AboutPage(self.driver)

        try:
            self.assertTrue(about_page.is_in_about_page(), "Can't go to About Page")

            '''Verify About Page content'''
            self.assertEqual(about_page.get_page_title_text(), self.get_string("about_menu_bar_title"), "Text \"About\" is not properly displayed")
            self.assertEqual(about_page.get_about_pixsee_text(), self.get_string("about_pixsee_bar_title"), "Text \"About FFI00\" is not properly displayed")
            self.assertEqual(about_page.get_terms_of_service_text(), self.get_string("about_terms_bar_title"), "Text \"Terms of Service\" is not properly displayed")
            self.assertEqual(about_page.get_privacy_policy_text(), self.get_string("privacy_policy"), "Text \"Privacy Policy\" is not properly displayed")
            self.assertEqual(about_page.get_app_version_text().split(':')[0] + ": ", self.get_string("about_app_version").split('%')[0], "Text \"App version: 'version number(%d)'\" is not properly displayed")
            self.assertEqual(about_page.get_camera_version_text().split(':')[0] + ": ", self.get_string("about_device_version").split('%')[0], "Text \"devices version: 'version number(%d)'\" is not properly displayed")

            '''Click Privacy Policy and verify content'''
            about_page.click_about_pixsee()
            self.assertTrue(about_page.is_in_about_pixsee_website(), "Can't go to About Pixsee website")
            '''Go back to About Page from Privacy Policy website'''
            self.go_back()
            self.assertTrue(about_page.is_in_about_page(), "Can't return to About Page from Privacy Policy website")


        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_privacy_policy(self):
        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        about_page = AboutPage(self.driver)

        try:
            self.assertTrue(about_page.is_in_about_page(), "Can't go to About Page")

            '''Verify About Page content'''
            self.assertEqual(about_page.get_page_title_text(), self.get_string("about_menu_bar_title"), "Text \"About\" is not properly displayed")
            self.assertEqual(about_page.get_about_pixsee_text(), self.get_string("about_pixsee_bar_title"), "Text \"About FFI00\" is not properly displayed")
            self.assertEqual(about_page.get_terms_of_service_text(), self.get_string("about_terms_bar_title"), "Text \"Terms of Service\" is not properly displayed")
            self.assertEqual(about_page.get_privacy_policy_text(), self.get_string("privacy_policy"), "Text \"Privacy Policy\" is not properly displayed")
            self.assertEqual(about_page.get_app_version_text().split(':')[0] + ": ", self.get_string("about_app_version").split('%')[0], "Text \"App version: 'version number(%d)'\" is not properly displayed")
            self.assertEqual(about_page.get_camera_version_text().split(':')[0] + ": ", self.get_string("about_device_version").split('%')[0], "Text \"devices version: 'version number(%d)'\" is not properly displayed")

            '''Click Privacy Policy and verify content'''
            about_page.click_privacy_policy()
            self.assertEqual(about_page.get_website_title_text(), self.get_string("privacy_policy"), "Text \"Privacy policy\" is not properly displayed")
            self.assertTrue(about_page.is_in_embedded_website(), "Can't go to Privacy Policy website")
            '''Go back to About Page from Privacy Policy website'''
            about_page.click_website_return()
            self.assertTrue(about_page.is_in_about_page(), "Can't return to About Page from Privacy Policy website")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

    def test_terms_of_service(self):
        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        about_page = AboutPage(self.driver)

        try:
            self.assertTrue(about_page.is_in_about_page(), "Can't go to About Page")

            '''Verify About Page content'''
            self.assertEqual(about_page.get_page_title_text(), self.get_string("about_menu_bar_title"), "Text \"About\" is not properly displayed")
            self.assertEqual(about_page.get_about_pixsee_text(), self.get_string("about_pixsee_bar_title"), "Text \"About FFI00\" is not properly displayed")
            self.assertEqual(about_page.get_terms_of_service_text(), self.get_string("about_terms_bar_title"), "Text \"Terms of Service\" is not properly displayed")
            self.assertEqual(about_page.get_privacy_policy_text(), self.get_string("privacy_policy"), "Text \"Privacy Policy\" is not properly displayed")
            self.assertEqual(about_page.get_app_version_text().split(':')[0] + ": ", self.get_string("about_app_version").split('%')[0], "Text \"App version: 'version number(%d)'\" is not properly displayed")
            self.assertEqual(about_page.get_camera_version_text().split(':')[0] + ": ", self.get_string("about_device_version").split('%')[0], "Text \"devices version: 'version number(%d)'\" is not properly displayed")

            '''Click Terms Of Service and verify content'''
            about_page.click_terms_of_service()
            self.assertEqual(about_page.get_website_title_text(), self.get_string("about_terms_bar_title"), "Text \"Terms of services\" is not properly displayed")
            self.assertTrue(about_page.is_in_embedded_website(), "Can't go to Terms Of Service website")
            '''Go back to About Page from Terms Of Service website'''
            about_page.click_website_return()
            self.assertTrue(about_page.is_in_about_page(), "Can't return to About Page from Terms Of Service website")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e

import time
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.cry_detection_page import CryDetectionPage





class CryDetectionCase(BaseTestCase):
    def setUp(self):
        super().setUp(no_reset=False)

    def test_01_cry_detection_switch(self):
        cry_detection_page = CryDetectionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page = BabyMonitorPage(self.driver)
        if not baby_monitor_page.is_connected():
            self.skipTest("not online，skip all test")
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()

        menu_page.click_settings()

        pixsee_settings_page.click_cry_detection()
        # check header text
        try:
            header = cry_detection_page.header_text()
            hint = self.get_string("crying_detection")
            self.assertEqual(header, hint)
            print("Cry detection header text right")
        except AssertionError:
            raise AssertionError("Cry detection header text wrong")
        # check Cry detection title
        try:
            title = cry_detection_page.title()
            hint = self.get_string("detection")
            self.assertEqual(title, hint)
            print("Cry detection title right")
        except AssertionError:
            raise AssertionError("Cry detection title wrong")
        # check Cry detection description
        try:
            subtitle = cry_detection_page.detection_description()
            hint = self.get_string("auto_detect_and_alert_when_baby_is_crying")
            self.assertEqual(subtitle, hint)
            print("Cry detection subtitle right")
        except AssertionError:
            raise AssertionError("Cry detection subtitle wrong")
        # switch status
        current_status = cry_detection_page.is_switch_on()
        self.check_switch_and_content(current_status, cry_detection_page.Sensitivity)
        cry_detection_page.click_switch()
        time.sleep(1)
        after_status = cry_detection_page.is_switch_on()
        self.check_switch_and_content(after_status, cry_detection_page.Sensitivity)
    def test_02_cry_detection_save(self):
        cry_detection_page = CryDetectionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page = BabyMonitorPage(self.driver)
        if not baby_monitor_page.is_connected():
            self.skipTest("not online，skip all test")
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()
        menu_page.click_settings()
        origin_status = pixsee_settings_page.cry_detection_status_text()
        pixsee_settings_page.click_cry_detection()
        # check save enable = false
        try:
            self.assertFalse(cry_detection_page.is_save_enable())
            print("Save diable test pass")
        except AssertionError:
            raise AssertionError("Save disable test failed")
        # turn on switch
        cry_detection_page.click_switch()
        cry_detection_page.click_save()
        new_status = pixsee_settings_page.cry_detection_status_text()
        if origin_status != new_status:
            print("save function success")
        else:
            raise AssertionError("Save function failed, status not changed")
    def test_03_cry_detection_back(self):
        cry_detection_page = CryDetectionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()

        self.skip_first_four_tutor()
        baby_monitor_page = BabyMonitorPage(self.driver)
        if not baby_monitor_page.is_connected():
            self.skipTest("not online，skip all test")
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()
        menu_page.click_settings()
        pixsee_settings_page.click_cry_detection()
        # back to settings page
        cry_detection_page.click_back()
        try:
            self.assertTrue(pixsee_settings_page.is_in_settings())
            print("Back to Pixsee Settings page")
        except AssertionError:
            raise AssertionError("Not in Pixsee Settings page")
    def test_04_cry_detection_tap_checkbox(self):
        cry_detection_page = CryDetectionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page = BabyMonitorPage(self.driver)
        if not baby_monitor_page.is_connected():
            self.skipTest("not online，skip all test")
        baby_monitor_page.click_home()
        # skip menu tutor
        time.sleep(2)

        menu_page.click_logout()

        menu_page.click_settings()

        pixsee_settings_page.click_cry_detection()
        if cry_detection_page.is_switch_on():
            pass
        else:
            cry_detection_page.click_switch()
        # check Cry detection type group titles
        try:
            sensitivity = cry_detection_page.sensitivity_text()
            hint = self.get_string("sensitivity_level")
            self.assertEqual(sensitivity, hint)
            print("Sensitivity title is correct")
        except AssertionError:
            raise AssertionError("Sensitivity title is wrong")
        try:
            music_settings = cry_detection_page.music_settings_text()
            hint = self.get_string("auto_play_music")
            self.assertEqual(music_settings, hint)
            print("music settings text right")
        except AssertionError:
            raise AssertionError("Music settings text wrong")
        try:
            smart_soothing = cry_detection_page.smart_soothing_text()
            hint = self.get_string("smart_soothing")
            self.assertEqual(smart_soothing, hint)
            print("smart soothing text right")
        except AssertionError:
            raise AssertionError("Smart soothing text wrong")
            # check box name
        try:
            low = cry_detection_page.low_text()
            hint = self.get_string("sensitivity_low")
            self.assertEqual(low, hint)
            print("Low checkbox text is correct")
        except AssertionError:
            raise AssertionError("Low checkbox text is wrong")
        try:
            medium = cry_detection_page.medium_text()
            hint = self.get_string("sensitivity_medium")
            self.assertEqual(medium, hint)
            print("Medium checkbox text is correct")
        except AssertionError:
            raise AssertionError("Medium checkbox text is wrong")
        try:
            high = cry_detection_page.high_text()
            hint = self.get_string("sensitivity_high")
            self.assertEqual(high, hint)
            print("High checkbox text is correct")
        except AssertionError:
            raise AssertionError("High checkbox text is wrong")
        # check clickable
        try:
            self.assertTrue(cry_detection_page.is_low_clickable())
            print("Low checkbox is clickable")
        except AssertionError:
            raise AssertionError("Low checkbox is not clickable")
        try:
            self.assertTrue(cry_detection_page.is_medium_clickable())
            print("Medium checkbox is clickable")
        except AssertionError:
            raise AssertionError("Medium checkbox is not clickable")
        try:
            self.assertTrue(cry_detection_page.is_high_clickable())
            print("High checkbox is clickable")
        except AssertionError:
            raise AssertionError("High checkbox is not clickable")
    def test_05_cry_detection_smart_soothing_switch(self):
        cry_detection_page = CryDetectionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page = BabyMonitorPage(self.driver)
        if not baby_monitor_page.is_connected():
            self.skipTest("not online，skip all test")
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()
        menu_page.click_settings()

        pixsee_settings_page.click_cry_detection()
        if cry_detection_page.is_switch_on() :
            pass
        else:
            cry_detection_page.click_switch()
        # switch status
        current_status = cry_detection_page.is_smart_soothing_switch_on()
        self.check_switch_and_content(current_status, cry_detection_page.Music)
        time.sleep(1)
        cry_detection_page.click_smart_soothing_switch()
        time.sleep(1)
        after_status = cry_detection_page.is_smart_soothing_switch_on()
        self.check_switch_and_content(after_status, cry_detection_page.Music)
    def test_06_cry_detection_music_page(self):
        cry_detection_page = CryDetectionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(), self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page = BabyMonitorPage(self.driver)
        if not baby_monitor_page.is_connected():
            self.skipTest("not online，skip all test")
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()
        menu_page.click_settings()

        pixsee_settings_page.click_cry_detection()
        if cry_detection_page.is_switch_on():
            pass
        else:
            cry_detection_page.click_switch()
        if cry_detection_page.is_smart_soothing_switch_on():
            pass
        else:
            cry_detection_page.click_smart_soothing_switch()
        cry_detection_page.click_music()
        # check enter music room
        try:
            self.assertTrue(cry_detection_page.is_in_music_page())
            print("entered music room successfully")
        except AssertionError:
            raise AssertionError("Not in music room")
    def test_07_cry_detection_back_discard(self):
        cry_detection_page = CryDetectionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page = BabyMonitorPage(self.driver)
        if not baby_monitor_page.is_connected():
            self.skipTest("not online，skip all test")
        baby_monitor_page.click_home()
        # skip menu tutor
        time.sleep(2)

        menu_page.click_logout()
        menu_page.click_settings()
        origin_status = pixsee_settings_page.cry_detection_status_text()
        pixsee_settings_page.click_cry_detection()
        cry_detection_page.click_switch()
        cry_detection_page.click_back()
        # check if is in discard dialog
        try:
            self.assertTrue(cry_detection_page.is_in_discard_dialog())
            print("In discard dialog")
            # check discard dialog text
            try:
                discard = cry_detection_page.discard_message_text()
                hint = self.get_string("discard_cry_detection_confirmation_message")
                self.assertEqual(discard, hint)
                print("Discard dialog title right")
            except AssertionError:
                raise AssertionError("Discard dialog title wrong")
            try:
                yes = cry_detection_page.discard_yes_text()
                hint = self.get_string("yes")
                self.assertEqual(yes, hint)
                print("Discard dialog yes text right")
            except AssertionError:
                raise AssertionError("Discard dialog yes text wrong")
            try:
                no = cry_detection_page.discard_no_text()
                hint = self.get_string("no")
                self.assertEqual(no, hint)
                print("Discard dialog no text right")
            except AssertionError:
                raise AssertionError("Discard dialog no text wrong")
            # click yes
            cry_detection_page.click_discard_yes()
            new_status = pixsee_settings_page.cry_detection_status_text()
            try:
                self.assertEqual(origin_status, new_status)
                print("Discard function success")
            except AssertionError:
                raise AssertionError("Discard function failed, status changed")
        except AssertionError:
            print("Not in discard dialog")
            raise AssertionError("Not in discard dialog")


















