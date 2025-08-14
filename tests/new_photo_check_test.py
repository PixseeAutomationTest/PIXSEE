

from pages.base import BaseTestCase
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.album_pages.photo_page import PhotoPage
from pages.menu_pages.menu_page import MenuPage
import time


class NewPhotoCheckCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=True)
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
	def test_new_photo_storaged(self):
		baby_monitor_page = BabyMonitorPage(self.driver)
		photo_page = PhotoPage(self.driver)
		menu_page = MenuPage(self.driver)

		time.sleep(5)

		# Get origin photo amount
		origin = photo_page.count_photos_today()


		# photo_page.click_back_button()
		self.go_back()
		# self.right_wipe()
		baby_monitor_page.click_home()
		# get new photo
		baby_monitor_page.click_capture()
		print("filming new photo")

		# get new amount of photo
		time.sleep(5)
		baby_monitor_page.click_home()
		menu_page.click_album()
		time.sleep(9)
		after = photo_page.count_photos_today()
		if after == origin + 1:
			print(f"new photo storage success origin amount: {origin}, current amount: {after}")
		else:
			raise AssertionError(f"failed origin amount: {origin}, current amount: {after}")



