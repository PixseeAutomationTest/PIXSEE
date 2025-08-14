import time

from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.menu_pages.pixsee_settings_pages.area_detection_page import AreaDetectionPage



class Reset(BaseTestCase):
        def setUp(self):
                super().setUp(no_reset=False)


        def test_wipe(self):
                area_detection_page = AreaDetectionPage(self.driver)
                pixsee_settings_page = PixseeSettingsPage(self.driver)

                print("⚠️ Medium checkbox is not clickable")
