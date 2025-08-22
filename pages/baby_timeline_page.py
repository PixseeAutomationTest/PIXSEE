from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pages.base as base

class BabyTimelinePage():
    def __init__(self, driver):
        self.driver = driver

        self.timeline = "com.compal.bioslab.pixsee.pixm01:id/rvTimeline"
        self.frameTutor = "com.compal.bioslab.pixsee.pixm01:id/clTutorialDescriptionContainer"
        self.homeButton = "com.compal.bioslab.pixsee.pixm01:id/ibButtonHome"
        self.menuButton = "com.compal.bioslab.pixsee.pixm01:id/ibDailyCoverTimelineMenuButtonHome" # When no device are connected
        self.albumButton = "com.compal.bioslab.pixsee.pixm01:id/ibAlbum"
        self.frameButton = "com.compal.bioslab.pixsee.pixm01:id/ibParentingTips"
        self.Tutor = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
        self.TutorDescription = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"

    def click_home(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.homeButton))
        )
        self.driver.find_element("id", self.homeButton).click()
        time.sleep(1)

    def click_menu(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.menuButton))
        )
        self.driver.find_element("id", self.menuButton).click()
        time.sleep(1)

    def click_album(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.albumButton))
        )
        self.driver.find_element("id", self.albumButton).click()
        time.sleep(1)

    def click_frame(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.frameButton))
        )
        self.driver.find_element("id", self.frameButton).click()
        time.sleep(1)

    def has_frame_tutor(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.frameTutor))
            )
            self.driver.find_element("id", self.frameTutor)
            return True
        except:
            return False

    def is_in_baby_timeline_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.timeline))
            )
            self.driver.find_element("id", self.timeline)
            return True
        except:
            return False

    def get_tutor_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.Tutor))
        )
        return self.driver.find_element("id", self.Tutor).text
    def get_tutor_description(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.TutorDescription))
        )
        return self.driver.find_element("id", self.TutorDescription).text.replace("\n", " ")
