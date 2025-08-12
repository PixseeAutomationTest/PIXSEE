from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from PIL import Image

class PixseeCloudPage():
    def __init__(self, driver):
        self.driver = driver
        self.Back = "com.compal.bioslab.pixsee.pixm01:id/ibBackButton"
        self.Header = "com.compal.bioslab.pixsee.pixm01:id/tvHelpMenuBarTitle"
        self.PreviousSubscription = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
        self.Remaining = "com.compal.bioslab.pixsee.pixm01:id/tvSubtitle"
        self.Description = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
        self.Download = "com.compal.bioslab.pixsee.pixm01:id/ivDownloadIcon"
        self.Percent = "com.compal.bioslab.pixsee.pixm01:id/tvPercentageValue"
        self.MBused = "com.compal.bioslab.pixsee.pixm01:id/tvUsedStorage"
        self.TotalStorage = "com.compal.bioslab.pixsee.pixm01:id/tvUsedStorageComplement"
        self.Upgrade = "com.compal.bioslab.pixsee.pixm01:id/btnUpgradePlan"
        self.Photo = "com.compal.bioslab.pixsee.pixm01:id/tvPhotos"
        self.PhotoStorage = "com.compal.bioslab.pixsee.pixm01:id/tvPhotosStorage"
        self.PhotoIndicator = "com.compal.bioslab.pixsee.pixm01:id/viewPhotos"
        self.Videos = "com.compal.bioslab.pixsee.pixm01:id/tvVideo"
        self.VideosStorage = "com.compal.bioslab.pixsee.pixm01:id/tvVideoStorage"
        self.VideosIndicator = "com.compal.bioslab.pixsee.pixm01:id/viewVideo"
        self.Story = "com.compal.bioslab.pixsee.pixm01:id/tvSlideshow"
        self.StoryStorage = "com.compal.bioslab.pixsee.pixm01:id/tvSlideshowStorage"
        self.StoryIndicator = "com.compal.bioslab.pixsee.pixm01:id/viewSlideshow"
        self.VoiceRecorder = "com.compal.bioslab.pixsee.pixm01:id/tvVoiceRecord"
        self.VoiceRecorderStorage = "com.compal.bioslab.pixsee.pixm01:id/tvVoiceRecordStorage"
        self.VoiceRecorderIndicator = "com.compal.bioslab.pixsee.pixm01:id/viewVoiceRecord"
        self.BackUpDataButton = "com.compal.bioslab.pixsee.pixm01:id/btBackupData"
        self.FreeUp = "com.compal.bioslab.pixsee.pixm01:id/tvCleanUpStorage"
        self.Ok = "com.compal.bioslab.pixsee.pixm01:id/btnOK"
        self.Cancel = "com.compal.bioslab.pixsee.pixm01:id/btnCancel"
        self.AllData = "com.compal.bioslab.pixsee.pixm01:id/tvAllData"
        self.AllDataCheckbox = "com.compal.bioslab.pixsee.pixm01:id/viewCbAllData"


    def click_back(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Back))
        )
        element = self.driver.find_element("id", self.Back)
        element.click()
    def click_download(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Download))
        )
        element = self.driver.find_element("id", self.Download)
        element.click()
    def click_upgrade(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Upgrade))
        )
        element = self.driver.find_element("id", self.Upgrade)
        element.click()
    def click_backup_data(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.BackUpDataButton))
        )
        element = self.driver.find_element("id", self.BackUpDataButton)
        element.click()
    def click_free_up(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.FreeUp))
        )
        element = self.driver.find_element("id", self.FreeUp)
        element.click()
    def click_ok(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Ok))
        )
        element = self.driver.find_element("id", self.Ok)
        element.click()
    def click_cancel(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Cancel))
        )
        element = self.driver.find_element("id", self.Cancel)
        element.click()

    def is_in_pixsee_cloud_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Story))
            )
            return True
        except :
            return False

    def header_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Header))
        )
        element = self.driver.find_element("id", self.Header)
        return element.text
    def previous_subscription_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.PreviousSubscription))
        )
        element = self.driver.find_element("id", self.PreviousSubscription)
        return element.text
    def remaining_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Remaining))
        )
        element = self.driver.find_element("id", self.Remaining)
        return element.text
    def description_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Description))
        )
        element = self.driver.find_element("id", self.Description)
        return element.text
    def upgrade_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Upgrade))
        )
        element = self.driver.find_element("id", self.Upgrade)
        return element.text
    def percent_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Percent))
        )
        element = self.driver.find_element("id", self.Percent)
        return element.text
    def mb_used_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.MBused))
        )
        element = self.driver.find_element("id", self.MBused)
        return element.text
    def total_storage_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.TotalStorage))
        )
        element = self.driver.find_element("id", self.TotalStorage)
        return element.text
    def photo_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Photo))
        )
        element = self.driver.find_element("id", self.Photo)
        return element.text
    def photo_storage_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.PhotoStorage))
        )
        element = self.driver.find_element("id", self.PhotoStorage)
        return element.text
    def videos_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Videos))
        )
        element = self.driver.find_element("id", self.Videos)
        return element.text
    def videos_storage_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.VideosStorage))
        )
        element = self.driver.find_element("id", self.VideosStorage)
        return element.text
    def story_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Story))
        )
        element = self.driver.find_element("id", self.Story)
        return element.text
    def story_storage_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.StoryStorage))
        )
        element = self.driver.find_element("id", self.StoryStorage)
        return element.text
    def voice_recorder_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.VoiceRecorder))
        )
        element = self.driver.find_element("id", self.VoiceRecorder)
        return element.text
    def voice_recorder_storage_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.VoiceRecorderStorage))
        )
        element = self.driver.find_element("id", self.VoiceRecorderStorage)
        return element.text
    def back_up_data_button_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.BackUpDataButton))
        )
        element = self.driver.find_element("id", self.BackUpDataButton)
        return element.text
    def free_up_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.FreeUp))
        )
        element = self.driver.find_element("id", self.FreeUp)
        return element.text

    def parse_storage_usage(self,text):
        # find numbers in the text
        numbers = re.findall(r"[\d.]+", text)
        if len(numbers) >= 2:
            used = float(numbers[0])  # first number
            total = float(numbers[1])  # second number
            return used, total
        else:
            num = float(numbers[0])
            return num

    def photo_color(self):
        element_color = self.driver.find_element("id", self.PhotoIndicator)
        x = element_color.location['x'] + 17
        y = element_color.location['y'] + 17
        '''
        w = element_color.size['width']
        h = element_color.size['height']
        center_x = x + w // 2
        center_y = y + h // 2
        '''
        return x, y
    def videos_color(self):
        element_color = self.driver.find_element("id", self.VideosIndicator)
        x = element_color.location['x'] + 17
        y = element_color.location['y'] + 17
        '''
        w = element_color.size['width']
        h = element_color.size['height']
        center_x = x + w // 2
        center_y = y + h // 2
        '''
        return x, y
    def story_color(self):
        element_color = self.driver.find_element("id", self.StoryIndicator)
        x = element_color.location['x'] + 17
        y = element_color.location['y'] + 17
        '''
        w = element_color.size['width']
        h = element_color.size['height']
        center_x = x + w // 2
        center_y = y + h // 2
        '''
        return x, y
    def voice_recorder_color(self):
        element_color = self.driver.find_element("id", self.VoiceRecorderIndicator)
        x = element_color.location['x'] + 17
        y = element_color.location['y'] + 17
        '''
        w = element_color.size['width']
        h = element_color.size['height']
        center_x = x + w // 2
        center_y = y + h // 2
        '''
        return x, y
    def is_pixel_color(self, x, y, target_color):
        """
        Take a screenshot and check if the pixel at coordinates (x, y) matches the given RGB color exactly.

        :param y: vertical coordinate
        :param x: horizontal coordinate
        :param target_color: (R, G, B) tuple
        :return: True or False
        """
        screenshot_path = "screen.png"
        self.driver.save_screenshot(screenshot_path)

        img = Image.open(screenshot_path)
        pixel = img.getpixel((x, y))[:3]  # 只取 R, G, B

        in_range = (pixel == target_color)
        print(f"Pixel at ({x},{y}) = {pixel}, match target: {in_range}")
        return in_range


