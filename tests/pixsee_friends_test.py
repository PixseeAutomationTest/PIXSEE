from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_friends_pages.pixsee_friends_page import PixseeFriendsPage
from pages.menu_pages.pixsee_friends_pages.activate_service_page import ActivateServicePage

class PixseeSettingsTest(BaseTestCase):
	def __init__(self, methodName='runTest', language="zh", locale="TW"):
		super().__init__(methodName)
		self.language = language
		self.locale = locale

	def setUp(self):
		super().setUp(language=self.language, locale=self.locale)
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
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_friends_page = PixseeFriendsPage(self.driver)
		try:
			self.assertTrue(pixsee_friends_page.is_in_pixsee_friends_page(), "Can't go to Pixsee Friends Page")
			'''Verify Pixsee Friends Page contents'''
			self.assertEqual(pixsee_friends_page.get_title_text(), self.get_string("menu_title_doll"),
							 "Text \"Pixsee Friends\" is not properly displayed")

			'''Click Close Button'''
			pixsee_friends_page.click_close_button()
			self.assertTrue(baby_monitor_page.is_in_baby_monitor_page(), "Can't go back to Baby Monitor Page after clicking Close Button in Pixsee Friends Page")
		except AssertionError as ae:
			print(f"Test failed with assertion error: {ae}")
			raise ae
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e
		finally:
			self.shutdown_app()

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
				self.assertEqual(pixsee_friends_page.get_outside_website_url(),"https://www.pixseecare.com/tw/support/pixseeplay/article/345", "Wrong URL for Pixsee Friends information website")
			else:
				self.assertEqual(pixsee_friends_page.get_outside_website_url(), "https://www.pixseecare.com/us/support/pixseeplay/article/345", "Wrong URL for Pixsee Friends information website")
			self.go_back()
		except AssertionError as ae:
			print(f"Test failed with assertion error: {ae}")
			raise ae
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e
		finally:
			self.shutdown_app()

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
		finally:
			self.shutdown_app()

	def test_activate_service_page_with_close(self):
		pixsee_friends_page = PixseeFriendsPage(self.driver)
		activate_service_page = ActivateServicePage(self.driver)
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

			'''Click Ok Button in Add Doll Dialog'''
			pixsee_friends_page.click_add_doll_dialog_ok_button()
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
		finally:
			self.shutdown_app()

	def test_activate_service_page_with_input_wrong_activation_number(self):
		pixsee_friends_page = PixseeFriendsPage(self.driver)
		activate_service_page = ActivateServicePage(self.driver)
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

			'''Click Ok Button in Add Doll Dialog'''
			pixsee_friends_page.click_add_doll_dialog_ok_button()
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
			self.assertEqual(activate_service_page.get_error_message_text(), self.get_string(""))

			'''Click Close Button in Activate Service Page'''
			activate_service_page.click_close_button()
		except AssertionError as ae:
			print(f"Test failed with assertion error: {ae}")
			raise ae
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e
		finally:
			self.shutdown_app()