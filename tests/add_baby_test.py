from pages.base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.add_baby_profile_page import AddBabyProfilePage

class AddBabyTest(BaseTestCase):

    def test_save_add_baby_profile(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            menu_page = MenuPage(self.driver)
            add_baby_profile_page = AddBabyProfilePage(self.driver)

            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")

            '''Go to Add Baby Profile Page'''
            menu_page.click_baby_add()
            self.assertTrue(add_baby_profile_page.is_in_add_baby_profile_page(), "Can't go to Add Baby Profile Page")

            '''Verify Add Baby Profile Page'''
            self.assertEqual(add_baby_profile_page.get_page_title(), self.get_string("baby_profile_title"), "Text \"Baby's profile\" is not properly displayed")
            self.assertTrue(add_baby_profile_page.get_gender_boy_status() or add_baby_profile_page.get_gender_girl_status(), "Boy button or Girl button should be selected")
            self.assertNotEqual(add_baby_profile_page.get_gender_boy_status(), add_baby_profile_page.get_gender_girl_status(), "Boy button and Girl button should not be selected at the same time")
            self.assertEqual(add_baby_profile_page.get_name_hint(), self.get_string("baby_profile_name"), "Hint \"Name\" is not properly displayed")
            self.assertEqual(add_baby_profile_page.get_birthday_hint(), self.get_string("baby_profile_birthday"), "Hint \"Birthday\" is not properly displayed")
            self.assertEqual(add_baby_profile_page.get_finish_button_text(), self.get_string("save"), "Text \"Save\" is not properly displayed")
            self.assertEqual(add_baby_profile_page.get_message_text(), self.get_string("baby_profile_footer_message"), "Text \"You can change the profile from settings\" is not properly displayed")

            '''Select one gender and verify their status'''
            add_baby_profile_page.click_gender_boy()
            self.assertTrue(add_baby_profile_page.get_gender_boy_status(), "Gender boy should be selected")
            self.assertFalse(add_baby_profile_page.get_gender_girl_status(), "Gender girl should not be selected")
            add_baby_profile_page.click_gender_girl()
            self.assertFalse(add_baby_profile_page.get_gender_boy_status(), "Gender boy should not be selected")
            self.assertTrue(add_baby_profile_page.get_gender_girl_status(), "Gender girl should be selected")

            '''Input name'''
            add_baby_profile_page.input_name("Test Baby01")

            #TODO: Only click confirm button, not change date
            '''Edit birthday and check it'''
            add_baby_profile_page.click_birthday()
            self.assertTrue(add_baby_profile_page.has_calendar(), "Calendar is not displayed")
            add_baby_profile_page.click_calendar_done()

            #TODO: No change nation
            '''Select nation and check it'''
            # add_baby_profile_page.click_nation()
            # self.assertTrue(add_baby_profile_page.has_list(), "Nation list is not displayed")
            # print(add_baby_profile_page.get_list_text(10))

            # TODO: No change relative
            '''Select relative and check it'''

            #TODO: Incomplete Verifying
            '''Save profile and verify it'''
            add_baby_profile_page.click_finish()


        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()
