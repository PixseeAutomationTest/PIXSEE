import re

from base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.album_pages.album_page import AlbumPage
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.album_pages.photo_page import PhotoPage
import time


class AlbumCase(BaseTestCase):
	@classmethod
	def setUpClass(cls):
		cls.language = getattr(cls, "language", "zh")
		cls.locale = getattr(cls, "locale", "TW")
		super().setUpClass()

	def setUp(self):
		super().setUp()
		baby_monitor_page = BabyMonitorPage(self.driver)
		menu_page = MenuPage(self.driver)
		album_page = AlbumPage(self.driver)
		try:
			while self.driver.current_package != self.driver.capabilities.get("appPackage"):
				self.driver.terminate_app(self.driver.current_package)
				self.open_app()
			if album_page.is_in_album_page():
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
		album_page = AlbumPage(self.driver)
		menu_page = MenuPage(self.driver)

		# Get origin photo amount
		origin = album_page.count_photos_today()

		# album_page.click_back_button()
		self.go_back()
		# self.right_wipe()
		baby_monitor_page.click_home()
		time.sleep(1)
		# get new photo
		baby_monitor_page.click_capture()
		self.assertTrue(baby_monitor_page.finish_uploading(), " photo upload failed")

		# get new amount of photo
		baby_monitor_page.click_home()
		menu_page.click_album()
		time.sleep(9)
		after = album_page.count_photos_today()
		if after == origin + 1:
			print(f"new photo storage success origin amount: {origin}, current amount: {after}")
		else:
			raise AssertionError(f"failed origin amount: {origin} not equal to current amount: {after} +1")

	def test_02_slide_button(self):
		album_page = AlbumPage(self.driver)
		# click photo button
		album_page.click_plus_button()
		album_page.click_slide_button()
		time.sleep(1)
		try:
			self.assertTrue(album_page.is_in_dialog(), "click slide button click failed, not in dialog")
			# check text
			self.assertEqual(self.get_string("slideshow_subscription_info"), album_page.dialog_text(),
							 "need to subscribe dialog text is wrong")
			self.assertEqual(self.get_string("subscription_go_to_subscription"), album_page.dialog_yes_text(),
							 "need to subscribe dialog yes text is wrong")
			self.assertEqual(self.get_string("no_thanks_action"), album_page.dialog_no_text(), "need to subscribe dialog no text is wrong")
			# click no
			album_page.click_dialog_no()
		except:
			pass

	def test_03_select_day_and_check_photo(self):
		album_page = AlbumPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)


		album_page.select_baby_birthday(self.locale, 2025, 8, 30)
		album_page.find_date_range("2025/08/30")

	def test_04_select_photo(self):
		album_page = AlbumPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)

		# check if the header change after clicking the select button
		album_page.click_select_button()
		self.assertEqual(self.get_string("x_items_selected_empty"), album_page.header_text(), "header text is wrong after clicking select button")
		self.assertEqual(self.get_string("cancel"), album_page.select_cancel_text(), "cancel text is wrong after clicking select button")
		# click cancel check if we quit the select mode
		album_page.click_select_cancel()
		self.assertEqual(self.get_string("daily_cover_gallery_album"), album_page.header_text(), "header text is wrong after clicking cancel button")
		# click select button again
		album_page.click_select_button()
		# select one photo
		album_page.click_recent_thumbnails(1)
		self.assertEqual(self.get_string("x_items_selected_plural[one]").replace("%s", "1"), album_page.header_text(), "header text is wrong after selecting one photo")
		album_page.click_select_cancel()
		# click select button again
		album_page.click_select_button()
		# select another photo
		album_page.click_recent_thumbnails(2)
		self.assertEqual(self.get_string("x_items_selected_plural[other]").replace("%s", "2"), album_page.header_text(), "header text is wrong after selecting two photos")
		album_page.click_select_cancel()

	def test_05_check_select_detail(self):
		album_page = AlbumPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		photo_page = PhotoPage(self.driver)

		# check if the header change after clicking the select button
		album_page.click_select_button()
		# check four buttons are not able to click
		try:
			self.assertFalse(album_page.is_garbage_enabled(), "garbage button is able to click in select mode with no photo selected")
			self.assertFalse(album_page.is_download_enabled(), "download button is able to click in select mode with no photo selected")
			self.assertFalse(album_page.is_share_enabled(), "share button is able to click in select mode with no photo selected")
			self.assertFalse(album_page.is_visible_enabled(), "visible button is able to click in select mode with no photo selected")
		except AssertionError as e:
			print(e)
			raise e
		# click download button assume we want to download 4 photos
		album_page.click_recent_thumbnails(4)
		album_page.click_download_button()
		self.assertEqual(self.get_string("downloaded"), album_page.download_success_text(), "toast text is wrong after downloading photo")
		# click share button assume we want to share 1 photo
		album_page.click_select_button()
		album_page.click_recent_thumbnails(1)
		album_page.click_share_button()
		self.assertTrue(album_page.is_chooser_appeared(), "share chooser not appear after clicking share button")
		self.go_back()
		# click hidden assume we want to hide 4 photos
		hide_number = 4
		album_page.click_select_button()
		album_page.click_recent_thumbnails(hide_number)
		album_page.click_visible_button()
		self.assertTrue(album_page.numbers_of_photo_hidden() >= hide_number, "photo not hidden after clicking visible button")
		for i in range(hide_number):
			album_page.click_specific_thumbnail(i)
			photo_page.click_eye()
			self.go_back()
		# delete function assume we want to delete 6th photo
		delete_photo_number = 5
		album_page.click_select_button()
		album_page.click_specific_thumbnail(delete_photo_number)
		album_page.click_garbage_button()
		self.assertTrue(album_page.is_in_dialog(), "click garbage button click failed, not in dialog")
		self.assertEqual(self.get_string("delete_confirm"), album_page.dialog_text(), "delete dialog text is wrong")
		self.assertEqual(self.get_string("delete"), album_page.dialog_yes_text(), "delete dialog yes text is wrong")
		self.assertEqual(self.get_string("cancel"), album_page.dialog_no_text(), "delete dialog no text is wrong")
		album_page.click_dialog_no()
		self.assertTrue(album_page.is_in_select_mode(), "click no button click failed, not in select mode")
		album_page.click_specific_thumbnail(delete_photo_number)
		# delete 6th photo
		album_page.delete_and_verify_thumbnail(delete_photo_number)

	def test_06_check_photo_detail(self):
		album_page = AlbumPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		photo_page = PhotoPage(self.driver)

		album_page.click_specific_thumbnail(5)
		self.assertTrue(photo_page.is_in_photo_page(), "click photo button click failed, not in photo page")
		# check four properties
		photo_page.click_share()
		self.assertTrue(album_page.is_chooser_appeared(), "share chooser not appear after clicking share button")
		self.go_back()

		photo_page.click_trash()
		self.assertEqual(self.get_string("delete_confirm"), photo_page.get_dialog_text(), "delete dialog text is wrong")
		self.assertEqual(self.get_string("delete"), photo_page.dialog_delete_text(), "delete dialog yes text is wrong")
		self.assertEqual(self.get_string("cancel"), photo_page.dialog_cancel_text(), "delete dialog no text is wrong")
		photo_page.click_dialog_cancel()
		self.assertTrue(photo_page.is_in_photo_page(), "click cancel button click failed, not in photo page")

		photo_page.click_note()
		# check diary
		self.assertEqual(self.get_string("note"), photo_page.get_diary_head(), "note title text is wrong")
		self.assertEqual(self.get_string("media_note_field_hint"), photo_page.note_input_hint(), "note input hint text is wrong")
		self.assertEqual(self.get_string("done"), photo_page.complete_button_text(), "note complete button text is wrong")
		try:
			character = photo_page.get_chart_count()
			hint = self.get_string("media_note_char_count")
			pattern = "^" + re.escape(hint).replace("%d", r".+") + "$"
			self.assertRegex(character, pattern)
		except Exception as e:
			print(f"Character count test failed: {e}")
			raise e
		# check original character count is 1000
		number = photo_page.find_numbers_in_text(photo_page.get_chart_count())
		self.assertTrue(number == 1000, "initial character count is wrong, should be 1000")
		photo_page.input_note("office romance is forbidden")
		photo_page.click_complete()
		# check the word we just input showed correctly
		self.assertEqual("office romance is forbidden", photo_page.get_note_text(), "note text is wrong")
		photo_page.click_note()
		# check the count after input
		number_after = photo_page.find_numbers_in_text(photo_page.get_chart_count())
		self.assertTrue(number_after == 1000 - len("office romance is forbidden"), "character count after input is wrong")
		photo_page.input_note("")
		photo_page.click_complete()
		self.go_back()
	def test_07_back(self):
		album_page = AlbumPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)

		self.assertEqual(self.get_string("daily_cover_gallery_album"), album_page.header_text(), "not in photo page, header text is wrong")

		# click back button
		album_page.click_back_button()
		self.assertTrue(menu_page.is_in_menu_page(), "back button click failed, not in menu page")
		menu_page.click_home()


# time.sleep(1)
# self.assertFalse(album_page.is_in_album_page(), "photo button click failed, still in photo page")



