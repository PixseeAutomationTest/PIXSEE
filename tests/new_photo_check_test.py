

from pages.base import BaseTestCase
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.album_pages.photo_page import PhotoPage
from pages.menu_pages.menu_page import MenuPage
import time


class NewPhotoCheckCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)

	def test_new_photo_storaged(self):
		login_page = LoginPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		photo_page = PhotoPage(self.driver)
		menu_page = MenuPage(self.driver)

		login_page.login("amypixsee03@gmail.com", "@Aa12345")
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()
		# ensure is connected to machine
		baby_monitor_page = BabyMonitorPage(self.driver)
		if not baby_monitor_page.is_connected():
			self.skipTest("not online，skip all test")

		baby_monitor_page.click_home()
		# skip menu tutor
		time.sleep(1)

		menu_page.click_logout()
		menu_page.click_album()
		photo_page.click_iknow_button()
		self.click_middle()
		print("finish login photo")
		time.sleep(5)

		# 獲取原本的照片數量
		origin = photo_page.count_photos_today()


		photo_page.click_back_button()
		# self.right_wipe()
		baby_monitor_page.click_home()
		# 拍攝新照片
		baby_monitor_page.click_capture()
		print("filming new photo")

		# 等待一段時間，確保有新照片被拍攝
		time.sleep(5)
		baby_monitor_page.click_home()
		menu_page.click_album()
		time.sleep(5)
		after = photo_page.count_photos_today()
		if after == origin + 1:
			print(f"new photo storage success origin amount: {origin}, current amount: {after}")
		else:
			raise AssertionError(f"failed origin amount: {origin}, current amount: {after}")



