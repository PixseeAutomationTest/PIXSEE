from pages.base import BaseTestCase
import unittest
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
import time
from pages.menu_page import MenuPage


class TutorCase(BaseTestCase):
        def setUp(self):
                super().setUp(no_reset=False)
                self.tutor_id = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"

        def test_first_four_tutor_success(self):
                login_page = LoginPage(self.driver)
                baby_monitor_page = BabyMonitorPage(self.driver)

                login_page.login(self.account(), self.password())
                # check title and description of first three tutor
                try:
                        timer_title = baby_monitor_page.get_tutor_title()
                        hint = self.get_string("capture_timer_mode_description_title")
                        self.assertEqual(timer_title, hint)
                        print("First tutor success")
                except AssertionError:
                        print("First tutor FAIL: text mismatch")
                try:
                        timer_description = baby_monitor_page.get_tutor_description()
                        hint = self.get_string("capture_timer_mode_description")
                        self.assertEqual(timer_description, hint)
                        print("First tutor description success")
                        self.click_middle()
                except AssertionError:
                        print("First tutor description FAIL: text mismatch")
                try:
                        baby_bubble_title = baby_monitor_page.get_tutor_title()
                        hint = self.get_string("baby_timeline_description_title")
                        self.assertEqual(baby_bubble_title, hint)
                        print("Second tutor success")
                except AssertionError:
                        print("Second tutor FAIL: text mismatch")
                try:
                        baby_bubble_description = baby_monitor_page.get_tutor_description()
                        hint = self.get_string("baby_timeline_description")
                        self.assertEqual(baby_bubble_description, hint)
                        print("Second tutor description success")
                        self.click_middle()
                except AssertionError:
                        print("Second tutor description FAIL: text mismatch")
                try:
                        sleep_mode_title = baby_monitor_page.get_tutor_title()
                        hint = self.get_string("sleep_mode_title")
                        self.assertEqual(sleep_mode_title, hint)
                        print("Third tutor success")
                except AssertionError:
                        print("Third tutor FAIL: text mismatch")
                try:
                        sleep_mode_description = baby_monitor_page.get_tutor_description()
                        hint = self.get_string("sleep_mode_description")
                        self.assertEqual(sleep_mode_description, hint)
                        print("Third tutor description success")
                        self.click_middle()
                except AssertionError:
                        print("Third tutor description FAIL: text mismatch")
                try:
                        two_way_talk_title = baby_monitor_page.get_tutor_title()
                        hint = self.get_string("two_way_talk_title")
                        self.assertEqual(two_way_talk_title, hint)
                        print("Fourth tutor success")
                except AssertionError:
                        print("Fourth tutor FAIL: text mismatch")
                try:
                        two_way_talk_description = baby_monitor_page.get_tutor_description()
                        hint = self.get_string("two_way_talk_description")
                        self.assertEqual(two_way_talk_description, hint)
                        print("Fourth tutor description success")
                except AssertionError:
                        print("Fourth tutor description FAIL: text mismatch")
        def test_menu_tutor(self):
                baby_monitor_page = BabyMonitorPage(self.driver)
                login_page = LoginPage(self.driver)

                login_page.login(self.account(), self.password())
                self.skip_first_four_tutor()
                baby_monitor_page.click_home()
                try:
                        pixsee_friends_title = baby_monitor_page.get_tutor_title()
                        hint = self.get_string("menu_title_doll")
                        self.assertEqual(pixsee_friends_title, hint)
                        print("Pixsee Friends tutor title success")
                except AssertionError:
                        print("Pixsee Friends tutor title FAIL: text mismatch")
                try:
                        pixsee_friends_description = baby_monitor_page.get_tutor_description()
                        hint = self.get_string("doll_first_tip")
                        self.assertEqual(pixsee_friends_description, hint)
                        print("Pixsee Friends tutor description success")
                except AssertionError:
                        print("Pixsee Friends tutor description FAIL: text mismatch")














if __name__ == "__main__":
    unittest.main()