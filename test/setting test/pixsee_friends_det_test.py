from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from pages.menu_page import MenuPage
from pages.setting.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.setting.pixsee_friends_det_page import PixseeFriendsDetPage





class PixseeFriendsDetTest(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)


	def test_01_enter_page(self):
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		# check friends detection title on settings page
		try:
			hint = self.get_string("pixsee_settings_menu_pixsee_friends_detection_title_menu")
			self.assertEqual(pixsee_settings_page.pixsee_friends_detection_text(), hint)
			print("Friends detection title right")
		except AssertionError:
			print("Friends detection title wrong")
			raise AssertionError("Friends detection title mismatch")
		# enter friends detection page
		pixsee_settings_page.click_PixseeFriendsDetection()

		# check if is in friends detection page
		try:
			self.assertTrue(pixsee_friends_page.is_in_pixsee_friends_det_page())
			print("In Pixsee Friends Detection page")
		except AssertionError:
			print("Not in Pixsee Friends Detection page")
			raise AssertionError("Not in Pixsee Friends Detection page")
	def test_02_friends_detection_switch(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")
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


			# pixsee_friends_page.click_switch()
			# try:
			# 	dettype = pixsee_friends_page.dettype()
			# 	hint = self.get_string("efence_type_detection")
			# 	self.assertEqual(dettype, hint)
			# 	print("Friends detection type is correct")
			# except AssertionError:
			# 	print("Friends detection type is wrong")
			# 	raise AssertionError("detection doesn't show up after switch on")





		# check switch is on
		try:
			self.assertTrue(pixsee_friends_page.is_switch_on())
			print("Friends detection switch is on")
		except AssertionError:
			print("Friends detection switch is off")
			raise AssertionError("Friends detection switch is off")
	def test_03_friends_detection_save(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")
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

	def test_04_friends_detection_tap_on(self):
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")
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
		# check text
		try:
			time_span = pixsee_friends_page.time_span()
			hint = self.get_string("time_lapse_time_span")
			self.assertEqual(time_span, hint)
			print("Friends detection time span title right")
		except AssertionError:
			print("Friends detection time span title wrong")
			raise AssertionError("Friends detection time span title mismatch")
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
		self.tap_on_visibility(pixsee_friends_page.SetTime, "Set Time",True)
		pixsee_friends_page.click_all_day()
		self.tap_on_visibility(pixsee_friends_page.AllDay, "All Day", False)













# def test_03_friends_detection_switch_off(self):