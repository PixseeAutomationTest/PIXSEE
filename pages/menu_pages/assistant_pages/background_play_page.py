from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages.base as base
import time

class BackgroundPlayPage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
        self.keepPlayingTitleText = "com.compal.bioslab.pixsee.pixm01:id/bg_play_settings_status_text"
        self.keepPlayingDescriptionText = "com.compal.bioslab.pixsee.pixm01:id/bg_play_settings_subtext"
        self.playingTypesText = "com.compal.bioslab.pixsee.pixm01:id/type_detection_section"
        self.audioOnlyText = "com.compal.bioslab.pixsee.pixm01:id/rb_audio_only_radio_txt"
        self.floatingVideoText = "com.compal.bioslab.pixsee.pixm01:id/rb_floating_video_radio_txt"

        self.saveButton = "com.compal.bioslab.pixsee.pixm01:id/tv_save"
        self.returnButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
        self.keepPlayingButton = "com.compal.bioslab.pixsee.pixm01:id/bg_play_keep_playing_switch"
        self.audioOnlyButton = "com.compal.bioslab.pixsee.pixm01:id/rb_audio_only_radio"
        self.floatingVideoButton = "com.compal.bioslab.pixsee.pixm01:id/rb_floating_video_radio"

        # elements in "Discard setting" window
        self.discardMessage = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
        self.discardYesButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
        self.discardNoButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"


    def click_save(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.saveButton))
        )
        element = self.driver.find_element("id", self.saveButton)
        element.click()

    def click_return(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.returnButton))
        )
        element = self.driver.find_element("id", self.returnButton)
        element.click()

    def click_keep_playing(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.keepPlayingButton))
        )
        element = self.driver.find_element("id", self.keepPlayingButton)
        element.click()

    def click_audio_only(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.audioOnlyButton))
        )
        element = self.driver.find_element("id", self.audioOnlyButton)
        element.click()

    def click_floating_video(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.floatingVideoButton))
        )
        element = self.driver.find_element("id", self.floatingVideoButton)
        element.click()

    def click_discard_yes(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.discardYesButton))
        )
        element = self.driver.find_element("id", self.discardYesButton)
        element.click()

    def click_discard_no(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.discardNoButton))
        )
        element = self.driver.find_element("id", self.discardNoButton)
        element.click()

    def get_page_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def get_keep_playing_status(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.keepPlayingButton))
        )
        element = self.driver.find_element("id", self.keepPlayingButton)
        return element.get_attribute("checked") == "true"

    def get_discard_message(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.discardMessage))
        )
        element = self.driver.find_element("id", self.discardMessage)
        return element.text

    def get_discard_yes_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.discardYesButton))
        )
        element = self.driver.find_element("id", self.discardYesButton)
        return element.text

    def get_discard_no_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.discardNoButton))
        )
        element = self.driver.find_element("id", self.discardNoButton)
        return element.text

    def is_in_background_play_page(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.keepPlayingButton))
            )
            self.driver.find_element("id", self.keepPlayingButton)
            return True
        except:
            return False
