from pages.menu_page import MenuPage
from pages.setting.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.setting.SD_card_stat_page import PixseeFriendsSDcardPage




class PixseeFriendsSDcardTest(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)
	def test_01_check_word(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		sd_card_page = PixseeFriendsSDcardPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		pixsee_settings_page.click_SDcard()
		try:
			header = sd_card_page.header_text()
			hint = self.get_string("sd_card_status")
			self.assertEqual(header, hint)
			print("Header text test success")
		except AssertionError:
			print("Header text test failed")
			raise AssertionError("Header text test failed, expected text not found")
		if sd_card_page.format_button_enabled():
			try:
				format_button_text = sd_card_page.format_button_text()
				hint = self.get_string("format")
				self.assertEqual(format_button_text, hint)
				print("Format button text test success")
			except AssertionError:
				print("Format button text test failed")
				raise AssertionError("Format button text test failed, expected text not found")
			try:
				title = sd_card_page.title_text()
				hint = self.get_string("external_sd_card_storage")
				self.assertEqual(title, hint)
				print("Title text test success")
			except AssertionError:
				print("Title text test failed")
				raise AssertionError("Title text test failed, expected text not found")
		else:
			try:
				title = sd_card_page.title_text()
				hint = self.get_string("sd_card_is_not_available")
				self.assertEqual(title, hint)
				print("Title text test success")
			except AssertionError:
				print("Title text test failed")
				raise AssertionError("Title text test failed, expected text not found")
	def test_02_format_sd_card(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		sd_card_page = PixseeFriendsSDcardPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		pixsee_settings_page.click_SDcard()
		sd_card_page.click_format()
		# check if in format dialog
		try:
			self.assertTrue(sd_card_page.is_in_format_dialog())
			print("Format dialog test success")
		except AssertionError:
			print("Format dialog test failed")
			raise AssertionError("Format dialog test failed, expected dialog not found")







