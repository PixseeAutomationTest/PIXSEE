from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class WifiSettingsPage():
    def __init__(self, driver):
        self.driver = driver
        self.PopUpTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitleResetWifiAct"
        self.PopUpOk = "com.compal.bioslab.pixsee.pixm01:id/btnResetWifiOk"
        self.PopUpCancel = "com.compal.bioslab.pixsee.pixm01:id/btnResetWifiCancel"
        self.Back = "com.compal.bioslab.pixsee.pixm01:id/ibTimeLapseSettingsBack"
        self.Save = "com.compal.bioslab.pixsee.pixm01:id/tvTimeLapseSettingsSave"
        self.Detection = "com.compal.bioslab.pixsee.pixm01:id/timeLapse_settings_status_text"
        self.DetectionSubtitle = "com.compal.bioslab.pixsee.pixm01:id/timeLapse_settings_subtext"
        self.Switch = "com.compal.bioslab.pixsee.pixm01:id/timeLapse_settings_status_switch"

    def is_in_wifi_settings_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.PopUpTitle))
            )
            return True
        except:
            return False

    def title(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Detection))
            )
            element = self.driver.find_element("id", self.Detection)
            return element.text
        except:
            return None
    def detection_description(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.DetectionSubtitle))
            )
            element = self.driver.find_element("id", self.DetectionSubtitle)
            return element.text
        except:
            return None
    def pop_up_title_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.PopUpTitle))
            )
            element = self.driver.find_element("id", self.PopUpTitle)
            return element.text
        except:
            return None
    def pop_up_ok_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.PopUpOk))
            )
            element = self.driver.find_element("id", self.PopUpOk)
            return element.text
        except:
            return None
    def pop_up_cancel_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.PopUpCancel))
            )
            element = self.driver.find_element("id", self.PopUpCancel)
            return element.text
        except:
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
    def click_pop_up_ok(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.PopUpOk))
        )
        element = self.driver.find_element("id", self.PopUpOk)
        element.click()
    def click_pop_up_cancel(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.PopUpCancel))
        )
        element = self.driver.find_element("id", self.PopUpCancel)
        element.click()





