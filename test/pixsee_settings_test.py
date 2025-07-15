from pages.menu_page import MenuPage
from pages.setting.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
import time

from appium.webdriver.common.appiumby import AppiumBy

class PixseeSettingsTest(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)

	def test_01_pixsee_settings(self):
		menu_page = MenuPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")

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
	def test_02_shutter_sound(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")

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
	def test_03_LED_indicator(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")

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
	def test_04_night_mode(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")

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
	def test_05_privacy_mode(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")

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
















