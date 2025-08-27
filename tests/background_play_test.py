from base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.assistant_pages.assistant_page import AssistantPage
from pages.menu_pages.assistant_pages.background_play_page import BackgroundPlayPage

class BackgroundPlayTest(BaseTestCase):

    def test_discard_settings(self):
        self.open_app()

        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        assistant_page = AssistantPage(self.driver)
        background_play_page = BackgroundPlayPage(self.driver)
        try:
            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")
            '''Go to Assistant Page'''
            menu_page.click_assistant()
            self.assertTrue(assistant_page.is_in_assistant_page(), "Can't go to Assistant Page")
            '''Go to Background Page'''
            assistant_page.click_background_play()
            self.assertTrue(background_play_page.is_in_background_play_page(), "Can't go to Background Play Page")

            '''Discard Settings'''
            before_status = background_play_page.get_keep_playing_status()
            background_play_page.click_keep_playing()
            background_play_page.click_return()

            '''Checking words in "Discard Settings" window'''
            self.assertEqual(self.get_string("bg_play_discard_changes_message"),background_play_page.get_discard_message(), "Text \"Discard background monitoring settings ?\" is not properly displayed")
            self.assertEqual(self.get_string("yes"), background_play_page.get_discard_yes_button_text(), "\"Yes\" Button is not properly displayed")
            self.assertEqual(self.get_string("no"), background_play_page.get_discard_no_button_text(), "\"No\" Button is not properly displayed")

            '''Discard Settings'''
            background_play_page.click_discard_yes()
            self.assertTrue(assistant_page.is_in_assistant_page(), "Background Play Page is not closed after discard settings")

            '''Checking status of "Keep Playing" button'''
            assistant_page.click_background_play()
            self.assertTrue(background_play_page.is_in_background_play_page(), "Can't go to Background Play Page")
            after_status = background_play_page.get_keep_playing_status()
            self.assertEqual(before_status, after_status)
        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_cancel_discard_settings(self):
        self.open_app()

        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        assistant_page = AssistantPage(self.driver)
        background_play_page = BackgroundPlayPage(self.driver)
        try:
            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")
            '''Go to Assistant Page'''
            menu_page.click_assistant()
            self.assertTrue(assistant_page.is_in_assistant_page(), "Can't go to Assistant Page")
            '''Go to Background Page'''
            assistant_page.click_background_play()
            self.assertTrue(background_play_page.is_in_background_play_page(), "Can't go to Background Play Page")

            '''Discard Settings'''
            before_status = background_play_page.get_keep_playing_status()
            background_play_page.click_keep_playing()
            background_play_page.click_return()

            '''Checking words in "Discard Settings" window'''
            self.assertEqual(self.get_string("bg_play_discard_changes_message"), background_play_page.get_discard_message(), "Text \"Discard background monitoring settings ?\" is not properly displayed")
            self.assertEqual(self.get_string("yes"), background_play_page.get_discard_yes_button_text(), "\"Yes\" Button is not properly displayed")
            self.assertEqual(self.get_string("no"), background_play_page.get_discard_no_button_text(), "\"No\" Button is not properly displayed")

            '''Discard Settings'''
            background_play_page.click_discard_no()
            self.assertTrue(background_play_page.is_in_background_play_page(), "Background Play Page is not closed after discard settings")

            '''Checking status of "Keep Playing" button'''
            after_status = background_play_page.get_keep_playing_status()
            self.assertNotEqual(before_status, after_status)
        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_floating_video(self):
        self.open_app()

        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        assistant_page = AssistantPage(self.driver)
        background_play_page = BackgroundPlayPage(self.driver)

        try:
            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")
            '''Go to Assistant Page'''
            menu_page.click_assistant()
            self.assertTrue(assistant_page.is_in_assistant_page(), "Can't go to Assistant Page")
            '''Go to Background Page'''
            assistant_page.click_background_play()
            self.assertTrue(background_play_page.is_in_background_play_page(), "Can't go to Background Play Page")

            '''Switch to floating video mode'''
            if not background_play_page.get_keep_playing_status():
                background_play_page.click_keep_playing()
            background_play_page.click_floating_video()
            background_play_page.click_save()
            self.assertTrue(assistant_page.is_in_assistant_page(), "Assistant Page is not opened after saving settings") #spec doesn't write about this.

            '''Go back to baby monitor page'''
            assistant_page.click_return()
            self.assertTrue(menu_page.is_in_menu_page(), "Menu Page is not opened after saving settings")
            menu_page.click_home()
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page(), "Baby Monitor Page is not opened after saving settings")

            '''Go to home screen and check floating video'''
            #TODO: Find picture-in-picture element in home screen
            self.go_to_home_screen()
        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()