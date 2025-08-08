import time
import re
from pages.menu_pages.menu_page import MenuPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.subscription_pages.already_subscription_page import SubscriptionPage2


class SubscriptionCase2(BaseTestCase):
    def setUp(self):
        super().setUp(no_reset=True)
        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        subscription_page = SubscriptionPage2(self.driver)
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
    def test_01_subscription_check_text(self):
        subscription_page = SubscriptionPage2(self.driver)
        menu_page = MenuPage(self.driver)

        # check if in subscription page
        try:
            self.assertTrue(subscription_page.is_in_subscription_page())
            print("In subscription page")
        except AssertionError:
            print("Not in subscription page")
            raise AssertionError("Not in subscription page")
        # check text
        try:
            current_plan = subscription_page.current_plan_text()
            hint = self.get_string("current_plan")
            pattern = "^" + re.escape(hint).replace("%s", r".+") + "$"
            self.assertRegex(current_plan, pattern)
            # self.assertEqual(current_plan, hint)
            print("Subscription current plan text right")
        except AssertionError:
            raise AssertionError("Subscription current plan text wrong")
        try:
            payment_method = subscription_page.payment_method_text()
            hint = self.get_string("subscribed_payment_method")
            self.assertEqual(payment_method, hint)
            print("Subscription payment method text right")
        except AssertionError:
            raise AssertionError("Subscription payment method text wrong")
        try:
            in_app_purchase = subscription_page.in_app_purchase_text()
            hint = self.get_string("subscribed_store_google")
            self.assertEqual(in_app_purchase, hint)
            print("Subscription in app purchase text right")
        except AssertionError:
            raise AssertionError("Subscription in app purchase text wrong")
        try:
            expiration = subscription_page.expiration_text()
            hint = self.get_string("subscribed_expiration_date")
            pattern = "^" + re.escape(hint).replace("%s", r".+") + "$"
            self.assertRegex(expiration, pattern)
            # self.assertEqual(expiration, hint)
            print("Subscription expiration text right")
        except AssertionError:
            raise AssertionError("Subscription expiration text wrong")
        try:
            promotion = subscription_page.promotion_text()
            hint = self.get_string("subscribed_latest_news_and_promotions")
            self.assertEqual(promotion, hint)
            print("Subscription promotion text right")
        except AssertionError:
            raise AssertionError("Subscription promotion text wrong")
    # start from subscription page
    def test_02_subscription_click_back(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        subscription_page = SubscriptionPage2(self.driver)

        subscription_page.click_back()
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
        subscription_page = SubscriptionPage2(self.driver)
        menu_page = MenuPage(self.driver)

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
        subscription_page = SubscriptionPage2(self.driver)
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
            for i in range(0, 7):
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
    def test_05_subscription_button(self):
        subscription_page = SubscriptionPage2(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)

        subscription_page.click_change()
        # check popup dialog
        try:
            self.assertTrue(subscription_page.is_in_price_plan_dialog())
            print("gold star button works, in prize plan dialog")
        except AssertionError:
            raise AssertionError("Not in prize plan dialog")
        self.go_back()
        # check checkbox checkable
        try:
            self.assertTrue(subscription_page.is_checkbox_checkable())
            print("Checkbox is checkable")
        except AssertionError:
            raise AssertionError("Checkbox is not checkable")
        # check ok button
        try:
            ok = subscription_page.ok_button_text()
            hint = self.get_string("ok")
            self.assertEqual(ok, hint)
            print("Ok button text right")
        except AssertionError:
            raise AssertionError("Ok button text wrong")
        subscription_page.click_ok()
        # check if back to baby monitor page
        try:
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page())
            print("Ok button works, back to baby monitor page")
        except AssertionError:
            raise AssertionError("Not in baby monitor page after click ok")
        baby_monitor_page.click_home()
        menu_page.click_subscription()



