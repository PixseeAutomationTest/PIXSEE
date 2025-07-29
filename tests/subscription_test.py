import time

from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.subscription_pages.subscription_page import SubscriptionPage


class SubscriptionCase(BaseTestCase):
    def setUp(self):
        super().setUp(no_reset=False)
    def test_01_subscription_check_text(self):
        subscription_page = SubscriptionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()

        self.skip_first_four_tutor()
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()
        menu_page.click_subscription()
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
            hint = self.get_string("new_subscription_gold_star_plan")
            self.assertEqual(header, hint)
            print("Subscription header text right")
        except AssertionError:
            print("Subscription header text wrong")
        # check title text
        # check by color
        light_blue_range = ((0, 0, 0), (150, 255, 255))
        light_orange_range = ((151, 0, 0), (255, 255, 255))
        x, y = subscription_page.find_stream_left_top()
        result = subscription_page.is_color_in_range(x, y, light_orange_range)
        # check gold star color
        if result:
            print("gold star color is correct")
        else:
            print("gold star color is wrong")
        self.right_wipe()
        time.sleep(1)
        x, y = subscription_page.find_stream_left_top()
        result = subscription_page.is_color_in_range(x, y, light_blue_range)
        # check standard color
        if result:
            print("standard color is correct")
        else:
            print("standard color is wrong")
    def test_02_subscription_click_x(self):
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        login_page = LoginPage(self.driver)
        subscription_page = SubscriptionPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()

        self.skip_first_four_tutor()
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()
        menu_page.click_subscription()
        subscription_page.click_x()
        # check if back to baby monitor page
        try:
            self.assertTrue(baby_monitor_page.is_in_baby_monitor_page())
            print("x works, back to baby monitor page")
        except AssertionError:
            print("x not works, not in baby monitor page")
            raise AssertionError("Not in baby monitor page after click x")
    def test_04_subscription_information(self):
        subscription_video = SubscriptionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)
        subscription_page = SubscriptionPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()

        self.skip_first_four_tutor()
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()
        menu_page.click_subscription()
        subscription_page.click_info()
        # check if in subscription information page
        try:
            self.assertTrue(subscription_video.is_in_chrome())
            print("In subscription information page")
        except AssertionError:
            print("Not in subscription information page")
    def test_05_subscription_couponself(self):
        subscription_video = SubscriptionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)


        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page.click_home()

        # skip menu tutor
        menu_page.click_logout()
        menu_page.click_subscription()
        subscription_video.click_coupon()
        # check if in coupon dialog
    def test_05_subscription_video_check_text(self):
        subscription_video = SubscriptionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()

        menu_page.click_settings()
        pixsee_settings_page.click_subscription_video()
        # ensure time lapse video switch is on
        if subscription_video.is_switch_on() == "true":
            pass
        else:
            subscription_video.click_switch()

        # check text
        try:
            mode = subscription_video.recording_mode_text()
            hint = self.get_string("subscription_recording_mode")
            self.assertEqual(mode, hint)
            print("subscription_video recording mode text right")
        except AssertionError:
            print("subscription_video recording mode text wrong")
        try:
            time_span = subscription_video.time_span_text()
            hint = self.get_string("subscription_time_span")
            self.assertEqual(time_span, hint)
            print("subscription_video time span text right")
        except AssertionError:
            print("subscription_video time span text wrong")
        try:
            start_time = subscription_video.starting_time_text()
            hint = self.get_string("new_subscription_starting_time")
            self.assertEqual(start_time, hint)
            print("subscription_video start time text right")
        except AssertionError:
            print("subscription_video start time text wrong")
        try:
            entire_time = subscription_video.entire_time_text()
            hint = self.get_string("new_subscription_entire_time")
            self.assertEqual(entire_time, hint)
            print("subscription_video entire time text right")
        except AssertionError:
            print("subscription_video entire time text wrong")
        try:
            people_in_view = subscription_video.people_in_view_text()
            hint = self.get_string("new_subscription_people_in_view")
            self.assertEqual(people_in_view, hint)
            print("subscription_video people in view text right")
        except AssertionError:
            print("subscription_video people in view text wrong")
        try:
            twelve_hour = subscription_video.twelve_hours_text()
            hint = self.get_string("new_subscription_12_hours")
            self.assertEqual(twelve_hour, hint)
            print("subscription_video twelve hour text right")
        except AssertionError:
            print("subscription_video twelve hour text wrong")
        try:
            twenty_four_hour = subscription_video.twenty_four_hours_text()
            hint = self.get_string("new_subscription_24_hours")
            self.assertEqual(twenty_four_hour, hint)
            print("subscription_video twenty four hour text right")
        except AssertionError:
            print("subscription_video twenty four hour text wrong")
    def test_06_subscription_video_checkbox(self):
        subscription_video = SubscriptionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()

        menu_page.click_settings()
        pixsee_settings_page.click_subscription_video()
        # ensure time lapse video switch is on
        if subscription_video.is_switch_on() == "true":
            pass
        else:
            subscription_video.click_switch()
        # check if recording mode checkbox is checked
        subscription_video.click_entire_time_checkbox()
        time.sleep(1)
        self.tap_on_visibility(subscription_video.HumanWarning, "Entire Time", False)
        subscription_video.click_people_in_view_checkbox()
        time.sleep(1)
        self.tap_on_visibility(subscription_video.HumanWarning, "People in view", True)
        # check if timespan checkbox is checked
        subscription_video.click_twelve_hours_checkbox()
        try:
            self.assertTrue(subscription_video.is_twelve_hours_clicked())
            print("Twelve hours checkbox is checked")
        except AssertionError:
            print("Twelve hours checkbox is not checked")
            raise AssertionError("Twelve hours checkbox is not checked")
        subscription_video.click_twenty_four_hours_checkbox()
        try:
            self.assertTrue(subscription_video.is_twenty_four_hours_clicked())
            print("Twenty four hours checkbox is checked")
        except AssertionError:
            print("Twenty four hours checkbox is not checked")
            raise AssertionError("Twenty four hours checkbox is not checked")
    def test_07_subscription_video_select_time(self):
        subscription_video = SubscriptionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()

        menu_page.click_settings()
        pixsee_settings_page.click_subscription_video()
        # ensure time lapse video switch is on
        if subscription_video.is_switch_on() == "true":
            pass
        else:
            subscription_video.click_switch()
        # check enter timer
        subscription_video.click_timer()
        try:
            self.assertTrue(subscription_video.is_in_timer())
            print("In time selecter")
        except AssertionError:
            print("Not in time selecter")
            raise AssertionError("Not in time selecter")
        # check start time block's clickable and confirm
        current = subscription_video.timer_text()
        subscription_video.click_timer()
        try:
            self.assertTrue(subscription_video.is_in_timer())
            print("In time selecter")
            # check cancel,confirm text
            try:
                cancel = subscription_video.cancel_txt()
                hint = self.get_string("cancel")
                self.assertEqual(cancel, hint)
                print("Start time block cancel text right")
            except AssertionError:
                print("Start time block cancel text wrong")
            try:
                confirm = subscription_video.confirm_txt()
                hint = self.get_string("code_verification_verify_button")
                self.assertEqual(confirm, hint)
                print("Start time block confirm text right")
            except AssertionError:
                print("Start time block confirm text wrong")
            # check time scrollable
            subscription_video.change_hour_by_scroll()
            subscription_video.change_am_to_pm_by_scroll()
            subscription_video.click_confirm()
            after = subscription_video.timer_text()
            try:
                self.assertNotEqual(current, after)
                print("timer confirm function success")
            except AssertionError:
                print("timer confirm function failed")
                raise AssertionError("timer confirm function failed, start time not changed")
        except AssertionError:
            print("Not in time selecter")
            raise AssertionError("Not in time selecter")
    def test_08_subscription_video_save(self):
        subscription_video = SubscriptionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()

        menu_page.click_settings()
        origin_status = pixsee_settings_page.subscription_video_status_text()
        pixsee_settings_page.click_subscription_video()
        # check save enable = false
        try:
            self.assertFalse(subscription_video.is_save_enable())
            print("Save diable test pass")
        except AssertionError:
            print("Save diable test failed")
            raise AssertionError("Save diable test failed")

        subscription_video.click_switch()
        # save
        subscription_video.click_save()
        new_status = pixsee_settings_page.subscription_video_status_text()
        if origin_status != new_status:
            print("save function success")
        else:
            print("save function failed")
            raise AssertionError("save function failed, status not changed")
    def test_09_subscription_video_back(self):
        subscription_video = SubscriptionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()

        menu_page.click_settings()
        pixsee_settings_page.click_subscription_video()
        # check back to pixsee settings page
        subscription_video.click_back()
        try:
            self.assertTrue(pixsee_settings_page.is_in_settings())
            print("Back to pixsee settings page")
        except AssertionError:
            print("Not in pixsee settings page")
            raise AssertionError("Not in pixsee settings page")
    def test_10_subscription_video_discard_dialog(self):
        subscription_video = SubscriptionPage(self.driver)
        menu_page = MenuPage(self.driver)
        baby_monitor_page = BabyMonitorPage(self.driver)
        pixsee_settings_page = PixseeSettingsPage(self.driver)
        login_page = LoginPage(self.driver)

        login_page.login(self.account(),self.password())
        baby_monitor_page.is_in_baby_monitor_page()
        self.skip_first_four_tutor()
        baby_monitor_page.click_home()
        # skip menu tutor
        menu_page.click_logout()

        menu_page.click_settings()
        pixsee_settings_page.click_subscription_video()
        subscription_video.click_switch()
        # check discard dialog
        try:
            self.assertTrue(subscription_video.is_in_discard_dialog())
            print("In discard dialog")
            # check discard dialog title
            try:
                discard_title = subscription_video.discard_message_txt()
                hint = self.get_string("timelapse_discard")
                self.assertEqual(discard_title, hint)
                print("Discard dialog title right")
            except AssertionError:
                print("Discard dialog title wrong")
            # check discard dialog cancel text
            try:
                discard_cancel = subscription_video.discard_no_txt()
                hint = self.get_string("no")
                self.assertEqual(discard_cancel, hint)
                print("Discard dialog cancel text right")
            except AssertionError:
                print("Discard dialog cancel text wrong")
            # check discard dialog confirm text
            try:
                discard_confirm = subscription_video.discard_yes_txt()
                hint = self.get_string("yes")
                self.assertEqual(discard_confirm, hint)
                print("Discard dialog confirm text right")
            except AssertionError:
                print("Discard dialog confirm text wrong")
            # click confirm
            subscription_video.click_discard_yes()
            # back to pixsee settings page
            try:
                self.assertTrue(pixsee_settings_page.is_in_settings())
                print("Back to pixsee settings page after discard")
            except AssertionError:
                print("Not in pixsee settings page after discard")
                raise AssertionError("Not in pixsee settings page after discard")
        except AssertionError:
            print("Not in discard dialog")
            raise AssertionError("Not in discard dialog")















































# check popup dialog
try:
	self.assertTrue(subscription_page.is_in_prize_plan_dialog())
	print("gold star button works, in prize plan dialog")
except AssertionError:
	print("gold star button not works, not in prize plan dialog")
	raise AssertionError("Not in prize plan dialog")
