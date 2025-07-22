
import time
from pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.area_detection_page import AreaDetectionPage
from appium.webdriver.common.appiumby import AppiumBy




class AreaDetectionCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)
		# ensure is connected to machine
		baby_monitor_page = BabyMonitorPage(self.driver)
		if not baby_monitor_page.is_connected():
			self.skipTest("not online，skip all test")

	def test_01_area_detection_tutor_skip_1(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()

		menu_page.click_settings()

		pixsee_settings_page.click_area_detection()
		# check first tutor title
		try:
			title = area_detection_page.tutor_first_title_text()
			hint = self.get_string("safe_area_tutorial_title")
			self.assertEqual(title, hint)
			print("first tutor  title right")
		except AssertionError :
			print("first tutor  title wrong")
		# check first tutor indicator
		try:
			self.assertTrue(area_detection_page.is_in_tutor_first_page())
			print("first tutor indicator displayed")
		except AssertionError :
			print("first tutor indicator displayed")
		# check skip
		try:
			skip = area_detection_page.skip_text()
			hint = self.get_string("skip")
			self.assertEqual(skip, hint)
			print("skip display right")
		except AssertionError :
			print("skip display wrong")
		area_detection_page.click_skip()
		# check in area area_detection_page
		try:
			self.assertTrue(area_detection_page.is_in_area_detection_page())
			print("skip first tutor successfully")
		except AssertionError :
			print("skip first tutor unsuccessfully")
			raise AssertionError("error")
	def test_02_area_detection_tutor_skip_2(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()

		menu_page.click_settings()

		pixsee_settings_page.click_area_detection()
		self.right_wipe()
		# check second tutor title
		try:
			title = area_detection_page.tutor_second_title_text()
			hint = self.get_string("caution_area_tutorial_title")
			self.assertEqual(title, hint)
			print("second tutor  title right")
		except AssertionError :
			print("second tutor  title wrong")
		# check second tutor indicator
		try:
			self.assertTrue(area_detection_page.is_in_tutor_second_page())
			print("second tutor indicator displayed")
		except AssertionError :
			print("second tutor indicator displayed")
		# check skip
		try:
			skip = area_detection_page.skip_text()
			hint = self.get_string("skip")
			self.assertEqual(skip, hint)
			print("skip display right")
		except AssertionError :
			print("skip display wrong")

		area_detection_page.click_skip()
		# check in area area_detection_page
		try:
			self.assertTrue(area_detection_page.is_in_area_detection_page())
			print("skip second tutor successfully")
		except AssertionError :
			print("skip second tutor unsuccessfully")
			raise AssertionError("error")
	def test_03_area_detection_tutor_skip_121(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()

		menu_page.click_settings()

		pixsee_settings_page.click_area_detection()

		# check first tutor page
		try:
			self.assertTrue(area_detection_page.is_in_tutor_first_page())
			print("first tutor displayed")
		except AssertionError :
			print("first tutor displayed")
			raise AssertionError("error")

		self.right_wipe()
		# check second tutor page
		try:
			self.assertTrue(area_detection_page.is_in_tutor_second_page())
			print("second tutor indicator displayed")
		except AssertionError :
			print("second tutor indicator displayed")

		self.left_wipe()
		# check first tutor page
		try:
			self.assertTrue(area_detection_page.is_in_tutor_first_page())
			print("first tutor displayed")
		except AssertionError :
			print("first tutor displayed")
			raise AssertionError("error")

		area_detection_page.click_skip()
		# check in area area_detection_page
		try:
			self.assertTrue(area_detection_page.is_in_area_detection_page())
			print("skip second tutor successfully")
		except AssertionError :
			print("skip second tutor unsuccessfully")
			raise AssertionError("error")
	def test_04_area_detection_switch(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()

		menu_page.click_settings()

		pixsee_settings_page.click_area_detection()
		area_detection_page.click_skip()
		# check Area detection title
		try:
			title = area_detection_page.title()
			hint = self.get_string("detection")
			self.assertEqual(title, hint)
			print("Area detection title right")
		except AssertionError :
			print("Area detection title wrong")
		# check Area detection description
		try:
			subtitle = area_detection_page.detection_description()
			hint = self.get_string("efence_settings_status_description")
			self.assertEqual(subtitle, hint)
			print("Area detection subtitle right")
		except AssertionError :
			print("Area detection subtitle wrong")
		# switch status
		current_status = area_detection_page.is_switch_on()
		if current_status:
			try:
				is_visible = len(self.driver.find_elements(AppiumBy.ID, area_detection_page.Sensitivity)) > 0
				assert is_visible, "switch on failed"
				print("switch on success")
			except AssertionError :
				print("switch on failed")
			area_detection_page.click_switch()
			# check in turn off dialog
			try:
				self.assertTrue(area_detection_page.is_in_turn_off_dialog())
				print("switch off successfully")
			except AssertionError :
				print("switch off unsuccessfully")
				raise AssertionError("error")
		else:
			self.check_switch_and_content(current_status, area_detection_page.Sensitivity)
			area_detection_page.click_switch()
			after_status = area_detection_page.is_switch_on()
			self.check_switch_and_content(after_status, area_detection_page.Sensitivity)
	def test_05_area_detection_save(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()

		self.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()
		menu_page.click_settings()
		origin_status = pixsee_settings_page.area_detection_status_text()
		pixsee_settings_page.click_area_detection()
		area_detection_page.click_skip()
		# check save enable = false
		try:
			self.assertFalse(area_detection_page.is_save_enable())
			print("Save diable test pass")
		except AssertionError :
			print("Save diable test failed")
			raise AssertionError("Save diable test failed")
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
			print("save function failed")
			raise AssertionError("save function failed, status not changed")
	def test_06_area_detection_back(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()

		self.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()
		menu_page.click_settings()
		pixsee_settings_page.click_area_detection()
		area_detection_page.click_skip()
		# back to settings page
		area_detection_page.click_back()
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("Back to Pixsee Settings page")
		except AssertionError :
			print("Not in Pixsee Settings page")
			raise AssertionError("Not in Pixsee Settings page")
	def test_07_area_detection_tap_checkbox_sensitivity(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		time.sleep(2)

		menu_page.click_logout()

		menu_page.click_settings()

		pixsee_settings_page.click_area_detection()
		area_detection_page.click_skip()
		if area_detection_page.is_switch_on() == "true":
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
			print("Sensitivity title is wrong")
		try:
			dettype = area_detection_page.dettype_txt()
			hint = self.get_string("efence_type_detection")
			self.assertEqual(dettype, hint)
			print("detection type is correct")
		except AssertionError :
			print("detection type is wrong")
		# check box name
		try:
			low = area_detection_page.low_text()
			hint = self.get_string("sensitivity_low")
			self.assertEqual(low, hint)
			print("Low checkbox text is correct")
		except AssertionError :
			print("Low checkbox text is wrong")
		try:
			medium = area_detection_page.medium_text()
			hint = self.get_string("sensitivity_medium")
			self.assertEqual(medium, hint)
			print("Medium checkbox text is correct")
		except AssertionError :
			print("Medium checkbox text is wrong")
		try:
			high = area_detection_page.high_text()
			hint = self.get_string("sensitivity_high")
			self.assertEqual(high, hint)
			print("High checkbox text is correct")
		except AssertionError :
			print("High checkbox text is wrong")
		# check clickable
		try:
			self.assertTrue(area_detection_page.is_low_clickable())
			print("Low checkbox is clickable")
		except AssertionError :
			print("Low checkbox is not clickable")
		try:
			self.assertTrue(area_detection_page.is_medium_clickable())
			print("Medium checkbox is clickable")
		except AssertionError :
			print("Medium checkbox is not clickable")
		try:
			self.assertTrue(area_detection_page.is_high_clickable())
			print("High checkbox is clickable")
		except AssertionError :
			print("High checkbox is not clickable")
	def test_08_area_detection_tap_checkbox_detection_type(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()
		menu_page.click_settings()

		pixsee_settings_page.click_area_detection()
		area_detection_page.click_skip()
		if area_detection_page.is_switch_on() == "true":
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
			print("baby in text is wrong")
		try:
			babyout = area_detection_page.baby_out_text()
			hint = self.get_string("efence_dangerous_area")
			self.assertEqual(babyout, hint)
			print("baby out text is correct")
		except AssertionError :
			print("baby out text is wrong")
		# check box clickable
		area_detection_page.click_baby_in()
		try:
			drag = area_detection_page.drag_text()
			hint = self.get_string("detection_settings_safety_area_title")
			self.assertEqual(drag, hint)
			print("baby in clickable")
		except AssertionError :
			print("baby in unclickable")
		area_detection_page.click_baby_out()
		try:
			drag = area_detection_page.drag_text()
			hint = self.get_string("detection_settings_caution_area_title")
			self.assertEqual(drag, hint)
			print("baby out clickable")
		except AssertionError :
			print("baby out unclickable")
	def test_09_area_detection_turn_off_page(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()
		menu_page.click_settings()

		pixsee_settings_page.click_area_detection()
		area_detection_page.click_skip()
		if area_detection_page.is_switch_on() == "true":
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
		except AssertionError :
			print("turn off dialog title  is wrong")
		try:
			fifteenmin = area_detection_page.turn_off_15_min_text()
			hint = self.get_string("Snooze for 15 minutes")
			self.assertEqual(fifteenmin, hint)
			print("turn off 15 is correct")
		except AssertionError :
			print("turn off 15 is wrong")
		try:
			thirtymin = area_detection_page.turn_off_30_min_text()
			hint = self.get_string("Snooze for 30 minutes")
			self.assertEqual(thirtymin, hint)
			print("turn off 30 is correct")
		except AssertionError :
			print("turn off 30 is wrong")
		try:
			off = area_detection_page.turn_off_text()
			hint = self.get_string("Turn off detection")
			self.assertEqual(off, hint)
			print("turn off text is correct")
		except AssertionError :
			print("turn off text is wrong")
		try:
			cancel = area_detection_page.turn_off_cancel_text()
			hint = self.get_string("cancel")
			self.assertEqual(cancel, hint)
			print("turn off cancel text is correct")
		except AssertionError :
			print("turn off cancel text is wrong")
		# check each button
		try:
			area_detection_page.click_turn_off_15_min()
			self.assertEqual(pixsee_settings_page.area_detection_status_text(), "Off")
			print("15 min button worked")
		except AssertionError:
			print("15 min button failed")
		pixsee_settings_page.click_area_detection()
		area_detection_page.click_switch()
		area_detection_page.click_switch()
		try:
			area_detection_page.click_turn_off_cancel()
			self.assertTrue(area_detection_page.is_switch_on())
			print("turn off cancel worked")
		except AssertionError:
			print("turn off cancel failed")
		area_detection_page.click_switch()
		try:
			area_detection_page.click_turn_off_30_min()
			self.assertEqual(pixsee_settings_page.area_detection_status_text(), "Off")
			print("30 min button worked")
		except AssertionError:
			print("30 min button failed")
		pixsee_settings_page.click_area_detection()
		area_detection_page.click_switch()
		area_detection_page.click_switch()
		try:
			area_detection_page.click_turn_off()
			self.assertEqual(pixsee_settings_page.area_detection_status_text(), "Off")
			print("turn off detection worked")
		except AssertionError:
			print("turn off detection failed")
	def test_10_area_detection_back_discard(self):
		area_detection_page = AreaDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		# login
		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		time.sleep(2)

		menu_page.click_logout()
		menu_page.click_settings()
		pixsee_settings_page.click_area_detection()
		area_detection_page.click_skip()
		# check if is in discard dialog
		if area_detection_page.is_switch_on() == "true":
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
			except AssertionError :
				print("Discard dialog title wrong")
			try:
				yes = area_detection_page.discard_yes_text()
				hint = self.get_string("yes")
				self.assertEqual(yes, hint)
				print("Discard dialog yes text right")
			except AssertionError :
				print("Discard dialog yes text wrong")
			try:
				no = area_detection_page.discard_no_text()
				hint = self.get_string("no")
				self.assertEqual(no, hint)
				print("Discard dialog no text right")
			except AssertionError :
				print("Discard dialog no text wrong")
			# click yes
			area_detection_page.click_discard_yes()
			# check status = false
			self.assertEqual(pixsee_settings_page.area_detection_status_text(),"Off")
			print("back button worked")
		except AssertionError :
			print("Not in discard dialog")
			raise AssertionError("Not in discard dialog")



















