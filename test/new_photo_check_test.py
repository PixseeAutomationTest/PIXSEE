

from pages.base import BaseTestCase
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
from pages.photo_page import PhotoPage
from pages.menu_page import MenuPage
import time
import datetime

class NewPhotoCheckCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)

	def test_new_photo_storaged(self):
		login_page = LoginPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		photo_page = PhotoPage(self.driver)
		menu_page = MenuPage(self.driver)

		login_page.login("amypixsee02@gmail.com", "@Aa12345")



		for i in range(4):
			baby_monitor_page.get_tutor_description()
			self.click_middle()
			time.sleep(1)

		time.sleep(5)
		baby_monitor_page.click_home()
		self.click_middle()
		menu_page.click_album()
		photo_page.click_iknow_button()
		self.click_middle()
		print("finish login photo")

		# 獲取原本的照片數量
		origin = photo_page.count_photos_today()
		print(f"原本共有{origin}張照片")

		# photo_page.click_back_button()
		time.sleep(3)
		self.right_wipe()
		baby_monitor_page.click_home()
		# 拍攝新照片
		baby_monitor_page.click_capture()
		print("正在拍照")

		# 等待一段時間，確保有新照片被拍攝
		time.sleep(5)
		baby_monitor_page.click_home()
		menu_page.click_album()
		after = photo_page.count_photos_today()
		print(f"現在共有{after}張照片")




