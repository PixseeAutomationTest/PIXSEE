from pages.menu_page import MenuPage
from pages.setting.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.setting.pixsee_friends_det_page import PixseeFriendsDetPage





class PixseeFriendsDetTest(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=True)

	def test_save_function(self):
		menu_page = MenuPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_friends_page = PixseeFriendsDetPage(self.driver)

		self.open_app()
		baby_monitor_page.click_home()
		menu_page.click_settings()
		# check friends detection title on settings page
		try:
			hint = self.get_string("pixsee_settings_menu_pixsee_friends_detection_title_menu")
			self.assertEqual(pixsee_settings_page.pixsee_friends_detection_text(), hint)
			print("Friends detection title right")
		except AssertionError:
			print("Friends detection title wrong")
			raise AssertionError("Friends detection title mismatch")

		pixsee_settings_page.click_PixseeFriendsDetection()
		# check if is in friends detection page
		try:
			self.assertTrue(pixsee_friends_page.is_in_pixsee_friends_det_page())

			print("In Pixsee Friends Detection page")
		except AssertionError:
			print("Not in Pixsee Friends Detection page")
			raise AssertionError("Not in Pixsee Friends Detection page")
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
			desc = pixsee_friends_page.description()
			hint = self.get_string("pixsee_friends_detection_subtitle")
			self.assertEqual(desc, hint)
			print("Friends detection description right")
		except AssertionError:
			print("Friends detection description wrong")
			raise AssertionError("Friends detection description mismatch")
		# check friends detection subtitle
		try:
			subtitle = pixsee_friends_page.description_subtitle()
			hint = self.get_string("pixsee_friends_detection_subtitle")
			self.assertEqual(subtitle, hint)
			print("Friends detection subtitle right")
		except AssertionError:
			print("Friends detection subtitle wrong")
			raise AssertionError("Friends detection subtitle mismatch")

		pixsee_friends_page.click_switch()
		# check switch is on
		try:
			self.assertTrue(pixsee_friends_page.is_switch_on())
			print("Friends detection switch is on")
		except AssertionError:
			print("Friends detection switch is off")
			raise AssertionError("Friends detection switch is off")