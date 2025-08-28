import time

from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.subscription_pages.havent_subscription_page import SubscriptionPage1


class SubscriptionCase1(BaseTestCase):
    def __init__(self, methodName='runTest', language="zh", locale="TW"):
        super().__init__(methodName)
        self.language = language
        self.locale = locale

    def setUp(self):
        super().setUp(language=self.language, locale=self.locale)
        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        subscription_page = SubscriptionPage1(self.driver)
        try:
            while self.driver.current_package != self.driver.capabilities.get("appPackage"):
                self.driver.terminate_app(self.driver.current_package)
                self.open_app()
            if subscription_page.is_in_subscription_page():
                return
            elif not baby_monitor_page.is_in_baby_monitor_page():
                self.shutdown_app()
                self.open_app()
            print("Finish opening app.")
            baby_monitor_page.click_home()
            menu_page.click_subscription()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
    # start from subscription page
    def test_01_subscription_check_text_and_color(self):
        subscription_page = SubscriptionPage1(self.driver)
        menu_page = MenuPage(self.driver)

        # check if in subscription page
        try:
            self.assertTrue(subscription_page.is_in_subscription_page())
            print("In subscription page")
        except AssertionError:
            print("Not in subscription page")
            raise AssertionError("Not in subscription page")
        # check header text
        try:
            header = subscription_page.header_text()
            hint = self.get_string("subscription_bar_title")
            self.assertEqual(header, hint)
            print("Subscription header text right")
        except AssertionError:
            print("Subscription header text wrong")
        # check title text
        # check by color
        light_blue_range = ((0, 0, 0), (150, 255, 255))
        light_orange_range = ((151, 0, 0), (255, 255, 255))
        x, y = subscription_page.plan_2_color()
        result = subscription_page.is_color_in_range(x, y, light_orange_range)
        # check gold star plan color
        if result:
            print("gold star plan color is correct")
        else:
            raise AssertionError("gold star plan color is wrong")
        self.right_wipe()
        time.sleep(1)
        x, y = subscription_page.plan_1_color()
        result = subscription_page.is_color_in_range(x, y, light_blue_range)
        # check standard plan color
        if result:
            print("standard plan color is correct")
        else:
            raise AssertionError("standard plan color is wrong")
    # start from subscription page
    def test_02_subscription_click_x(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        subscription_page = SubscriptionPage1(self.driver)

        subscription_page.click_x()
        # check if back to baby monitor page
        try:
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page())
            print("x works, back to baby monitor page")
        except AssertionError:
            print("x not works, not in baby monitor page")
            raise AssertionError("Not in baby monitor page after click x")
        baby_monitor_page.click_home()
        menu_page.click_subscription()
    # start from subscription page
    def test_03_subscription_information(self):
        subscription_page = SubscriptionPage1(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        subscription_page = SubscriptionPage1(self.driver)

        subscription_page.click_info()
        # check if in subscription information page
        try:
            self.assertTrue(subscription_page.is_in_chrome())
            print("In subscription information page")
        except AssertionError:
            print("Not in subscription information page")
        self.go_back()
    # start from subscription page
    def test_04_subscription_coupon(self):
        subscription_page = SubscriptionPage1(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)

        subscription_page.click_coupon()
        # check if in coupon dialog
        try:
            self.assertTrue(subscription_page.is_in_coupon_dialog())
            print("In coupon dialog")
            # check coupon dialog title
            try:
                coupon_title = subscription_page.coupon_title_txt()
                hint = self.get_string("new_subscription_dialog_coupon_title")
                self.assertEqual(coupon_title, hint)
                print("Coupon dialog title right")
            except AssertionError:
                raise AssertionError("Coupon dialog title wrong")
            # check coupon dialog cancel text
            try:
                coupon_cancel = subscription_page.coupon_cancel_txt()
                hint = self.get_string("cancel")
                self.assertEqual(coupon_cancel, hint)
                print("Coupon dialog cancel text right")
            except AssertionError:
                raise AssertionError("Coupon dialog cancel text wrong")
            # check coupon dialog confirm text
            try:
                coupon_confirm = subscription_page.coupon_ok_txt()
                hint = self.get_string("ok")
                self.assertEqual(coupon_confirm, hint)
                print("Coupon dialog confirm text right")
            except AssertionError:
                raise AssertionError("Coupon dialog confirm text wrong")
            # check code enter field hint
            try:
                code_hint = subscription_page.coupon_code_hint()
                hint = self.get_string("new_subscription_dialog_coupon_edit_hint")
                self.assertEqual(code_hint, hint)
                print("Coupon code hint text right")
            except AssertionError:
                raise AssertionError("Coupon code hint text wrong")
            # enter code
            for i in range(0,7):
                subscription_page.enter_coupon_code(10 ** i)
                # check if ok able to click
                try:
                    self.assertFalse(subscription_page.is_coupon_ok_enabled())
                    print(f"{i} digit code test pass")
                except AssertionError:
                    raise AssertionError(f"{i} digit code test failed, ok button is enabled")
            subscription_page.enter_coupon_code("10000000")
            subscription_page.click_coupon_ok()
            # check wrong code
            try:
                wrong_code = subscription_page.coupon_wrong_code_text()
                hint = self.get_string("coupon_error_code_empty")
                self.assertEqual(wrong_code, hint)
                print("Wrong code text right")
            except AssertionError:
                raise AssertionError("Wrong code text wrong, coupon dialog not working")
            # click coupon information
            subscription_page.click_coupon_info()
            # check if in chrome
            try:
                self.assertTrue(subscription_page.is_in_chrome())
                print("In coupon information page")
            except AssertionError:
                raise AssertionError("Not in coupon information page after click coupon info")
            self.go_back()
            # click cancel
            subscription_page.click_coupon_cancel()
            # check if back to subscription page
            try:
                self.assertTrue(subscription_page.is_in_subscription_page())
                print("Back to subscription page after click cancel")
            except AssertionError:
                raise AssertionError("Not in subscription page after click cancel")
        except AssertionError:
                raise AssertionError("Not in coupon dialog after click coupon")
    # start from subscription page
    def test_05_subscription_page_check_gold_button(self):
        subscription_page = SubscriptionPage1(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)

        # check button text
        try:
            gold_star_button_text = subscription_page.gold_star_button_text()
            hint = self.get_string("new_subscription_gold_star_plan")
            self.assertEqual(gold_star_button_text, hint)
            print("Gold star button text right")
        except AssertionError:
            raise AssertionError("Gold star button text wrong")
        subscription_page.click_gold_star()
        # check popup dialog
        try:
            self.assertTrue(subscription_page.is_in_price_plan_dialog())
            print("gold star button works, in prize plan dialog")
        except AssertionError:
            print("gold star button not works, not in prize plan dialog")
            raise AssertionError("Not in prize plan dialog")














































