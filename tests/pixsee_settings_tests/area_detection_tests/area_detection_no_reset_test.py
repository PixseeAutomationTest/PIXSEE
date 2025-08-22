
import time
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.area_detection_page import AreaDetectionPage
from appium.webdriver.common.appiumby import AppiumBy


class AreaDetectionCase2(BaseTestCase):
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
	def test_01_area_detection_back(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		pixsee_settings_page.click_area_detection()
		# check save enable = false
		try:
			self.assertFalse(area_detection_page.is_save_enable())
			print("Save diable test pass")
		except AssertionError:
			raise AssertionError("Save diable test failed")
		# back to settings page
		area_detection_page.click_back()
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("Back to Pixsee Settings page")
		except AssertionError :
			raise AssertionError("Not in Pixsee Settings page")
	# start from pixsee settings page
	def test_02_area_detection_save(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		origin_status = pixsee_settings_page.area_detection_status_text()
		pixsee_settings_page.click_area_detection()
		# change switch status
		if area_detection_page.is_switch_on():
			area_detection_page.click_switch()
			area_detection_page.click_turn_off()
		else:
			area_detection_page.click_switch()
			area_detection_page.click_save()
		new_status = pixsee_settings_page.area_detection_status_text()
		if origin_status != new_status:
			print("save function success")
		else:
			raise AssertionError("save function failed, status not changed")
	# start from pixsee settings page
	def test_03_area_detection_back_discard(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		pixsee_settings_page.click_area_detection()
		# check if is in discard dialog
		if area_detection_page.is_switch_on():
			area_detection_page.click_switch()
			area_detection_page.click_turn_off()
			pixsee_settings_page.click_area_detection()
			area_detection_page.click_switch()
		else:
			area_detection_page.click_switch()
		area_detection_page.click_back()
		try:
			self.assertTrue(area_detection_page.is_in_discard_dialog())
			print("In discard dialog")
			# check discard dialog text
			try:
				discard = area_detection_page.discard_message_text()
				hint = self.get_string("efence_confirmation_message")
				self.assertEqual(discard, hint)
				print("Discard dialog title right")
			except AssertionError:
				raise AssertionError("Discard dialog title wrong")
			try:
				yes = area_detection_page.discard_yes_text()
				hint = self.get_string("yes")
				self.assertEqual(yes, hint)
				print("Discard dialog yes text right")
			except AssertionError:
				raise AssertionError("Discard dialog yes text wrong")
			try:
				no = area_detection_page.discard_no_text()
				hint = self.get_string("no")
				self.assertEqual(no, hint)
				print("Discard dialog no text right")
			except AssertionError:
				raise AssertionError("Discard dialog no text wrong")
			# click yes
			area_detection_page.click_discard_yes()
			# check status = false
			self.assertEqual(pixsee_settings_page.area_detection_status_text(), self.get_string("off_selection"))
			print("back button worked")
		except AssertionError:
			raise AssertionError("Not in discard dialog")
	# start from pixsee settings page
	def test_04_area_detection_information(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		pixsee_settings_page.click_area_detection()
		area_detection_page.click_information()
		# check if is in information page
		try:
			self.assertTrue(area_detection_page.is_in_tutor_first_page())
			print("information button worked")
		except AssertionError:
			raise AssertionError("Not in information page")
		area_detection_page.click_skip()
		if area_detection_page.is_save_enable():
			area_detection_page.click_save()
		else:
			area_detection_page.click_back()
	# start from pixsee settings page
	def test_05_area_detection_switch(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		pixsee_settings_page.click_area_detection()
		# check header text
		try:
			header = area_detection_page.header_text()
			hint = self.get_string("area_detection")
			self.assertEqual(header, hint)
			print("Area detection header right")
		except AssertionError :
			raise AssertionError("Area detection header wrong")
		# check Area detection title
		try:
			title = area_detection_page.title()
			hint = self.get_string("detection")
			self.assertEqual(title, hint)
			print("Area detection title right")
		except AssertionError :
			raise AssertionError("Area detection title wrong")
		# check Area detection description
		try:
			subtitle = area_detection_page.detection_description()
			hint = self.get_string("efence_settings_status_description")
			self.assertEqual(subtitle, hint)
			print("Area detection subtitle right")
		except AssertionError :
			raise AssertionError("Area detection subtitle wrong")
		# switch status
		current_status = area_detection_page.is_switch_on()
		if current_status:
			try:
				is_visible = len(self.driver.find_elements(AppiumBy.ID, area_detection_page.Sensitivity)) > 0
				assert is_visible, "switch on failed"
				print("switch on success")
			except AssertionError :
				raise AssertionError("switch on failed")
			area_detection_page.click_switch()
			# check in turn off dialog
			try:
				self.assertTrue(area_detection_page.is_in_turn_off_dialog())
				print("switch off successfully")
				area_detection_page.click_turn_off_cancel()
			except AssertionError :
				raise AssertionError("switch off unsuccessfully")
		else:
			self.check_switch_and_content(current_status, area_detection_page.Sensitivity)
			area_detection_page.click_switch()
			time.sleep(1)
			after_status = area_detection_page.is_switch_on()
			self.check_switch_and_content(after_status, area_detection_page.Sensitivity)

class AreaDetectionCase3(BaseTestCase):
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
		area_detection_page = AreaDetectionPage(self.driver)
		try:
			while self.driver.current_package != self.driver.capabilities.get("appPackage"):
				self.driver.terminate_app(self.driver.current_package)
				self.open_app()
			if area_detection_page.is_in_area_detection_page():
				return
			elif not baby_monitor_page.is_in_baby_monitor_page():
				self.shutdown_app()
				self.open_app()
			print("Finish opening app.")
			baby_monitor_page.click_home()
			menu_page.click_settings()
			pixsee_settings_page.click_area_detection()
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e
	# start from area detection page
	def test_01_area_detection_tap_checkbox_sensitivity(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		if area_detection_page.is_switch_on():
			pass
		else:
			area_detection_page.click_switch()
		# check Area detection type group titles
		try:
			sensitivity = area_detection_page.sensitivity_text()
			hint = self.get_string("sensitivity_level")
			self.assertEqual(sensitivity, hint)
			print("Sensitivity title is correct")
		except AssertionError :
			raise AssertionError("Sensitivity title is wrong")
		try:
			dettype = area_detection_page.dettype_txt()
			hint = self.get_string("efence_type_detection")
			self.assertEqual(dettype, hint)
			print("detection type is correct")
		except AssertionError :
			raise AssertionError("detection type is wrong")
		# check box name
		try:
			low = area_detection_page.low_text()
			hint = self.get_string("sensitivity_low")
			self.assertEqual(low, hint)
			print("Low checkbox text is correct")
		except AssertionError :
			raise AssertionError("Low checkbox text is wrong")
		try:
			medium = area_detection_page.medium_text()
			hint = self.get_string("sensitivity_medium")
			self.assertEqual(medium, hint)
			print("Medium checkbox text is correct")
		except AssertionError :
			raise AssertionError("Medium checkbox text is wrong")
		try:
			high = area_detection_page.high_text()
			hint = self.get_string("sensitivity_high")
			self.assertEqual(high, hint)
			print("High checkbox text is correct")
		except AssertionError :
			raise AssertionError("High checkbox text is wrong")
		# check clickable
		try:
			self.assertTrue(area_detection_page.is_low_clickable())
			print("Low checkbox is clickable")
		except AssertionError :
			raise AssertionError("Low checkbox is not clickable")
		try:
			self.assertTrue(area_detection_page.is_medium_clickable())
			print("Medium checkbox is clickable")
		except AssertionError :
			raise AssertionError("Medium checkbox is not clickable")
		try:
			self.assertTrue(area_detection_page.is_high_clickable())
			print("High checkbox is clickable")
		except AssertionError :
			raise AssertionError("High checkbox is not clickable")
	# start from area detection page
	def test_02_area_detection_tap_checkbox_detection_type(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		if area_detection_page.is_switch_on():
			pass
		else:
			area_detection_page.click_switch()
		# check box name
		try:
			babyin = area_detection_page.baby_in_text()
			hint = self.get_string("efence_safety_area")
			self.assertEqual(babyin, hint)
			print("baby in text is correct")
		except AssertionError :
			raise AssertionError("baby in text is wrong")
		try:
			babyout = area_detection_page.baby_out_text()
			hint = self.get_string("efence_dangerous_area")
			self.assertEqual(babyout, hint)
			print("baby out text is correct")
		except AssertionError :
			raise AssertionError("baby out text is wrong")
		# check box clickable
		area_detection_page.click_baby_in()
		try:
			drag = area_detection_page.drag_text()
			hint = self.get_string("detection_settings_safety_area_title")
			self.assertEqual(drag, hint)
			print("baby in clickable")
		except AssertionError :
			raise AssertionError("baby in unclickable")
		area_detection_page.click_baby_out()
		try:
			drag = area_detection_page.drag_text()
			hint = self.get_string("detection_settings_caution_area_title")
			self.assertEqual(drag, hint)
			print("baby out clickable")
		except AssertionError :
			raise AssertionError("baby out unclickable")
		# check by color
		light_blue_range = ((0, 0, 0), (150, 255, 255))
		light_orange_range = ((151, 0, 0), (255, 255, 255))
		area_detection_page.click_baby_in()
		time.sleep(1)
		x, y = area_detection_page.find_stream_left_top()
		result = area_detection_page.is_color_in_range( x, y, light_blue_range)
		# check baby in color
		if result:
			print("baby in color is correct")
		else:
			print("baby in color is wrong")
		area_detection_page.click_baby_out()
		time.sleep(1)
		x, y = area_detection_page.find_stream_left_top()
		result = area_detection_page.is_color_in_range(x, y, light_orange_range)
		# check baby out color
		if result:
			print("baby out color is correct")
		else:
			print("baby out color is wrong")
	# start from area detection page
	def test_03_area_detection_turn_off_page(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		if area_detection_page.is_switch_on():
			pass
		else:
			area_detection_page.click_switch()
		area_detection_page.click_switch()
		# check turn off dialog text
		try:
			title = area_detection_page.turn_off_dialog_title()
			hint = self.get_string("turn_off_area_detection")
			self.assertEqual(title, hint)
			print("turn off dialog title is correct")
		except AssertionError:
			raise AssertionError("turn off dialog title  is wrong")
		try:
			fifteenmin = area_detection_page.turn_off_15_min_text()
			hint = self.get_string("snooze_detection_fifteen_minutes")
			self.assertEqual(fifteenmin, hint)
			print("turn off 15 is correct")
		except AssertionError:
			raise AssertionError("turn off 15 is wrong")
		try:
			thirtymin = area_detection_page.turn_off_30_min_text()
			hint = self.get_string("snooze_detection_thirty_minutes")
			self.assertEqual(thirtymin, hint)
			print("turn off 30 is correct")
		except AssertionError:
			raise AssertionError("turn off 30 is wrong")
		try:
			off = area_detection_page.turn_off_text()
			hint = self.get_string("turn_off_detection")
			self.assertEqual(off, hint)
			print("turn off text is correct")
		except AssertionError:
			raise AssertionError("turn off text is wrong")
		try:
			cancel = area_detection_page.turn_off_cancel_text()
			hint = self.get_string("cancel")
			self.assertEqual(cancel, hint)
			print("turn off cancel text is correct")
		except AssertionError:
			raise AssertionError("turn off cancel text is wrong")
		# check each button
		try:
			area_detection_page.click_turn_off_15_min()
			self.assertEqual(pixsee_settings_page.area_detection_status_text(), self.get_string("off_selection"))
			print("15 min button worked")
		except AssertionError:
			raise AssertionError("15 min button failed")
		pixsee_settings_page.click_area_detection()
		area_detection_page.click_switch()
		area_detection_page.click_switch()
		try:
			area_detection_page.click_turn_off_cancel()
			self.assertTrue(area_detection_page.is_switch_on())
			print("turn off cancel worked")
		except AssertionError:
			raise AssertionError("turn off cancel failed")
		area_detection_page.click_switch()
		try:
			area_detection_page.click_turn_off_30_min()
			time.sleep(1)
			self.assertEqual(pixsee_settings_page.area_detection_status_text(), self.get_string("off_selection"))
			print("30 min button worked")
		except AssertionError:
			raise AssertionError("30 min button failed")
		pixsee_settings_page.click_area_detection()
		area_detection_page.click_switch()
		area_detection_page.click_switch()
		try:
			area_detection_page.click_turn_off()
			time.sleep(1)
			self.assertEqual(pixsee_settings_page.area_detection_status_text(), self.get_string("off_selection"))
			print("turn off detection worked")
		except AssertionError:
			raise AssertionError("turn off detection failed")




















