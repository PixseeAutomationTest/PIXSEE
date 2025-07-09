from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base import BaseTestCase

class FamilyAlbumCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.menuButton = "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome"
        self.familyAlbumButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsGallery"
        self.familyAlbumActivity = "com.compal.bioslab.pixsee.pixm01:id/clDailyCoverGallery"

    def test_size_familyAlbum(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.menuButton))
        )
        self.driver.find_element(AppiumBy.ID, self.menuButton).click()
        self.driver.find_element(AppiumBy.ID, self.familyAlbumButton).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.familyAlbumActivity))
        )
        photos = self.driver.find_elements(By.ID, "com.compal.bioslab.pixsee.pixm01:id/gallery_thumbnail")
        print("找到的相片數量:", len(photos))
