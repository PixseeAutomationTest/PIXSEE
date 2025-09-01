import time

from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.pixsee_settings_pages.pixsee_friends_detection_page import PixseeFriendsDetPage

class PixseeFriendsDetectionCase1(BaseTestCase):
	@classmethod
	def setUpClass(cls):
		cls.language = getattr(cls, "language", "zh")
		cls.locale = getattr(cls, "locale", "TW")
		super().setUpClass()

	# start from pixsee settings page
	def setUp(self):
		super().setUp()
		baby_monitor_page = BabyMonitorPage(self.driver)
		menu_page = MenuPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
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
	def test_01_friends_detection_back(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		pixsee_settings_page.click_pixsee_friends_detection()
		# back to settings page
		pixsee_friends_page.click_back()
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("Back to Pixsee Settings page")
		except AssertionError:
			raise AssertionError("Not in Pixsee Settings page")
	# start from pixsee settings page
	def test_02_friends_detection_save(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		origin_status = pixsee_settings_page.pixsee_friends_detection_status_text()
		pixsee_settings_page.click_pixsee_friends_detection()
		# check save enable == false
		try:
			self.assertFalse(pixsee_friends_page.is_save_enable())
			print("Save diable test pass")
		except AssertionError:
			raise AssertionError("Save diable test failed")
		# turn on switch
		pixsee_friends_page.click_switch()
		pixsee_friends_page.click_save()
		new_status = pixsee_settings_page.pixsee_friends_detection_status_text()
		if origin_status != new_status:
			print("save function success")
		else:
			raise AssertionError("save function failed, status not changed")
	# start from pixsee settings page
	def test_03_friends_detection_back_discard(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		origin_status = pixsee_settings_page.pixsee_friends_detection_status_text()
		pixsee_settings_page.click_pixsee_friends_detection()
		pixsee_friends_page.click_switch()
		pixsee_friends_page.click_back()
		# check if is in discard dialog
		try:
			self.assertTrue(pixsee_friends_page.is_in_discard_dialog())
			print("In discard dialog")
			# check discard dialog text
			try:
				discard = pixsee_friends_page.discard_message_txt()
				hint = self.get_string("pixsee_friends_detection_popup_discard_changes")
				self.assertEqual(discard, hint)
				print("Discard dialog title right")
			except AssertionError:
				raise AssertionError("Discard dialog title wrong")
			try:
				yes = pixsee_friends_page.discard_yes_txt()
				hint = self.get_string("yes")
				self.assertEqual(yes, hint)
				print("Discard dialog yes text right")
			except AssertionError:
				raise AssertionError("Discard dialog yes text wrong")
			try:
				no = pixsee_friends_page.discard_no_txt()
				hint = self.get_string("no")
				self.assertEqual(no, hint)
				print("Discard dialog no text right")
			except AssertionError:
				raise AssertionError("Discard dialog no text wrong")
			# click yes
			pixsee_friends_page.click_discard_yes()
			new_status = pixsee_settings_page.pixsee_friends_detection_status_text()
			try:
				self.assertEqual(origin_status, new_status)
				print("Discard function success")
			except AssertionError:
				raise AssertionError("Discard function failed, status changed")
		except AssertionError:
			raise AssertionError("Not in discard dialog")
	# start from pixsee settings page
	def test_04_friends_detection_switch(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		pixsee_settings_page.click_pixsee_friends_detection()
		# check friends detection header
		try:
			title = pixsee_friends_page.title()
			hint = self.get_string("pixsee_friends_detection_title")
			self.assertEqual(title, hint)
			print("Friends detection title right")
		except AssertionError:
			raise AssertionError("Friends detection title wrong")
		# check friends detection description
		try:
			subtitle = pixsee_friends_page.description_subtitle()
			print(pixsee_friends_page.description_subtitle())
			hint = self.get_string("pixsee_friends_detection_subtext")
			self.assertEqual(subtitle, hint)
			print("Friends detection subtitle right")
		except AssertionError:
			raise AssertionError("Friends detection subtitle wrong")
		# switch status
		current_status = pixsee_friends_page.is_switch_on()
		self.check_switch_and_content(current_status, pixsee_friends_page.DetectionType)
		pixsee_friends_page.click_switch()
		time.sleep(1)
		after_status = pixsee_friends_page.is_switch_on()
		self.check_switch_and_content(after_status, pixsee_friends_page.DetectionType)

class PixseeFriendsDetectionCase2(BaseTestCase):
	@classmethod
	def setUpClass(cls):
		cls.language = getattr(cls, "language", "zh")
		cls.locale = getattr(cls, "locale", "TW")
		super().setUpClass()

	# start from friends detection page
	def setUp(self):
		super().setUp()
		baby_monitor_page = BabyMonitorPage(self.driver)
		menu_page = MenuPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		try:
			while self.driver.current_package != self.driver.capabilities.get("appPackage"):
				self.driver.terminate_app(self.driver.current_package)
				self.open_app()
			if pixsee_friends_page.is_in_pixsee_friends_det_page():
				return
			elif not baby_monitor_page.is_in_baby_monitor_page():
				self.shutdown_app()
				self.open_app()
			print("Finish opening app.")
			baby_monitor_page.click_home()
			menu_page.click_settings()
			pixsee_settings_page.click_pixsee_friends_detection()
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e
	def test_05_friends_detection_tap_checkbox(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		if pixsee_friends_page.is_switch_on() :
			pass
		else:
			pixsee_friends_page.click_switch()
		# check friends detection type group titles
		try:
			dettype = pixsee_friends_page.dettype_txt()
			hint = self.get_string("efence_type_detection")
			self.assertEqual(dettype, hint)
			print("Friends detection type is correct")
		except AssertionError:
			raise AssertionError("Friends detection type is wrong")
		try:
			all_days = pixsee_friends_page.all_day_txt()
			hint = self.get_string("pixsee_friends_detection_all_day_type")
			self.assertEqual(all_days, hint)
			print("Friends detection all day text right")
		except AssertionError:
			print("Friends detection all day text wrong")
		try:
			set_time = pixsee_friends_page.set_time_txt()
			hint = self.get_string("pixsee_friends_detection_set_time_type")
			self.assertEqual(set_time, hint)
			print("Friends detection set time text right")
		except AssertionError:
			raise AssertionError("Friends detection set time text wrong")
		# check clickable
		pixsee_friends_page.click_set_time()
		time.sleep(1)
		self.tap_on_visibility(pixsee_friends_page.TimeSpan, "Set Time",True)
		pixsee_friends_page.click_all_day()
		time.sleep(1)
		self.tap_on_visibility(pixsee_friends_page.TimeSpan, "All Day", False)
	# stay
	def test_06_friends_detection_time_span(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		if pixsee_friends_page.is_switch_on() :
			pass
		else:
			pixsee_friends_page.click_switch()

		pixsee_friends_page.click_set_time()
		# check time span group titles
		try:
			time_span = pixsee_friends_page.time_span_txt()
			hint = self.get_string("time_lapse_time_span")
			self.assertEqual(time_span, hint)
			print("Friends detection time span title right")
		except AssertionError:
			raise AssertionError("Friends detection time span title wrong")
		try:
			start_time = pixsee_friends_page.start_time_txt()
			hint = self.get_string("pixsee_friends_detection_starting_time")
			self.assertEqual(start_time, hint)
			print("Friends detection start time text right")
		except AssertionError:
			raise AssertionError("Friends detection start time text wrong")
		try:
			end_time = pixsee_friends_page.end_time_txt()
			hint = self.get_string("pixsee_friends_detection_ending_time")
			self.assertEqual(end_time, hint)
			print("Friends detection end time text right")
		except AssertionError:
			raise AssertionError("Friends detection end time text wrong")
		# check start time block's clickable and confirm
		current = pixsee_friends_page.start_time_block_txt()
		pixsee_friends_page.click_start_time_block()
		try:
			self.assertTrue(pixsee_friends_page.is_in_timer())
			print("In start time block")
			# check cancel,confirm text
			try:
				cancel = pixsee_friends_page.cancel_txt()
				hint = self.get_string("cancel")
				self.assertEqual(cancel, hint)
				print("Start time block cancel text right")
			except AssertionError:
				print("Start time block cancel text wrong")
			try:
				confirm = pixsee_friends_page.confirm_txt()
				hint = self.get_string("code_verification_verify_button")
				self.assertEqual(confirm, hint)
				print("Start time block confirm text right")
			except AssertionError:
				print("Start time block confirm text wrong")
			# check time scrollable
			pixsee_friends_page.change_hour_by_scroll()
			pixsee_friends_page.change_minutes_by_scroll()
			pixsee_friends_page.change_am_to_pm_by_scroll()
			pixsee_friends_page.click_confirm()
			after = pixsee_friends_page.start_time_block_txt()
			try:
				self.assertNotEqual(current, after)
				print("timer confirm function success")
			except AssertionError:
				raise AssertionError("timer confirm function failed, start time not changed")
		except AssertionError:
			print("Not in start time block")
			raise AssertionError("Not in start time block")
		# check end time block's clickable and cancel
		before = pixsee_friends_page.end_time_block_txt()
		pixsee_friends_page.click_end_time_block()
		try:
			self.assertTrue(pixsee_friends_page.is_in_timer())
			print("In end time block")
			pixsee_friends_page.click_cancel()
			after = pixsee_friends_page.end_time_block_txt()
			try:
				self.assertEqual(before, after)
				print("timer cancel function success")
			except AssertionError:
				raise AssertionError("timer cancel function failed, end time changed")
		except AssertionError:
			raise AssertionError("Not in end time block")
		pixsee_friends_page.click_save()
	# back to pixsee settings page




















