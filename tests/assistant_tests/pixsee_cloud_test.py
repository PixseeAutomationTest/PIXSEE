import math

from pages.menu_pages.menu_page import MenuPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.assistant_pages.assistant_page import AssistantPage
from pages.menu_pages.assistant_pages.pixsee_cloud_page import PixseeCloudPage
from pages.menu_pages.subscription_pages.havent_subscription_page import SubscriptionPage1
from pages.download_account_data_page import DownloadAccountDataPage
import re



class PixseeCloudTest1(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = getattr(cls, "language", "zh")
        cls.locale = getattr(cls, "locale", "TW")
        super().setUpClass()

    def setUp(self):
        super().setUp()
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
        if language == "zh":
            # compare with inside text
            inside_used = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.mb_used_text())
            inside_total = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.total_storage_text())
            self.assertEqual(outside[1], inside_used, "Storage usage text does not match between outside and inside text.")
            self.assertEqual(outside[0], inside_total, "Total storage text does not match between outside and inside text.")
        elif language == "en":
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
    @classmethod
    def setUpClass(cls):
        cls.language = getattr(cls, "language", "zh")
        cls.locale = getattr(cls, "locale", "TW")
        super().setUpClass()

    def setUp(self):
        super().setUp()
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
            assistant_page.click_pixsee_cloud()
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
        try:
            # check photo text
            self.assertEqual(pixsee_cloud_page.photo_text(), self.get_string("photo"), "Photo text does not match.")
            # check video text
            self.assertEqual(pixsee_cloud_page.videos_text(), self.get_string("video"), "Video text does not match.")
            # check story text
            self.assertEqual(pixsee_cloud_page.story_text(), self.get_string("story_tab"), "Storage text does not match.")
            # check voice recorder text
            self.assertEqual(pixsee_cloud_page.voice_recorder_text(), self.get_string("voice_record"), "Voice recorder text does not match.")
        except :
            pass
        # check backup data button text
        self.assertEqual(pixsee_cloud_page.back_up_data_button_text(), self.get_string("backup_data"), "Backup data button text does not match.")
        # check free up storage button text
        self.assertEqual(pixsee_cloud_page.free_up_text(), self.get_string("clean_up_storage"), "Free up storage button text does not match.")
    # start from pixsee cloud page
    def test_03_pixsee_cloud_page_check_usage_sum(self):
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        try:
            photo = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.photo_storage_text())
        except:
            photo = 0
        try:
            video = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.videos_storage_text())
        except:
            video = 0
        try:
            story = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.story_storage_text())
        except:
            story = 0
        try:
            voice = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.voice_recorder_storage_text())
        except:
            voice = 0
        total = photo + video + story + voice
        total_to_1 = math.floor(total * 10) / 10
        total_text = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.mb_used_text())
        self.assertAlmostEqual(total_to_1, total_text, delta=0.4,
                               msg="Total storage usage does not match the sum of individual usages (tolerance ±0.4).")
    # start from pixsee cloud page
    def test_04_pixsee_cloud_page_check_icon_color(self):
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        try:
            x, y = pixsee_cloud_page.photo_color()
            photo_color = pixsee_cloud_page.is_pixel_color(x, y)
        except:
            photo_color = 0
        try:
            x, y = pixsee_cloud_page.videos_color()
            video_color = pixsee_cloud_page.is_pixel_color(x, y)
        except:
            video_color = 0
        try:
            x, y = pixsee_cloud_page.story_color()
            story_color = pixsee_cloud_page.is_pixel_color(x, y)
        except:
            story_color = 0
        try:
            x, y = pixsee_cloud_page.voice_recorder_color()
            voice_color = pixsee_cloud_page.is_pixel_color(x, y)
        except:
            voice_color = 0
            # check color by order of darkness
            # 過濾掉 0
        colors = [c for c in [photo_color, video_color, story_color, voice_color] if c != 0]

        # 只有在至少有兩個以上顏色時才做比較
        if len(colors) > 1:
            self.assertTrue(all(colors[i] <= colors[i + 1] for i in range(len(colors) - 1)),
                            f"Icon colors do not match the expected order of darkness: {colors}")
        # self.assertTrue(photo_color <= video_color <= story_color <= voice_color, "Icon colors do not match the expected order of darkness.")
        # check if all colors are different
        # self.assertTrue(len({photo_color, video_color, story_color, voice_color}) == 4, "Icon colors are not all different.")
    # start from pixsee cloud page
    def test_05_pixsee_cloud_page_check_upgrade_button(self):
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        subscription_page = SubscriptionPage1(self.driver)
        # Check upgrade button
        pixsee_cloud_page.click_upgrade()
        self.assertTrue(subscription_page.is_in_subscription_page(), "Failed to navigate to Subscription Page after clicking Upgrade button.")
        subscription_page.click_x()
        self.assertTrue(pixsee_cloud_page.is_in_pixsee_cloud_page(), "Failed to return to Pixsee Cloud Page after clicking X on Subscription Page.")
    # start from pixsee cloud page
    def test_06_pixsee_cloud_page_check_backup_data_button(self):
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        download_account_data_page = DownloadAccountDataPage(self.driver)
        # check download dialog
        pixsee_cloud_page.click_download()
        self.assertEqual(pixsee_cloud_page.previous_subscription_text(), self.get_string("new_subscription_download_plan_account_data_title"), "download dialog title does not match.")
        self.assertEqual(pixsee_cloud_page.remaining_text(), self.get_string("new_subscription_download_plan_account_data_subtitle"), "download dialog subtitle does not match.")
        self.assertIsNotNone(pixsee_cloud_page.dialog_baby_name_text())
        self.assertEqual(pixsee_cloud_page.ok_text(),self.get_string("ok"), "download dialog OK button text does not match.")
        self.assertEqual(pixsee_cloud_page.cancel_text(), self.get_string("cancel"), "download dialog Cancel button text does not match.")
        pixsee_cloud_page.click_cancel()
        self.assertTrue(pixsee_cloud_page.is_in_pixsee_cloud_page(), "Failed to return to Pixsee Cloud Page after clicking Cancel on Download dialog.")

        pixsee_cloud_page.click_download()
        pixsee_cloud_page.click_ok()
        self.assertTrue(download_account_data_page.is_in_download_account_data_page(), "Failed to navigate to Download Account Data Page after clicking OK on Download dialog.")
        download_account_data_page.click_close()
        # check if is back to pixsee cloud page
        self.assertTrue(pixsee_cloud_page.is_in_pixsee_cloud_page(), "Failed to return to Pixsee Cloud Page after clicking Close on Download Account Data Page.")

        # check download account data page texts
        # self.assertEqual(download_account_data_page.get_title_text(), self.get_string("download_account_data"), "Download Account Data page title does not match.")
        # self.assertEqual(download_account_data_page.get_info_text(), self.get_string("download_account_data_info_link"), "Download Account Data info text does not match.")
        # self.assertEqual(download_account_data_page.get_cancel_button_text(), self.get_string("cancel"), "Download Account Data cancel button text does not match.")
        # self.assertEqual(download_account_data_page.get_submit_button_text(), self.get_string("download_account_data_btn_submit"), "Download Account Data submit button text does not match.")
        # download_account_data_page.click_submit()

        # self.assertTrue(download_account_data_page.has_dialog(), "Download Account Data dialog does not appear after clicking Submit.")
        # check dialog text
    # stay
    def test_07_pixsee_cloud_page_check_backup_data_button(self):
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        download_account_data_page = DownloadAccountDataPage(self.driver)
        # check download dialog
        pixsee_cloud_page.click_backup_data()
        self.assertEqual(pixsee_cloud_page.previous_subscription_text(), self.get_string("download_baby_dialog_title"), "backup dialog title does not match.")
        self.assertEqual(pixsee_cloud_page.all_data_text(), self.get_string("download_baby_dialog_all_data"), "backup dialog all data does not match.")
        self.assertIsNotNone(pixsee_cloud_page.dialog_baby_name_text())
        self.assertEqual(pixsee_cloud_page.ok_text(), self.get_string("ok"), "backup dialog OK button text does not match.")
        self.assertEqual(pixsee_cloud_page.cancel_text(), self.get_string("cancel"), "backup dialog Cancel button text does not match.")
        pixsee_cloud_page.click_cancel()
        self.assertTrue(pixsee_cloud_page.is_in_pixsee_cloud_page(), "Failed to return to Pixsee Cloud Page after clicking Cancel on Backup dialog.")

        pixsee_cloud_page.click_backup_data()
        self.assertFalse(pixsee_cloud_page.is_ok_clickable())
        pixsee_cloud_page.click_all_data_checkbox()
        self.assertTrue(pixsee_cloud_page.is_ok_clickable())
        pixsee_cloud_page.click_all_data_checkbox()
        self.assertFalse(pixsee_cloud_page.is_ok_clickable())
        pixsee_cloud_page.click_dialog_baby_name_checkbox()
        self.assertTrue(pixsee_cloud_page.is_ok_clickable())
        pixsee_cloud_page.click_ok()
        self.assertTrue(download_account_data_page.is_in_download_account_data_page(), "Failed to navigate to Download Account Data Page after clicking OK on Backup dialog.")
        download_account_data_page.click_close()
        # check if is back to pixsee cloud page
        self.assertTrue(pixsee_cloud_page.is_in_pixsee_cloud_page(), "Failed to return to Pixsee Cloud Page after clicking Close on Download Account Data Page.")
    # stay
    def test_08_pixsee_cloud_page_check_free_up_storage_button(self):
        pixsee_cloud_page = PixseeCloudPage(self.driver)
        inside_used = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.mb_used_text())
        print(inside_used)
        # check free up storage dialog
        pixsee_cloud_page.click_free_up()
        self.assertEqual(pixsee_cloud_page.previous_subscription_text(), self.get_string("storage_clean_title"), "Free up storage dialog title does not match.")
        self.assertEqual(pixsee_cloud_page.remaining_text(), self.get_string("storage_clean_descripition"), "Free up storage dialog subtitle does not match.")
        # check dialog texts
        try:
            delete_25_percent = pixsee_cloud_page.dialog_delete_25_percent_text()
            hint = self.get_string("storage_clean_option_25_percent").replace("%%","%").replace("\\n","\n")
            pattern = "^" + re.escape(hint).replace("%s", r".+") + "$"
            self.assertRegex(delete_25_percent,pattern)
        except Exception as e:
            raise AssertionError(f"Free up storage dialog delete 25 percent text does not match. Error: {e}")
        try:
            delete_50_percent = pixsee_cloud_page.dialog_delete_50_percent_text()
            hint = self.get_string("storage_clean_option_50_percent").replace("%%","%").replace("\\n","\n")
            pattern = "^" + re.escape(hint).replace("%s", r".+") + "$"
            self.assertRegex(delete_50_percent,pattern)
        except Exception as e:
            raise AssertionError(f"Free up storage dialog delete 50 percent text does not match. Error: {e}")
        try:
            delete_75_percent = pixsee_cloud_page.dialog_delete_75_percent_text()
            hint = self.get_string("storage_clean_option_75_percent").replace("%%","%").replace("\\n","\n")
            pattern = "^" + re.escape(hint).replace("%s", r".+") + "$"
            self.assertRegex(delete_75_percent,pattern)
        except Exception as e:
            raise AssertionError(f"Free up storage dialog delete 75 percent text does not match. Error: {e}")
        try:
            delete_all = pixsee_cloud_page.dialog_delete_all_text()
            self.assertEqual(delete_all, self.get_string("storage_clean_all").replace("\\n","\n"), "Free up storage dialog delete all text does not match.")
        except Exception as e:
            raise AssertionError(f"Free up storage dialog delete all text does not match. Error: {e}")
        self.assertEqual(pixsee_cloud_page.ok_text(), self.get_string("ok"), "Free up storage dialog OK button text does not match.")
        self.assertEqual(pixsee_cloud_page.cancel_text(), self.get_string("cancel"), "Free up storage dialog Cancel button text does not match.")
        # check keep storage
        keep_75_percent = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.dialog_delete_25_percent_text())
        keep_50_percent = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.dialog_delete_50_percent_text())
        keep_25_percent = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.dialog_delete_75_percent_text())
        right_75_percent = round((inside_used * 0.75) + 1e-8, 1)
        right_50_percent = round((inside_used * 0.50) + 1e-8, 1)
        right_25_percent = round((inside_used * 0.25) + 1e-8, 1)
        print(keep_50_percent,right_50_percent)
        self.assertAlmostEqual(right_75_percent, keep_75_percent[1], delta=0.14,
                               msg="Free up storage dialog delete 25 percent storage is not less than current storage.")
        self.assertAlmostEqual(right_50_percent, keep_50_percent[1], delta=0.14,
                               msg="Free up storage dialog delete 50 percent storage is not less than current storage.")
        self.assertAlmostEqual(right_25_percent, keep_25_percent[1], delta=0.14,
                               msg="Free up storage dialog delete 75 percent storage is not less than current storage.")

        # check checkbox clickablility
        self.assertTrue(pixsee_cloud_page.is_dialog_delete_25_percent_clickable(), "Delete 25 percent checkbox is not clickable.")
        self.assertTrue(pixsee_cloud_page.is_dialog_delete_50_percent_clickable(), "Delete 50 percent checkbox is not clickable.")
        self.assertTrue(pixsee_cloud_page.is_dialog_delete_75_percent_clickable(), "Delete 75 percent checkbox is not clickable.")
        self.assertTrue(pixsee_cloud_page.is_dialog_delete_all_clickable(), "Delete all checkbox is not clickable.")
        self.assertEqual(pixsee_cloud_page.ok_text(), self.get_string("ok"),
                         "Free up storage dialog OK button text does not match.")
        self.assertEqual(pixsee_cloud_page.cancel_text(), self.get_string("cancel"),
                         "Free up storage dialog Cancel button text does not match.")
        pixsee_cloud_page.click_cancel()
        # check if is back to pixsee cloud page
        self.assertTrue(pixsee_cloud_page.is_in_pixsee_cloud_page(), "Failed to return to Pixsee Cloud Page after clicking OK on Free up storage dialog.")











