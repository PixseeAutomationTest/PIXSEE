from pages.menu_pages.menu_page import MenuPage
from base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.assistant_pages.assistant_page import AssistantPage
from pages.menu_pages.assistant_pages.send_error_dialog_page import SendErrorPage
from pages.menu_pages.assistant_pages.background_play_page import BackgroundPlayPage
from pages.menu_pages.assistant_pages.tutorial_page import TutorialPage
from pages.menu_pages.assistant_pages.pixsee_cloud_page import PixseeCloudPage
import re


class AssistantTest(BaseTestCase):
    def __init__(self, methodName='runTest', language="zh", locale="TW"):
        super().__init__(methodName)
        self.language = language
        self.locale = locale

    def setUp(self):
        super().setUp(language=self.language, locale=self.locale)
        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        assistant_page = AssistantPage(self.driver)
        try:
            while self.driver.current_package != self.driver.capabilities.get("appPackage"):
                self.driver.terminate_app(self.driver.current_package)
                self.open_app()
            if assistant_page.is_in_assistant_page():
                return
            elif not baby_monitor_page.is_in_baby_monitor_page():
                self.shutdown_app()
                self.open_app()
            print("Finish opening app.")
            baby_monitor_page.click_home()
            menu_page.click_assistant()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
    # all start from assistant page
    def test_01_background_play(self):
        assistant_page = AssistantPage(self.driver)
        background_play_page = BackgroundPlayPage(self.driver)
        if assistant_page.is_backgroud_play_able_to_click():
        # check title
            try:
                background_play_title = assistant_page.background_play_text()
                hint = self.get_string("background_play")
                self.assertEqual(background_play_title, hint)
            except Exception as e:
                print(f"title Test failed with exception: {e}")
                self.fail(f"Failed to retrieve or verify the Background Play title: {e}")
            try:
                background_play_sub = assistant_page.background_play_sub_text()
                hint = self.get_string("background_monitoring_subtitle")
                self.assertEqual(background_play_sub, hint)
            except Exception as e:
                print(f"Sub title Test failed with exception: {e}")
                self.fail(f"Failed to retrieve or verify the Background Play subtitle: {e}")
            assistant_page.click_background_play()
        else:
            print("Background Play is not available, skipping test.")
            raise AssertionError("Background Play is not available, skipping test.")
        # check if is in
        try:
            self.assertTrue(background_play_page.is_in_background_play_page())
        except Exception as e:
            print(f"Background Play Page Test failed with exception: {e}")
            self.fail(f"Failed to navigate to Background Play page: {e}")

        background_play_page.click_return()
    def test_02_pixsee_cloud(self):
        assistant_page = AssistantPage(self.driver)
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        # check title
        try:
            pixsee_cloud_title = assistant_page.pixsee_cloud_text()
            hint = self.get_string("pixsee_cloud")
            self.assertEqual(pixsee_cloud_title, hint)
        except Exception as e:
            print(f"title Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Pixsee Cloud title: {e}")

        try:
            pixsee_cloud_sub = assistant_page.pixsee_cloud_sub_text()
            hint = self.get_string("pixsee_cloud_usage")
            pattern = "^" + re.escape(hint).replace("%s", r".+") + "$"
            self.assertRegex(pixsee_cloud_sub,pattern)
        except Exception as e:
            print(f"Sub title Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Pixsee Cloud subtitle: {e}")

        assistant_page.click_pixsee_cloud()
        # check if is in pixsee cloud page
        try:
            self.assertTrue(pixsee_cloud_page.is_in_pixsee_cloud_page())
        except Exception as e:
            print(f"Pixsee Cloud Page Test failed with exception: {e}")
            self.fail(f"Failed to navigate to Pixsee Cloud page: {e}")
        pixsee_cloud_page.click_back()
    def test_03_tutorial(self):
        assistant_page = AssistantPage(self.driver)
        tutorial_page = TutorialPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        # check title
        try:
            tutorial_title = assistant_page.tutorial_text()
            hint = self.get_string("tutorial_menu_item_title")
            self.assertEqual(tutorial_title, hint)
        except Exception as e:
            print(f"title Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Tutorial title: {e}")

        assistant_page.click_tutorial()
        # check tutorial 1 text and index
        try:
            first_tutorial_text = tutorial_page.title_text()
            hint = self.get_string("tutorial_title_1")
            self.assertEqual(first_tutorial_text, hint)
        except Exception as e:
            print(f"First Tutorial Text Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the first tutorial text: {e}")
        # check first tutor indicator
        try:
            self.assertTrue(tutorial_page.is_in_tutor_first_page())
            print("first tutor indicator displayed")
        except AssertionError:
            raise AssertionError("first tutor indicator doesn't displayed")
        # check skip
        try:
            skip = tutorial_page.skip_button_text()
            hint = self.get_string("skip")
            self.assertEqual(skip, hint)
            print("skip display right")
        except AssertionError:
            raise AssertionError("skip display wrong")

        tutorial_page.click_skip()
        # check if is in menu page
        try:
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page())
            print("skip first tutor successfully")
        except AssertionError:
            raise AssertionError("skip first tutor unsuccessfully")
        # back to assistant page
        menu_page.click_assistant()
        assistant_page.click_tutorial()
        self.left_wipe()
        # check tutorial 2 text and index
        try:
            second_tutorial_text = tutorial_page.title_text()
            hint = self.get_string("tutorial_title_2").replace("\\n", "\n")
            self.assertEqual(second_tutorial_text, hint)
        except Exception as e:
            print(f"Second Tutorial Text Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the second tutorial text: {e}")
        # check second tutor indicator
        try:
            self.assertTrue(tutorial_page.is_in_tutor_second_page())
            print("second tutor indicator displayed")
        except AssertionError:
            raise AssertionError("second tutor indicator doesn't displayed")
        # check skip
        try:
            skip = tutorial_page.skip_button_text()
            hint = self.get_string("skip")
            self.assertEqual(skip, hint)
            print("skip display right")
        except AssertionError:
            raise AssertionError("skip display wrong")
        # check tutorial 3 text and index
        self.left_wipe()
        try:
            third_tutorial_text = tutorial_page.title_text()
            hint = self.get_string("tutorial_title_3")
            self.assertEqual(third_tutorial_text, hint)
        except Exception as e:
            print(f"Third Tutorial Text Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the third tutorial text: {e}")
        # check third tutor indicator
        try:
            self.assertTrue(tutorial_page.is_in_tutor_third_page())
            print("third tutor indicator displayed")
        except AssertionError:
            raise AssertionError("third tutor indicator doesn't displayed")
        # check skip
        try:
            skip = tutorial_page.skip_button_text()
            hint = self.get_string("skip")
            self.assertEqual(skip, hint)
            print("skip display right")
        except AssertionError:
            raise AssertionError("skip display wrong")
        # check tutorial 4 text and index
        self.left_wipe()
        try:
            fourth_tutorial_text = tutorial_page.title_text()
            hint = self.get_string("tutorial_title_4").replace("\\n", "\n")
            self.assertEqual(fourth_tutorial_text, hint)
        except Exception as e:
            print(f"Fourth Tutorial Text Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the fourth tutorial text: {e}")
        # check fourth tutor indicator
        try:
            self.assertTrue(tutorial_page.is_in_tutor_fourth_page())
            print("fourth tutor indicator displayed")
        except AssertionError:
            raise AssertionError("fourth tutor indicator doesn't displayed")
        # check skip
        try:
            skip = tutorial_page.skip_button_text()
            hint = self.get_string("skip")
            self.assertEqual(skip, hint)
            print("skip display right")
        except AssertionError:
            raise AssertionError("skip display wrong")
        # check tutorial 5 text and index
        self.left_wipe()
        try:
            fifth_tutorial_text = tutorial_page.title_text()
            hint = self.get_string("tutorial_title_5")
            self.assertEqual(fifth_tutorial_text, hint)
        except Exception as e:
            print(f"Fifth Tutorial Text Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the fifth tutorial text: {e}")
        # check fifth tutor indicator
        try:
            self.assertTrue(tutorial_page.is_in_tutor_fifth_page())
            print("fifth tutor indicator displayed")
        except AssertionError:
            raise AssertionError("fifth tutor indicator doesn't displayed")
        # check skip
        try:
            skip = tutorial_page.skip_button_text()
            hint = self.get_string("skip")
            self.assertNotEqual(skip, hint)
            print("let's start display right")
        except AssertionError:
            raise AssertionError("let's start display wrong")
        # click skip
        tutorial_page.click_skip()
        # check if is in menu page
        try:
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page())
            print("skip fifth tutor successfully")
        except AssertionError:
            raise AssertionError("skip fifth tutor unsuccessfully")
        # back to assistant page
        menu_page.click_assistant()
    def test_04_questions_and_answers(self):
        assistant_page = AssistantPage(self.driver)
        # check title
        try:
            qa_title = assistant_page.qa_text()
            hint = self.get_string("qea_menu_item_title")
            self.assertEqual(qa_title, hint)
        except Exception as e:
            print(f"title Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Q&A title: {e}")

        assistant_page.click_qa()

        try:
            qa_web = assistant_page.url_text()
            hint = self.get_string("__global__url_support").replace("https://www.", "")
            self.assertEqual(qa_web, hint)
        except Exception as e:
            print(f"url Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Q&A URL text: {e}")
        self.go_back()
    def test_05_contact_us(self):
        assistant_page = AssistantPage(self.driver)

        # check title
        try:
            contact_us_title = assistant_page.contact_us_text()
            hint = self.get_string("trouble_shooting_menu_item_title")
            self.assertEqual(contact_us_title, hint)
        except Exception as e:
            print(f"title Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Contact Us title: {e}")
        assistant_page.click_contact_us()

        try:
            contact_us_text = assistant_page.url_text()
            hint = self.get_string("__global__url_contact").replace("https://www.", "")
            self.assertIn(hint, contact_us_text)
        except Exception as e:
            print(f"Url Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Contact Us URL text: {e}")
        self.go_back()
    def test_06_report_error(self):
        assistant_page = AssistantPage(self.driver)
        send_error_page = SendErrorPage(self.driver)
        # check title
        try:
            send_error_title = assistant_page.send_error_text()
            hint = self.get_string("report_error_title")
            self.assertEqual(send_error_title, hint)
        except Exception as e:
            print(f"title Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error title: {e}")
        try:
            send = assistant_page.send_button_text()
            hint = self.get_string("send_report")
            self.assertEqual(send, hint)
        except Exception as e:
            print(f"Send button Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send button text: {e}")
        assistant_page.click_send_error()
        # check if is in send error dialog

        try:
            self.assertTrue(send_error_page.is_in_send_error_dialog())
        except Exception as e:
            print(f"Send Error Dialog Test failed with exception: {e}")
            self.fail(f"Failed to navigate to Send Error dialog: {e}")
        try:
            title = send_error_page.title_text()
            hint = self.get_string("send_report_dialog_title")
            self.assertEqual(title, hint)
        except Exception as e:
            print(f"Send Error Dialog Title Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error dialog title: {e}")
        try:
            text = send_error_page.text()
            hint = self.get_string("send_report_dialog_message")
            self.assertEqual(text, hint)
        except Exception as e:
            print(f"Send Error Dialog Text Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error dialog text: {e}")
        try:
            cancel = send_error_page.cancel_button_text()
            hint = self.get_string("cancel")
            self.assertEqual(cancel, hint)
        except Exception as e:
            print(f"Send Error Dialog Cancel Button Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error dialog cancel button text: {e}")
        try:
            send = send_error_page.send_button_text()
            hint = self.get_string("send_report")
            self.assertEqual(send, hint)
        except Exception as e:
            print(f"Send Error Dialog Send Button Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error dialog send button text: {e}")
        # click cancel
        send_error_page.click_cancel()
        assistant_page.click_send()
        # check if is in send error dialog
        try:
            self.assertTrue(send_error_page.is_in_send_error_dialog())
        except Exception as e:
            print(f"Send Error Dialog Test failed with exception: {e}")
            self.fail(f"Failed to navigate to Send Error dialog: {e}")
        try:
            title = send_error_page.title_text()
            hint = self.get_string("send_report_dialog_title")
            self.assertEqual(title, hint)
        except Exception as e:
            print(f"Send Error Dialog Title Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error dialog title: {e}")
        try:
            text = send_error_page.text()
            hint = self.get_string("send_report_dialog_message")
            self.assertEqual(text, hint)
        except Exception as e:
            print(f"Send Error Dialog Text Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error dialog text: {e}")
        try:
            cancel = send_error_page.cancel_button_text()
            hint = self.get_string("cancel")
            self.assertEqual(cancel, hint)
        except Exception as e:
            print(f"Send Error Dialog Cancel Button Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error dialog cancel button text: {e}")
        try:
            send = send_error_page.send_button_text()
            hint = self.get_string("send_report")
            self.assertEqual(send, hint)
        except Exception as e:
            print(f"Send Error Dialog Send Button Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error dialog send button text: {e}")
        # click send
        send_error_page.click_send()
        # check if is in assistant page
        try:
            sending = send_error_page.title_text()
            hint = self.get_string("send_report_dialog_being_send")
            self.assertEqual(sending, hint)
        except Exception as e:
            print(f"Send Error Dialog Sending Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error dialog sending text: {e}")
        try:
            cancel = send_error_page.send_button_text()
            hint = self.get_string("cancel")
            self.assertEqual(cancel, hint)
        except Exception as e:
            print(f"Send Error Dialog Cancel Button Test failed with exception: {e}")
            self.fail(f"Failed to retrieve or verify the Send Error dialog cancel button text: {e}")
        send_error_page.click_send()
