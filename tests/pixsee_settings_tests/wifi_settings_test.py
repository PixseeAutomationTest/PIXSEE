import time
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.wifi_settings_page import WifiSettingsPage




class WifiSettingsCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=True)
	# start from pixsee settings page
	def test_01_wifi_reset_cancel(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		pixsee_settings_page.click_wifi_settings()
		# check the text on popup screen
		try:
			title = wifi_settings_page.pop_up_title_text()
			hint = self.get_string("reset_wifi")
			self.assertEqual(title, hint)
			print("popup title correct")
		except AssertionError:
			raise AssertionError("popup title wrong")
		try:
			ok = wifi_settings_page.pop_up_ok_text()
			hint = self.get_string("ok")
			self.assertEqual(ok, hint)
			print("ok button correct")
		except AssertionError:
			raise AssertionError("ok button wrong")
		try:
			cancel = wifi_settings_page.pop_up_cancel_text()
			hint = self.get_string("cancel")
			self.assertEqual(cancel, hint)
			print("cancel button correct")
		except AssertionError:
			raise AssertionError("cancel button wrong")
		# click cancel
		wifi_settings_page.click_pop_up_cancel()
		# check if back to settings page
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("back to settings page")
		except AssertionError:
			raise AssertionError("not back to settings page")
	# start from pixsee settings page
	def test_02_wifi_reset_ok(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		pixsee_settings_page.click_wifi_settings()
		wifi_settings_page.click_pop_up_ok()
		time.sleep(2)
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_settings_page())
			print("ok function success")
		except AssertionError:
			raise AssertionError("ok function failed")
	# start from wifi settings page
	def test_03_wifi_settings_x(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		# check header text
		try:
			header_text = wifi_settings_page.header_text()
			hint = self.get_string("wifi_settings")
			self.assertEqual(header_text, hint)
			print("header text correct")
		except AssertionError:
			raise AssertionError("header text wrong")
		try:
			description_text = wifi_settings_page.description()
			hint = self.get_string("choose_wifi_network")
			self.assertEqual(description_text, hint)
			print("description text correct")
		except AssertionError:
			raise AssertionError("description text wrong")
		wifi_settings_page.click_x()
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_quit_dialog())
			print("x function success")
		except AssertionError:
			raise AssertionError("x function failed")
	# start from wifi settings quit dialog
	def test_04_wifi_quit_dialog_no_yes(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		# check dialog text
		try:
			dialog_text = wifi_settings_page.quit_dialog_text()
			hint = self.get_string("quit_setup")
			self.assertEqual(dialog_text, hint)
			print("quit dialog text correct")
		except AssertionError:
			raise AssertionError("quit dialog text wrong")
		try:
			yes_text = wifi_settings_page.quit_dialog_yes_text()
			hint = self.get_string("yes")
			self.assertEqual(yes_text, hint)
			print("quit dialog yes text correct")
		except AssertionError:
			raise AssertionError("quit dialog yes text wrong")
		try:
			no_text = wifi_settings_page.quit_dialog_no_text()
			hint = self.get_string("no")
			self.assertEqual(no_text, hint)
			print("quit dialog no text correct")
		except AssertionError:
			raise AssertionError("quit dialog no text wrong")
		# click no
		wifi_settings_page.click_quit_no()
		# check if back to wifi settings page
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_settings_page())
			print("quit dialog no function success")
		except AssertionError:
			raise AssertionError("quit dialog no function failed, not in wifi settings page")
		# check yes
		wifi_settings_page.click_x()
		wifi_settings_page.click_quit_yes()
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("quit dialog yes function success")
		except AssertionError:
			raise AssertionError("quit dialog yes function failed")
	# start from pixsee settings page
	def test_05_wifi_settings_next_empty_password(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		pixsee_settings_page.click_wifi_settings()
		wifi_settings_page.click_pop_up_ok()
		wifi_settings_page.click_next()
		# check if in wifi empty password alert dialog
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_password_empty_dialog())
			print("empty password  alert success")
		except AssertionError:
			raise AssertionError("empty password alert failed, not in wifi empty password dialog")
		# check dialog text
		try:
			dialog_text = wifi_settings_page.empty_dialog_text()
			hint = self.get_string("wifi_settings_empty_password_dialog_title")
			self.assertEqual(dialog_text, hint)
			print("password empty dialog text correct")
		except AssertionError:
			raise AssertionError("password empty dialog text wrong")
		try:
			yes_text = wifi_settings_page.empty_dialog_yes_text()
			hint = self.get_string("ok")
			self.assertEqual(yes_text, hint)
			print("password empty dialog ok text correct")
		except AssertionError:
			raise AssertionError("password empty dialog yes text wrong")
		wifi_settings_page.click_empty_dialog_yes()
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_settings_page())
			print("empty password dialog yes function success")
		except AssertionError:
			raise AssertionError("empty password dialog yes function failed, not in wifi settings page")
	# start from wifi settings page
	def test_06_wifi_settings_next(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		wifi_settings_page.input_password("12345678")
		wifi_settings_page.click_next()
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_searching_device())
			print("next function success")
		except AssertionError:
			raise AssertionError("next function failed")
		time.sleep(30)
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_quit_dialog())
			print("wifi settings function success")
		except AssertionError:
			raise AssertionError("wifi settings function failed")
	# back to pixsee settings page











