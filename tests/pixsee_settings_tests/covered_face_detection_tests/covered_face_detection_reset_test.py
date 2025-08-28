from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.covered_face_detection_page import CoveredFaceDetectionPage


class CoveredFaceDetectionCase1(BaseTestCase):
	def __init__(self, methodName='runTest', language="zh", locale="TW"):
		super().__init__(methodName)
		self.language = language
		self.locale = locale

	def setUp(self):
		super().setUp(language=self.language, locale=self.locale, no_reset=False)

	def test_01_covered_face_detection_tutor_skip(self):
		covered_face_detection_page = CoveredFaceDetectionPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		self.skip_first_four_tutor()
		# ensure is connected to machine
		baby_monitor_page = BabyMonitorPage(self.driver)
		if not baby_monitor_page.is_connected():
			self.skipTest("not online，skip all test")

		baby_monitor_page.click_home()
		# skip menu tutor
		menu_page.click_logout()

		menu_page.click_settings()

		pixsee_settings_page.click_covered_face_detection()
		# check first tutor title
		try:
			title = covered_face_detection_page.tutor_title_text()
			hint = self.get_string("covered_face")
			self.assertEqual(title, hint)
			print("tutor title right")
		except AssertionError :
			raise AssertionError("tutor title wrong")
		# check skip
		try:
			skip = covered_face_detection_page.skip_text()
			hint = self.get_string("skip")
			self.assertEqual(skip, hint)
			print("skip display right")
		except AssertionError :
			raise AssertionError("skip display wrong")
		covered_face_detection_page.click_skip()
		# check in covered_face_detection_page
		try:
			self.assertTrue(covered_face_detection_page.is_in_covered_face_detection_page())
			print("skip tutor successfully")
		except AssertionError :
			raise AssertionError("skip tutor unsuccessfully")