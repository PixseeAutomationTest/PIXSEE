from pages.base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.baby_timeline_page import BabyTimelinePage
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.add_baby_profile_page import AddBabyProfilePage
from pages.menu_pages.edit_baby_profile_pages.edit_baby_profile_page import EditBabyProfilePage
import random

class AddBabyTest(BaseTestCase):

    def test_save_add_baby_profile(self):
        try:
            self.open_app()

            baby_monitor_page = BabyMonitorPage(self.driver)
            baby_timeline_page = BabyTimelinePage(self.driver)
            menu_page = MenuPage(self.driver)
            add_baby_profile_page = AddBabyProfilePage(self.driver)
            edit_baby_profile_page = EditBabyProfilePage(self.driver)

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
            self.assertTrue(add_baby_profile_page.get_gender_boy_status(), "Gender boy should be selected after clicking gender boy")
            self.assertFalse(add_baby_profile_page.get_gender_girl_status(), "Gender girl should not be selected after clicking gender boy")
            add_baby_profile_page.click_gender_girl()
            self.assertFalse(add_baby_profile_page.get_gender_boy_status(), "Gender boy should not be selected after clicking gender girl")
            self.assertTrue(add_baby_profile_page.get_gender_girl_status(), "Gender girl should be selected after clicking gender girl")

            '''Input name'''
            add_baby_profile_page.input_name("Test_Baby 01")
            new_baby_name = add_baby_profile_page.get_name_text()

            #TODO: Only click confirm button, not change date
            '''Edit birthday'''
            add_baby_profile_page.click_birthday()
            self.assertTrue(add_baby_profile_page.has_calendar(), "Calendar is not displayed")
            add_baby_profile_page.click_calendar_done()
            new_baby_birthday = add_baby_profile_page.get_birthday_text()

            '''Select nation'''
            add_baby_profile_page.select_nation(random.randint(1, 58))
            new_baby_nation = add_baby_profile_page.get_nation_text()

            '''Select relative'''
            add_baby_profile_page.select_relative(random.randint(1, 10))
            new_baby_relative = add_baby_profile_page.get_relative_text()

            '''Save profile and go to Edit Baby Profile Page'''
            add_baby_profile_page.click_finish()
            self.assertTrue(baby_timeline_page.is_in_baby_timeline_page(), "Can't automatically go to Baby Timeline Page after adding a baby profile")
            baby_timeline_page.click_menu()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page from Baby Timeline Page")
            menu_page.click_baby_edit()
            self.assertTrue(edit_baby_profile_page.is_in_edit_baby_profile_page(), "Can't go to Edit Baby Profile Page")

            '''Check the contents about the new baby profile'''
            self.assertEqual(edit_baby_profile_page.get_baby_name_text(), new_baby_name, "Baby's name is not properly displayed in Edit Baby Profile Page")
            self.assertEqual(edit_baby_profile_page.get_baby_birthday_text(), new_baby_birthday, "Baby's birthday is not properly displayed in Edit Baby Profile Page")
            self.assertEqual(edit_baby_profile_page.get_nation_text(), new_baby_nation, "Baby's nation is not properly displayed in Edit Baby Profile Page")
            self.assertEqual(edit_baby_profile_page.get_relative_text(), new_baby_relative, "Baby's relative is not properly displayed in Edit Baby Profile Page")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()
