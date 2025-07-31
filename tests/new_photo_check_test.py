

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

		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		photo_page = PhotoPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()

		menu_page.click_album()
		photo_page.click_iknow_button()
		self.click_middle()
		print("finish login photo")

		# 獲取原本的照片數量
		origin = photo_page.count_photos_today()
		print(f"原本共有{origin}張照片")

		time.sleep(3)
		photo_page.click_back_button()
		menu_page.click_home()
		# 拍攝新照片
		baby_monitor_page.click_capture()
		print("正在拍照")

		# 等待一段時間，確保有新照片被拍攝
		time.sleep(5)
		self.assertTrue(baby_monitor_page.has_photo_upload_dialog(), "沒有出現照片上傳對話框")
		time.sleep(5)
		baby_monitor_page.click_home()
		menu_page.click_album()
		after = photo_page.count_photos_today()
		print(f"現在共有{after}張照片")




