from base import BaseTestCase

from pages.baby_monitor_page import BabyMonitorPage

class BabyMonitorTestCase(BaseTestCase):
    def test_change_camera_mode(self):
        baby_monitor_page = BabyMonitorPage(self.driver)
        baby_monitor_page.click()
