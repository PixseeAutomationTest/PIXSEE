import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class MusicTutorial:
    def __init__(self,driver):
        self.driver=driver

        self.skip="com.compal.bioslab.pixsee.pixm01:id/btnSkip"#Let's start也是這個
        self.close="com.compal.bioslab.pixsee.pixm01:id/ibBackButton"
    def click_close(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.close))
        )
        element = self.driver.find_element("id", self.close)
        element.click()
    def find_close(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(("id", self.close))
            )
            return True
        except:
            return False
    def success_check(self):
        time.sleep(0.5)
        try:
            if self.find_close() == False:
                print("----success: Music Tutorial skip success")
            else:
                print("----failed: Music Tutorial skip failed")
        except:
            print("----error: Music Tutorial skip failed")
    def click_skip(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.skip))
        )
        element = self.driver.find_element("id", self.skip)
        element.click()