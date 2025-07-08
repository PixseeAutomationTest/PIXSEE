

from pages.base import BaseTestCase
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
from pages.photo_page import PhotoPage
from pages.menu_page import MenuPage
import time

class NewPhotoCheckTest(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)

	def test_new_photo_storaged(self):
		login_page = LoginPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		photo_page = PhotoPage(self.driver)
		menu_page = MenuPage(self.driver)

		login_page.login("amypixsee02@gmail.com", "@Aa12345")
		try:
			self.assertTrue(baby_monitor_page.is_in_baby_monitor_page())
			print("login sucess")
		except:
			print("login fail")


		for i in range(4):
			self.click_middle()
			time.sleep(0.5)

		baby_monitor_page.click_home()
		self.click_middle()
		menu_page.click_album()
		self.click_middle()
		time.sleep(3)