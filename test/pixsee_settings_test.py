from pages.menu_page import MenuPage
from pages.pixsee_settings.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.pixsee_settings.pixsee_friends_detection_page import PixseeFriendsDetPage
from pages.pixsee_settings.enviroment_settings_page import EnvironmentSettingsPage
from pages.pixsee_settings.SD_card_stat_page import SDcardStatusPage
import time


class PixseeSettingsTest(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)
	def test_01_enter_pixsee_profile(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		# check pixsee profile title on settings page
		try:
			hint = self.get_string("profile_settings")
			self.assertEqual(pixsee_settings_page.profile_text(),hint)
		except AssertionError:
			print("Pixsee profile title wrong")
			raise AssertionError("Pixsee profile title mismatch")
		# enter pixsee profile page
		pixsee_settings_page.click_PixseeProfile()
		# check if is in pixsee profile page
	def test_02_enter_wifi_settings(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		# check wifi settings title on settings page
		try:
			hint = self.get_string("wifi_settings")
			self.assertEqual(pixsee_settings_page.wifi_text(), hint)
			print("Wifi settings title right")
		except AssertionError:
			print("Wifi settings title wrong")
			raise AssertionError("Wifi settings title mismatch")
		# enter wifi settings page
		pixsee_settings_page.click_WifiSettings()
		# check if is in wifi settings page
	def test_03_enter_pixsee_friends_detection(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		# check friends detection title on settings page
		try:
			hint = self.get_string("pixsee_settings_menu_pixsee_friends_detection_title_menu")
			self.assertEqual(pixsee_settings_page.pixsee_friends_detection_text(), hint)
			print("Friends detection title right")
		except AssertionError:
			print("Friends detection title wrong")
			raise AssertionError("Friends detection title mismatch")
		# enter friends detection page
		pixsee_settings_page.click_PixseeFriendsDetection()

		# check if is in friends detection page
		try:
			self.assertTrue(pixsee_friends_page.is_in_pixsee_friends_det_page())
			print("In Pixsee Friends Detection page")
		except AssertionError:
			print("Not in Pixsee Friends Detection page")
			raise AssertionError("Not in Pixsee Friends Detection page")
	def test_04_enter_environment_settings(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		environment_settings_page = EnvironmentSettingsPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		# check environment settings title on settings page
		try:
			hint = self.get_string("sensor_settings")
			self.assertEqual(pixsee_settings_page.environment_settings_text(), hint)
			print("Environment settings title right")
		except AssertionError:
			print("Environment settings title wrong")
			raise AssertionError("Environment settings title mismatch")
		# enter environment settings page
		pixsee_settings_page.click_EnvironmentSettings()
		# check if is in environment settings page
		try:
			self.assertTrue(environment_settings_page.is_in_envir_page())
			print("In Environment Settings page")
		except AssertionError:
			print("Not in Environment Settings page")
			raise AssertionError("Not in Environment Settings page")
	def test_05_enter_cry_detection(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		# check cry detection title on settings page
		try:
			hint = self.get_string("crying_detection")
			self.assertEqual(pixsee_settings_page.cry_detection_text(), hint)
			print("Cry detection title right")
		except AssertionError:
			print("Cry detection title wrong")
			raise AssertionError("Cry detection title mismatch")
		# enter cry detection page
		pixsee_settings_page.click_CryDetection()
		# check if is in cry detection page
	def test_06_enter_area_detection(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()
	def test_07_enter_covered_face_detection(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()
	def test_08_enter_timelapse_video(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()
	def test_09_enter_voice_service(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()
	def test_10_pixsee_settings(self):
		menu_page = MenuPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())

		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		hint = self.get_string("device_settings")
		try:
			# check pixsee settings title correct
			self.assertEqual(menu_page.PixseeSettingstxt_text(), hint)
			print("Settings page title right")
		except AssertionError:
			print("Settings page title wrong")
			raise AssertionError("Settings page title mismatch")

		menu_page.click_settings()


		try:
			# check pixsee settings clickable
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

		login_page.login(self.account(),self.password())

		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		try:
			# check shutter sound title correct
			hint = self.get_string("shutter_sound")
			self.assertEqual(pixsee_settings_page.shutter_sound_text(), hint)
			print("Shutter sound title right")
		except AssertionError:
			print("Shutter sound title wrong")
			raise AssertionError("Shutter sound title mismatch")

		# check the switch's status
		current_status = pixsee_settings_page.shutter_sound_switch_status()  # True/False

		pixsee_settings_page.click_ShutterSoundSwitch()
		new_status = pixsee_settings_page.shutter_sound_switch_status()

		assert new_status != current_status,"shutter sound switch fail"
		print("Shutter sound switch status changed successfully")







		pixsee_settings_page.click_ShutterSoundSwitch()
	def test_12_LED_indicator(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())

		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		try:
			# check LED title correct
			hint = self.get_string("indicator_led")
			self.assertEqual(pixsee_settings_page.led_indicator_text(), hint)
			print("LED indicator title right")
		except AssertionError:
			print("LED indicator title wrong")
			raise AssertionError("LED indicator title mismatch")

		# check the LED switch's status
		current_status = pixsee_settings_page.led_indicator_switch_status()  # True/False

		pixsee_settings_page.click_LEDIndicatorSwitch()
		new_status = pixsee_settings_page.led_indicator_switch_status()

		assert new_status != current_status, "LED indicator switch fail"
		print("LED indicator switch status changed successfully")
	def test_13_night_mode(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())

		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		try:
			# check night mode title correct
			hint = self.get_string("detection_settings_night_vision")
			self.assertEqual(pixsee_settings_page.night_mode_text(), hint)
			print("Night mode title right")
		except AssertionError:
			print("Night mode title wrong")
			raise AssertionError("Night mode title mismatch")

		try:
			# check night mode description correct
			hint = self.get_string("detection_settings_night_vision_subtext")
			self.assertEqual(pixsee_settings_page.night_mode_subtext(), hint)
			print("Night mode description right")
		except AssertionError:
			print("Night mode description wrong")
			raise AssertionError("Night mode description mismatch")

		# check the night mode switch's status
		current_status = pixsee_settings_page.night_mode_switch_status()
		pixsee_settings_page.click_NightModeSwitch()
		new_status = pixsee_settings_page.night_mode_switch_status()

		assert new_status != current_status, "Night mode switch fail"
		print("Night mode switch status changed successfully")
	def test_14_privacy_mode(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())

		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()
		time.sleep(1)
		self.down_scroll()

		try:
			# check privacy mode title correct
			hint = self.get_string("privacy_control_vision")
			self.assertEqual(pixsee_settings_page.privacy_mode_text(), hint)
			print("Privacy mode title right")
		except AssertionError:
			print("Privacy mode title wrong")
			raise AssertionError("Privacy mode title mismatch")

		try:
			# check privacy mode description correct
			hint = self.get_string("privacy_control_subtext")
			self.assertEqual(pixsee_settings_page.privacy_mode_subtext(), hint)
			print("Privacy mode description right")
		except AssertionError:
			print("Privacy mode description wrong")
			raise AssertionError("Privacy mode description mismatch")

		# check the privacy mode switch's status
		current_status = pixsee_settings_page.privacy_mode_switch_status()
		pixsee_settings_page.click_PrivacyModeSwitch()
		new_status = pixsee_settings_page.privacy_mode_switch_status()

		assert new_status != current_status, "Privacy mode switch fail"
		print("Privacy mode switch status changed successfully")
		self.shutdown_app()
	def test_15_enter_SDcard_status(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		sd_card_page = SDcardStatusPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		# check SD card status title on settings page
		try:
			hint = self.get_string("sd_card_status")
			self.assertEqual(pixsee_settings_page.sdcard_status_text(), hint)
			print("SD card status title right")
		except AssertionError:
			print("SD card status title wrong")
			raise AssertionError("SD card status title mismatch")
		# enter SD card status page
		pixsee_settings_page.click_SDcard()
		# check if is in SD card status page
		try:
			self.assertTrue(sd_card_page.is_in_sdcard_page())
			print("In SD card status page")
		except AssertionError:
			print("Not in SD card status page")
			raise AssertionError("Not in SD card status page")



















