from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeviceUnbindPage:
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
        self.messageText = "com.compal.bioslab.pixsee.pixm01:id/tvSubtitle"
        self.resetImage = "com.compal.bioslab.pixsee.pixm01:id/ivResetMonitor"

        self.closeButton = "com.compal.bioslab.pixsee.pixm01:id/ibClose"
        self.seenFlashLightButton = "com.compal.bioslab.pixsee.pixm01:id/btnSeenFlashLight"
        self.cancelButton = "com.compal.bioslab.pixsee.pixm01:id/btnCancel"

        '''Unbind Complete Dialog Elements'''
        self.unbindCompletedialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"
        self.unbindCompleteDialogTitle = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
        self.unbindCompleteDialogOkButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"

    def click_close(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.closeButton))
        )
        element = self.driver.find_element("id", self.closeButton)
        element.click()

    def click_seen_flash_light(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.seenFlashLightButton))
        )
        element = self.driver.find_element("id", self.seenFlashLightButton)
        element.click()

    def click_cancel(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelButton))
        )
        element = self.driver.find_element("id", self.cancelButton)
        element.click()

    def click_unbind_complete_dialog_ok(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.unbindCompleteDialogOkButton))
        )
        element = self.driver.find_element("id", self.unbindCompleteDialogOkButton)
        element.click()

    def get_page_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def get_message_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.messageText))
        )
        element = self.driver.find_element("id", self.messageText)
        return element.text

    def get_seen_flash_light_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.seenFlashLightButton))
        )
        element = self.driver.find_element("id", self.seenFlashLightButton)
        return element.text

    def get_cancel_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelButton))
        )
        element = self.driver.find_element("id", self.cancelButton)
        return element.text

    def get_unbind_complete_dialog_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.unbindCompleteDialogTitle))
        )
        element = self.driver.find_element("id", self.unbindCompleteDialogTitle)
        return element.text

    def get_unbind_complete_dialog_ok_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.unbindCompleteDialogOkButton))
        )
        element = self.driver.find_element("id", self.unbindCompleteDialogOkButton)
        return element.text

    def has_unbind_complete_dialog(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.unbindCompletedialog))
            )
            self.driver.find_element("id", self.unbindCompletedialog)
            return True
        except:
            return False

    def is_in_device_unbind_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.resetImage))
            )
            self.driver.find_element("id", self.resetImage)
            return True
        except:
            return False