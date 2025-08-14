from pages.menu_pages.menu_page import MenuPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.assistant_pages.assistant_page import AssistantPage
from pages.menu_pages.assistant_pages.pixsee_cloud_page import PixseeCloudPage
from pages.menu_pages.subscription_pages.havent_subscription_page import SubscriptionPage1
from pages.download_account_data_page import DownloadAccountDataPage
import re



class PixseeCloudTest1(BaseTestCase):
    def __init__(self, methodName='runTest', language="zh", locale="TW"):
        super().__init__(methodName)
        self.language = language
        self.locale = locale

    def setUp(self):
        super().setUp(language=self.language, locale=self.locale)
        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        assistant_page = AssistantPage(self.driver)
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        try:
            while self.driver.current_package != self.driver.capabilities.get("appPackage"):
                self.driver.terminate_app(self.driver.current_package)
                self.open_app()
            if assistant_page.is_in_assistant_page():
                return
            elif not baby_monitor_page.is_in_baby_monitor_page():
                self.shutdown_app()
                self.open_app()
            print("Finish opening app.")
            baby_monitor_page.click_home()
            menu_page.click_assistant()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
    # start from assistant page
    def test_01_pixsee_cloud_page_check_storage(self):
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        assistant_page = AssistantPage(self.driver)
        # get ouside text
        outside = pixsee_cloud_page.parse_storage_usage(assistant_page.pixsee_cloud_sub_text())

        assistant_page.click_pixsee_cloud()
        language = self.driver.capabilities.get("language")
        inside_used = None
        inside_total = None
        if language == "tw text" or language == "cn text":
            # compare with inside text
            inside_used = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.mb_used_text())
            inside_total = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.total_storage_text())
            self.assertEqual(outside[1], inside_used, "Storage usage text does not match between outside and inside text.")
            self.assertEqual(outside[0], inside_total, "Total storage text does not match between outside and inside text.")
        elif language == "en-us text":
            # compare with inside text
            inside_used = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.mb_used_text())
            inside_total = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.total_storage_text())
            self.assertEqual(outside[0], inside_used, "Storage usage text does not match between outside and inside text.")
            self.assertEqual(outside[1], inside_total, "Total storage text does not match between outside and inside text.")
        else:
            pass

        if int(inside_total) == 1:
            used_percent = int(inside_used/1000 * 100)
            self.assertEqual(str(used_percent),pixsee_cloud_page.percent_text())
        else:
            raise AssertionError("Total storage is not 1GB, cannot calculate used percent.")
class PixseeCloudTest2(BaseTestCase):
    def __init__(self, methodName='runTest', language="zh", locale="TW"):
        super().__init__(methodName)
        self.language = language
        self.locale = locale

    def setUp(self):
        super().setUp(language=self.language, locale=self.locale)
        baby_monitor_page = BabyMonitorPage(self.driver)
        menu_page = MenuPage(self.driver)
        assistant_page = AssistantPage(self.driver)
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        try:
            while self.driver.current_package != self.driver.capabilities.get("appPackage"):
                self.driver.terminate_app(self.driver.current_package)
                self.open_app()
            if pixsee_cloud_page.is_in_pixsee_cloud_page():
                return
            elif not baby_monitor_page.is_in_baby_monitor_page():
                self.shutdown_app()
                self.open_app()
            print("Finish opening app.")
            baby_monitor_page.click_home()
            menu_page.click_assistant()
        except Exception as e:
            print(f"Test failed with exception: {e}")
            raise e
    # start from pixsee cloud page
    def test_02_pixsee_cloud_page_check_all_texts(self):
        pixsee_cloud_page = PixseeCloudPage(self.driver)

        # Check header text
        self.assertEqual(pixsee_cloud_page.header_text(), self.get_string("pixsee_cloud"), "Header text does not match.")
        try:
            # Check previous subscription text
            self.assertEqual(pixsee_cloud_page.previous_subscription_text(), self.get_string("new_subscription_your_plan_data_title"), "Previous subscription text does not match.")

            # Check remaining text
            try:
                remaining = pixsee_cloud_page.remaining_text()
                hint = self.get_string("new_subscription_days_remaining")
                pattern = "^" + re.escape(hint).replace("%s", r".+") + "$"
                self.assertRegex(remaining,pattern)
            except AssertionError:
                raise AssertionError("Remaining text does not match the expected pattern.")

            # Check description text
            self.assertEqual(pixsee_cloud_page.description_text(), self.get_string("new_subscription_your_premiere__plan_data_description"), "Description text does not match.")
        except :
            pass
        # Check upgrade text
        self.assertEqual(pixsee_cloud_page.upgrade_text(), self.get_string("upgrade_subscription").replace("<b>", "").replace("</b>", ""), "Upgrade text does not match.")

        # check photo text
        self.assertEqual(pixsee_cloud_page.photo_text(), self.get_string("photo"), "Photo text does not match.")
        # check video text
        self.assertEqual(pixsee_cloud_page.videos_text(), self.get_string("video"), "Video text does not match.")
        # check story text
        self.assertEqual(pixsee_cloud_page.story_text(), self.get_string("story_tab"), "Storage text does not match.")
        # check voice recorder text
        self.assertEqual(pixsee_cloud_page.voice_recorder_text(), self.get_string("voice_record"), "Voice recorder text does not match.")
        # check backup data button text
        self.assertEqual(pixsee_cloud_page.back_up_data_button_text(), self.get_string("backup_data"), "Backup data button text does not match.")
        # check free up storage button text
        self.assertEqual(pixsee_cloud_page.free_up_text(), self.get_string("clean_up_storage"), "Free up storage button text does not match.")
    # start from pixsee cloud page
    def test_03_pixsee_cloud_page_check_usage_sum(self):
        pixsee_cloud_page = PixseeCloudPage(self.driver)

        photo = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.photo_storage_text())
        video = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.videos_storage_text())
        story = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.story_storage_text())
        voice = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.voice_recorder_storage_text())
        total = photo + video + story + voice
        total_to_1 = round(total, 1)
        total_text = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.mb_used_text())
        self.assertAlmostEqual(total_to_1, total_text, delta=0.15,
                               msg="Total storage usage does not match the sum of individual storage usages.")
    # start from pixsee cloud page
    def test_04_pixsee_cloud_page_check_icon_color(self):
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        photo_color = (29, 69, 64)
        video_color = (60, 121, 111)
        story_color = (93, 192, 178)
        voice_color = (255,255,255)
        x, y = pixsee_cloud_page.photo_color()
        result = pixsee_cloud_page.is_pixel_color(x, y, photo_color)
        # check baby in color
        if result:
            print("photo icon color is correct")
        else:
            raise AssertionError("photo icon color is wrong")
        x, y = pixsee_cloud_page.videos_color()
        result = pixsee_cloud_page.is_pixel_color(x, y, video_color)
        # check video icon color
        if result:
            print("video icon color is correct")
        else:
            raise AssertionError("video icon color is wrong")
        x, y = pixsee_cloud_page.story_color()
        result = pixsee_cloud_page.is_pixel_color(x, y, story_color)
        # check story icon color
        if result:
            print("story icon color is correct")
        else:
            raise AssertionError("story icon color is wrong")
        x, y = pixsee_cloud_page.voice_recorder_color()
        result = pixsee_cloud_page.is_pixel_color(x, y, voice_color)
        # check voice recorder icon color
        if result:
            print("voice recorder icon color is correct")
        else:
            raise AssertionError("voice recorder icon color is wrong")
    # start from pixsee cloud page
    # def test_05_pixsee_cloud_page_check_upgrade_button(self):
    #     pixsee_cloud_page = PixseeCloudPage(self.driver)
    #     subscription_page = SubscriptionPage1(self.driver)
    #     # Check upgrade button
    #     pixsee_cloud_page.click_upgrade()
    #     self.assertTrue(subscription_page.is_in_subscription_page(), "Failed to navigate to Subscription Page after clicking Upgrade button.")
    #     subscription_page.click_x()
    #     self.assertTrue(pixsee_cloud_page.is_in_pixsee_cloud_page(), "Failed to return to Pixsee Cloud Page after clicking X on Subscription Page.")
    # start from pixsee cloud page
    # def test_06_pixsee_cloud_page_check_backup_data_button(self):
    #     pixsee_cloud_page = PixseeCloudPage(self.driver)
    #     download_account_data_page = DownloadAccountDataPage(self.driver)
    #     # check download dialog
    #     pixsee_cloud_page.click_download()
    #     self.assertEqual(pixsee_cloud_page.previous_subscription_text(), self.get_string("new_subscription_download_plan_account_data_title"), "download dialog title does not match.")
    #     self.assertEqual(pixsee_cloud_page.remaining_text(), self.get_string("new_subscription_download_plan_account_data_subtitle"), "download dialog subtitle does not match.")
    #     pixsee_cloud_page.click_cancel()
    #     self.assertTrue(pixsee_cloud_page.is_in_pixsee_cloud_page(), "Failed to return to Pixsee Cloud Page after clicking Cancel on Download dialog.")
    #
    #     pixsee_cloud_page.click_download()
    #     pixsee_cloud_page.click_ok()
    #     self.assertTrue(download_account_data_page.is_in_download_account_data_page(), "Failed to navigate to Download Account Data Page after clicking OK on Download dialog.")
    #     # check download account data page texts
    #     self.assertEqual(download_account_data_page.get_title_text(), self.get_string("download_account_data"), "Download Account Data page title does not match.")
    #     self.assertEqual(download_account_data_page.get_info_text(), self.get_string("download_account_data_info_link"), "Download Account Data info text does not match.")
    #     self.assertEqual(download_account_data_page.get_cancel_button_text(), self.get_string("cancel"), "Download Account Data cancel button text does not match.")
    #     self.assertEqual(download_account_data_page.get_submit_button_text(), self.get_string("download_account_data_btn_submit"), "Download Account Data submit button text does not match.")
    #     download_account_data_page.click_submit()
    #
    #     self.assertTrue(download_account_data_page.has_dialog(), "Download Account Data dialog does not appear after clicking Submit.")
    #     # check dialog text
    #     def test_07_pixsee_cloud_page_check_backup_data_button(self):
    #         pixsee_cloud_page = PixseeCloudPage(self.driver)
    #         download_account_data_page = DownloadAccountDataPage(self.driver)
    #         # check download dialog
    #         pixsee_cloud_page.click_download()






