
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.time_lapse_video_page import TimeLapseVideoPage
from pages.menu_pages.subscription_page import SubscriptionPage


class TimeLapseVideoCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)
		baby_monitor_page = BabyMonitorPage(self.driver)
		if not baby_monitor_page.is_connected():
			self.skipTest("not online，skip all test")

	def test_01_time_lapse_video_subscription_click_no(self):
		time_lapse_video = TimeLapseVideoPage(self.driver)
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

		pixsee_settings_page.click_time_lapse_video()
		# check header text
		try:
			header = time_lapse_video.header_text()
			hint = self.get_string("time_lapse")
			self.assertEqual(header, hint)
			print("time-lapse header text right")
		except AssertionError:
			print("time-lapse header text wrong")
		# check time-lapse recording title
		try:
			title = time_lapse_video.title()
			hint = self.get_string("timelapse_recording_settings")
			self.assertEqual(title, hint)
			print("time_lapse_video title right")
		except AssertionError:
			print("time_lapse_video title wrong")
		# check time_lapse_video description
		try:
			subtitle = time_lapse_video.description()
			hint = self.get_string("time_lapse_recording_mode_text_settings")
			self.assertEqual(subtitle, hint)
			print("time_lapse_video subtitle right")
		except AssertionError:
			print("time_lapse_video subtitle wrong")
		# switch on
		time_lapse_video.click_switch()
		# check if in upgrade dialog
		try:
			self.assertTrue(time_lapse_video.is_in_timelapse_upgrade_dialog())
			print("In time lapse video upgrade dialog")
			# check upgrade dialog title
			try:
				upgrade_title = time_lapse_video.upgrade_title_txt()
				hint = self.get_string("new_subscription_timelapse_info")
				self.assertEqual(upgrade_title, hint)
				print("Upgrade dialog title right")
			except AssertionError:
				print("Upgrade dialog title wrong")
			# check upgrade dialog button text
			try:
				upgrade_description = time_lapse_video.upgrade_subscription_txt()
				hint = self.get_string("subscription_go_to_subscription")
				self.assertEqual(upgrade_description, hint)
				print("Upgrade dialog subscription right")
			except AssertionError:
				print("Upgrade dialog subscription wrong")
			try:
				upgrade_no = time_lapse_video.upgrade_no_txt()
				hint = self.get_string("no_thanks_action")
				self.assertEqual(upgrade_no, hint)
				print("Upgrade dialog no text right")
			except AssertionError:
				print("Upgrade dialog no text wrong")
			# click no
			time_lapse_video.click_upgrade_no()
			# back to time lapse video page
			try:
				self.assertTrue(time_lapse_video.is_in_timelapse_video_page())
				print("Back to time lapse video page")
			except AssertionError:
				print("Not in time lapse video page")
				raise AssertionError("Not in time lapse video page")
		except AssertionError:
			print("Not in time lapse video upgrade dialog")
			raise AssertionError("Not in time lapse video upgrade dialog")
	def test_02_time_lapse_video_subscription_click_yes(self):
		time_lapse_video = TimeLapseVideoPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		subscriptionion_page = SubscriptionPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()

		baby_monitor_page.click_home()

		# skip menu tutor
		menu_page.click_logout()

		menu_page.click_settings()

		pixsee_settings_page.click_time_lapse_video()
		time_lapse_video.click_switch()
		time_lapse_video.click_upgrade_subscription()
		# check if in subscription page
		try:
			self.assertTrue(subscriptionion_page.is_in_subscription_page())
			print("In subscription page")
		except AssertionError:
			print("Not in subscription page")
			raise AssertionError("Not in subscription page")
	def test_03_time_lapse_video_subscription_x(self):
		time_lapse_video = TimeLapseVideoPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		subscription_page = SubscriptionPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()

		self.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()

		menu_page.click_settings()
		pixsee_settings_page.click_time_lapse_video()
		time_lapse_video.click_switch()
		time_lapse_video.click_upgrade_subscription()
		subscription_page.click_x()
		# check if back to time lapse video page
		try:
			self.assertTrue(time_lapse_video.is_in_timelapse_video_page())
			print("x works, back to time lapse video page")
		except AssertionError:
			print("x not works, not in time lapse video page")
			raise AssertionError("Not in time lapse video page")
	def test_04_time_lapse_subscribe(self):
		time_lapse_video = TimeLapseVideoPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		subscription_page = SubscriptionPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()

		self.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()
		menu_page.click_settings()
		pixsee_settings_page.click_time_lapse_video()
		time_lapse_video.click_switch()
		# subscribe
		time_lapse_video.click_upgrade_subscription()
		subscription_page.click_gold_star()
		subscription_page.click_plan1()
		subscription_page.click_pay()
		# check if back to time lapse video page
		try:
			self.assertTrue(time_lapse_video.is_in_timelapse_video_page())
			print("subscribe successfully")
		except AssertionError:
			print("subscribe failed")
			raise AssertionError("Not in time lapse video page after subscribe")
		# Already subscribed
	def test_05_time_lapse_video_switch(self):
		time_lapse_video = TimeLapseVideoPage(self.driver)
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
		pixsee_settings_page.click_time_lapse_video()
		current_status = time_lapse_video.is_switch_on()
		self.check_switch_and_content(current_status, time_lapse_video.RecordingMode)
		time_lapse_video.click_switch()
		after_status = time_lapse_video.is_switch_on()
		self.check_switch_and_content(after_status, time_lapse_video.RecordingMode)
	def test_05_time_lapse_video_check_text(self):
		time_lapse_video = TimeLapseVideoPage(self.driver)
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
		pixsee_settings_page.click_time_lapse_video()
		# ensure time lapse video switch is on
		if time_lapse_video.is_switch_on() == "true":
			pass
		else:
			time_lapse_video.click_switch()

		# check text
		try:
			mode = time_lapse_video.recording_mode_text()
			hint = self.get_string("time_lapse_recording_mode")
			self.assertEqual(mode, hint)
			print("time_lapse_video recording mode text right")
		except AssertionError:
			print("time_lapse_video recording mode text wrong")
		try:
			time_span = time_lapse_video.time_span_text()
			hint = self.get_string("time_lapse_time_span")
			self.assertEqual(time_span, hint)
			print("time_lapse_video time span text right")
		except AssertionError:
			print("time_lapse_video time span text wrong")
		try:
			start_time = time_lapse_video.starting_time_text()
			hint = self.get_string("new_subscription_starting_time")
			self.assertEqual(start_time, hint)
			print("time_lapse_video start time text right")
		except AssertionError:
			print("time_lapse_video start time text wrong")
		try:
			entire_time = time_lapse_video.entire_time_text()
			hint = self.get_string("new_subscription_entire_time")
			self.assertEqual(entire_time, hint)
			print("time_lapse_video entire time text right")
		except AssertionError:
			print("time_lapse_video entire time text wrong")
		try:
			people_in_view = time_lapse_video.people_in_view_text()
			hint = self.get_string("new_subscription_people_in_view")
			self.assertEqual(people_in_view, hint)
			print("time_lapse_video people in view text right")
		except AssertionError:
			print("time_lapse_video people in view text wrong")
		try:
			twelve_hour = time_lapse_video.twelve_hours_text()
			hint = self.get_string("new_subscription_12_hours")
			self.assertEqual(twelve_hour, hint)
			print("time_lapse_video twelve hour text right")
		except AssertionError:
			print("time_lapse_video twelve hour text wrong")
		try:
			twenty_four_hour = time_lapse_video.twenty_four_hours_text()
			hint = self.get_string("new_subscription_24_hours")
			self.assertEqual(twenty_four_hour, hint)
			print("time_lapse_video twenty four hour text right")
		except AssertionError:
			print("time_lapse_video twenty four hour text wrong")
	def test_06_time_lapse_video_checkbox(self):
		time_lapse_video = TimeLapseVideoPage(self.driver)
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
		pixsee_settings_page.click_time_lapse_video()
		# ensure time lapse video switch is on
		if time_lapse_video.is_switch_on() == "true":
			pass
		else:
			time_lapse_video.click_switch()
		# check if checkbox is checked


		origin_status = pixsee_settings_page.pixsee_time_lapse_video_status_text()
		pixsee_settings_page.click_pixsee_time_lapse_video()
		time_lapse_video.click_switch()
		time_lapse_video.click_back()
		# check if is in discard dialog
		try:
			self.assertTrue(time_lapse_video.is_in_discard_dialog())
			print("In discard dialog")
			# check discard dialog text
			try:
				discard = time_lapse_video.discard_message_txt()
				hint = self.get_string("pixsee_time_lapse_video_popup_discard_changes")
				self.assertEqual(discard, hint)
				print("Discard dialog title right")
			except AssertionError:
				print("Discard dialog title wrong")
			try:
				yes = time_lapse_video.discard_yes_txt()
				hint = self.get_string("yes")
				self.assertEqual(yes, hint)
				print("Discard dialog yes text right")
			except AssertionError:
				print("Discard dialog yes text wrong")
			try:
				no = time_lapse_video.discard_no_txt()
				hint = self.get_string("no")
				self.assertEqual(no, hint)
				print("Discard dialog no text right")
			except AssertionError:
				print("Discard dialog no text wrong")
			# click yes
			time_lapse_video.click_discard_yes()
			new_status = pixsee_settings_page.pixsee_time_lapse_video_status_text()
			try:
				self.assertEqual(origin_status, new_status)
				print("Discard function success")
			except AssertionError:
				print("Discard function failed")
				raise AssertionError("Discard function failed, status changed")
		except AssertionError:
			print("Not in discard dialog")
			raise AssertionError("Not in discard dialog")



















