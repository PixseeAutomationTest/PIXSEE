from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AssistantPage():
    def __init__(self, driver):
        self.driver = driver

        self.backgroundPlayButton = "com.compal.bioslab.pixsee.pixm01:id/clBackgroundPlayContainer"
        self.pixseeCloudButton = "com.compal.bioslab.pixsee.pixm01:id/clPixseeCloudAssistant"
        self.tutorialButton = "com.compal.bioslab.pixsee.pixm01:id/clTutorialButton"
        self.qaButton = "com.compal.bioslab.pixsee.pixm01:id/clQeAButton"
        self.contactUsButton = "com.compal.bioslab.pixsee.pixm01:id/clTroubleShootingButton"
        self.sendErrorButton = "com.compal.bioslab.pixsee.pixm01:id/clSendReportError"

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
