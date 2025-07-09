from pages.base import BaseTestCase


class reset(BaseTestCase):


        def test_wipe(self):
                self.up_scroll()
                self.down_scroll()
                self.right_wipe()
                self.left_wipe()
                print("wipe test success")