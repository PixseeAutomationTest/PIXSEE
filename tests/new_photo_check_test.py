

from pages.base import BaseTestCase
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.album_pages.photo_page import PhotoPage
from pages.menu_pages.menu_page import MenuPage
import time


class NewPhotoCheckCase(BaseTestCase):
	@classmethod
	def setUpClass(cls):
		cls.language = getattr(cls, "language", "zh")
		cls.locale = getattr(cls, "locale", "TW")
		super().setUpClass()

	def setUp(self):
		super().setUp()
		baby_monitor_page = BabyMonitorPage(self.driver)
		menu_page = MenuPage(self.driver)
		photo_page = PhotoPage(self.driver)
		try:
			while self.driver.current_package != self.driver.capabilities.get("appPackage"):
				self.driver.terminate_app(self.driver.current_package)
				self.open_app()
			if photo_page.is_in_photo_page():
				return
			elif not baby_monitor_page.is_in_baby_monitor_page():
				self.shutdown_app()
				self.open_app()
			print("Finish opening app.")
			baby_monitor_page.click_home()
			menu_page.click_album()
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e
	def test_01_new_photo_storaged(self):
		baby_monitor_page = BabyMonitorPage(self.driver)
		photo_page = PhotoPage(self.driver)
		menu_page = MenuPage(self.driver)


		# Get origin photo amount
		origin = photo_page.count_photos_today()


		# photo_page.click_back_button()
		self.go_back()
		# self.right_wipe()
		baby_monitor_page.click_home()
		# get new photo
		baby_monitor_page.click_capture()
		self.assertTrue(baby_monitor_page.finish_uploading()," photo upload failed")




		# get new amount of photo
		baby_monitor_page.click_home()
		menu_page.click_album()
		time.sleep(9)
		after = photo_page.count_photos_today()
		if after == origin + 1:
			print(f"new photo storage success origin amount: {origin}, current amount: {after}")
		else:
			raise AssertionError(f"failed origin amount: {origin}, current amount: {after}")
	def test_02_photo_button(self):
		photo_page = PhotoPage(self.driver)
		# click photo button
		photo_page.click_plus_button()
		photo_page.click_slide_button()
		time.sleep(1)
		self.assertTrue(photo_page.is_in_dialog(), "photo button click failed, not in dialog")
		# check text
		self.assertEqual(self.get_string("slideshow_subscription_info"),photo_page.dialog_text(), "dialog text is wrong")
		self.assertEqual(self.get_string("subscription_go_to_subscription"), photo_page.dialog_yes_text(), "dialog yes text is wrong")
		self.assertEqual(self.get_string("no_thanks_action"), photo_page.dialog_no_text(), "dialog no text is wrong")
		# click no
		photo_page.click_dialog_no()
		# time.sleep(1)
		# self.assertFalse(photo_page.is_in_photo_page(), "photo button click failed, still in photo page")



