from pages.menu_page import MenuPage
from pages.setting.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.setting.pixsee_friends_det_page import PixseeFriendsDetPage
from appium.webdriver.common.appiumby import AppiumBy

class PixseeSettingsTest(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)

	def test_pixsee_settings(self):
		menu_page = MenuPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login("amypixsee02@gmail.com", "@Aa12345")

		baby_monitor_page.click_home()
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

		self.shutdown_app()
	def test_shutter_sound(self):
		menu_page = MenuPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login("amypixsee02@gmail.com", "@Aa12345")
		baby_monitor_page.click_home()
		menu_page.click_settings()

		try:
			# check shutter sound title correct
			hint = self.get_string("shutter_sound")
			self.assertEqual(pixsee_settings_page.shutter_sound_text(), hint)
			print("Shutter sound title right")
		except AssertionError:
			print("Shutter sound title wrong")
			raise AssertionError("Shutter sound title mismatch")
		pixsee_settings_page.click_ShutterSoundSwitch()












