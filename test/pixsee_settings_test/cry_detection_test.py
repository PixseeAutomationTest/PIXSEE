
import time
from pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.cry_detection_page import CryDetectionPage





class CryDetectionCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)
		baby_monitor_page = BabyMonitorPage(self.driver)
		if not baby_monitor_page.is_connected():
			self.skipTest("not online，skip all test")


	def test_01_cry_detection_switch(self):
		cry_detection_page = CryDetectionPage(self.driver)
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

		pixsee_settings_page.click_CryDetection()
		# check Cry detection title
		try:
			title = cry_detection_page.title()
			hint = self.get_string("detection")
			self.assertEqual(title, hint)
			print("Cry detection title right")
		except AssertionError:
			print("Cry detection title wrong")
			raise AssertionError("Cry detection title mismatch")
		# check Cry detection description
		try:
			subtitle = cry_detection_page.detection_description()
			hint = self.get_string("auto_detect_and_alert_when_baby_is_crying")
			self.assertEqual(subtitle, hint)
			print("Cry detection subtitle right")
		except AssertionError:
			print("Cry detection subtitle wrong")
			raise AssertionError("Cry detection subtitle mismatch")
		# switch status
		current_status = cry_detection_page.is_switch_on()
		self.check_switch_and_content(current_status, cry_detection_page.Sensitivity)
		cry_detection_page.click_switch()
		after_status = cry_detection_page.is_switch_on()
		self.check_switch_and_content(after_status, cry_detection_page.Sensitivity)
	def test_02_cry_detection_save(self):
		cry_detection_page = CryDetectionPage(self.driver)
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
		origin_status = pixsee_settings_page.cry_detection_status_text()
		pixsee_settings_page.click_CryDetection()
		# turn on switch
		cry_detection_page.click_switch()
		cry_detection_page.click_save()
		new_status = pixsee_settings_page.cry_detection_status_text()
		if origin_status != new_status:
			print("save function success")
		else:
			print("save function failed")
			raise AssertionError("save function failed, status not changed")
	def test_03_cry_detection_back(self):
		cry_detection_page = CryDetectionPage(self.driver)
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
		pixsee_settings_page.click_CryDetection()
		# back to settings page
		cry_detection_page.click_back()
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("Back to Pixsee Settings page")
		except AssertionError:
			print("Not in Pixsee Settings page")
			raise AssertionError("Not in Pixsee Settings page")
	def test_04_cry_detection_tap_checkbox(self):
		cry_detection_page = CryDetectionPage(self.driver)
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

		pixsee_settings_page.click_CryDetection()
		if cry_detection_page.is_switch_on() == "true":
			pass
		else:
			cry_detection_page.click_switch()
		# check Cry detection type group titles
		try:
			sensitivity = cry_detection_page.sensitivity_text()
			hint = self.get_string("sensitivity_level")
			self.assertEqual(sensitivity, hint)
			print("Sensitivity title is correct")
		except AssertionError:
			print("Sensitivity title is wrong")
			raise AssertionError("sensitivity doesn't show up after switch on")
		try:
			music_settings = cry_detection_page.music_settings_text()
			hint = self.get_string("auto_play_music")
			self.assertEqual(music_settings, hint)
			print("music settings text right")
		except AssertionError:
			print("music settings text wrong")
			raise AssertionError("music settings text mismatch")
		try:
			smart_soothing = cry_detection_page.smart_soothing_text()
			hint = self.get_string("smart_soothing")
			self.assertEqual(smart_soothing, hint)
			print("smart soothing text right")
		except AssertionError:
			print("smart soothing text wrong")
			raise AssertionError("smart soothing text mismatch")
			# check box name
		try:
			low = cry_detection_page.low_text()
			hint = self.get_string("sensitivity_low")
			self.assertEqual(low, hint)
			print("Low checkbox text is correct")
		except AssertionError:
			print("Low checkbox text is wrong")
			raise AssertionError("low checkbox text mismatch")
		try:
			medium = cry_detection_page.medium_text()
			hint = self.get_string("sensitivity_medium")
			self.assertEqual(medium, hint)
			print("Medium checkbox text is correct")
		except AssertionError:
			print("Medium checkbox text is wrong")
			raise AssertionError("medium checkbox text mismatch")
		try:
			high = cry_detection_page.high_text()
			hint = self.get_string("sensitivity_high")
			self.assertEqual(high, hint)
			print("High checkbox text is correct")
		except AssertionError:
			print("High checkbox text is wrong")
			raise AssertionError("high checkbox text mismatch")
		# check clickable
		try:
			self.assertTrue(cry_detection_page.is_low_clickable())
			print("Low checkbox is clickable")
		except AssertionError:
			print("Low checkbox is not clickable")
			raise AssertionError("Low checkbox is not clickable")
		try:
			self.assertTrue(cry_detection_page.is_medium_clickable())
			print("Medium checkbox is clickable")
		except AssertionError:
			print("Medium checkbox is not clickable")
			raise AssertionError("Medium checkbox is not clickable")
		try:
			self.assertTrue(cry_detection_page.is_high_clickable())
			print("High checkbox is clickable")
		except AssertionError:
			print("High checkbox is not clickable")
			raise AssertionError("High checkbox is not clickable")
	def test_05_cry_detection_smart_soothing_switch(self):
		cry_detection_page = CryDetectionPage(self.driver)
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

		pixsee_settings_page.click_CryDetection()
		if cry_detection_page.is_switch_on() == "true":
			pass
		else:
			cry_detection_page.click_switch()

		# switch status
		current_status = cry_detection_page.is_switch_on()
		self.check_switch_and_content(current_status, cry_detection_page.Music)
		cry_detection_page.click_smart_soothing_switch()
		after_status = cry_detection_page.is_switch_on()
		self.check_switch_and_content(after_status, cry_detection_page.Music)
	def test_06_cry_detection_music_page(self):
		cry_detection_page = CryDetectionPage(self.driver)
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

		pixsee_settings_page.click_CryDetection()
		if cry_detection_page.is_switch_on() == "true":
			pass
		else:
			cry_detection_page.click_switch()
		if cry_detection_page.is_smart_soothing_switch_on() == "true":
			pass
		else:
			cry_detection_page.click_smart_soothing_switch()
		cry_detection_page.click_music()
		# check enter music room
		try:
			self.assertTrue(cry_detection_page.is_in_cry_detection_page())
			print("entered music room successfully")
		except AssertionError:
			print("entered music room unsuccessfully")
			raise AssertionError("Not in music room")
	def test_07_cry_detection_back_discard(self):
		cry_detection_page = CryDetectionPage(self.driver)
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
		origin_status = pixsee_settings_page.cry_detection_status_text()
		pixsee_settings_page.click_CryDetection()
		cry_detection_page.click_switch()
		cry_detection_page.click_back()
		# check if is in discard dialog
		try:
			self.assertTrue(cry_detection_page.is_in_discard_dialog())
			print("In discard dialog")
			# check discard dialog text
			try:
				discard = cry_detection_page.discard_message_text()
				hint = self.get_string("discard_cry_detection_confirmation_message")
				self.assertEqual(discard, hint)
				print("Discard dialog title right")
			except AssertionError:
				print("Discard dialog title wrong")
				raise AssertionError("Discard dialog title mismatch")
			try:
				yes = cry_detection_page.discard_yes_text()
				hint = self.get_string("yes")
				self.assertEqual(yes, hint)
				print("Discard dialog yes text right")
			except AssertionError:
				print("Discard dialog yes text wrong")
				raise AssertionError("Discard dialog yes text mismatch")
			try:
				no = cry_detection_page.discard_no_text()
				hint = self.get_string("no")
				self.assertEqual(no, hint)
				print("Discard dialog no text right")
			except AssertionError:
				print("Discard dialog no text wrong")
				raise AssertionError("Discard dialog no text mismatch")
			# click yes
			cry_detection_page.click_discard_yes()
			new_status = pixsee_settings_page.cry_detection_status_text()
			try:
				self.assertEqual(origin_status, new_status)
				print("Discard function success")
			except AssertionError:
				print("Discard function failed")
				raise AssertionError("Discard function failed, status changed")
		except AssertionError:
			print("Not in discard dialog")
			raise AssertionError("Not in discard dialog")



















