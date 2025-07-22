from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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
        self.TimeSelecter ="com.compal.bioslab.pixsee.pixm01:id/tvStartingTimeHour"
        
        
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
    def click_time_selecter(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.TimeSelecter))
        )
        element = self.driver.find_element("id", self.TimeSelecter)
        element.click()
