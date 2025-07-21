from pages.base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_page import MenuPage
from pages.pixsee_settings.pixsee_settings_page import PixseeSettingsPage
from pages.pixsee_settings.voice_service_page import VoiceServicePage
from pages.pixsee_settings.voice_service_pages.voice_command_page import VoiceCommandPage

class VoiceServiceTest(BaseTestCase):
    def test_changing_status_discard_with_yes(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            voice_service_page = VoiceServicePage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Baby Monitor Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Voice Service Page'''
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")

            '''Verify Voice Service Page'''
            self.assertEqual(voice_service_page.get_page_title(), self.get_string("voice_service_settings_title"), "Text \"Voice Service\" is not properly displayed")
            self.assertEqual(voice_service_page.get_save_button_text(), self.get_string("save"), "button \"Save\" is not properly displayed")
            self.assertFalse(voice_service_page.get_save_button_enabled(), "button \"Save\" is enabled before changing detection switch")
            self.assertEqual(voice_service_page.get_detection_notification(), self.get_string("detection"), "Text \"Detection\" is not properly displayed")
            before_detection_switch_status = voice_service_page.get_detection_switch_status()
            if not before_detection_switch_status:
                voice_service_page.click_detection_switch()
            self.assertEqual(voice_service_page.get_service_section(), self.get_string("voice_service_settings_section_service"), "Text \"Service\" is not properly displayed")
            self.assertEqual(voice_service_page.get_voice_command_button_text(), self.get_string("voice_service_settings_option_local"), "Text \"Local Voice Commands\" is not properly displayed")
            '''Check save button is enabled after changing detection switch'''
            if before_detection_switch_status == voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            self.assertTrue(voice_service_page.get_save_button_enabled(), "button \"Save\" is not enabled after changing detection switch")

            '''Verify Discard dialog'''
            if before_detection_switch_status == voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            voice_service_page.click_back()
            self.assertTrue(voice_service_page.has_discard_dialog(), "\"Discard Voice Commands settings\" window doesn't appear")
            self.assertEqual(voice_service_page.get_discard_dialog_title(), self.get_string("voice_commands_discard"), "Text \"Discard Voice Commands settings?\" is not properly displayed")
            self.assertEqual(voice_service_page.get_discard_dialog_yes_button_text(), self.get_string("yes"), "button \"Yes\" is not properly displayed")
            self.assertEqual(voice_service_page.get_discard_dialog_no_button_text(), self.get_string("no"), "button \"No\" is not properly displayed")

            '''Click yes button and go back to Voice Service Page to check if settings are discarded'''
            voice_service_page.click_discard_dialog_yes()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't automatically go to Pixsee Settings Page after discarding changes")
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")
            self.assertEqual(before_detection_switch_status, voice_service_page.get_detection_switch_status(), "Changing detection switch is not discarded")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_changing_status_discard_with_no(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            voice_service_page = VoiceServicePage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Baby Monitor Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Voice Service Page'''
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")

            '''Verify Voice Service Page'''
            self.assertEqual(voice_service_page.get_page_title(), self.get_string("voice_service_settings_title"), "Text \"Voice Service\" is not properly displayed")
            self.assertEqual(voice_service_page.get_save_button_text(), self.get_string("save"), "button \"Save\" is not properly displayed")
            self.assertFalse(voice_service_page.get_save_button_enabled(), "button \"Save\" is enabled before changing detection switch")
            self.assertEqual(voice_service_page.get_detection_notification(), self.get_string("detection"), "Text \"Detection\" is not properly displayed")
            before_detection_switch_status = voice_service_page.get_detection_switch_status()
            if not before_detection_switch_status:
                voice_service_page.click_detection_switch()
            self.assertEqual(voice_service_page.get_service_section(), self.get_string("voice_service_settings_section_service"), "Text \"Service\" is not properly displayed")
            self.assertEqual(voice_service_page.get_voice_command_button_text(), self.get_string("voice_service_settings_option_local"), "Text \"Local Voice Commands\" is not properly displayed")
            '''Check save button is enabled after changing detection switch'''
            if before_detection_switch_status == voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            self.assertTrue(voice_service_page.get_save_button_enabled(), "button \"Save\" is not enabled after changing detection switch")

            '''Verify Discard dialog'''
            if before_detection_switch_status == voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            voice_service_page.click_back()
            self.assertTrue(voice_service_page.has_discard_dialog(), "\"Discard Voice Commands settings\" window doesn't appear")
            self.assertEqual(voice_service_page.get_discard_dialog_title(), self.get_string("voice_commands_discard"), "Text \"Discard Voice Commands settings?\" is not properly displayed")
            self.assertEqual(voice_service_page.get_discard_dialog_yes_button_text(), self.get_string("yes"), "button \"Yes\" is not properly displayed")
            self.assertEqual(voice_service_page.get_discard_dialog_no_button_text(), self.get_string("no"), "button \"No\" is not properly displayed")

            '''Click no button and check if settings are not discarded'''
            voice_service_page.click_discard_dialog_no()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Canceling discard dialog doesn't return to Voice Service Page")
            self.assertNotEqual(before_detection_switch_status, voice_service_page.get_detection_switch_status(), "Changing detection switch is discarded")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_changing_status_save(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            voice_service_page = VoiceServicePage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Baby Monitor Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Voice Service Page'''
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")

            '''Verify Voice Service Page'''
            self.assertEqual(voice_service_page.get_page_title(), self.get_string("voice_service_settings_title"), "Text \"Voice Service\" is not properly displayed")
            self.assertEqual(voice_service_page.get_save_button_text(), self.get_string("save"), "button \"Save\" is not properly displayed")
            self.assertFalse(voice_service_page.get_save_button_enabled(), "button \"Save\" is enabled before changing detection switch")
            self.assertEqual(voice_service_page.get_detection_notification(), self.get_string("detection"), "Text \"Detection\" is not properly displayed")
            before_detection_switch_status = voice_service_page.get_detection_switch_status()
            if not before_detection_switch_status:
                voice_service_page.click_detection_switch()
            self.assertEqual(voice_service_page.get_service_section(), self.get_string("voice_service_settings_section_service"), "Text \"Service\" is not properly displayed")
            self.assertEqual(voice_service_page.get_voice_command_button_text(), self.get_string("voice_service_settings_option_local"), "Text \"Local Voice Commands\" is not properly displayed")
            '''Check save button is enabled after changing detection switch'''
            if before_detection_switch_status == voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            self.assertTrue(voice_service_page.get_save_button_enabled(), "button \"Save\" is not enabled after changing detection switch")

            '''Click save button and go back to Voice Service Page to check if settings are saved'''
            voice_service_page.click_save()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't automatically go to Pixsee Settings Page after changing voice settings")
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")
            self.assertNotEqual(before_detection_switch_status, voice_service_page.get_detection_switch_status(), "Changing detection switch is not saved")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_no_changing_status(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            voice_service_page = VoiceServicePage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Baby Monitor Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Voice Service Page'''
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")

            '''Verify Voice Service Page'''
            self.assertEqual(voice_service_page.get_page_title(), self.get_string("voice_service_settings_title"), "Text \"Voice Service\" is not properly displayed")
            self.assertEqual(voice_service_page.get_save_button_text(), self.get_string("save"), "button \"Save\" is not properly displayed")
            self.assertFalse(voice_service_page.get_save_button_enabled(), "button \"Save\" is enabled before changing detection switch")
            self.assertEqual(voice_service_page.get_detection_notification(), self.get_string("detection"), "Text \"Detection\" is not properly displayed")
            before_detection_switch_status = voice_service_page.get_detection_switch_status()
            if not before_detection_switch_status:
                voice_service_page.click_detection_switch()
            self.assertEqual(voice_service_page.get_service_section(), self.get_string("voice_service_settings_section_service"), "Text \"Service\" is not properly displayed")
            self.assertEqual(voice_service_page.get_voice_command_button_text(), self.get_string("voice_service_settings_option_local"), "Text \"Local Voice Commands\" is not properly displayed")
            '''Check button "save" is enabled after changing detection switch'''
            if before_detection_switch_status == voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            self.assertTrue(voice_service_page.get_save_button_enabled(), "button \"Save\" is not enabled after changing detection switch")

            '''Click back button and go back to Voice Service Page to check if settings are no changed'''
            if before_detection_switch_status != voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            voice_service_page.click_back()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page after clicking back button without changing settings")
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")
            self.assertEqual(before_detection_switch_status, voice_service_page.get_detection_switch_status(), "Detection switch is changed")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_changing_language_discard_with_yes(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            voice_service_page = VoiceServicePage(self.driver)
            voice_command_page = VoiceCommandPage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Baby Monitor Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Voice Service Page'''
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")

            '''Go to Voice Command Page'''
            if not voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            voice_service_page.click_voice_command_button()
            self.assertTrue(voice_command_page.is_in_voice_command_page(), "Can't go to Voice Command Page")

            '''Verify Voice Command Page'''
            self.assertEqual(voice_command_page.get_page_title(), self.get_string("local_voice_commands_settings_title"), "Text \"Local Voice Commands\" is not properly displayed")
            self.assertEqual(voice_command_page.get_save_button_text(), self.get_string("save"), "button \"Save\" is not properly displayed")
            self.assertEqual(voice_command_page.get_choosing_language_text(), self.get_string("voice_command_language"), "Text \"Language\" is not properly displayed")
            self.assertEqual(voice_command_page.get_english_text(), self.get_string("voice_command_language_english"), "Text \"English\" is not properly displayed")
            self.assertEqual(voice_command_page.get_chinese_text(), self.get_string("voice_command_language_chinese"), "Text \"Chinese\" is not properly displayed")

            before_english_checkbox_status = voice_command_page.get_english_checkbox_status()
            before_chinese_checkbox_status = voice_command_page.get_chinese_checkbox_status()
            self.assertNotEqual(before_english_checkbox_status, before_chinese_checkbox_status, "English and Chinese checkboxes can't be in the same status")

            '''Click English checkbox or Chinese checkbox'''
            now_language = "tw text" if before_english_checkbox_status else "en-us text"
            if before_english_checkbox_status:
                voice_command_page.click_chinese_checkbox()
            else:
                voice_command_page.click_english_checkbox()
            self.assertTrue(voice_command_page.get_save_button_enabled(), "button \"Save\" isn't enable after changing language checkbox")

            self.assertEqual(voice_command_page.get_voice_assistant_text(), self.get_string("voice_command_tip", now_language), "Text \"Voice assistant (we provide 5 commands\" is not properly displayed")
            self.assertEqual(voice_command_page.get_music_command_title(), self.get_string("voice_command_music_section_title", now_language), "Text \"Music\" is not properly displayed")
            self.assertEqual(voice_command_page.get_music_command_content(), self.get_string("voice_command_music_section_example1", now_language).replace('\\"', '"') + "\n" + self.get_string("voice_command_music_section_example2", now_language).replace('\\"', '"'), "Music Command Text is not properly displayed")
            self.assertEqual(voice_command_page.get_volume_command_title(), self.get_string("voice_command_volume_section_title", now_language), "Text \"Volume\" is not properly displayed")
            self.assertEqual(voice_command_page.get_volume_command_content(), self.get_string("voice_command_volume_section_example1", now_language).replace('\\"', '"') + "\n" + self.get_string("voice_command_volume_section_example2", now_language).replace('\\"', '"'), "Volume Command Text is not properly displayed")
            self.assertEqual(voice_command_page.get_camera_command_title(), self.get_string("voice_command_camera_section_title", now_language), "Text \"Camera\" is not properly displayed")
            self.assertEqual(voice_command_page.get_camera_command_content(), self.get_string("voice_command_camera_section_example1", now_language).replace('\\"', '"') + "\n", "Camera Command Text is not properly displayed")

            '''Verify Discard dialog'''
            voice_command_page.click_back()
            self.assertTrue(voice_command_page.has_discard_dialog(), "\"Discard Voice Commands settings\" window doesn't appear")
            self.assertEqual(voice_command_page.get_discard_dialog_title(), self.get_string("voice_commands_discard"), "Text \"Discard Voice Commands settings?\" is not properly displayed")
            self.assertEqual(voice_command_page.get_discard_dialog_yes_button_text(), self.get_string("yes"), "button \"Yes\" is not properly displayed")
            self.assertEqual(voice_command_page.get_discard_dialog_no_button_text(), self.get_string("no"), "button \"No\" is not properly displayed")

            '''Click yes button and go back to Voice Command Page to check if settings are discarded'''
            voice_command_page.click_discard_dialog_yes()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't automatically go to Voice Service Page after discarding changes")
            voice_service_page.click_voice_command_button()
            self.assertTrue(voice_command_page.is_in_voice_command_page(), "Can't go to Voice Command Page")
            self.assertEqual(before_english_checkbox_status, voice_command_page.get_english_checkbox_status(), "Changing English checkbox is not discarded")
            self.assertEqual(before_chinese_checkbox_status, voice_command_page.get_chinese_checkbox_status(), "Changing Chinese checkbox is not discarded")


        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_changing_language_discard_with_no(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            voice_service_page = VoiceServicePage(self.driver)
            voice_command_page = VoiceCommandPage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Baby Monitor Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Voice Service Page'''
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")

            '''Go to Voice Command Page'''
            if not voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            voice_service_page.click_voice_command_button()
            self.assertTrue(voice_command_page.is_in_voice_command_page(), "Can't go to Voice Command Page")

            '''Verify Voice Command Page'''
            self.assertEqual(voice_command_page.get_page_title(), self.get_string("local_voice_commands_settings_title"), "Text \"Local Voice Commands\" is not properly displayed")
            self.assertEqual(voice_command_page.get_save_button_text(), self.get_string("save"), "button \"Save\" is not properly displayed")
            self.assertEqual(voice_command_page.get_choosing_language_text(), self.get_string("voice_command_language"), "Text \"Language\" is not properly displayed")
            self.assertEqual(voice_command_page.get_english_text(), self.get_string("voice_command_language_english"), "Text \"English\" is not properly displayed")
            self.assertEqual(voice_command_page.get_chinese_text(), self.get_string("voice_command_language_chinese"), "Text \"Chinese\" is not properly displayed")

            before_english_checkbox_status = voice_command_page.get_english_checkbox_status()
            before_chinese_checkbox_status = voice_command_page.get_chinese_checkbox_status()
            self.assertNotEqual(before_english_checkbox_status, before_chinese_checkbox_status, "English and Chinese checkboxes can't be in the same status")

            '''Click English checkbox or Chinese checkbox'''
            now_language = "tw text" if before_english_checkbox_status else "en-us text"
            if before_english_checkbox_status:
                voice_command_page.click_chinese_checkbox()
            else:
                voice_command_page.click_english_checkbox()
            self.assertTrue(voice_command_page.get_save_button_enabled(), "button \"Save\" isn't enable after changing language checkbox")

            self.assertEqual(voice_command_page.get_voice_assistant_text(), self.get_string("voice_command_tip", now_language), "Text \"Voice assistant (we provide 5 commands\" is not properly displayed")
            self.assertEqual(voice_command_page.get_music_command_title(), self.get_string("voice_command_music_section_title", now_language), "Text \"Music\" is not properly displayed")
            self.assertEqual(voice_command_page.get_music_command_content(), self.get_string("voice_command_music_section_example1", now_language).replace('\\"', '"') + "\n" + self.get_string("voice_command_music_section_example2", now_language).replace('\\"', '"'), "Music Command Text is not properly displayed")
            self.assertEqual(voice_command_page.get_volume_command_title(), self.get_string("voice_command_volume_section_title", now_language), "Text \"Volume\" is not properly displayed")
            self.assertEqual(voice_command_page.get_volume_command_content(), self.get_string("voice_command_volume_section_example1", now_language).replace('\\"', '"') + "\n" + self.get_string("voice_command_volume_section_example2", now_language).replace('\\"', '"'), "Volume Command Text is not properly displayed")
            self.assertEqual(voice_command_page.get_camera_command_title(), self.get_string("voice_command_camera_section_title", now_language), "Text \"Camera\" is not properly displayed")
            self.assertEqual(voice_command_page.get_camera_command_content(), self.get_string("voice_command_camera_section_example1", now_language).replace('\\"', '"') + "\n", "Camera Command Text is not properly displayed")

            '''Verify Discard dialog'''
            voice_command_page.click_back()
            self.assertTrue(voice_command_page.has_discard_dialog(), "\"Discard Voice Commands settings\" window doesn't appear")
            self.assertEqual(voice_command_page.get_discard_dialog_title(), self.get_string("voice_commands_discard"), "Text \"Discard Voice Commands settings?\" is not properly displayed")
            self.assertEqual(voice_command_page.get_discard_dialog_yes_button_text(), self.get_string("yes"), "button \"Yes\" is not properly displayed")
            self.assertEqual(voice_command_page.get_discard_dialog_no_button_text(), self.get_string("no"), "button \"No\" is not properly displayed")

            '''Click no button and check if settings are not discarded'''
            voice_command_page.click_discard_dialog_no()
            self.assertTrue(voice_command_page.is_in_voice_command_page(), "Canceling discard dialog doesn't return to Voice Command Page")
            self.assertNotEqual(before_english_checkbox_status, voice_command_page.get_english_checkbox_status(), "Changing English checkbox is discarded")
            self.assertNotEqual(before_chinese_checkbox_status, voice_command_page.get_chinese_checkbox_status(), "Changing Chinese checkbox is discarded")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_changing_language_save(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            voice_service_page = VoiceServicePage(self.driver)
            voice_command_page = VoiceCommandPage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Baby Monitor Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Voice Service Page'''
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")

            '''Go to Voice Command Page'''
            if not voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            voice_service_page.click_voice_command_button()
            self.assertTrue(voice_command_page.is_in_voice_command_page(), "Can't go to Voice Command Page")

            '''Verify Voice Command Page'''
            self.assertEqual(voice_command_page.get_page_title(), self.get_string("local_voice_commands_settings_title"), "Text \"Local Voice Commands\" is not properly displayed")
            self.assertEqual(voice_command_page.get_save_button_text(), self.get_string("save"), "button \"Save\" is not properly displayed")
            self.assertEqual(voice_command_page.get_choosing_language_text(), self.get_string("voice_command_language"), "Text \"Language\" is not properly displayed")
            self.assertEqual(voice_command_page.get_english_text(), self.get_string("voice_command_language_english"), "Text \"English\" is not properly displayed")
            self.assertEqual(voice_command_page.get_chinese_text(), self.get_string("voice_command_language_chinese"), "Text \"Chinese\" is not properly displayed")

            before_english_checkbox_status = voice_command_page.get_english_checkbox_status()
            before_chinese_checkbox_status = voice_command_page.get_chinese_checkbox_status()
            self.assertNotEqual(before_english_checkbox_status, before_chinese_checkbox_status, "English and Chinese checkboxes can't be in the same status")

            '''Click English checkbox or Chinese checkbox'''
            now_language = "tw text" if before_english_checkbox_status else "en-us text"
            if before_english_checkbox_status:
                voice_command_page.click_chinese_checkbox()
            else:
                voice_command_page.click_english_checkbox()
            self.assertTrue(voice_command_page.get_save_button_enabled(), "button \"Save\" isn't enable after changing language checkbox")

            self.assertEqual(voice_command_page.get_voice_assistant_text(), self.get_string("voice_command_tip", now_language), "Text \"Voice assistant (we provide 5 commands\" is not properly displayed")
            self.assertEqual(voice_command_page.get_music_command_title(), self.get_string("voice_command_music_section_title", now_language), "Text \"Music\" is not properly displayed")
            self.assertEqual(voice_command_page.get_music_command_content(), self.get_string("voice_command_music_section_example1", now_language).replace('\\"', '"') + "\n" + self.get_string("voice_command_music_section_example2", now_language).replace('\\"', '"'), "Music Command Text is not properly displayed")
            self.assertEqual(voice_command_page.get_volume_command_title(), self.get_string("voice_command_volume_section_title", now_language), "Text \"Volume\" is not properly displayed")
            self.assertEqual(voice_command_page.get_volume_command_content(), self.get_string("voice_command_volume_section_example1", now_language).replace('\\"', '"') + "\n" + self.get_string("voice_command_volume_section_example2", now_language).replace('\\"', '"'), "Volume Command Text is not properly displayed")
            self.assertEqual(voice_command_page.get_camera_command_title(), self.get_string("voice_command_camera_section_title", now_language), "Text \"Camera\" is not properly displayed")
            self.assertEqual(voice_command_page.get_camera_command_content(), self.get_string("voice_command_camera_section_example1", now_language).replace('\\"', '"') + "\n", "Camera Command Text is not properly displayed")

            '''Click save button and check if settings are saved'''
            voice_command_page.click_save()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Saving setting doesn't automatically return to Voice Service Page")
            voice_service_page.click_voice_command_button()
            self.assertTrue(voice_command_page.is_in_voice_command_page(), "Can't go to Voice Command Page")
            self.assertNotEqual(before_english_checkbox_status, voice_command_page.get_english_checkbox_status(), "Changing English checkbox is not saved")
            self.assertNotEqual(before_chinese_checkbox_status, voice_command_page.get_chinese_checkbox_status(), "Changing Chinese checkbox is not saved")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_no_changing_language(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            pixsee_settings_page = PixseeSettingsPage(self.driver)
            voice_service_page = VoiceServicePage(self.driver)
            voice_command_page = VoiceCommandPage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Baby Monitor Page")

            '''Go to Pixsee Settings Page'''
            menu_page.click_settings()
            self.assertTrue(pixsee_settings_page.is_in_settings(), "Can't go to Pixsee Settings Page")

            '''Go to Voice Service Page'''
            pixsee_settings_page.click_VoiceService()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Can't go to Voice Service Page")

            '''Go to Voice Command Page'''
            if not voice_service_page.get_detection_switch_status():
                voice_service_page.click_detection_switch()
            voice_service_page.click_voice_command_button()
            self.assertTrue(voice_command_page.is_in_voice_command_page(), "Can't go to Voice Command Page")

            '''Verify Voice Command Page'''
            self.assertEqual(voice_command_page.get_page_title(), self.get_string("local_voice_commands_settings_title"), "Text \"Local Voice Commands\" is not properly displayed")
            self.assertEqual(voice_command_page.get_save_button_text(), self.get_string("save"), "button \"Save\" is not properly displayed")
            self.assertEqual(voice_command_page.get_choosing_language_text(), self.get_string("voice_command_language"), "Text \"Language\" is not properly displayed")
            self.assertEqual(voice_command_page.get_english_text(), self.get_string("voice_command_language_english"), "Text \"English\" is not properly displayed")
            self.assertEqual(voice_command_page.get_chinese_text(), self.get_string("voice_command_language_chinese"), "Text \"Chinese\" is not properly displayed")

            english_checkbox_status = voice_command_page.get_english_checkbox_status()
            chinese_checkbox_status = voice_command_page.get_chinese_checkbox_status()
            self.assertNotEqual(english_checkbox_status, chinese_checkbox_status, "English and Chinese checkboxes can't be in the same status")

            '''Click English checkbox or Chinese checkbox'''
            now_language = "tw text" if chinese_checkbox_status else "en-us text"
            self.assertFalse(voice_command_page.get_save_button_enabled(), "button \"Save\" is enable before changing language checkbox")

            self.assertEqual(voice_command_page.get_voice_assistant_text(), self.get_string("voice_command_tip", now_language), "Text \"Voice assistant (we provide 5 commands\" is not properly displayed")
            self.assertEqual(voice_command_page.get_music_command_title(), self.get_string("voice_command_music_section_title", now_language), "Text \"Music\" is not properly displayed")
            self.assertEqual(voice_command_page.get_music_command_content(), self.get_string("voice_command_music_section_example1", now_language).replace('\\"', '"') + "\n" + self.get_string("voice_command_music_section_example2", now_language).replace('\\"', '"'), "Music Command Text is not properly displayed")
            self.assertEqual(voice_command_page.get_volume_command_title(), self.get_string("voice_command_volume_section_title", now_language), "Text \"Volume\" is not properly displayed")
            self.assertEqual(voice_command_page.get_volume_command_content(), self.get_string("voice_command_volume_section_example1", now_language).replace('\\"', '"') + "\n" + self.get_string("voice_command_volume_section_example2", now_language).replace('\\"', '"'), "Volume Command Text is not properly displayed")
            self.assertEqual(voice_command_page.get_camera_command_title(), self.get_string("voice_command_camera_section_title", now_language), "Text \"Camera\" is not properly displayed")
            self.assertEqual(voice_command_page.get_camera_command_content(), self.get_string("voice_command_camera_section_example1", now_language).replace('\\"', '"') + "\n", "Camera Command Text is not properly displayed")

            '''Click back button and check if settings aren't changed'''
            voice_command_page.click_back()
            self.assertTrue(voice_service_page.is_in_voice_service_page(), "Clicking back button doesn't return to Voice Service Page")
            voice_service_page.click_voice_command_button()
            self.assertTrue(voice_command_page.is_in_voice_command_page(), "Can't go to Voice Command Page")
            self.assertEqual(english_checkbox_status, voice_command_page.get_english_checkbox_status(),  "English checkbox is changed after clicking back button")
            self.assertEqual(chinese_checkbox_status, voice_command_page.get_chinese_checkbox_status(), "Chinese checkbox is changed after clicking back button")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()