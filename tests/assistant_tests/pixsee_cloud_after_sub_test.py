import math

from pages.menu_pages.menu_page import MenuPage
from base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.menu_pages.assistant_pages.assistant_page import AssistantPage
from pages.menu_pages.assistant_pages.pixsee_cloud_page import PixseeCloudPage
import re



class PixseeCloudTest3(BaseTestCase):
    def __init__(self, methodName='runTest', language="en", locale="US"):
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
        match = re.match(r"([\d.]+)\s*(MB|GB)", pixsee_cloud_page.mb_used_text())
        if match:
            unit = match.group(2)  # 單位
            if unit == "GB":
                inside_used = float(match.group(1)) * 1000
            elif unit == "MB":
                inside_used = float(match.group(1))
        if int(inside_total) == 30:
            used_percent = int(inside_used/30000 * 100)
            self.assertEqual(str(used_percent),pixsee_cloud_page.percent_text())
        else:
            raise AssertionError("Total storage is not 30 GB, cannot calculate used percent.")
class PixseeCloudTest4(BaseTestCase):
    def __init__(self, methodName='runTest', language="en", locale="US"):
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
            photo = 0
            match = re.match(r"([\d.]+)\s*(MB|GB)", pixsee_cloud_page.photo_storage_text())
            if match:
                unit = match.group(2)  # 單位
                if unit == "GB":
                    photo = float(match.group(1)) * 1000
                elif unit == "MB":
                    photo = float(match.group(1))
        except:
            photo = 0
        try:
            video = 0
            match = re.match(r"([\d.]+)\s*(MB|GB)", pixsee_cloud_page.videos_storage_text())
            if match:
                unit = match.group(2)  # 單位
                if unit == "GB":
                    video = float(match.group(1)) * 1000
                elif unit == "MB":
                    video = float(match.group(1))
        except:
            video = 0
        try:
            story = 0
            match = re.match(r"([\d.]+)\s*(MB|GB)", pixsee_cloud_page.story_storage_text())
            if match:
                unit = match.group(2)  # 單位
                if unit == "GB":
                    story = float(match.group(1)) * 1000
                elif unit == "MB":
                    story = float(match.group(1))
        except:
            story = 0
        try:
            voice = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.voice_recorder_storage_text())
            match = re.match(r"([\d.]+)\s*(MB|GB)", pixsee_cloud_page.voice_recorder_storage_text())
            if match:
                unit = match.group(2)  # 單位
                if unit == "GB":
                    video = float(match.group(1)) * 1000
                elif unit == "MB":
                    video = float(match.group(1))
        except:
            voice = 0
        # calculate total storage usage
        match = re.match(r"([\d.]+)\s*(MB|GB)", pixsee_cloud_page.mb_used_text())
        if match:
            unit = match.group(2)
            if unit == "GB":
                total = photo + video + story + voice
                total = total/ 1000  # convert to GB
                total_to_1 = math.floor(total * 100) / 100
                total_text = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.mb_used_text())
                self.assertEqual(total_to_1, total_text, msg="Total storage usage does not match the sum of individual usages.")
            elif unit == "MB":
                total = photo + video + story + voice
                total_to_1 = math.floor(total * 10) / 10
                total_text = pixsee_cloud_page.parse_storage_usage(pixsee_cloud_page.mb_used_text())
                self.assertEqual(total_to_1, total_text, msg="Total storage usage does not match the sum of individual usages.")











