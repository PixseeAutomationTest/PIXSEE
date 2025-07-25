from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages import add_baby_profile_page
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.add_baby_profile_page import AddBabyProfilePage


class reset(BaseTestCase):
        def setUp(self):
                super().setUp(no_reset=True)


        def test_wipe(self):

                self.open_app()

                add_baby_profile_page = AddBabyProfilePage(self.driver)
                # add_baby_profile_page.select_birthday(2023, 7, 25)
                add_baby_profile_page.select_birthday(2018, 9, 30)

