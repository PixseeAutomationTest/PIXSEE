from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base as base

class BabyCarePage():
    def __init__(self, driver):
        self.driver = driver
        self.Header = "com.compal.bioslab.pixsee.pixm01:id/tvCryAnalysisTitle"
        self.Title = "com.compal.bioslab.pixsee.pixm01:id/tvBabyCareTitleCryDecoder"
        self.CryTipTitle = "com.compal.bioslab.pixsee.pixm01:id/tvCryTipTitle"
        self.CryTipPreview = "com.compal.bioslab.pixsee.pixm01:id/jtvCryTipPreview"

    def header_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.Header))
        )
        return self.driver.find_element("id", self.Header).text
    def title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.Title))
        )
        return self.driver.find_element("id", self.Title).text
    def cry_tip_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.CryTipTitle))
        )
        return self.driver.find_element("id", self.CryTipTitle).text
    def cry_tip_preview(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.CryTipPreview))
        )
        return self.driver.find_element("id", self.CryTipPreview).text