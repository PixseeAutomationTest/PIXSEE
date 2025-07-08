from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import Interaction

class BabyMonitorPage():
    def __init__(self, driver):
        self.driver = driver

        self.babyMonitorScreen = "com.compal.bioslab.pixsee.pixm01:id/videoTextureView"
        self.sleepButton = "com.compal.bioslab.pixsee.pixm01:id/ibSleepMode"
        self.twoWayTalkButton = "com.compal.bioslab.pixsee.pixm01:id/ibPushToTalkHomeAct"
        self.musicButton = "com.compal.bioslab.pixsee.pixm01:id/ibPlayMusic"
        self.recordButton = "com.compal.bioslab.pixsee.pixm01:id/ibRecordVideo"
        self.captureButton = "com.compal.bioslab.pixsee.pixm01:id/btnSwipeCapture"
        self.changeQualityButton = "com.compal.bioslab.pixsee.pixm01:id/ibQualityStream"
        self.muteButton = "com.compal.bioslab.pixsee.pixm01:id/bStreamOptions"

    def click_sleep(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.sleepButton))
        )
        element = self.driver.find_element("id", self.sleepButton)
        element.click()

    def click_two_way_talk(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.twoWayTalkButton))
        )
        element = self.driver.find_element("id", self.twoWayTalkButton)
        element.click()

    def click_music(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.musicButton))
        )
        element = self.driver.find_element("id", self.musicButton)
        element.click()

    def click_record(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.recordButton))
        )
        element = self.driver.find_element("id", self.recordButton)
        element.click()

    def click_capture(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.captureButton))
        )
        element = self.driver.find_element("id", self.captureButton)
        element.click()

    def change_camera_mode(self):
        # 等待按鈕出現並抓到元素
        element = WebDriverWait(self.driver, 10).until(
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
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.changeQualityButton))
        )
        element = self.driver.find_element("id", self.changeQualityButton)
        element.click()

    def click_mute(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.muteButton))
        )
        element = self.driver.find_element("id", self.muteButton)
        element.click()

        def is_in_baby_monitor_page(self):
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((AppiumBy.ID, self.babyMonitorScreen))
                )
                self.driver.find_element(AppiumBy.ID, self.babyMonitorScreen)
                return True

            except:
                return False

        def wait_for_tutor_by_id(self, tutor_id, timeout=20):
            """等待 tutor 元素出現，並回傳元素文字"""
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ID, tutor_id))
            )
            return self.driver.find_element(AppiumBy.ID, tutor_id).text

        def click_stream_title(self):
            """點擊畫面標題"""
            self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/tvStreamTitle").click()

        def click_home(self):
            self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome").click()






