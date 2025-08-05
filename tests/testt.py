from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages import add_baby_profile_page
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.add_baby_profile_page import AddBabyProfilePage
from pages.menu_pages.user_profile_pages.add_backup_email import AddBackupEmailPage


class reset(BaseTestCase):
        def setUp(self):
                super().setUp(no_reset=True)


        def test_wipe(self):

                self.open_app()

                add_backup_email_page = AddBackupEmailPage(self.driver)
                print(add_backup_email_page.has_error_message_text())
                '''00000000-0000-01d3-0000-035300000770'''
                '''00000000-0000-01d3-0000-035600000770'''
                '''00000000-0000-01d3-0000-035c00000770'''
                '''00000000-0000-01d3-0000-035e00000770'''
                '''00000000-0000-01d3-0000-036b00000770'''


