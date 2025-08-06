from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_profile_page import PixseeProfilePage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.pixsee_friends_detection_page import PixseeFriendsDetPage
from pages.menu_pages.pixsee_settings_pages.enviroment_settings_page import EnvironmentSettingsPage
from pages.menu_pages.pixsee_settings_pages.SD_card_stat_page import SDcardStatusPage
import time
from pages.menu_pages.pixsee_settings_pages.cry_detection_page import CryDetectionPage
from pages.menu_pages.pixsee_settings_pages.covered_face_detection_page import CoveredFaceDetectionPage
from pages.menu_pages.pixsee_settings_pages.area_detection_page import AreaDetectionPage
from pages.menu_pages.pixsee_settings_pages.time_lapse_video_page import TimeLapseVideoPage
from pages.menu_pages.pixsee_settings_pages.voice_service_pages.voice_service_page import VoiceServicePage
from pages.menu_pages.pixsee_settings_pages.wifi_settings_page import WifiSettingsPage



class PixseeSettingsTest(BaseTestCase):
    def setUp(self):
        super().setUp(no_reset=True)
    def test_00_open_app(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        self.shutdown_app()
        # open app
        self.open_app()
        baby_monitor_page.is_in_baby_monitor_page()
        baby_monitor_page.click_home()
        menu_page.click_settings()
    # all start from pixsee settings page end up in pixsee settings page too
    def test_01_enter_pixsee_profile(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        pixsee_profile_page = PixseeProfilePage(self.driver)

        # check pixsee profile title on settings page
        try:
            hint = self.get_string("profile_settings")
            self.assertEqual(pixsee_settings_page.profile_text(),hint)
        except AssertionError:
            print("Pixsee profile title wrong")
            raise AssertionError("Pixsee profile title mismatch")
        # enter pixsee profile page
        pixsee_settings_page.click_pixsee_profile()
        # check if is in pixsee profile page
        try:
            self.assertTrue(pixsee_profile_page.is_in_pixsee_profile_page())
            print("successfully enter Pixsee Profile page")
        except AssertionError:
            raise AssertionError("failed to enter Pixsee Profile page")
        pixsee_profile_page.click_back()
    def test_02_enter_wifi_settings(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        wifi_settings_page = WifiSettingsPage(self.driver)

        # check wifi settings title on settings page
        try:
            hint = self.get_string("wifi_settings")
            self.assertEqual(pixsee_settings_page.wifi_text(), hint)
            print("Wifi settings title right")
        except AssertionError:
            raise AssertionError("Wifi settings title wrong")
        # enter wifi settings page
        pixsee_settings_page.click_wifi_settings()
        # check if is in wifi settings page
        try:
            self.assertTrue(wifi_settings_page.is_in_wifi_popup_page())
            print("successfully enter wifi settings page")
        except AssertionError:
            print("failed to enter wifi settings page")
            raise AssertionError("Not in Wifi Settings page")
        wifi_settings_page.click_pop_up_cancel()
    def test_03_enter_pixsee_friends_detection(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        pixsee_friends_page = PixseeFriendsDetPage(self.driver)

        # check friends detection title on settings page
        try:
            hint = self.get_string("pixsee_settings_menu_pixsee_friends_detection_title_menu")
            self.assertEqual(pixsee_settings_page.pixsee_friends_detection_text(), hint)
            print("Friends detection title right")
        except AssertionError:
            raise AssertionError("Friends detection title wrong")
        # enter friends detection page
        pixsee_settings_page.click_pixsee_friends_detection()

        # check if is in friends detection page
        try:
            self.assertTrue(pixsee_friends_page.is_in_pixsee_friends_det_page())
            print("successfully enter Pixsee Friends Detection page")
        except AssertionError:
            print("failed to enter Pixsee Friends Detection page")
            raise AssertionError("Not in Pixsee Friends Detection page")
        pixsee_friends_page.click_back()
    def test_04_enter_environment_settings(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        environment_settings_page = EnvironmentSettingsPage(self.driver)
        # check environment settings title on settings page
        try:
            hint = self.get_string("sensor_settings")
            self.assertEqual(pixsee_settings_page.environment_settings_text(), hint)
            print("Environment settings title right")
        except AssertionError:
            raise AssertionError("Environment settings title wrong")
        # enter environment settings page
        pixsee_settings_page.click_environment_settings()
        # check if is in environment settings page
        try:
            self.assertTrue(environment_settings_page.is_in_envir_page())
            print("In Environment Settings page")
        except AssertionError:
            print("Not in Environment Settings page")
            raise AssertionError("Not in Environment Settings page")
        environment_settings_page.click_back()
    def test_05_enter_cry_detection(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        cry_detection_page = CryDetectionPage(self.driver)

        self.shutdown_app()
        self.open_app()
        baby_monitor_page.is_in_baby_monitor_page()
        if baby_monitor_page.is_connected():
            baby_monitor_page.click_home()
            menu_page.click_settings()
            # check cry detection title on settings page
            try:
                hint = self.get_string("crying_detection")
                self.assertEqual(pixsee_settings_page.cry_detection_text(), hint)
                print("Cry detection title right")
            except AssertionError:
                raise AssertionError("Cry detection title wrong")
            # enter cry detection page
            pixsee_settings_page.click_cry_detection()
            # check if is in cry detection page
            try:
                self.assertTrue(cry_detection_page.is_in_cry_detection_page())
                print("entered Cry Detection page successfully")
            except AssertionError:
                print("entered Cry Detection page unsuccessfully")
                raise AssertionError("Not in Cry Detection page")
        else:
            print("Baby monitor is not connected, can't enter Cry Detection page")
            raise AssertionError("Baby monitor is not connected, can't enter Cry Detection page")
    def test_06_enter_area_detection(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        area_detection_page = AreaDetectionPage(self.driver)

        self.shutdown_app()
        self.open_app()
        baby_monitor_page.is_in_baby_monitor_page()
        if baby_monitor_page.is_connected():
            baby_monitor_page.click_home()
            menu_page.click_settings()
            # check area detection title on settings page
            try:
                hint = self.get_string("area_detection")
                self.assertEqual(pixsee_settings_page.area_detection_text(), hint)
                print("Area detection title right")
            except AssertionError:
                raise AssertionError("Area detection title wrong")
            # enter area detection page
            pixsee_settings_page.click_area_detection()
            # check if is in area detection page
            try:
                self.assertTrue(area_detection_page.is_in_area_detection_page())
                print("entered Area Detection page successfully")
            except AssertionError:
                print("entered Area Detection page unsuccessfully")
                raise AssertionError("Not in Area Detection page")
        else:
            print("Baby monitor is not connected, can't enter Area Detection page")
            raise AssertionError("Baby monitor is not connected, can't enter Area Detection page")
    def test_07_enter_covered_face_detection(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        covered_face_page = CoveredFaceDetectionPage(self.driver)

        self.shutdown_app()
        self.open_app()
        baby_monitor_page.is_in_baby_monitor_page()
        if baby_monitor_page.is_connected():
            baby_monitor_page.click_home()
            menu_page.click_settings()
            # check covered face detection title on settings page
            try:
                hint = self.get_string("cover_detection_settings_label")
                self.assertEqual(pixsee_settings_page.covered_face_detection_text(), hint)
                print("Covered Face detection title right")
            except AssertionError:
                raise AssertionError("Covered Face detection title wrong")
            # enter covered face detection page
            pixsee_settings_page.click_covered_face_detection()
            # check if is in covered face detection page
            try:
                self.assertTrue(covered_face_page.is_in_covered_face_detection_page())
                print("entered Covered Face Detection page successfully")
            except AssertionError:
                print("entered Covered Face Detection page unsuccessfully")
                raise AssertionError("Not in Covered Face Detection page")
        else:
            print("Baby monitor is not connected, can't enter Covered Face Detection page")
            raise AssertionError("Baby monitor is not connected, can't enter Covered Face Detection page")
    def test_08_enter_timelapse_video(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        timelapse_video_page = TimeLapseVideoPage(self.driver)

        self.shutdown_app()
        self.open_app()
        baby_monitor_page.is_in_baby_monitor_page()
        if baby_monitor_page.is_connected():
            baby_monitor_page.click_home()
            menu_page.click_settings()
            # check timelapse video title on settings page
            try:
                hint = self.get_string("time_lapse")
                self.assertEqual(pixsee_settings_page.time_lapse_video_text(), hint)
                print("Timelapse video title right")
            except AssertionError:
                raise AssertionError("Timelapse video title wrong")
            # enter timelapse video page
            pixsee_settings_page.click_time_lapse_video()
            # check if is in timelapse video page
            try:
                self.assertTrue(timelapse_video_page.is_in_timelapse_video_page())
                print("entered Timelapse Video page successfully")
            except AssertionError:
                print("entered Timelapse Video page unsuccessfully")
                raise AssertionError("Not in Timelapse Video page")
        else:
            print("Baby monitor is not connected, can't enter Timelapse Video page")
            raise AssertionError("Baby monitor is not connected, can't enter Timelapse Video page")
        timelapse_video_page.click_back()
    def test_09_enter_voice_service(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        login_page = LoginPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        voice_service_page = VoiceServicePage(self.driver)

        # check voice service title on settings page
        try:
            hint = self.get_string("voice_service_settings_title")
            self.assertEqual(pixsee_settings_page.voice_service_text(), hint)
            print("Voice service title right")
        except AssertionError:
            raise AssertionError("Voice service title wrong")
        # enter environment settings page
        pixsee_settings_page.click_voice_service()
        # check if is in voice service page
        try:
            self.assertTrue(voice_service_page.is_in_voice_service_page())
            print("In Voice Service page")
        except AssertionError:
            print("Not in Voice Service page")
        voice_service_page.click_back()
    def test_10_pixsee_settings(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)
        sd_card_page = SDcardStatusPage(self.driver)

        self.shutdown_app()
        self.open_app()
        baby_monitor_page.is_in_baby_monitor_page()
        baby_monitor_page.click_home()

        hint = self.get_string("device_settings")
        try:
            # check pixsee settings title correct
            self.assertEqual(menu_page.pixsee_settingstxt_text(), hint)
            print("Settings page title right")
        except AssertionError:
            raise AssertionError("Settings page title wrong")

        menu_page.click_settings()

        try:
            # check if is in pixsee settings
            self.assertTrue(pixsee_settings_page.is_in_settings())
            print("In Pixsee Settings page")
        except AssertionError:
            print("Not in Pixsee Settings page")
            raise AssertionError("Not in Pixsee Settings page")
    def test_11_shutter_sound(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)
        sd_card_page = SDcardStatusPage(self.driver)


        try:
            # check shutter sound title correct
            hint = self.get_string("shutter_sound")
            self.assertEqual(pixsee_settings_page.shutter_sound_text(), hint)
            print("Shutter sound title right")
        except AssertionError:
            raise AssertionError("Shutter sound title wrong")

        # check the switch's status
        current_status = pixsee_settings_page.shutter_sound_switch_status()  # True/False

        pixsee_settings_page.click_shutter_sound_switch()
        new_status = pixsee_settings_page.shutter_sound_switch_status()

        assert new_status != current_status,"shutter sound switch fail"
        print("Shutter sound switch status changed successfully")
    def test_12_LED_indicator(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)
        sd_card_page = SDcardStatusPage(self.driver)


        try:
            # check LED title correct
            hint = self.get_string("indicator_led")
            self.assertEqual(pixsee_settings_page.led_indicator_text(), hint)
            print("LED indicator title right")
        except AssertionError:
            raise AssertionError("LED indicator title wrong")

        # check the LED switch's status
        current_status = pixsee_settings_page.led_indicator_switch_status()  # True/False

        pixsee_settings_page.click_led_indicator_switch()
        new_status = pixsee_settings_page.led_indicator_switch_status()

        assert new_status != current_status, "LED indicator switch fail"
        print("LED indicator switch status changed successfully")
    def test_13_night_mode(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)
        sd_card_page = SDcardStatusPage(self.driver)



        try:
            # check night mode title correct
            hint = self.get_string("detection_settings_night_vision")
            self.assertEqual(pixsee_settings_page.night_mode_text(), hint)
            print("Night mode title right")
        except AssertionError:
            raise AssertionError("Night mode title wrong")

        try:
            # check night mode description correct
            hint = self.get_string("detection_settings_night_vision_subtext")
            self.assertEqual(pixsee_settings_page.night_mode_subtext(), hint)
            print("Night mode description right")
        except AssertionError:
            raise AssertionError("Night mode description wrong")

        # check the night mode switch's status
        current_status = pixsee_settings_page.night_mode_switch_status()
        pixsee_settings_page.click_night_mode_switch()
        new_status = pixsee_settings_page.night_mode_switch_status()

        assert new_status != current_status, "Night mode switch fail"
        print("Night mode switch status changed successfully")
    def test_14_privacy_mode(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)
        sd_card_page = SDcardStatusPage(self.driver)


        time.sleep(1)
        self.up_scroll()
        time.sleep(2)
        try:
            # check privacy mode title correct
            hint = self.get_string("privacy_control_vision")
            self.assertEqual(pixsee_settings_page.privacy_mode_text(), hint)
            print("Privacy mode title right")
        except AssertionError:
            raise AssertionError("Privacy mode title wrong")

        try:
            # check privacy mode description correct
            hint = self.get_string("privacy_control_subtext")
            self.assertEqual(pixsee_settings_page.privacy_mode_subtext(), hint)
            print("Privacy mode description right")
        except AssertionError:
            raise AssertionError("Privacy mode description wrong")

        # check the privacy mode switch's status
        current_status = pixsee_settings_page.privacy_mode_switch_status()
        pixsee_settings_page.click_privacy_mode_switch()
        new_status = pixsee_settings_page.privacy_mode_switch_status()

        assert new_status != current_status, "Privacy mode switch fail"
        print("Privacy mode switch status changed successfully")
    def test_15_enter_SDcard_status(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)
        sd_card_page = SDcardStatusPage(self.driver)


        time.sleep(1)
        self.up_scroll()
        time.sleep(2)
        # check SD card status title on settings page
        try:
            hint = self.get_string("sd_card_status")
            self.assertEqual(pixsee_settings_page.sdcard_status_text(), hint)
            print("SD card status title right")
        except AssertionError:
            raise AssertionError("SD card status title wrong")
        # enter SD card status page
        pixsee_settings_page.click_sd_card()
        # check if is in SD card status page
        try:
            self.assertTrue(sd_card_page.is_in_sdcard_page())
            print("In SD card status page")
        except AssertionError:
            print("Not in SD card status page")
            raise AssertionError("Not in SD card status page")



















