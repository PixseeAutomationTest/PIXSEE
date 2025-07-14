from pages.menu_page import MenuPage
from pages.setting.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage

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
			self.assertEqual(menu_page.PixseeSettingstxt_text(), hint)
			print("Settings page title right")
		except AssertionError:
			print("Settings page title wrong")
			raise AssertionError("Settings page title mismatch")
		menu_page.click_settings()
		try:
			self.assertTrue(pixsee_settings_page.is_in_pixsee_settings_page())
			print("In Pixsee Settings page")
		except AssertionError:
			print("Not in Pixsee Settings page")
			raise AssertionError("Not in Pixsee Settings page")




