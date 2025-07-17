from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BabyTimelinePage():
    def __init__(self, driver):
        self.driver = driver

        self.timeline = "com.compal.bioslab.pixsee.pixm01:id/rvTimeline"
        self.homeButton = "com.compal.bioslab.pixsee.pixm01:id/ibButtonHome"
        self.menuButton = "com.compal.bioslab.pixsee.pixm01:id/ibDailyCoverTimelineMenuButtonHome" # When no device are connected
        self.albumButton = "com.compal.bioslab.pixsee.pixm01:id/ibAlbum"
        self.frameButton = "com.compal.bioslab.pixsee.pixm01:id/ibParentingTips"

    def click_home(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.homeButton))
        )
        self.driver.find_element("id", self.homeButton).click()
        time.sleep(1)

    def click_menu(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.menuButton))
        )
        self.driver.find_element("id", self.menuButton).click()
        time.sleep(1)

    def click_album(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.albumButton))
        )
        self.driver.find_element("id", self.albumButton).click()
        time.sleep(1)

    def click_frame(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.frameButton))
        )
        self.driver.find_element("id", self.frameButton).click()
        time.sleep(1)

    def is_in_baby_timeline_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.timeline))
            )
            self.driver.find_element("id", self.timeline)
            return True
        except:
            return False
