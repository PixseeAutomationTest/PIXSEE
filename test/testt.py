from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage


class reset(BaseTestCase):
        def setUp(self):
                super().setUp(no_reset=True)


        def test_wipe(self):
                # pixsee_friends_page = PixseeFriendsDetPage(self.driver)
                # try:
                #         title = pixsee_friends_page.title()
                #         hint = self.get_string("pixsee_friends_detection_title")
                #         self.assertEqual(title, hint)
                #         print("Friends detection title right")
                # except AssertionError:
                #         print("Friends detection title wrong")
                #         raise AssertionError("Friends detection title mismatch")
                baby = BabyMonitorPage(self.driver)
                baby.click_home()

