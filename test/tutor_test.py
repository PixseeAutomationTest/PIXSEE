from pages.base import BaseTestCase
import unittest
from pages.login_page import LoginPage
from pages.baby_monitor_page import BabyMonitorPage
import time

from pages.menu_page import MenuPage


class TutorCase(BaseTestCase):

        @classmethod
        def setUpClass(cls):
                super().setUp(no_reset=False)

        def test_first_three_tutor_success(self):
                login_page = LoginPage(self.driver)
                baby_monitor_page = BabyMonitorPage(self.driver)

                login_page.login("jackypixsee02@gmail.com", "@Aa12345")



                tutor_id = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
                expected_texts = [
                        "Hold and swipe up\nto switch on timer.\nDevice will flash\nwhile shooting."
                        , "Drag to view daily cover"
                        , "Long press for 2-way talk"
                        ]

                for i in range(3):
                        try:
                                actual_text = baby_monitor_page.wait_for_tutor_by_id(tutor_id)
                                self.assertEqual(actual_text, expected_texts[i])
                                print(f"no.{i + 1} tutor success")
                        except AssertionError:
                                print(f"no.{i + 1} tutor FAIL: text mismatch, expected '{expected_texts[i]}', got '{actual_text}'")
                        except Exception as e:
                                print(f"no.{i + 1} tutor FAIL: Exception occurred - {str(e)}")
                        finally:
                                try:
                                        baby_monitor_page.click_stream_title()
                                        time.sleep(1)
                                except:
                                        print(f"no.{i + 1} failed to click stream title")

        def test_menu_tutor(self):
                menu_page = MenuPage(self.driver)
                baby_monitor_page = BabyMonitorPage(self.driver)
                baby_monitor_page.click_home()
                tutor_id = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
                expected_texts = [
                        "Pixsee Friends specially created as companion toys to the Pixsee Play AI Smart Baby Camera."
                ]
                click_id = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsAbout"
                self.verify_text_and_click(tutor_id, expected_texts, click_id, "menu")












if __name__ == "__main__":
    unittest.main()