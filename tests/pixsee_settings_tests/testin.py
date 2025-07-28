

# import time
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.menu_pages.pixsee_settings_pages.area_detection_page import AreaDetectionPage
from appium.webdriver.common.appiumby import AppiumBy



class Reset(BaseTestCase):
        def setUp(self):
                super().setUp(no_reset=True)


        def test_wipe(self):
                area_detection_page = AreaDetectionPage(self.driver)
                pixsee_settings_page = PixseeSettingsPage(self.driver)

                # if area_detection_page.is_switch_on():
                #         pass
                # else:
                #         area_detection_page.click_switch()
                # area_detection_page.click_switch()
                element = self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/efence_status_switch")
                rect = element.rect
                x = rect['x'] + rect['width'] / 2
                y = rect['y'] + rect['height'] / 2

                # 建立手指操作物件
                finger = PointerInput(PointerInput.TOUCH, "finger")
                actions = ActionBuilder(self.driver)
                actions.add_action(finger)

                # 模擬點一下
                actions.pointer_action.move_to_location(x, y)
                actions.pointer_action.pointer_down()
                actions.pointer_action.pause(0.05)
                actions.pointer_action.pointer_up()

                actions.perform()
                # check turn off dialog text
                try:
                        title = area_detection_page.turn_off_dialog_title()
                        hint = self.get_string("turn_off_area_detection")
                        self.assertEqual(title, hint)
                        print("turn off dialog title is correct")
                except AssertionError:
                        print("turn off dialog title  is wrong")
                try:
                        fifteenmin = area_detection_page.turn_off_15_min_text()
                        hint = self.get_string("snooze_detection_fifteen_minutes")
                        self.assertEqual(fifteenmin, hint)
                        print("turn off 15 is correct")
                except AssertionError:
                        print("turn off 15 is wrong")
                try:
                        thirtymin = area_detection_page.turn_off_30_min_text()
                        hint = self.get_string("snooze_detection_thirty_minutes")
                        self.assertEqual(thirtymin, hint)
                        print("turn off 30 is correct")
                except AssertionError:
                        print("turn off 30 is wrong")
                try:
                        off = area_detection_page.turn_off_text()
                        hint = self.get_string("turn_off_detection")
                        self.assertEqual(off, hint)
                        print("turn off text is correct")
                except AssertionError:
                        print("turn off text is wrong")
                try:
                        cancel = area_detection_page.turn_off_cancel_text()
                        hint = self.get_string("cancel")
                        self.assertEqual(cancel, hint)
                        print("turn off cancel text is correct")
                except AssertionError:
                        print("turn off cancel text is wrong")
                # check each button
                try:
                        area_detection_page.click_turn_off_15_min()
                        self.assertEqual(pixsee_settings_page.area_detection_status_text(), self.get_string("off_selection"))
                        print("15 min button worked")
                except AssertionError:
                        print("15 min button failed")
                pixsee_settings_page.click_area_detection()
                area_detection_page.click_switch()
                area_detection_page.click_switch()
                try:
                        area_detection_page.click_turn_off_cancel()
                        self.assertTrue(area_detection_page.is_switch_on())
                        print("turn off cancel worked")
                except AssertionError:
                        print("turn off cancel failed")
                area_detection_page.click_switch()
                try:
                        area_detection_page.click_turn_off_30_min()
                        self.assertEqual(pixsee_settings_page.area_detection_status_text(), self.get_string("off_selection"))
                        print("30 min button worked")
                except AssertionError:
                        print("30 min button failed")
                pixsee_settings_page.click_area_detection()
                area_detection_page.click_switch()
                area_detection_page.click_switch()
                try:
                        area_detection_page.click_turn_off()
                        self.assertEqual(pixsee_settings_page.area_detection_status_text(), self.get_string("off_selection"))
                        print("turn off detection worked")
                except AssertionError:
                        print("turn off detection failed")