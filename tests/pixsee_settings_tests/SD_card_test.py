import time

from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.pixsee_settings_pages.SD_card_stat_page import SDcardStatusPage




class SDcardCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=True)
	# start from pixsee settings page
	def test_01_check_word(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		sd_card_page = SDcardStatusPage(self.driver)

		time.sleep(1)  # wait for settings page to load
		self.up_scroll()
		time.sleep(2)
		pixsee_settings_page.click_sd_card()
		# check header text
		try:
			header = sd_card_page.header_text()
			hint = self.get_string("sd_card_status")
			self.assertEqual(header, hint)
			print("Header text test success")
		except AssertionError:
			raise AssertionError("Header text test failed")

		if sd_card_page.format_button_enabled():
			# check button text
			try:
				format_button_text = sd_card_page.format_button_text()
				hint = self.get_string("format")
				self.assertEqual(format_button_text, hint)
				print("Format button text test success")
			except AssertionError:
				raise AssertionError("Format button text test failed")
			# check description text
			try:
				title = sd_card_page.title_text()
				hint = self.get_string("external_sd_card_storage")
				self.assertEqual(title, hint)
				print("Title text test success")
			except AssertionError:
				raise AssertionError("Title text test failed")
		else:
			# check no sd card text
			try:
				title = sd_card_page.title_text()
				hint = self.get_string("sd_card_is_not_available")
				self.assertEqual(title, hint)
				print("Title text test success")
			except AssertionError:
				raise AssertionError("Title text test failed")
	# start from sd card page
	def test_02_check_back_button(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		sd_card_page = SDcardStatusPage(self.driver)

		sd_card_page.click_back()
		# back to settings page
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("Back to Pixsee Settings page")
		except AssertionError:
			raise AssertionError("Not in Pixsee Settings page")
	# start from pixsee settings page
	def test_03_check_format_button(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		sd_card_page = SDcardStatusPage(self.driver)

		self.up_scroll()
		time.sleep(2)
		pixsee_settings_page.click_sd_card()
		sd_card_page.click_format()
		# check if is in format dialog
		try:
			self.assertTrue(sd_card_page.is_in_format_dialog())
			print("Format dialog test success")
		except AssertionError:
			raise AssertionError("Format dialog test failed")
	# start from dialog
	def test_04_check_format_go_and_no(self):
		sd_card_page = SDcardStatusPage(self.driver)

		# check dialog title
		try:
			title = sd_card_page.dialog_text()
			hint = self.get_string("are_you_sure_format_sd_card")
			self.assertEqual(title, hint)
			print("Dialog title test success")
		except AssertionError:
			raise AssertionError("Dialog title test failed")
		# check dialog button text
		try:
			go_button_text = sd_card_page.go_button_text()
			hint = self.get_string("go_to_format")
			self.assertEqual(go_button_text, hint)
			print("Go button text test success")
		except AssertionError:
			raise AssertionError("Go button text test failed")
		try:
			no_button_text = sd_card_page.no_button_text()
			hint = self.get_string("no_go_back")
			self.assertEqual(no_button_text, hint)
			print("No button text test success")
		except AssertionError:
			raise AssertionError("No button text test failed")
		# click no button
		sd_card_page.click_no()
		# check if back to sd card page
		try:
			self.assertTrue(sd_card_page.is_in_sdcard_page())
			print("Back to sd card page test success")
		except AssertionError:
			raise AssertionError("Back to sd card page test failed")
		# click format button
		sd_card_page.click_format()
		# click go button
		sd_card_page.click_go()
		# check if is formatting
		try:
			self.assertTrue(sd_card_page.is_formatting())
			print("Formatting test success")
		except AssertionError:
			raise AssertionError("Formatting test failed")
	# start from formatting dialog
	def test_05_check_formatting_close(self):
		sd_card_page = SDcardStatusPage(self.driver)
		# check formatted dialog
		time.sleep(150)
		try:
			self.assertTrue(sd_card_page.is_in_format_dialog())
			print("Formatted dialog test success")
		except AssertionError:
			raise AssertionError("Formatted dialog test failed")
		# check dialog title
		try:
			title = sd_card_page.dialog_text()
			hint = self.get_string("sd_card_formatted_succesfully")
			self.assertEqual(title, hint)
			print("Formatted dialog title test success")
		except AssertionError:
			raise AssertionError("Formatted dialog title test failed")
		# check dialog button text
		try:
			go_button_text = sd_card_page.go_button_text()
			hint = self.get_string("sd_card_button_got_it")
			self.assertEqual(go_button_text, hint)
			print("Formatted dialog go button text test success")
		except AssertionError:
			raise AssertionError("Formatted dialog go button text test failed")
		# click go button
		sd_card_page.click_go()

		# click close button
		sd_card_page.click_close()
		# check if is in pixsee settings page
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("Back to Pixsee Settings page test success")
		except AssertionError:
			raise AssertionError("Back to Pixsee Settings page test failed")
	# back to pixsee settings page









