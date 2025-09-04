from base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.menu_page import MenuPage
from pages.baby_timeline_page import BabyTimelinePage
from pages.menu_pages.album_pages.album_page import AlbumPage
from pages.camera_pages.camera_main_page import CameraMainPage
from pages.camera_pages.play_back_page import PlayBackPage
import time


class TutorCase(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = getattr(cls, "language", "zh")
        cls.locale = getattr(cls, "locale", "TW")
        super().setUpClass()
    # start from babymonitor page
    def setUp(self):
            super().setUp()
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
            errors = []
            # check title and description of first three tutor
            try:
                    timer_title = baby_monitor_page.get_tutor_title()
                    hint = self.get_string("capture_timer_mode_description_title")
                    self.assertEqual(timer_title, hint)
                    print("First tutor success")
            except AssertionError as e:
                    print("First tutor FAIL: text mismatch")
                    errors.append(e)
            try:
                    timer_description = baby_monitor_page.get_tutor_description()
                    hint = self.get_string("capture_timer_mode_description").replace("\\n", "\n")
                    self.assertEqual(timer_description, hint)
                    print("First tutor description success")
            except AssertionError as e:
                    print("First tutor description FAIL: text mismatch")
                    errors.append(e)
            self.click_middle()
            try:
                    baby_bubble_title = baby_monitor_page.get_tutor_title()
                    hint = self.get_string("baby_timeline_description_title")
                    self.assertEqual(baby_bubble_title, hint)
                    print("Second tutor success")
            except AssertionError as e:
                    print("Second tutor FAIL: text mismatch")
                    errors.append(e)
            try:
                    baby_bubble_description = baby_monitor_page.get_tutor_description()
                    hint = self.get_string("baby_timeline_description")
                    self.assertEqual(baby_bubble_description, hint)
                    print("Second tutor description success")
            except AssertionError as e:
                    print("Second tutor description FAIL: text mismatch")
                    errors.append(e)
            self.click_middle()
            try:
                    sleep_mode_title = baby_monitor_page.get_tutor_title()
                    hint = self.get_string("sleep_mode_title")
                    self.assertEqual(sleep_mode_title, hint)
                    print("Third tutor success")
            except AssertionError as e:
                    print("Third tutor FAIL: text mismatch")
                    errors.append(e)
            try:
                    sleep_mode_description = baby_monitor_page.get_tutor_description()
                    hint = self.get_string("sleep_mode_description")
                    self.assertEqual(sleep_mode_description, hint)
                    print("Third tutor description success")
            except AssertionError as e:
                    print("Third tutor description FAIL: text mismatch")
                    errors.append(e)
            self.click_middle()
            try:
                    two_way_talk_title = baby_monitor_page.get_tutor_title()
                    hint = self.get_string("two_way_talk_title")
                    self.assertEqual(two_way_talk_title, hint)
                    print("Fourth tutor success")
            except AssertionError as e:
                    print("Fourth tutor FAIL: text mismatch")
                    errors.append(e)
            try:
                    two_way_talk_description = baby_monitor_page.get_tutor_description()
                    hint = self.get_string("two_way_talk_description")
                    self.assertEqual(two_way_talk_description, hint)
                    print("Fourth tutor description success")
            except AssertionError as e:
                    print("Fourth tutor description FAIL: text mismatch")
                    errors.append(e)
            self.click_middle()

            if errors:
                    raise AssertionError(errors)

    def test_02_menu_tutor(self):
            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            errors = []

            baby_monitor_page.click_home()
            try:
                    pixsee_friends_title = baby_monitor_page.get_tutor_title()
                    hint = self.get_string("menu_title_doll")
                    self.assertEqual(pixsee_friends_title, hint)
                    print("Pixsee Friends tutor title success")
            except AssertionError as e:
                    print("Pixsee Friends tutor title FAIL: text mismatch")
                    errors.append(e)
            try:
                    pixsee_friends_description = baby_monitor_page.get_tutor_description()
                    hint = self.get_string("doll_first_tip")
                    self.assertEqual(pixsee_friends_description, hint)
                    print("Pixsee Friends tutor description success")
            except AssertionError as e:
                    print("Pixsee Friends tutor description FAIL: text mismatch")
                    errors.append(e)
            menu_page.click_logout()
            baby_monitor_page.click_home()

            if errors:
                    raise AssertionError(errors)

    def test_03_tree_tutor(self):
            baby_monitor_page = BabyMonitorPage(self.driver)
            baby_timeline_page = BabyTimelinePage(self.driver)
            errors = []

            self.down_scroll()
            tree_title = baby_timeline_page.get_tutor_title()
            hint = self.get_string("special_card_description_title")
            try:
                    self.assertEqual(tree_title, hint)
                    print("Tree tutor title success")
            except AssertionError as e:
                    print("Tree tutor title FAIL: text mismatch")
                    errors.append(e)

            tree_description = baby_timeline_page.get_tutor_description()
            hint = self.get_string("special_card_description").replace("\\n", " ")
            try:
                    self.assertEqual(tree_description, hint)
                    print("Tree tutor description success")
            except AssertionError as e:
                    print("Tree tutor description FAIL: text mismatch")
                    errors.append(e)

            self.click_middle()
            baby_timeline_page.click_home()

            # 測試結束前再丟出錯誤
            if errors:
                    raise AssertionError(errors)

    def test_04_album_tutor(self):
            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            album_page = AlbumPage(self.driver)
            errors = []

            baby_monitor_page.click_home()
            menu_page.click_album()
            try:
                    album_title = album_page.new_function_title()
                    hint = self.get_string("slideshow_whats_new").replace("\\", "")
                    self.assertEqual(album_title, hint)
                    print("new function title success")
            except AssertionError as e:
                    print("new function title FAIL: text mismatch")
                    errors.append(e)
            try:
                    album_description = album_page.new_function_msg()
                    hint = self.get_string("slideshow_whats_new_info")
                    self.assertEqual(album_description, hint)
                    print("new function message description success")
            except AssertionError as e:
                    print("new function message FAIL: text mismatch")
                    errors.append(e)
            try:
                    iknow_button_text = album_page.iknow_button_text()
                    hint = self.get_string("slideshow_i_got_it")
                    self.assertEqual(iknow_button_text, hint)
                    print("I know button text success")
            except AssertionError as e:
                    print("I know button text FAIL: text mismatch")
                    errors.append(e)
            album_page.click_iknow_button()
            try:
                    view_tutor_title = album_page.tutor_title()
                    hint = self.get_string("first_tip_preview_photo_title")
                    self.assertEqual(view_tutor_title, hint)
                    print("View tutor title success")
            except AssertionError as e:
                    print("View tutor title FAIL: text mismatch")
                    errors.append(e)
            try:
                    view_tutor_description = album_page.tutor_description()
                    hint = self.get_string("first_tip_preview_photo_info")
                    self.assertEqual(view_tutor_description, hint)
                    print("View tutor description success")
            except AssertionError as e:
                    print("View tutor description FAIL: text mismatch")
                    errors.append(e)
            self.click_middle()
            album_page.click_plus_button()
            time.sleep(1)
            try:
                    create_tutor_title = album_page.tutor_title()
                    hint = self.get_string("first_tip_create_slideshow_title")
                    self.assertEqual(create_tutor_title, hint)
                    print("Create tutor title success")
            except AssertionError as e:
                    print("Create tutor title FAIL: text mismatch")
                    errors.append(e)
            try:
                    create_tutor_description = album_page.tutor_description()
                    hint = self.get_string("first_tip_create_slideshow_info")
                    self.assertEqual(create_tutor_description, hint)
                    print("Create tutor description success")
            except AssertionError as e:
                    print("Create tutor description FAIL: text mismatch")
                    errors.append(e)
            self.click_middle()
            album_page.click_plus_button()
            self.go_back()
            baby_monitor_page.click_home()

            if errors:
                    raise AssertionError(errors)

    def test_05_camera_tutor(self):
                baby_monitor_page = BabyMonitorPage(self.driver)
                camera_main_page = CameraMainPage(self.driver)
                play_back_page = PlayBackPage(self.driver)
                errors = []

                baby_monitor_page.click_middle()
                self.click_middle()
                try:
                        camera_tutor_title = camera_main_page.tutor_title()
                        hint = self.get_string("playback_first_tip_playback_title")
                        self.assertEqual(camera_tutor_title, hint)
                        print("Camera tutor title success")
                except AssertionError as e:
                        print("Camera tutor title FAIL: text mismatch")
                        errors.append(e)
                try:
                        camera_tutor_description = camera_main_page.tutor_description()
                        hint = self.get_string("playback_first_tip_playback_description")
                        self.assertEqual(camera_tutor_description, hint)
                        print("Camera tutor description success")
                except AssertionError as e:
                        print("Camera tutor description FAIL: text mismatch")
                        errors.append(e)
                self.click_middle()
                # get in to play back page
                camera_main_page.click_play_back()

                try:
                        playback_tutor_title = play_back_page.tutor_title()
                        hint = self.get_string("playback_first_tip_zoom_in_title")
                        self.assertEqual(playback_tutor_title, hint)
                        print("Playback first tutor title success")
                except AssertionError as e:
                        print("Playback first tutor title FAIL: text mismatch")
                        errors.append(e)
                try:
                        playback_tutor_description = play_back_page.tutor_description()
                        hint = self.get_string("playback_first_tip_zoom_in_description")
                        self.assertEqual(playback_tutor_description, hint)
                        print("Playback first tutor description success")
                except AssertionError as e:
                        print("Playback first tutor description FAIL: text mismatch")
                        errors.append(e)

                self.click_middle()
                try:
                        playback_tutor_title = play_back_page.tutor_title()
                        hint = self.get_string("playback_first_tip_calendar_title")
                        self.assertEqual(playback_tutor_title, hint)
                        print("Playback second tutor title success")
                except AssertionError as e:
                        print("Playback second tutor title FAIL: text mismatch")
                        errors.append(e)
                try:
                        playback_tutor_description = play_back_page.tutor_description()
                        hint = self.get_string("playback_first_tip_calendar_description")
                        self.assertEqual(playback_tutor_description, hint)
                        print("Playback second tutor description success")
                except AssertionError as e:
                        print("Playback second tutor description FAIL: text mismatch")
                        errors.append(e)

                self.click_middle()

                camera_main_page.click_home()
                if errors:
                        raise AssertionError(errors)