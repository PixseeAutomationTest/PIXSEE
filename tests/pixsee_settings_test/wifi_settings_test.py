import time
from pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.wifi_settings_page import WifiSettingsPage




class WifiSettingsCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)
	def test_wifi_reset_cancel(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()
		menu_page.click_settings()
		pixsee_settings_page.click_wifi_settings()
		# check the text on popup screen
		try:
			title = wifi_settings_page.pop_up_title_text()
			hint = self.get_string("reset_wifi")
			self.assertEqual(title, hint)
			print("popup title correct")
		except AssertionError:
			print("popup title wrong")
		try:
			ok = wifi_settings_page.pop_up_title_text()
			hint = self.get_string("ok")
			self.assertEqual(ok, hint)
			print("ok button correct")
		except AssertionError:
			print("ok button wrong")
		try:
			cancel = wifi_settings_page.pop_up_cancel_text()
			hint = self.get_string("cancel")
			self.assertEqual(cancel, hint)
			print("cancel button correct")
		except AssertionError:
			print("cancel button wrong")
		# click cancel
		wifi_settings_page.click_pop_up_cancel()
		# check if back to settings page
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("back to settings page")
		except AssertionError:
			print("not back to settings page")
	def test_wifi_reset_ok(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()
		menu_page.click_logout()
		menu_page.click_settings()
		pixsee_settings_page.click_wifi_settings()
		wifi_settings_page.click_pop_up_ok()
		time.sleep(2)
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_settings_page())
			print("ok function success")
		except AssertionError:
			print("ok function failed")
	def test_wifi_settings_x(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()
		menu_page.click_logout()
		menu_page.click_settings()
		pixsee_settings_page.click_wifi_settings()
		wifi_settings_page.click_pop_up_ok()
		# check header text
		try:
			header_text = wifi_settings_page.header_text()
			hint = self.get_string("wifi_settings")
			self.assertEqual(header_text, hint)
			print("header text correct")
		except AssertionError:
			print("header text wrong")
		try:
			description_text = wifi_settings_page.description()
			hint = self.get_string("choose_wifi_network")
			self.assertEqual(description_text, hint)
			print("description text correct")
		except AssertionError:
			print("description text wrong")
		wifi_settings_page.click_x()
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_quit_dialog())
			print("x function success")
		except AssertionError:
			print("x function failed")
	def test_wifi_quit_dialog_no_yes(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()
		menu_page.click_logout()
		menu_page.click_settings()
		pixsee_settings_page.click_wifi_settings()
		wifi_settings_page.click_pop_up_ok()
		wifi_settings_page.click_x()
		# check dialog text
		try:
			dialog_text = wifi_settings_page.quit_dialog_text()
			hint = self.get_string("quit_setup")
			self.assertEqual(dialog_text, hint)
			print("quit dialog text correct")
		except AssertionError:
			print("quit dialog text wrong")
		try:
			yes_text = wifi_settings_page.quit_dialog_yes_text()
			hint = self.get_string("yes")
			self.assertEqual(yes_text, hint)
			print("quit dialog yes text correct")
		except AssertionError:
			print("quit dialog yes text wrong")
		try:
			no_text = wifi_settings_page.quit_dialog_no_text()
			hint = self.get_string("no")
			self.assertEqual(no_text, hint)
			print("quit dialog no text correct")
		except AssertionError:
			print("quit dialog no text wrong")
		# click no
		wifi_settings_page.click_quit_no()
		# check if back to wifi settings page
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_settings_page())
			print("quit dialog no function success")
		except AssertionError:
			print("quit dialog no function failed")
			raise AssertionError("quit dialog no function failed, not in wifi settings page")
		# check yes
		wifi_settings_page.click_x()
		wifi_settings_page.click_quit_yes()
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("quit dialog yes function success")
		except AssertionError:
			print("quit dialog yes function failed")
	def test_wifi_settings_next_empty_password(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()
		menu_page.click_logout()
		menu_page.click_settings()
		pixsee_settings_page.click_wifi_settings()
		wifi_settings_page.click_pop_up_ok()
		wifi_settings_page.click_next()
		# check if in wifi empty password alert dialog
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_password_empty_dialog())
			print("empty password  alert success")
		except AssertionError:
			print("empty password alert failed")
			raise AssertionError("empty password alert failed, not in wifi empty password dialog")
		# check dialog text
		try:
			dialog_text = wifi_settings_page.empty_dialog_text()
			hint = self.get_string("wifi_settings_empty_password_dialog_title")
			self.assertEqual(dialog_text, hint)
			print("password empty dialog text correct")
		except AssertionError:
			print("password empty dialog text wrong")
		try:
			yes_text = wifi_settings_page.empty_dialog_yes_text()
			hint = self.get_string("yes")
			self.assertEqual(yes_text, hint)
			print("password empty dialog yes text correct")
		except AssertionError:
			print("password empty dialog yes text wrong")
		wifi_settings_page.click_empty_dialog_yes()
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_settings_page())
			print("empty password dialog yes function success")
		except AssertionError:
			print("empty password dialog yes function failed")
			raise AssertionError("empty password dialog yes function failed, not in wifi settings page")
	def test_wifi_settings_next(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		wifi_settings_page = WifiSettingsPage(self.driver)

		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()
		menu_page.click_logout()
		menu_page.click_settings()
		pixsee_settings_page.click_wifi_settings()
		wifi_settings_page.click_pop_up_ok()
		wifi_settings_page.input_password("12345678")
		wifi_settings_page.click_next()
		try:
			self.assertTrue(wifi_settings_page.is_in_wifi_searching_device())
			print("next function success")
		except AssertionError:
			print("next function failed")









