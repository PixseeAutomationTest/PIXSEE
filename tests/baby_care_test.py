
from base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.baby_care_page import BabyCarePage
import time



class BabyCareCase(BaseTestCase):
	def __init__(self, methodName='runTest', language="zh", locale="TW"):
		super().__init__(methodName)
		self.language = language
		self.locale = locale

	def setUp(self):
		super().setUp(language=self.language, locale=self.locale)

		baby_monitor_page = BabyMonitorPage(self.driver)
		try:
			while self.driver.current_package != self.driver.capabilities.get("appPackage"):
				self.driver.terminate_app(self.driver.current_package)
				self.open_app()
			if baby_monitor_page.is_in_baby_monitor_page():
				return
			elif not baby_monitor_page.is_in_baby_monitor_page():
				self.shutdown_app()
				self.open_app()
			print("Finish opening app.")
		except Exception as e:
			print(f"Test failed with exception: {e}")
			raise e
	# start from the baby monitor page
	def test_baby_care_text(self):
		baby_monitor_page = BabyMonitorPage(self.driver)
		baby_care_page = BabyCarePage(self.driver)

		self.up_scroll()
		# check if the text is correct
		try:
			header = baby_care_page.header_text()
			hint = self.get_string("baby_care")
			self.assertEqual(header, hint)
			print("Header is correct")
		except AssertionError:
			raise AssertionError("Header is wrong")
		try:
			title = baby_care_page.title()
			hint = self.get_string("baby_care_cry_tips_title")
			self.assertEqual(title, hint)
			print("Title is correct")
		except AssertionError:
			raise AssertionError("Title is wrong")
		try:
			hungry_title = baby_care_page.cry_tip_title()
			hint = self.get_string("hungry_tip_title")
			self.assertEqual(hungry_title, hint)
			print("hungry title is correct")
		except AssertionError:
			raise AssertionError("hungry title is wrong")
		try:
			hungry_preview = baby_care_page.cry_tip_preview()
			hint = self.get_string("hungry_tip_text")
			self.assertEqual(hungry_preview, hint)
			print("hungry preview is correct")
		except AssertionError:
			raise AssertionError("hungry preview is wrong")
		self.left_wipe()
		time.sleep(1)
		try:
			sleepy_title = baby_care_page.cry_tip_title()
			hint = self.get_string("sleepy_tip_title")
			self.assertEqual(sleepy_title, hint)
			print("sleepy title is correct")
		except AssertionError:
			raise AssertionError("sleepy title is wrong")
		try:
			sleepy_preview = baby_care_page.cry_tip_preview()
			hint = self.get_string("sleepy_tip_text").replace("\\n", "\n")
			self.assertEqual(sleepy_preview, hint)
			print("sleepy preview is correct")
		except AssertionError:
			raise AssertionError("sleepy preview is wrong")
		self.left_wipe()
		time.sleep(1)
		try:
			unwell_title = baby_care_page.cry_tip_title()
			hint = self.get_string("uncomfortable_tip_title")
			self.assertEqual(unwell_title, hint)
			print("unwell title is correct")
		except AssertionError:
			raise AssertionError("unwell title is wrong")
		try:
			unwell_preview = baby_care_page.cry_tip_preview()
			hint = self.get_string("uncomfortable_tip_text").replace("\\n", "\n")
			self.assertEqual(unwell_preview, hint)
			print("unwell preview is correct")
		except AssertionError:
			raise AssertionError("unwell preview is wrong")
		self.left_wipe()
		time.sleep(1)
		try:
			dirty_diaper_title = baby_care_page.cry_tip_title()
			hint = self.get_string("dirty_diaper_tip_title")
			self.assertEqual(dirty_diaper_title, hint)
			print("dirty diaper title is correct")
		except AssertionError:
			raise AssertionError("dirty diaper title is wrong")
		try:
			dirty_diaper_preview = baby_care_page.cry_tip_preview()
			hint = self.get_string("dirty_diaper_tip_text").replace("\\n", "\n")
			self.assertEqual(dirty_diaper_preview, hint)
			print("dirty diaper preview is correct")
		except AssertionError:
			raise AssertionError("dirty diaper preview is wrong")
		self.left_wipe()
		time.sleep(1)
		try:
			colic_title = baby_care_page.cry_tip_title()
			hint = self.get_string("colic_tip_title")
			self.assertEqual(colic_title, hint)
			print("colic title is correct")
		except AssertionError:
			raise AssertionError("colic title is wrong")
		try:
			colic_preview = baby_care_page.cry_tip_preview()
			hint = self.get_string("colic_tip_text").replace("\\n", "\n")
			self.assertEqual(colic_preview, hint)
			print("colic preview is correct")
		except AssertionError:
			raise AssertionError("colic preview is wrong")
		self.left_wipe()
		time.sleep(1)
		try:
			pain_title = baby_care_page.cry_tip_title()
			hint = self.get_string("pain_tip_title")
			self.assertEqual(pain_title, hint)
			print("pain title is correct")
		except AssertionError:
			raise AssertionError("pain title is wrong")
		try:
			pain_preview = baby_care_page.cry_tip_preview()
			hint = self.get_string("pain_tip_text").replace("\\n", "\n")
			self.assertEqual(pain_preview, hint)
			print("pain preview is correct")
		except AssertionError:
			raise AssertionError("pain preview is wrong")
		self.left_wipe()
		time.sleep(1)
		try:
			clothing_title = baby_care_page.cry_tip_title()
			hint = self.get_string("temperature_tip_title")
			self.assertEqual(clothing_title, hint)
			print("clothing title is correct")
		except AssertionError:
			raise AssertionError("clothing title is wrong")
		try:
			clothing_preview = baby_care_page.cry_tip_preview()
			hint = self.get_string("temperature_tip_text").replace("\\n", "\n")
			self.assertEqual(clothing_preview, hint)
			print("clothing preview is correct")
		except AssertionError:
			raise AssertionError("clothing preview is wrong")
		self.down_scroll()

