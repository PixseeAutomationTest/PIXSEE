from pages.base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_page import MenuPage
from pages.menu_pages.about_page import AboutPage

class AboutTest(BaseTestCase):
    def test_about_pixsee(self):
        self.open_app()

        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        about_page = AboutPage(self.driver)

        try:
            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")

            '''Go to About Page'''
            menu_page.click_about()
            self.assertTrue(about_page.is_in_about_page(), "Can't go to About Page")

            '''Verify About Page content'''
            self.assertEqual(about_page.get_page_title_text(), self.get_string("about_menu_bar_title"))
            self.assertEqual(about_page.get_about_pixsee_text(), self.get_string("about_pixsee_bar_title"))
            self.assertEqual(about_page.get_terms_of_service_text(), self.get_string("about_terms_bar_title"))
            self.assertEqual(about_page.get_privacy_policy_text(), self.get_string("privacy_policy"))
            self.assertEqual(about_page.get_app_version_text().split(':')[0] + ": ", self.get_string("about_app_version").split('%')[0])
            self.assertEqual(about_page.get_camera_version_text().split(':')[0] + ": ", self.get_string("about_device_version").split('%')[0])

            '''Click Privacy Policy and verify content'''
            about_page.click_about_pixsee()
            self.assertTrue(about_page.is_in_about_pixsee_website(), "Can't go to About Pixsee website")
            '''Go back to About Page from Privacy Policy website'''
            self.go_back()
            self.assertTrue(about_page.is_in_about_page(), "Can't return to About Page from Privacy Policy website")


        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_privacy_policy(self):
        self.open_app()

        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        about_page = AboutPage(self.driver)

        try:
            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")

            '''Go to About Page'''
            menu_page.click_about()
            self.assertTrue(about_page.is_in_about_page(), "Can't go to About Page")

            '''Verify About Page content'''
            self.assertEqual(about_page.get_page_title_text(), self.get_string("about_menu_bar_title"))
            self.assertEqual(about_page.get_about_pixsee_text(), self.get_string("about_pixsee_bar_title"))
            self.assertEqual(about_page.get_terms_of_service_text(), self.get_string("about_terms_bar_title"))
            self.assertEqual(about_page.get_privacy_policy_text(), self.get_string("privacy_policy"))
            self.assertEqual(about_page.get_app_version_text().split(':')[0] + ": ", self.get_string("about_app_version").split('%')[0])
            self.assertEqual(about_page.get_camera_version_text().split(':')[0] + ": ", self.get_string("about_device_version").split('%')[0])

            '''Click Privacy Policy and verify content'''
            about_page.click_privacy_policy()
            self.assertEqual(about_page.get_website_title_text(), self.get_string("privacy_policy"))
            self.assertTrue(about_page.is_in_embedded_website(), "Can't go to Privacy Policy website")
            '''Go back to About Page from Privacy Policy website'''
            about_page.click_website_return()
            self.assertTrue(about_page.is_in_about_page(), "Can't return to About Page from Privacy Policy website")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()

    def test_terms_of_service(self):
        self.open_app()

        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        about_page = AboutPage(self.driver)

        try:
            '''Go to Menu Page'''
            baby_monitor_page.click_home()
            self.assertTrue(menu_page.is_in_menu_page(), "Can't go to Menu Page")

            '''Go to About Page'''
            menu_page.click_about()
            self.assertTrue(about_page.is_in_about_page(), "Can't go to About Page")

            '''Verify About Page content'''
            self.assertEqual(about_page.get_page_title_text(), self.get_string("about_menu_bar_title"))
            self.assertEqual(about_page.get_about_pixsee_text(), self.get_string("about_pixsee_bar_title"))
            self.assertEqual(about_page.get_terms_of_service_text(), self.get_string("about_terms_bar_title"))
            self.assertEqual(about_page.get_privacy_policy_text(), self.get_string("privacy_policy"))
            self.assertEqual(about_page.get_app_version_text().split(':')[0] + ": ", self.get_string("about_app_version").split('%')[0])
            self.assertEqual(about_page.get_camera_version_text().split(':')[0] + ": ", self.get_string("about_device_version").split('%')[0])

            '''Click Terms Of Service and verify content'''
            about_page.click_terms_of_service()
            self.assertEqual(about_page.get_website_title_text(), self.get_string("about_terms_bar_title"))
            self.assertTrue(about_page.is_in_embedded_website(), "Can't go to Terms Of Service website")
            '''Go back to About Page from Terms Of Service website'''
            about_page.click_website_return()
            self.assertTrue(about_page.is_in_about_page(), "Can't return to About Page from Terms Of Service website")

        except AssertionError as ae:
            print(f"Test failed with assertion error: {ae}")
            raise ae
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
        finally:
            self.shutdown_app()