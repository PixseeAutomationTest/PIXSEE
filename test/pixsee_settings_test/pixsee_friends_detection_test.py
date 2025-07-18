

from pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.pixsee_friends_detection_page import PixseeFriendsDetPage





class PixseeFriendsDetectionCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)


	def test_01_friends_detection_switch(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		pixsee_settings_page.click_PixseeFriendsDetection()
		# check friends detection title
		try:
			title = pixsee_friends_page.title()
			hint = self.get_string("pixsee_friends_detection_title")
			self.assertEqual(title, hint)
			print("Friends detection title right")
		except AssertionError:
			print("Friends detection title wrong")
			raise AssertionError("Friends detection title mismatch")
		# check friends detection description
		try:
			subtitle = pixsee_friends_page.description_subtitle()
			hint = self.get_string("pixsee_friends_detection_subtitle")
			self.assertEqual(subtitle, hint)
			print("Friends detection subtitle right")
		except AssertionError:
			print("Friends detection subtitle wrong")
			raise AssertionError("Friends detection subtitle mismatch")
		# switch status
		current_status = pixsee_friends_page.is_switch_on()
		self.check_switch_and_content(current_status, pixsee_friends_page.DetectionType)
		pixsee_friends_page.click_switch()
		after_status = pixsee_friends_page.is_switch_on()
		self.check_switch_and_content(after_status, pixsee_friends_page.DetectionType)
	def test_02_friends_detection_save(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()

		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		origin_status = pixsee_settings_page.pixsee_friends_detection_status_text()
		pixsee_settings_page.click_PixseeFriendsDetection()
		# turn on switch
		pixsee_friends_page.click_switch()
		pixsee_friends_page.click_save()
		new_status = pixsee_settings_page.pixsee_friends_detection_status_text()
		if origin_status != new_status:
			print("save function success")
		else:
			print("save function failed")
			raise AssertionError("save function failed, status not changed")
	def test_03_friends_detection_back(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()

		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		pixsee_settings_page.click_PixseeFriendsDetection()
		# back to settings page
		pixsee_friends_page.click_back()
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("Back to Pixsee Settings page")
		except AssertionError:
			print("Not in Pixsee Settings page")
			raise AssertionError("Not in Pixsee Settings page")
	def test_04_friends_detection_tap_checkbox(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		pixsee_settings_page.click_PixseeFriendsDetection()
		if pixsee_friends_page.is_switch_on() == "true":
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
			print("Friends detection type is wrong")
			raise AssertionError("detection doesn't show up after switch on")
		try:
			all_days = pixsee_friends_page.all_day_txt()
			hint = self.get_string("pixsee_friends_detection_all_day_type")
			self.assertEqual(all_days, hint)
			print("Friends detection all day text right")
		except AssertionError:
			print("Friends detection all day text wrong")
			raise AssertionError("Friends detection all day text mismatch")
		try:
			set_time = pixsee_friends_page.set_time_txt()
			hint = self.get_string("pixsee_friends_detection_set_time_type")
			self.assertEqual(set_time, hint)
			print("Friends detection set time text right")
		except AssertionError:
			print("Friends detection set time text wrong")
			raise AssertionError("Friends detection set time text mismatch")
		# check clickable
		pixsee_friends_page.click_set_time()
		self.tap_on_visibility(pixsee_friends_page.TimeSpan, "Set Time",True)
		pixsee_friends_page.click_all_day()
		self.tap_on_visibility(pixsee_friends_page.TimeSpan, "All Day", False)
	def test_05_friends_detection_time_span(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		pixsee_settings_page.click_PixseeFriendsDetection()
		if pixsee_friends_page.is_switch_on() == "true":
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
			print("Friends detection time span title wrong")
			raise AssertionError("Friends detection time span title mismatch")
		try:
			start_time = pixsee_friends_page.start_time_txt()
			hint = self.get_string("time_lapse_start_time")
			self.assertEqual(start_time, hint)
			print("Friends detection start time text right")
		except AssertionError:
			print("Friends detection start time text wrong")
			raise AssertionError("Friends detection start time text mismatch")
		try:
			end_time = pixsee_friends_page.end_time_txt()
			hint = self.get_string("time_lapse_end_time")
			self.assertEqual(end_time, hint)
			print("Friends detection end time text right")
		except AssertionError:
			print("Friends detection end time text wrong")
			raise AssertionError("Friends detection end time text mismatch")
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
				raise AssertionError("Start time block cancel text mismatch")
			try:
				confirm = pixsee_friends_page.confirm_txt()
				hint = self.get_string("code_verification_verify_button")
				self.assertEqual(confirm, hint)
				print("Start time block confirm text right")
			except AssertionError:
				print("Start time block confirm text wrong")
				raise AssertionError("Start time block confirm text mismatch")
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
				print("timer confirm function failed")
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
				print("timer cancel function failed")
				raise AssertionError("timer cancel function failed, end time changed")
		except AssertionError:
			print("Not in end time block")
			raise AssertionError("Not in end time block")
	def test_06_friends_detection_back_discard(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		origin_status = pixsee_settings_page.pixsee_friends_detection_status_text()
		pixsee_settings_page.click_PixseeFriendsDetection()
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
				print("Discard dialog title wrong")
				raise AssertionError("Discard dialog title mismatch")
			try:
				yes = pixsee_friends_page.discard_yes_txt()
				hint = self.get_string("yes")
				self.assertEqual(yes, hint)
				print("Discard dialog yes text right")
			except AssertionError:
				print("Discard dialog yes text wrong")
				raise AssertionError("Discard dialog yes text mismatch")
			try:
				no = pixsee_friends_page.discard_no_txt()
				hint = self.get_string("no")
				self.assertEqual(no, hint)
				print("Discard dialog no text right")
			except AssertionError:
				print("Discard dialog no text wrong")
				raise AssertionError("Discard dialog no text mismatch")
			# click yes
			pixsee_friends_page.click_discard_yes()
			new_status = pixsee_settings_page.pixsee_friends_detection_status_text()
			try:
				self.assertEqual(origin_status, new_status)
				print("Discard function success")
			except AssertionError:
				print("Discard function failed")
				raise AssertionError("Discard function failed, status changed")
		except AssertionError:
			print("Not in discard dialog")
			raise AssertionError("Not in discard dialog")




















# def test_03_friends_detection_switch_off(self):