

import time
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.covered_face_detection_page import CoveredFaceDetectionPage
from appium.webdriver.common.appiumby import AppiumBy

class CoveredFaceDetectionCase2(BaseTestCase):
	@classmethod
	def setUpClass(cls):
		cls.language = getattr(cls, "language", "zh")
		cls.locale = getattr(cls, "locale", "TW")
		super().setUpClass()

	def setUp(self):
		super().setUp()
		baby_monitor_page = BabyMonitorPage(self.driver)
		menu_page = MenuPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		covered_face_detection_page = CoveredFaceDetectionPage(self.driver)
		try:
			while self.driver.current_package != self.driver.capabilities.get("appPackage"):
				self.driver.terminate_app(self.driver.current_package)
				self.open_app()
			if pixsee_settings_page.is_in_settings():
				return
			elif not baby_monitor_page.is_in_baby_monitor_page():
				self.shutdown_app()
				self.open_app()
			print("Finish opening app.")
			baby_monitor_page.click_home()
			menu_page.click_settings()
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e
	# start from pixsee settings page
	def test_02_covered_face_detection_back(self):
		covered_face_detection_page = CoveredFaceDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		pixsee_settings_page.click_covered_face_detection()
		# back to settings page
		covered_face_detection_page.click_back()
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("Back to Pixsee Settings page")
		except AssertionError :
			raise AssertionError("Not in Pixsee Settings page")
	# start from pixsee settings page
	def test_03_covered_face_detection_save(self):
		covered_face_detection_page = CoveredFaceDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		origin_status = pixsee_settings_page.covered_face_detection_status_text()
		pixsee_settings_page.click_covered_face_detection()
		# check save enable = false
		try:
			self.assertFalse(covered_face_detection_page.is_save_enable())
			print("Save diable test pass")
		except AssertionError:
			raise AssertionError("Save diable test failed")
		# change switch status
		if covered_face_detection_page.is_switch_on():
			covered_face_detection_page.click_switch()
			covered_face_detection_page.click_turn_off()
		else:
			covered_face_detection_page.click_switch()
			covered_face_detection_page.click_save()
		new_status = pixsee_settings_page.covered_face_detection_status_text()
		if origin_status != new_status:
			print("save function success")
		else:
			raise AssertionError("save function failed, status not changed")
	# start from pixsee settings page
	def test_04_covered_face_detection_back_discard(self):
		covered_face_detection_page = CoveredFaceDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		pixsee_settings_page.click_covered_face_detection()
		# check if is in discard dialog
		if covered_face_detection_page.is_switch_on() :
			covered_face_detection_page.click_switch()
			covered_face_detection_page.click_turn_off()
			pixsee_settings_page.click_covered_face_detection()
			covered_face_detection_page.click_switch()
		else:
			covered_face_detection_page.click_switch()
		time.sleep(2)
		covered_face_detection_page.click_back()
		try:
			self.assertTrue(covered_face_detection_page.is_in_discard_dialog())
			print("In discard dialog")
			# check discard dialog text
			try:
				discard = covered_face_detection_page.discard_message_text()
				hint = self.get_string("covered_face_detection_confirmation_message")
				self.assertEqual(discard, hint)
				print("Discard dialog title right")
			except AssertionError:
				raise AssertionError("Discard dialog title wrong")
			try:
				yes = covered_face_detection_page.discard_yes_text()
				hint = self.get_string("yes")
				self.assertEqual(yes, hint)
				print("Discard dialog yes text right")
			except AssertionError:
				raise AssertionError("Discard dialog yes text wrong")
			try:
				no = covered_face_detection_page.discard_no_text()
				hint = self.get_string("no")
				self.assertEqual(no, hint)
				print("Discard dialog no text right")
			except AssertionError:
				raise AssertionError("Discard dialog no text wrong")
			# click yes
			covered_face_detection_page.click_discard_yes()
			# check status = false
			self.assertEqual(pixsee_settings_page.covered_face_detection_status_text(),
							 self.get_string("off_selection"))
			print("back button worked")
		except AssertionError:
			raise AssertionError("Not in discard dialog")
	# start from pixsee settings page
	def test_05_covered_face_detection_information(self):
		covered_face_detection_page = CoveredFaceDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		pixsee_settings_page.click_covered_face_detection()
		# check if is in information page
		covered_face_detection_page.click_information()
		try:
			self.assertTrue(covered_face_detection_page.is_in_covered_face_detection_tutor_page())
			print("information button worked")
		except AssertionError:
			raise AssertionError("Not in information page")
		covered_face_detection_page.click_skip()
		if covered_face_detection_page.is_save_enable():
			covered_face_detection_page.click_save()
		else:
			covered_face_detection_page.click_back()
	# start from pixsee settings page
	def test_06_covered_face_detection_switch(self):
		covered_face_detection_page = CoveredFaceDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		pixsee_settings_page.click_covered_face_detection()
		# check header text
		try:
			header = covered_face_detection_page.header_text()
			hint = self.get_string("covered_face")
			self.assertEqual(header, hint)
			print("Covered Face Detection header right")
		except AssertionError:
			raise AssertionError("Covered Face Detection header wrong")
		# check Covered Face Detection title
		try:
			title = covered_face_detection_page.title()
			hint = self.get_string("detection")
			self.assertEqual(title, hint)
			print("Covered Face Detection title right")
		except AssertionError:
			raise AssertionError("Covered Face Detection title wrong")
		# check Covered Face Detection description
		try:
			subtitle = covered_face_detection_page.detection_description()
			hint = self.get_string("covered_face_detection_status_description")
			self.assertEqual(subtitle, hint)
			print("Covered Face Detection subtitle right")
		except AssertionError:
			raise AssertionError("Covered Face Detection subtitle wrong")
		# switch status
		current_status = covered_face_detection_page.is_switch_on()
		if current_status:
			try:
				is_visible = len(
					self.driver.find_elements(AppiumBy.ID, covered_face_detection_page.Sensitivity)) > 0
				assert is_visible, "switch on failed"
				print("switch on success")
			except AssertionError:
				raise AssertionError("switch on failed")
			covered_face_detection_page.click_switch()
			# check in dialog
			try:
				self.assertTrue(covered_face_detection_page.is_in_turn_off_dialog())
				print("switch off successfully")
				covered_face_detection_page.click_turn_off_cancel()
			except AssertionError:
				raise AssertionError("switch off unsuccessfully")
		else:
			self.check_switch_and_content(current_status, covered_face_detection_page.Sensitivity)
			covered_face_detection_page.click_switch()
			time.sleep(1)
			after_status = covered_face_detection_page.is_switch_on()
			self.check_switch_and_content(after_status, covered_face_detection_page.Sensitivity)

class CoveredFaceDetectionCase3(BaseTestCase):
	@classmethod
	def setUpClass(cls):
		cls.language = getattr(cls, "language", "zh")
		cls.locale = getattr(cls, "locale", "TW")
		super().setUpClass()

	def setUp(self):
		super().setUp()
		baby_monitor_page = BabyMonitorPage(self.driver)
		menu_page = MenuPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		covered_face_detection_page = CoveredFaceDetectionPage(self.driver)
		try:
			while self.driver.current_package != self.driver.capabilities.get("appPackage"):
				self.driver.terminate_app(self.driver.current_package)
				self.open_app()
			if covered_face_detection_page.is_in_covered_face_detection_page():
				return
			elif not baby_monitor_page.is_in_baby_monitor_page():
				self.shutdown_app()
				self.open_app()
			print("Finish opening app.")
			baby_monitor_page.click_home()
			menu_page.click_settings()
			pixsee_settings_page.click_covered_face_detection()
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e
	# start from covered face detection page
	def test_01_covered_face_detection_tap_checkbox_sensitivity(self):
		covered_face_detection_page = CoveredFaceDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		if covered_face_detection_page.is_switch_on() :
			pass
		else:
			covered_face_detection_page.click_switch()
		# check Covered Face Detection type group titles
		try:
			sensitivity = covered_face_detection_page.sensitivity_text()
			hint = self.get_string("sensitivity_level")
			self.assertEqual(sensitivity, hint)
			print("Sensitivity title is correct")
		except AssertionError :
			raise AssertionError("Sensitivity title is wrong")
		# check box name
		try:
			low = covered_face_detection_page.low_text()
			hint = self.get_string("sensitivity_low")
			self.assertEqual(low, hint)
			print("Low checkbox text is correct")
		except AssertionError :
			raise AssertionError("Low checkbox text is wrong")
		try:
			medium = covered_face_detection_page.medium_text()
			hint = self.get_string("sensitivity_medium")
			self.assertEqual(medium, hint)
			print("Medium checkbox text is correct")
		except AssertionError :
			raise AssertionError("Medium checkbox text is wrong")
		try:
			high = covered_face_detection_page.high_text()
			hint = self.get_string("sensitivity_high")
			self.assertEqual(high, hint)
			print("High checkbox text is correct")
		except AssertionError :
			raise AssertionError("High checkbox text is wrong")
		try:
			drag = covered_face_detection_page.drag_text()
			hint = self.get_string("detection_settings_detection_area_title")
			self.assertEqual(drag, hint)
			print("drag title right")
		except AssertionError :
			raise AssertionError("drag title wrong")
		# check clickable
		try:
			self.assertTrue(covered_face_detection_page.is_low_clickable())
			print("Low checkbox is clickable")
		except AssertionError :
			raise AssertionError("Low checkbox is not clickable")
		try:
			self.assertTrue(covered_face_detection_page.is_medium_clickable())
			print("Medium checkbox is clickable")
		except AssertionError :
			raise AssertionError("Medium checkbox is not clickable")
		try:
			self.assertTrue(covered_face_detection_page.is_high_clickable())
			print("High checkbox is clickable")
		except AssertionError :
			raise AssertionError("High checkbox is not clickable")
	# start from covered face detection page
	def test_02_covered_face_detection_turn_off_page(self):
		covered_face_detection_page = CoveredFaceDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		if covered_face_detection_page.is_switch_on() :
			pass
		else:
			covered_face_detection_page.click_switch()
		covered_face_detection_page.click_switch()
		# check turn off dialog text
		try:
			title = covered_face_detection_page.turn_off_dialog_title()
			hint = self.get_string("turn_off_covered_detection")
			self.assertEqual(title, hint)
			print("turn off dialog title is correct")
		except AssertionError :
			raise AssertionError("turn off dialog title  is wrong")
		try:
			fifteenmin = covered_face_detection_page.turn_off_15_min_text()
			hint = self.get_string("snooze_detection_fifteen_minutes")
			self.assertEqual(fifteenmin, hint)
			print("turn off 15 is correct")
		except AssertionError :
			raise AssertionError("turn off 15 is wrong")
		try:
			thirtymin = covered_face_detection_page.turn_off_30_min_text()
			hint = self.get_string("snooze_detection_thirty_minutes")
			self.assertEqual(thirtymin, hint)
			print("turn off 30 is correct")
		except AssertionError :
			raise AssertionError("turn off 30 is wrong")
		try:
			off = covered_face_detection_page.turn_off_text()
			hint = self.get_string("turn_off_detection")
			self.assertEqual(off, hint)
			print("turn off text is correct")
		except AssertionError :
			raise AssertionError("turn off text is wrong")
		try:
			cancel = covered_face_detection_page.turn_off_cancel_text()
			hint = self.get_string("cancel")
			self.assertEqual(cancel, hint)
			print("turn off cancel text is correct")
		except AssertionError :
			raise AssertionError("turn off cancel text is wrong")
		# check each button
		try:
			covered_face_detection_page.click_turn_off_15_min()
			time.sleep(1)
			self.assertEqual(pixsee_settings_page.covered_face_detection_status_text(), self.get_string("off_selection"))
			print("15 min button worked")
		except AssertionError:
			raise AssertionError("15 min button failed")
		pixsee_settings_page.click_covered_face_detection()
		covered_face_detection_page.click_switch()
		covered_face_detection_page.click_switch()
		try:
			covered_face_detection_page.click_turn_off_cancel()
			self.assertTrue(covered_face_detection_page.is_switch_on())
			time.sleep(1)
			print("turn off cancel worked")
		except AssertionError:
			raise AssertionError("turn off cancel failed")
		covered_face_detection_page.click_switch()
		try:
			covered_face_detection_page.click_turn_off_30_min()
			time.sleep(1)
			self.assertEqual(pixsee_settings_page.covered_face_detection_status_text(), self.get_string("off_selection"))
			print("30 min button worked")
		except AssertionError:
			raise AssertionError("30 min button failed")
		pixsee_settings_page.click_covered_face_detection()
		covered_face_detection_page.click_switch()
		covered_face_detection_page.click_switch()
		try:
			covered_face_detection_page.click_turn_off()
			self.assertEqual(pixsee_settings_page.covered_face_detection_status_text(), self.get_string("off_selection"))
			print("turn off detection worked")
		except AssertionError:
			raise AssertionError("turn off detection failed")


















