from pages.base import BaseTestCase
import unittest
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.menu_page import MenuPage
from pages.baby_timeline_page import BabyTimelinePage
from pages.menu_pages.album_pages.photo_page import PhotoPage
from pages.camera_pages.camera_main_page import CameraMainPage
import time


class TutorCase(BaseTestCase):
        def __init__(self, methodName='runTest', language="en", locale="US"):
                super().__init__(methodName)
                self.language = language
                self.locale = locale

        def setUp(self):
                super().setUp(language=self.language, locale=self.locale)
                self.tutor_id = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
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
        def test_01_skip_first_four_tutor(self):
                baby_monitor_page = BabyMonitorPage(self.driver)

                # check title and description of first three tutor
                try:
                        timer_title = baby_monitor_page.get_tutor_title()
                        hint = self.get_string("capture_timer_mode_description_title")
                        self.assertEqual(timer_title, hint)
                        print("First tutor success")
                except AssertionError:
                        raise AssertionError("First tutor FAIL: text mismatch")
                try:
                        timer_description = baby_monitor_page.get_tutor_description()
                        hint = self.get_string("capture_timer_mode_description").replace("\\n","\n")
                        self.assertEqual(timer_description, hint)
                        print("First tutor description success")
                except AssertionError:
                        raise AssertionError("First tutor description FAIL: text mismatch")
                self.click_middle()
                try:
                        baby_bubble_title = baby_monitor_page.get_tutor_title()
                        hint = self.get_string("baby_timeline_description_title")
                        self.assertEqual(baby_bubble_title, hint)
                        print("Second tutor success")
                except AssertionError:
                        raise AssertionError("Second tutor FAIL: text mismatch")
                try:
                        baby_bubble_description = baby_monitor_page.get_tutor_description()
                        hint = self.get_string("baby_timeline_description")
                        self.assertEqual(baby_bubble_description, hint)
                        print("Second tutor description success")
                except AssertionError:
                        raise AssertionError("Second tutor description FAIL: text mismatch")
                self.click_middle()
                try:
                        sleep_mode_title = baby_monitor_page.get_tutor_title()
                        hint = self.get_string("sleep_mode_title")
                        self.assertEqual(sleep_mode_title, hint)
                        print("Third tutor success")
                except AssertionError:
                        raise AssertionError("Third tutor FAIL: text mismatch")
                try:
                        sleep_mode_description = baby_monitor_page.get_tutor_description()
                        hint = self.get_string("sleep_mode_description")
                        self.assertEqual(sleep_mode_description, hint)
                        print("Third tutor description success")
                except AssertionError:
                        raise AssertionError("Third tutor description FAIL: text mismatch")
                self.click_middle()
                try:
                        two_way_talk_title = baby_monitor_page.get_tutor_title()
                        hint = self.get_string("two_way_talk_title")
                        self.assertEqual(two_way_talk_title, hint)
                        print("Fourth tutor success")
                except AssertionError:
                        raise AssertionError("Fourth tutor FAIL: text mismatch")
                try:
                        two_way_talk_description = baby_monitor_page.get_tutor_description()
                        hint = self.get_string("two_way_talk_description")
                        self.assertEqual(two_way_talk_description, hint)
                        print("Fourth tutor description success")
                except AssertionError:
                        raise AssertionError("Fourth tutor description FAIL: text mismatch")
                self.click_middle()
        def test_02_menu_tutor(self):
                baby_monitor_page = BabyMonitorPage(self.driver)
                menu_page = MenuPage(self.driver)

                baby_monitor_page.click_home()
                try:
                        pixsee_friends_title = baby_monitor_page.get_tutor_title()
                        hint = self.get_string("menu_title_doll")
                        self.assertEqual(pixsee_friends_title, hint)
                        print("Pixsee Friends tutor title success")
                except AssertionError:
                        raise AssertionError("Pixsee Friends tutor title FAIL: text mismatch")
                try:
                        pixsee_friends_description = baby_monitor_page.get_tutor_description()
                        hint = self.get_string("doll_first_tip")
                        self.assertEqual(pixsee_friends_description, hint)
                        print("Pixsee Friends tutor description success")
                except AssertionError:
                        raise AssertionError("Pixsee Friends tutor description FAIL: text mismatch")
                menu_page.click_logout()
                baby_monitor_page.click_home()
        def test_03_tree_tutor(self):
                baby_monitor_page = BabyMonitorPage(self.driver)
                baby_timeline_page = BabyTimelinePage(self.driver)

                self.down_scroll()
                try:
                        tree_title = baby_timeline_page.get_tutor_title()
                        hint = self.get_string("special_card_description_title")
                        self.assertEqual(tree_title, hint)
                        print("Tree tutor title success")
                except AssertionError:
                        raise AssertionError("Tree tutor title FAIL: text mismatch")
                try:
                        tree_description = baby_timeline_page.get_tutor_description()
                        hint = self.get_string("special_card_description").replace("\\n"," ")
                        self.assertEqual(tree_description, hint)
                        print("Tree tutor description success")
                except AssertionError:
                        raise AssertionError("Tree tutor description FAIL: text mismatch")
                self.click_middle()
                baby_timeline_page.click_home()
        def test_04_album_tutor(self):
                baby_monitor_page = BabyMonitorPage(self.driver)
                menu_page = MenuPage(self.driver)
                photo_page = PhotoPage(self.driver)

                baby_monitor_page.click_home()

                menu_page.click_album()
                try:
                        album_title = photo_page.new_function_title()
                        hint = self.get_string("slideshow_whats_new").replace("\\", "")
                        self.assertEqual(album_title, hint)
                        print("new function title success")
                except AssertionError:
                        raise AssertionError("new function title FAIL: text mismatch")
                try:
                        album_description = photo_page.new_function_msg()
                        hint = self.get_string("slideshow_whats_new_info")
                        self.assertEqual(album_description, hint)
                        print("new function message description success")
                except AssertionError:
                        raise AssertionError("new function message FAIL: text mismatch")
                try:
                        iknow_button_text = photo_page.iknow_button_text()
                        hint = self.get_string("slideshow_i_got_it")
                        self.assertEqual(iknow_button_text, hint)
                        print("I know button text success")
                except AssertionError:
                        raise AssertionError("I know button text FAIL: text mismatch")
                photo_page.click_iknow_button()
                try:
                        view_tutor_title = photo_page.tutor_title()
                        hint = self.get_string("first_tip_preview_photo_title")
                        self.assertEqual(view_tutor_title, hint)
                        print("View tutor title success")
                except AssertionError:
                        raise AssertionError("View tutor title FAIL: text mismatch")
                try:
                        view_tutor_description = photo_page.tutor_description()
                        hint = self.get_string("first_tip_preview_photo_info")
                        self.assertEqual(view_tutor_description, hint)
                        print("View tutor description success")
                except AssertionError:
                        raise AssertionError("View tutor description FAIL: text mismatch")
                self.click_middle()
                photo_page.click_plus_button()
                time.sleep(1)
                try:
                        create_tutor_title = photo_page.tutor_title()
                        hint = self.get_string("first_tip_create_slideshow_title")
                        self.assertEqual(create_tutor_title, hint)
                        print("Create tutor title success")
                except AssertionError:
                        raise AssertionError("Create tutor title FAIL: text mismatch")
                try:
                        create_tutor_description = photo_page.tutor_description()
                        hint = self.get_string("first_tip_create_slideshow_info")
                        self.assertEqual(create_tutor_description, hint)
                        print("Create tutor description success")
                except AssertionError:
                        raise AssertionError("Create tutor description FAIL: text mismatch")
                self.click_middle()
                photo_page.click_plus_button()
                self.go_back()
                baby_monitor_page.click_home()
        def test_05_camera_tutor(self):
                baby_monitor_page = BabyMonitorPage(self.driver)
                camera_main_page = CameraMainPage(self.driver)

                baby_monitor_page.click_middle()
                self.click_middle()
                try:
                        camera_tutor_title = camera_main_page.tutor_title()
                        hint = self.get_string("playback_first_tip_playback_title")
                        self.assertEqual(camera_tutor_title, hint)
                        print("Camera tutor title success")
                except AssertionError:
                        raise AssertionError("Camera tutor title FAIL: text mismatch")
                try:
                        camera_tutor_description = camera_main_page.tutor_description()
                        hint = self.get_string("playback_first_tip_playback_description")
                        self.assertEqual(camera_tutor_description, hint)
                        print("Camera tutor description success")
                except AssertionError:
                        raise AssertionError("Camera tutor description FAIL: text mismatch")
                self.click_middle()
                camera_main_page.click_home()


















if __name__ == "__main__":
    unittest.main()