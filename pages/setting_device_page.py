import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Setting:
    def __init__(self, driver):
        self.driver = driver

        self.back_button = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
        self.profile_button = "com.compal.bioslab.pixsee.pixm01:id/tvProfileSettings"
        self.wifi_button = "com.compal.bioslab.pixsee.pixm01:id/tvWifiSettings"
        self.pixsee_friend_button = "com.compal.bioslab.pixsee.pixm01:id/tvPixseeFriendsDetection"
        self.environment_button = "com.compal.bioslab.pixsee.pixm01:id/tvEnvironmentDetection"
        self.cry_button = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_crying_label"
        self.area_button = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_efence_label"
        self.cover_face_button = "com.compal.bioslab.pixsee.pixm01:id/cover_detection_settings_label"
        self.time_salpe_button = "com.compal.bioslab.pixsee.pixm01:id/time_lapse_settings_label"
        self.voice_button = "com.compal.bioslab.pixsee.pixm01:id/tvVoiceCommand"
        self.shhytter_button = "com.compal.bioslab.pixsee.pixm01:id/capture_sound_switch"
        self.led_button = "com.compal.bioslab.pixsee.pixm01:id/led_switch"
        self.night_mode_button = "com.compal.bioslab.pixsee.pixm01:id/night_vision_switch"
    def click_back(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.back_button))
        )
        element = self.driver.find_element("id", self.back_button)
        element.click()
    def click_profile(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.profile_button))
        )
        element = self.driver.find_element("id", self.profile_button)
        element.click()
    def click_wifi(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.wifi_button))
        )
        element = self.driver.find_element("id", self.wifi_button)
        element.click()