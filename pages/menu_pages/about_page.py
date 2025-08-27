from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base as base

class AboutPage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/tvContentPlayRoom"
        self.aboutPixseeText = "com.compal.bioslab.pixsee.pixm01:id/tvAboutPixseeTitle"
        self.termsOfServiceText = "com.compal.bioslab.pixsee.pixm01:id/tvTermsTitle"
        self.privacyPolicyText = "com.compal.bioslab.pixsee.pixm01:id/tvPrivacyTitle"
        self.appVersionText = "com.compal.bioslab.pixsee.pixm01:id/tvAppVersion"
        self.cameraVersionText = "com.compal.bioslab.pixsee.pixm01:id/tvDeviceVersion"

        self.returnButton = "com.compal.bioslab.pixsee.pixm01:id/ibBackButton"
        self.aboutPixseeButton = "com.compal.bioslab.pixsee.pixm01:id/clAboutPixseeButton"
        self.termsOfServiceButton = "com.compal.bioslab.pixsee.pixm01:id/clTermsButton"
        self.privacyPolicyButton = "com.compal.bioslab.pixsee.pixm01:id/clPrivacyButton"

        self.aboutPixseeWebsite = "com.android.chrome:id/coordinator"
        self.websiteTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
        self.websiteReturnButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
        self.websiteContent_xpath = '//android.view.View[@resource-id="app"]'
    def click_about_pixsee(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.aboutPixseeButton))
        )
        element = self.driver.find_element("id", self.aboutPixseeButton)
        element.click()

    def click_terms_of_service(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.termsOfServiceButton))
        )
        element = self.driver.find_element("id", self.termsOfServiceButton)
        element.click()

    def click_privacy_policy(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.privacyPolicyButton))
        )
        element = self.driver.find_element("id", self.privacyPolicyButton)
        element.click()

    def click_return(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.returnButton))
        )
        element = self.driver.find_element("id", self.returnButton)
        element.click()

    def click_website_return(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.websiteReturnButton))
        )
        element = self.driver.find_element("id", self.websiteReturnButton)
        element.click()

    def get_page_title_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def get_about_pixsee_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.aboutPixseeText))
        )
        element = self.driver.find_element("id", self.aboutPixseeText)
        return element.text

    def get_terms_of_service_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.termsOfServiceText))
        )
        element = self.driver.find_element("id", self.termsOfServiceText)
        return element.text

    def get_privacy_policy_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.privacyPolicyText))
        )
        element = self.driver.find_element("id", self.privacyPolicyText)
        return element.text

    def get_app_version_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.appVersionText))
        )
        element = self.driver.find_element("id", self.appVersionText)
        return element.text

    def get_camera_version_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.cameraVersionText))
        )
        element = self.driver.find_element("id", self.cameraVersionText)
        return element.text

    def get_website_title_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.websiteTitleText))
        )
        element = self.driver.find_element("id", self.websiteTitleText)
        return element.text

    def is_in_about_page(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.aboutPixseeText))
            )
            self.driver.find_element("id", self.aboutPixseeText)
            return True
        except:
            return False

    def is_in_about_pixsee_website(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.aboutPixseeWebsite))
            )
            self.driver.find_element("id", self.aboutPixseeWebsite)
            return True
        except:
            return False

    def is_in_embedded_website(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("xpath", self.websiteContent_xpath))
            )
            self.driver.find_element("xpath", self.websiteContent_xpath)
            return True
        except:
            return False