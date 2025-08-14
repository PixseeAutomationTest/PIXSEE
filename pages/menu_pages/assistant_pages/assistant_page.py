from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AssistantPage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/tvHelpMenuBarTitle"

        self.returnButton = "com.compal.bioslab.pixsee.pixm01:id/ibHelpMenuBackButton"
        self.backgroundPlayButton = "com.compal.bioslab.pixsee.pixm01:id/clBackgroundPlayContainer"
        self.backgroundPlayText = "com.compal.bioslab.pixsee.pixm01:id/background_play_label"
        self.backgroundPlaySubUp = "com.compal.bioslab.pixsee.pixm01:id/clBackgroundPlayContainer"
        self.backgroundPlaySub ="//android.widget.TextView"
        self.pixseeCloudButton = "com.compal.bioslab.pixsee.pixm01:id/clPixseeCloudAssistant"
        self.pixseeCloudText = "com.compal.bioslab.pixsee.pixm01:id/tvPixseeCloudItemTitle"
        self.pixseeCloudSub = "com.compal.bioslab.pixsee.pixm01:id/tvCloudUsage"
        self.tutorialButton = "com.compal.bioslab.pixsee.pixm01:id/clTutorialButton"
        self.tutorialText = "com.compal.bioslab.pixsee.pixm01:id/tvTutorialMenuItemTitle"
        self.qaButton = "com.compal.bioslab.pixsee.pixm01:id/clQeAButton"
        self.qaText = "com.compal.bioslab.pixsee.pixm01:id/tvQeAMenuItemTitle"
        self.contactUsButton = "com.compal.bioslab.pixsee.pixm01:id/clTroubleShootingButton"
        self.contactUsText = "com.compal.bioslab.pixsee.pixm01:id/tvTroubleShootingMenuItemTitle"
        self.sendErrorButton = "com.compal.bioslab.pixsee.pixm01:id/clSendReportError"
        self.sendErrorText = "com.compal.bioslab.pixsee.pixm01:id/tvSendReportErrorMenuItemTitle"
        self.sendButton = "com.compal.bioslab.pixsee.pixm01:id/btSendReportError"
        self.SupportWeb = "com.android.chrome:id/url_bar"

    def click_return(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.returnButton))
        )
        element = self.driver.find_element("id", self.returnButton)
        element.click()

    def click_background_play(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.backgroundPlayButton))
        )
        element = self.driver.find_element("id", self.backgroundPlayButton)
        element.click()

    def click_pixsee_cloud(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.pixseeCloudButton))
        )
        element = self.driver.find_element("id", self.pixseeCloudButton)
        element.click()

    def click_tutorial(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.tutorialButton))
        )
        element = self.driver.find_element("id", self.tutorialButton)
        element.click()

    def click_qa(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.qaButton))
        )
        element = self.driver.find_element("id", self.qaButton)
        element.click()

    def click_contact_us(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.contactUsButton))
        )
        element = self.driver.find_element("id", self.contactUsButton)
        element.click()

    def click_send_error(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.sendErrorButton))
        )
        element = self.driver.find_element("id", self.sendErrorButton)
        element.click()

    def click_send(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.sendButton))
        )
        element = self.driver.find_element("id", self.sendButton)
        element.click()

    def is_in_assistant_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.backgroundPlayButton))
            )
            self.driver.find_element("id", self.backgroundPlayButton)
            return True
        except:
            return False

    def url_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.SupportWeb))
            )
            element = self.driver.find_element("id", self.SupportWeb)
            return element.text
        except:
            return None

    def background_play_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.backgroundPlayText))
            )
            element = self.driver.find_element("id", self.backgroundPlayText)
            return element.text
        except:
            return None

    def background_play_sub_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.backgroundPlaySubUp))
            )
            uplayer = self.driver.find_element("id", self.backgroundPlaySubUp)
            elements = uplayer.find_elements("xpath", self.backgroundPlaySub)
            return elements[2].text
        except:
            return None

    def pixsee_cloud_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.pixseeCloudText))
            )
            element = self.driver.find_element("id", self.pixseeCloudText)
            return element.text
        except:
            return None

    def pixsee_cloud_sub_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.pixseeCloudSub))
            )
            element = self.driver.find_element("id", self.pixseeCloudSub)
            return element.text
        except:
            return None

    def tutorial_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.tutorialText))
            )
            element = self.driver.find_element("id", self.tutorialText)
            return element.text
        except:
            return None

    def qa_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.qaText))
            )
            element = self.driver.find_element("id", self.qaText)
            return element.text
        except:
            return None

    def contact_us_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.contactUsText))
            )
            element = self.driver.find_element("id", self.contactUsText)
            return element.text
        except:
            return None

    def send_error_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.sendErrorText))
            )
            element = self.driver.find_element("id", self.sendErrorText)
            return element.text
        except:
            return None

    def send_button_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.sendButton))
            )
            element = self.driver.find_element("id", self.sendButton)
            return element.text
        except:
            return None

    def is_backgroud_play_able_to_click(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.backgroundPlayButton))
        )
        button = self.driver.find_element("id", self.backgroundPlayButton)
        is_enable = button.get_attribute("enabled")
        return is_enable == "true"

