from base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_friends_pages.pixsee_friends_page import PixseeFriendsPage
from pages.menu_pages.pixsee_friends_pages.activate_service_page import ActivateServicePage
from pages.menu_pages.pixsee_friends_pages.music_doll_playlist_page import MusicDollPlaylistPage
from pages.menu_pages.pixsee_friends_pages.story_doll_playlist_page import StoryDollPlaylistPage
from pages.menu_pages.pixsee_friends_pages.doll_box_page import DollBoxPage

import time

class PixseeFriendsTest(BaseTestCase):
	@classmethod
	def setUpClass(cls):
		cls.language = getattr(cls, "language", "zh")
		cls.locale = getattr(cls, "locale", "TW")
		super().setUpClass()

	def setUp(self):
		super().setUp()
		baby_monitor_page = BabyMonitorPage(self.driver)
		menu_page = MenuPage(self.driver)
		pixsee_friends_page = PixseeFriendsPage(self.driver)
		try:
			while self.driver.current_package != self.driver.capabilities.get("appPackage"):
				self.driver.terminate_app(self.driver.current_package)
				self.open_app()
			if pixsee_friends_page.is_in_pixsee_friends_page():
				return
			elif not baby_monitor_page.is_in_baby_monitor_page():
				self.shutdown_app()
				self.open_app()
			print("Finish opening app.")
			baby_monitor_page.click_home()
			menu_page.click_friends()
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e

	def test_pixsee_friends_page_with_close(self):
		menu_page = MenuPage(self.driver)
		pixsee_friends_page = PixseeFriendsPage(self.driver)
		try:
			self.assertTrue(pixsee_friends_page.is_in_pixsee_friends_page(), "Can't go to Pixsee Friends Page")
			'''Verify Pixsee Friends Page contents'''
			self.assertEqual(pixsee_friends_page.get_title_text(), self.get_string("menu_title_doll"),
							 "Text \"Pixsee Friends\" is not properly displayed")

			'''Click Close Button'''
			pixsee_friends_page.click_close_button()
			self.assertTrue(menu_page.is_in_menu_page(), "Can't go back to Menu Page after clicking Close Button in Pixsee Friends Page")

			menu_page.click_friends()
		except AssertionError as ae:
			print(f"Test failed with assertion error: {ae}")
			raise ae
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e

	def test_pixsee_friends_page_with_info_website(self):
		pixsee_friends_page = PixseeFriendsPage(self.driver)
		try:
			self.assertTrue(pixsee_friends_page.is_in_pixsee_friends_page(), "Can't go to Pixsee Friends Page")
			'''Verify Pixsee Friends Page contents'''
			self.assertEqual(pixsee_friends_page.get_title_text(), self.get_string("menu_title_doll"), "Text \"Pixsee Friends\" is not properly displayed")

			'''Click Info Button'''
			pixsee_friends_page.click_info_button()
			self.assertTrue(pixsee_friends_page.is_in_outside_website(), "Can't open browser with Pixsee Friends information website")
			if self.language == "zh":
				self.assertEqual(pixsee_friends_page.get_outside_website_url(),"pixseecare.com/tw/support/pixseeplay/article/345", "Wrong URL for Pixsee Friends information website")
			else:
				self.assertEqual(pixsee_friends_page.get_outside_website_url(), "pixseecare.com/us/support/pixseeplay/article/345", "Wrong URL for Pixsee Friends information website")
			self.go_back()
		except AssertionError as ae:
			print(f"Test failed with assertion error: {ae}")
			raise ae
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e

	def test_add_doll_dialog_with_cancel(self):
		pixsee_friends_page = PixseeFriendsPage(self.driver)
		try:
			self.assertTrue(pixsee_friends_page.is_in_pixsee_friends_page(), "Can't go to Pixsee Friends Page")
			'''Verify Pixsee Friends Page contents'''
			self.assertEqual(pixsee_friends_page.get_title_text(), self.get_string("menu_title_doll"), "Text \"Pixsee Friends\" is not properly displayed")

			'''Click Add Doll Button and verify Add Doll Dialog contents'''
			pixsee_friends_page.click_add_doll_button()
			self.assertTrue(pixsee_friends_page.has_dialog(), "Add Doll Dialog is not displayed after clicking Add Doll Button")
			self.assertEqual(pixsee_friends_page.get_add_doll_dialog_alert_text(), self.get_string("doll_alert_notice_title_code"), "Text \"Notice\" is not properly displayed")
			self.assertEqual(pixsee_friends_page.get_add_doll_dialog_message_text(), self.get_string("doll_alert_notice_message_code"), "Text \"One QR code can only be linked to a single account. Once it's linked, it cannot be changed.\" is not properly displayed")
			self.assertEqual(pixsee_friends_page.get_add_doll_dialog_ok_button_text(), self.get_string("ok"), "button \"OK\" is not properly displayed")
			self.assertEqual(pixsee_friends_page.get_add_doll_dialog_cancel_button_text(),self.get_string("pixsee_friends_button_cancel"), "button \"Cancel\" is not properly displayed")

			'''Click Cancel Button in Add Doll Dialog'''
			pixsee_friends_page.click_add_doll_dialog_cancel_button()
			self.assertTrue(pixsee_friends_page.is_in_pixsee_friends_page(), "Can't go back to Pixsee Friends Page after clicking Cancel Button in Add Doll Dialog")
		except AssertionError as ae:
			print(f"Test failed with assertion error: {ae}")
			raise ae
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e

class PixseeFriendsTestInActivationService(BaseTestCase):
	@classmethod
	def setUpClass(cls):
		cls.language = getattr(cls, "language", "zh")
		cls.locale = getattr(cls, "locale", "TW")
		super().setUpClass()

	def setUp(self):
		super().setUp()
		baby_monitor_page = BabyMonitorPage(self.driver)
		menu_page = MenuPage(self.driver)
		pixsee_friends_page = PixseeFriendsPage(self.driver)
		activation_service_page = ActivateServicePage(self.driver)

		try:
			while self.driver.current_package != self.driver.capabilities.get("appPackage"):
				self.driver.terminate_app(self.driver.current_package)
				self.open_app()
			if activation_service_page.is_in_activate_service_page():
				return
			elif pixsee_friends_page.is_in_pixsee_friends_page():
				pixsee_friends_page.click_add_doll_button()
				pixsee_friends_page.click_add_doll_dialog_ok_button()
				return
			elif not baby_monitor_page.is_in_baby_monitor_page():
				self.shutdown_app()
				self.open_app()
			print("Finish opening app.")
			baby_monitor_page.click_home()
			menu_page.click_friends()
			pixsee_friends_page.click_add_doll_button()
			pixsee_friends_page.click_add_doll_dialog_ok_button()
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e

	def test_activate_service_page_with_close(self):
		pixsee_friends_page = PixseeFriendsPage(self.driver)
		activate_service_page = ActivateServicePage(self.driver)
		try:
			self.assertTrue(activate_service_page.is_in_activate_service_page(), "Can't go to Activate Service Page after clicking OK Button in Add Doll Dialog")

			'''Verify Activate Service Page contents'''
			self.assertEqual(activate_service_page.get_page_title_text(), self.get_string("doll_activate_service"), "Text \"Activate Service\" is not properly displayed")
			self.assertEqual(activate_service_page.get_label_text(), self.get_string("doll_serial_number_title"), "Text \"To activate service, please scan the QR code on the card\" is not properly displayed")
			self.assertEqual(activate_service_page.get_message_text(), self.get_string("doll_scan_qrcode"), "Text \"Scan the QR code on the card \" is not properly displayed")
			self.assertEqual(activate_service_page.get_doll_sn_code_hint(), self.get_string("doll_edit_enter_activate_number"), "Text \"Activation number\" is not properly displayed")
			self.assertEqual(activate_service_page.get_OK_button_text(), self.get_string("ok"), "button \"OK\" is not properly displayed")

			'''Click Close Button in Activate Service Page'''
			activate_service_page.click_close_button()
			self.assertTrue(pixsee_friends_page.is_in_pixsee_friends_page(), "Can't go back to Pixsee Friends Page after clicking Close Button in Activate Service Page")
		except AssertionError as ae:
			print(f"Test failed with assertion error: {ae}")
			raise ae
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e

	def test_activate_service_page_with_code_tip(self):
		activate_service_page = ActivateServicePage(self.driver)
		try:
			self.assertTrue(activate_service_page.is_in_activate_service_page(), "Can't go to Activate Service Page after clicking OK Button in Add Doll Dialog")

			'''Verify Activate Service Page contents'''
			self.assertEqual(activate_service_page.get_page_title_text(), self.get_string("doll_activate_service"), "Text \"Activate Service\" is not properly displayed")
			self.assertEqual(activate_service_page.get_label_text(), self.get_string("doll_serial_number_title"), "Text \"To activate service, please scan the QR code on the card\" is not properly displayed")
			self.assertEqual(activate_service_page.get_message_text(), self.get_string("doll_scan_qrcode"), "Text \"Scan the QR code on the card \" is not properly displayed")
			self.assertEqual(activate_service_page.get_doll_sn_code_hint(), self.get_string("doll_edit_enter_activate_number"), "Text \"Activation number\" is not properly displayed")
			self.assertEqual(activate_service_page.get_OK_button_text(), self.get_string("ok"), "button \"OK\" is not properly displayed")

			'''Click Code Tip Button in Activate Service Page'''
			activate_service_page.click_code_tip_button()

			'''Verify Code Tip Dialog contents'''
			self.assertTrue(activate_service_page.has_dialog(), "Code Tip Dialog is not displayed after clicking Code Tip Button")
			self.assertEqual(activate_service_page.get_dialog_message_text(), self.get_string("doll_alert_tip_activation_number"), "Text \"Please scan the QR code with camera to get the activation number!\" is not properly displayed")
			self.assertEqual(activate_service_page.get_dialog_i_got_it_button_text(), self.get_string("doll_alert_i_got_it"), "button \"I got it\" is not properly displayed")

			'''Click I Know Button in Code Tip Dialog'''
			activate_service_page.click_dialog_i_got_it_button()
			self.assertTrue(activate_service_page.is_in_activate_service_page(), "Can't go back to Activate Service Page after clicking \"I got it\" Button in Code Tip Dialog")
		except AssertionError as ae:
			print(f"Test failed with assertion error: {ae}")
			raise ae
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e

	def test_activate_service_page_with_input_wrong_activation_number(self):
		activate_service_page = ActivateServicePage(self.driver)
		try:
			self.assertTrue(activate_service_page.is_in_activate_service_page(), "Can't go to Activate Service Page after clicking OK Button in Add Doll Dialog")

			'''Verify Activate Service Page contents'''
			self.assertEqual(activate_service_page.get_page_title_text(), self.get_string("doll_activate_service"), "Text \"Activate Service\" is not properly displayed")
			self.assertEqual(activate_service_page.get_label_text(), self.get_string("doll_serial_number_title"), "Text \"To activate service, please scan the QR code on the card\" is not properly displayed")
			self.assertEqual(activate_service_page.get_message_text(), self.get_string("doll_scan_qrcode"), "Text \"Scan the QR code on the card \" is not properly displayed")
			self.assertEqual(activate_service_page.get_doll_sn_code_hint(), self.get_string("doll_edit_enter_activate_number"), "Text \"Activation number\" is not properly displayed")
			self.assertEqual(activate_service_page.get_OK_button_text(), self.get_string("ok"), "button \"OK\" is not properly displayed")

			'''Input Wrong Activation Number'''
			activate_service_page.input_doll_sn_code("Aa12345")
			activate_service_page.click_OK_button()
			self.assertTrue(activate_service_page.has_error_message(), "Error message is not displayed after inputting wrong activation number")
			self.assertEqual(activate_service_page.get_error_message_text(), self.get_string("doll_serial_number_is_not_found"), "Text \"Activation number not found\" is not properly displayed")

		except AssertionError as ae:
			print(f"Test failed with assertion error: {ae}")
			raise ae
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e

	def test_activate_service_page_with_input_used_activation_number(self):
		activate_service_page = ActivateServicePage(self.driver)
		try:
			self.assertTrue(activate_service_page.is_in_activate_service_page(), "Can't go to Activate Service Page after clicking OK Button in Add Doll Dialog")

			'''Verify Activate Service Page contents'''
			self.assertEqual(activate_service_page.get_page_title_text(), self.get_string("doll_activate_service"), "Text \"Activate Service\" is not properly displayed")
			self.assertEqual(activate_service_page.get_label_text(), self.get_string("doll_serial_number_title"), "Text \"To activate service, please scan the QR code on the card\" is not properly displayed")
			self.assertEqual(activate_service_page.get_message_text(), self.get_string("doll_scan_qrcode"), "Text \"Scan the QR code on the card \" is not properly displayed")
			self.assertEqual(activate_service_page.get_doll_sn_code_hint(), self.get_string("doll_edit_enter_activate_number"), "Text \"Activation number\" is not properly displayed")
			self.assertEqual(activate_service_page.get_OK_button_text(), self.get_string("ok"), "button \"OK\" is not properly displayed")

			'''Input Used Activation Number'''
			activate_service_page.input_doll_sn_code("0110Q20787470139")
			activate_service_page.click_OK_button()
			self.assertTrue(activate_service_page.has_error_message(), "Error message is not displayed after inputting wrong activation number")
			self.assertEqual(activate_service_page.get_error_message_text(), self.get_string("doll_serial_number_was_binded"), "Text \"Activation number has already been used\" is not properly displayed")

		except AssertionError as ae:
			print(f"Test failed with assertion error: {ae}")
			raise ae
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e

class PixseeFriendsTestInDollPlaylist(BaseTestCase):
	@classmethod
	def setUpClass(cls):
		cls.language = getattr(cls, "language", "zh")
		cls.locale = getattr(cls, "locale", "TW")
		super().setUpClass()

	def setUp(self):
		super().setUp()
		baby_monitor_page = BabyMonitorPage(self.driver)
		menu_page = MenuPage(self.driver)
		pixsee_friends_page = PixseeFriendsPage(self.driver)
		activation_service_page = ActivateServicePage(self.driver)
		music_doll_playlist_page = MusicDollPlaylistPage(self.driver)
		story_doll_playlist_page = StoryDollPlaylistPage(self.driver)

		try:
			while self.driver.current_package != self.driver.capabilities.get("appPackage"):
				self.driver.terminate_app(self.driver.current_package)
				self.open_app()
			if activation_service_page.is_in_activate_service_page():
				return
			elif pixsee_friends_page.is_in_pixsee_friends_page():
				pixsee_friends_page.click_add_doll_button()
				pixsee_friends_page.click_add_doll_dialog_ok_button()
				return
			elif not baby_monitor_page.is_in_baby_monitor_page():
				self.shutdown_app()
				self.open_app()
			print("Finish opening app.")
			baby_monitor_page.click_home()
			menu_page.click_friends()
			pixsee_friends_page.click_add_doll_button()
			pixsee_friends_page.click_add_doll_dialog_ok_button()
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e
