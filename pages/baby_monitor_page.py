from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains
import pages.base as base
import time
from selenium.webdriver.common.actions.interaction import Interaction

class BabyMonitorPage():
    def __init__(self, driver):
        self.driver = driver

        self.liveStreamScreen = "com.compal.bioslab.pixsee.pixm01:id/backgroundHomeLivestreamCardAuxView"
        self.sleepButton = "com.compal.bioslab.pixsee.pixm01:id/ibSleepMode"
        self.twoWayTalkButton = "com.compal.bioslab.pixsee.pixm01:id/ibPushToTalkHomeAct"
        self.musicButton = "com.compal.bioslab.pixsee.pixm01:id/ibPlayMusic"
        self.recordButton = "com.compal.bioslab.pixsee.pixm01:id/ibRecordVideo"
        # self.captureButton = "com.compal.bioslab.pixsee.pixm01:id/btnSwipeCapture"
        self.changeQualityButton = "com.compal.bioslab.pixsee.pixm01:id/ibQualityStream"
        self.muteButton = "com.compal.bioslab.pixsee.pixm01:id/bStreamOptions"
        self.homeButton = "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome"
        self.stream_title = "com.compal.bioslab.pixsee.pixm01:id/tvStreamTitle"
        self.LiveStatus = "com.compal.bioslab.pixsee.pixm01:id/tvLiveStatus"
        self.tutor_id = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
        self.tutor_title = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
        self.connectingStatusText = "com.compal.bioslab.pixsee.pixm01:id/tvConnectingStatus"
        self.photoUploadDialog = "com.compal.bioslab.pixsee.pixm01:id/tvSnackbarToastLabel"

        self.captureButton_xpath = '//android.widget.RelativeLayout[@resource-id="com.compal.bioslab.pixsee.pixm01:id/btnSwipeCapture"]/android.widget.ImageView[2]'

    def click_sleep(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.sleepButton))
        )
        element = self.driver.find_element("id", self.sleepButton)
        element.click()
    def click_two_way_talk(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.twoWayTalkButton))
        )
        element = self.driver.find_element("id", self.twoWayTalkButton)
        element.click()
    def click_music(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.musicButton))
        )
        element = self.driver.find_element("id", self.musicButton)
        element.click()
    def click_record(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.recordButton))
        )
        element = self.driver.find_element("id", self.recordButton)
        element.click()
    def click_capture(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("xpath", self.captureButton_xpath))
        )
        element = self.driver.find_element("xpath", self.captureButton_xpath)
        element.click()
    def click_middle(self):
        size = self.driver.get_window_size()
        x = size['width'] // 2
        y = size['height'] // 2

        self.driver.execute_script("mobile: clickGesture", {
            "x": x,
            "y": y
        })
        time.sleep(1)



    #TODO: function uncompleted 2025/07/15

    def change_camera_mode(self):
        # 等待按鈕出現並抓到元素
        element = WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.captureButton))
        )

        element.click()

        # 建立一支 touch 指標裝置
        finger = PointerInput("touch", "finger")  # 就這一行改成字串

        # 用 ActionChains + ActionBuilder 組 W3C Action
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=finger)

        # 長按 2 秒
        actions.w3c_actions.pointer_action.move_to(element)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(2)  # 2 秒
        actions.w3c_actions.pointer_action.pointer_up()

        actions.perform()
    def click_change_quality(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.changeQualityButton))
        )
        element = self.driver.find_element("id", self.changeQualityButton)
        element.click()
    def click_mute(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.muteButton))
        )
        element = self.driver.find_element("id", self.muteButton)
        element.click()
    def is_in_baby_monitor_page(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located((AppiumBy.ID, self.liveStreamScreen))
            )
            self.driver.find_element(AppiumBy.ID, self.liveStreamScreen)
            return True

        except:
            return False
    def get_tutor_description(self):
        """wait for the tutor text to appear by its ID"""
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located((AppiumBy.ID, self.tutor_id))
        )
        return self.driver.find_element(AppiumBy.ID, self.tutor_id).text
    def get_tutor_title(self):
        """wait for the tutor title to appear by its ID"""
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located((AppiumBy.ID, self.tutor_title))
        )
        return self.driver.find_element(AppiumBy.ID, self.tutor_title).text
    def click_stream_title(self):
        """點擊畫面標題"""
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located((AppiumBy.ID, self.stream_title))
        )
        self.driver.find_element(AppiumBy.ID, self.stream_title).click()
    def click_home(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located((AppiumBy.ID, self.homeButton))
        )
        self.driver.find_element(AppiumBy.ID, self.homeButton).click()
    def get_stream_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located((AppiumBy.ID, self.stream_title))
        )
        element = self.driver.find_element("id", self.stream_title)
        return element.text

    def get_connecting_status_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located((AppiumBy.ID, self.connectingStatusText))
        )
        element = self.driver.find_element("id", self.connectingStatusText)
        return element.text
    def has_photo_upload_dialog(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located((AppiumBy.ID, self.photoUploadDialog))
            )
            self.driver.find_element(AppiumBy.ID, self.photoUploadDialog)
            return True
        except:
            return False
    def is_connected(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located((AppiumBy.ID, self.twoWayTalkButton))
        )
        button = self.driver.find_element(AppiumBy.ID, self.twoWayTalkButton)
        is_connected = button.get_attribute("enabled")
        return is_connected == "true"







