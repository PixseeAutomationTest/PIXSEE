from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TimeLapseVideoPage():
    def __init__(self, driver):
        self.driver = driver
        self.Header = "com.compal.bioslab.pixsee.pixm01:id/textView5"
        self.Back = "com.compal.bioslab.pixsee.pixm01:id/ibTimeLapseSettingsBack"
        self.Save = "com.compal.bioslab.pixsee.pixm01:id/tvTimeLapseSettingsSave"
        self.TimeLapseRecording = "com.compal.bioslab.pixsee.pixm01:id/timeLapse_settings_status_text"
        self.Subtitle = "com.compal.bioslab.pixsee.pixm01:id/timeLapse_settings_subtext"
        self.Switch = "com.compal.bioslab.pixsee.pixm01:id/timeLapse_settings_status_switch"
        self.UpgradeTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitleUpgradeTimeLapseAct"
        self.UpgradeSubscription = "com.compal.bioslab.pixsee.pixm01:id/btnUpgradeTimeLapseOk"
        self.UpgradeNo = "com.compal.bioslab.pixsee.pixm01:id/btnUpgradeTimeLapseCancel"
        self.RecordingMode = "com.compal.bioslab.pixsee.pixm01:id/type_detection_section"
        self.TimeSpan = "com.compal.bioslab.pixsee.pixm01:id/tvTimeSpanLabelSection"
        self.EntireTime = "com.compal.bioslab.pixsee.pixm01:id/rb_full_time_txt"
        self.PeopleInView = "com.compal.bioslab.pixsee.pixm01:id/rb_human_time_radio_txt"
        self.EntireTimeCheckbox = "com.compal.bioslab.pixsee.pixm01:id/rb_full_time_radio"
        self.PeopleInViewCheckbox = "com.compal.bioslab.pixsee.pixm01:id/rb_human_time_radio"
        self.TwelveHours = "com.compal.bioslab.pixsee.pixm01:id/rb_12_hours_txt"
        self.TwentyFourHours = "com.compal.bioslab.pixsee.pixm01:id/rb_24_hours_radio_txt"
        self.TwelveHoursCheckbox = "com.compal.bioslab.pixsee.pixm01:id/rb_12_hours_radio"
        self.TwentyFourHoursCheckbox = "com.compal.bioslab.pixsee.pixm01:id/rb_24_hours_radio"
        self.StartingTime = "com.compal.bioslab.pixsee.pixm01:id/tvStartingTime"
        self.Timer = "com.compal.bioslab.pixsee.pixm01:id/tvStartingTimeHour"
        self.HumanWarning = "com.compal.bioslab.pixsee.pixm01:id/tv_human_warning"
        self.Hours = "com.compal.bioslab.pixsee.pixm01:id/rvHours"
        self.AmPm = "com.compal.bioslab.pixsee.pixm01:id/rvAmPm"
        self.Cancel = "com.compal.bioslab.pixsee.pixm01:id/cancel"
        self.Confirm = "com.compal.bioslab.pixsee.pixm01:id/confirm"
        self.DiscardMessage = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
        self.DiscardYes = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
        self.DiscardNo = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"

    def is_in_timelapse_video_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Header))
            )
            return True
        except AssertionError:
            return False
    def is_in_timelapse_upgrade_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.UpgradeTitle))
            )
            return True
        except AssertionError:
            return False
    def is_in_upgrade_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.UpgradeTitle))
            )
            return True
        except AssertionError:
            return False
    def is_in_discard_dialog(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.ID, self.DiscardMessage))
            )
            self.driver.find_element(AppiumBy.ID, self.DiscardMessage)
            return True

        except AssertionError:
            return False
    def is_in_timer(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.ID, self.Cancel))
            )
            self.driver.find_element(AppiumBy.ID, self.Cancel)
            return True

        except AssertionError:
            return False

    def is_switch_on(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Switch))
            )
            element = self.driver.find_element("id", self.Switch)
            return element.is_selected()
        except AssertionError:
            return False

    def header_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Header))
            )
            element = self.driver.find_element("id", self.Header)
            return element.text
        except AssertionError:
            return None
    def title(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.TimeLapseRecording))
            )
            element = self.driver.find_element("id", self.TimeLapseRecording)
            return element.text
        except AssertionError:
            return None
    def description(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Subtitle))
            )
            element = self.driver.find_element("id", self.Subtitle)
            return element.text
        except AssertionError:
            return None
    def upgrade_title_txt(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.UpgradeTitle))
            )
            element = self.driver.find_element("id", self.UpgradeTitle)
            return element.text
        except AssertionError:
            return None
    def upgrade_subscription_txt(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.UpgradeSubscription))
            )
            element = self.driver.find_element("id", self.UpgradeSubscription)
            return element.text
        except AssertionError:
            return None
    def upgrade_no_txt(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.UpgradeNo))
            )
            element = self.driver.find_element("id", self.UpgradeNo)
            return element.text
        except AssertionError:
            return None
    def recording_mode_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.RecordingMode))
            )
            element = self.driver.find_element("id", self.RecordingMode)
            return element.text
        except AssertionError:
            return None
    def time_span_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.TimeSpan))
            )
            element = self.driver.find_element("id", self.TimeSpan)
            return element.text
        except AssertionError:
            return None
    def entire_time_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.EntireTime))
            )
            element = self.driver.find_element("id", self.EntireTime)
            return element.text
        except AssertionError:
            return None
    def people_in_view_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.PeopleInView))
            )
            element = self.driver.find_element("id", self.PeopleInView)
            return element.text
        except AssertionError:
            return None
    def twelve_hours_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.TwelveHours))
            )
            element = self.driver.find_element("id", self.TwelveHours)
            return element.text
        except AssertionError:
            return None
    def twenty_four_hours_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.TwentyFourHours))
            )
            element = self.driver.find_element("id", self.TwentyFourHours)
            return element.text
        except AssertionError:
            return None
    def starting_time_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.StartingTime))
            )
            element = self.driver.find_element("id", self.StartingTime)
            return element.text
        except AssertionError:
            return None
    def timer_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Timer))
            )
            element = self.driver.find_element("id", self.Timer)
            return element.text
        except AssertionError:
            return None
    def cancel_txt(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.Cancel))
        )
        return self.driver.find_element(AppiumBy.ID, self.Cancel).text
    def confirm_txt(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.Confirm))
        )
        return self.driver.find_element(AppiumBy.ID, self.Confirm).text
    def discard_message_txt(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.DiscardMessage))
        )
        return self.driver.find_element(AppiumBy.ID, self.DiscardMessage).text
    def discard_yes_txt(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.DiscardYes))
        )
        return self.driver.find_element(AppiumBy.ID, self.DiscardYes).text
    def discard_no_txt(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.DiscardNo))
        )
        return self.driver.find_element(AppiumBy.ID, self.DiscardNo).text

    def change_hour_by_scroll(self):
        window = self.driver.get_window_size()
        x = window["width"] // 2.5  # number should be changed when on ios
        start_y = int(window["height"] * 0.6)  # number should be changed when on ios
        end_y = int(window["height"] * 0.5)  # number should be changed when on ios

        self.driver.swipe(x, start_y, x, end_y, 500)  # 500 毫秒完成滑動
        time.sleep(1)
    def change_am_to_pm_by_scroll(self):
        window = self.driver.get_window_size()
        x = window["width"] // 6 * 5  # number should be changed when on ios
        start_y = int(window["height"] * 0.6)  # number should be changed when on ios
        end_y = int(window["height"] * 0.5)  # number should be changed when on ios

        self.driver.swipe(x, start_y, x, end_y, 500)  # 500 毫秒完成滑動
        time.sleep(1)

    def click_back(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Back))
        )
        element = self.driver.find_element("id", self.Back)
        element.click()
    def click_save(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Save))
        )
        element = self.driver.find_element("id", self.Save)
        element.click()
    def click_switch(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Switch))
        )
        element = self.driver.find_element("id", self.Switch)
        element.click()
    def click_upgrade_subscription(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.UpgradeSubscription))
        )
        element = self.driver.find_element("id", self.UpgradeSubscription)
        element.click()
    def click_upgrade_no(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.UpgradeNo))
        )
        element = self.driver.find_element("id", self.UpgradeNo)
        element.click()
    def click_entire_time_checkbox(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.EntireTimeCheckbox))
        )
        element = self.driver.find_element("id", self.EntireTimeCheckbox)
        element.click()
    def click_people_in_view_checkbox(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.PeopleInViewCheckbox))
        )
        element = self.driver.find_element("id", self.PeopleInViewCheckbox)
        element.click()
    def click_twelve_hours_checkbox(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.TwelveHoursCheckbox))
        )
        element = self.driver.find_element("id", self.TwelveHoursCheckbox)
        element.click()
    def click_twenty_four_hours_checkbox(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.TwentyFourHoursCheckbox))
        )
        element = self.driver.find_element("id", self.TwentyFourHoursCheckbox)
        element.click()
    def click_timer(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Timer))
        )
        element = self.driver.find_element("id", self.Timer)
        element.click()
    def click_cancel(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.Cancel))
        )
        self.driver.find_element(AppiumBy.ID, self.Cancel).click()
    def click_confirm(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.Confirm))
        )
        self.driver.find_element(AppiumBy.ID, self.Confirm).click()
    def click_discard_yes(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.DiscardYes))
        )
        self.driver.find_element(AppiumBy.ID, self.DiscardYes).click()
    def click_discard_no(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.DiscardNo))
        )
        self.driver.find_element(AppiumBy.ID, self.DiscardNo).click()

    def is_save_enable(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.Save))
        )
        button = self.driver.find_element(AppiumBy.ID, self.Save)
        is_enable = button.get_attribute("enabled")
        return is_enable == "true"

    # check if the checkbox is clicked
    def is_twelve_hours_clicked(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.TwelveHoursCheckbox))
        )
        button = self.driver.find_element(AppiumBy.ID, self.TwelveHoursCheckbox)
        is_clickable = button.get_attribute("checked")
        return is_clickable == "true"
    def is_twenty_four_hours_clicked(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.TwentyFourHoursCheckbox))
        )
        button = self.driver.find_element(AppiumBy.ID, self.TwentyFourHoursCheckbox)
        is_clickable = button.get_attribute("checked")
        return is_clickable == "true"
