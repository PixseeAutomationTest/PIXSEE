from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages.base as base

class VoiceCommandPage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
        self.choosingLanguageText = "com.compal.bioslab.pixsee.pixm01:id/tvLanguage"
        self.englishText = "com.compal.bioslab.pixsee.pixm01:id/rb_voice_command_language_english_txt"
        self.chineseText = "com.compal.bioslab.pixsee.pixm01:id/rb_voice_command_language_chinese_txt"
        self.voiceAssistantText = "com.compal.bioslab.pixsee.pixm01:id/vVoiceCommandLabel"
        self.commandTitlesText = "com.compal.bioslab.pixsee.pixm01:id/tvVoiceCommandCardTitle"
        self.commandContentsText = "com.compal.bioslab.pixsee.pixm01:id/tvVoiceCommandCardContent"

        self.backButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back"
        self.saveButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_save"
        self.englishCheckbox = "com.compal.bioslab.pixsee.pixm01:id/rb_voice_command_language_english"
        self.chineseCheckbox = "com.compal.bioslab.pixsee.pixm01:id/rb_voice_command_language_chinese"

        '''Discard dialog'''
        self.discardDialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"
        self.discardDialogTitle = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
        self.discardDialogYesButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
        self.discardDialogNoButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"

    def click_back(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.backButton))
        )
        element = self.driver.find_element("id", self.backButton)
        element.click()

    def click_save(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.saveButton))
        )
        element = self.driver.find_element("id", self.saveButton)
        element.click()

    def click_english_checkbox(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.englishCheckbox))
        )
        element = self.driver.find_element("id", self.englishCheckbox)
        element.click()

    def click_chinese_checkbox(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.chineseCheckbox))
        )
        element = self.driver.find_element("id", self.chineseCheckbox)
        element.click()

    def click_discard_dialog_yes(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.discardDialogYesButton))
        )
        element = self.driver.find_element("id", self.discardDialogYesButton)
        element.click()

    def click_discard_dialog_no(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.discardDialogNoButton))
        )
        element = self.driver.find_element("id", self.discardDialogNoButton)
        element.click()

    def get_page_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def get_save_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.saveButton))
        )
        element = self.driver.find_element("id", self.saveButton)
        return element.text

    def get_save_button_enabled(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.saveButton))
        )
        element = self.driver.find_element("id", self.saveButton)
        return element.get_attribute("enabled") == "true"

    def get_choosing_language_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.choosingLanguageText))
        )
        element = self.driver.find_element("id", self.choosingLanguageText)
        return element.text

    def get_english_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.englishText))
        )
        element = self.driver.find_element("id", self.englishText)
        return element.text

    def get_english_checkbox_status(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.englishCheckbox))
        )
        element = self.driver.find_element("id", self.englishCheckbox)
        return element.get_attribute("checked") == "true"

    def get_chinese_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.chineseText))
        )
        element = self.driver.find_element("id", self.chineseText)
        return element.text

    def get_chinese_checkbox_status(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.chineseCheckbox))
        )
        element = self.driver.find_element("id", self.chineseCheckbox)
        return element.get_attribute("checked") == "true"

    def get_voice_assistant_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.voiceAssistantText))
        )
        element = self.driver.find_element("id", self.voiceAssistantText)
        return element.text

    def get_music_command_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.commandTitlesText))
        )
        elements = self.driver.find_elements("id", self.commandTitlesText)
        return elements[0].text

    def get_music_command_content(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.commandContentsText))
        )
        elements = self.driver.find_elements("id", self.commandContentsText)
        return elements[0].text

    def get_volume_command_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.commandTitlesText))
        )
        elements = self.driver.find_elements("id", self.commandTitlesText)
        return elements[1].text

    def get_volume_command_content(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.commandContentsText))
        )
        elements = self.driver.find_elements("id", self.commandContentsText)
        return elements[1].text

    def get_camera_command_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.commandTitlesText))
        )
        elements = self.driver.find_elements("id", self.commandTitlesText)
        return elements[2].text

    def get_camera_command_content(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.commandContentsText))
        )
        elements = self.driver.find_elements("id", self.commandContentsText)
        return elements[2].text

    def get_discard_dialog_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.discardDialogTitle))
        )
        element = self.driver.find_element("id", self.discardDialogTitle)
        return element.text

    def get_discard_dialog_yes_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.discardDialogYesButton))
        )
        element = self.driver.find_element("id", self.discardDialogYesButton)
        return element.text

    def get_discard_dialog_no_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.discardDialogNoButton))
        )
        element = self.driver.find_element("id", self.discardDialogNoButton)
        return element.text

    def has_discard_dialog(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.discardDialog))
            )
            find_element = self.driver.find_element("id", self.discardDialog)
            return True
        except:
            return False

    def is_in_voice_command_page(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.choosingLanguageText))
            )
            self.driver.find_elements("id", self.commandContentsText)
            return True
        except:
            return False
