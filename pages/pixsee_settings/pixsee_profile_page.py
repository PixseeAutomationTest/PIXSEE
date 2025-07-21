from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time

class PixseeProfilePage:
    def __init__(self,driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/tvBarTitle"
        self.videoView = "com.compal.bioslab.pixsee.pixm01:id/videoTextureView"
        self.locationTitleText = "com.compal.bioslab.pixsee.pixm01:id/tvDeviceLocationTitle"
        self.timeZoneTitleText = "com.compal.bioslab.pixsee.pixm01:id/tvTimeZoneTitle"
        self.currentVersionText = "com.compal.bioslab.pixsee.pixm01:id/tvCurrentVersion"

        self.backButton = "com.compal.bioslab.pixsee.pixm01:id/ibProfileSettingsBackButton"
        self.unbindDeviceButton = "com.compal.bioslab.pixsee.pixm01:id/btnDisconnectDevice"
        self.deviceInfo = "com.compal.bioslab.pixsee.pixm01:id/deviceInfoTextView"
        self.locationButton = "com.compal.bioslab.pixsee.pixm01:id/msDeviceLocationName"
        self.timeZoneButton = "com.compal.bioslab.pixsee.pixm01:id/msTimezoneName"
        self.checkUpdateButton = "com.compal.bioslab.pixsee.pixm01:id/checkUpdate"
        self.rebootDeviceButton = "com.compal.bioslab.pixsee.pixm01:id/btnRebootDevice"

        self.dialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"

        '''Device Info Dialog'''
        self.deviceInfoDialogTitleText = "com.compal.bioslab.pixsee.pixm01:id/alertDialogTitleTextView"
        self.productNameTitleText = "com.compal.bioslab.pixsee.pixm01:id/productNameTitleTextView"
        self.productModelTitleText = "com.compal.bioslab.pixsee.pixm01:id/productModelTitleTextView"
        self.productSerialNumberTitleText = "com.compal.bioslab.pixsee.pixm01:id/serialNumberTitleTextView"
        self.warrantyPeriodTitleText = "com.compal.bioslab.pixsee.pixm01:id/warrantyPeriodTitleTextView"
        self.deviceInfoDialogOkButton = "com.compal.bioslab.pixsee.pixm01:id/deviceInfoDialogOkButton"

        '''Device Unbind Dialog'''
        self.deviceUnbindDialogTitleText = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
        self.deviceUnbindDialogDescriptionText = "com.compal.bioslab.pixsee.pixm01:id/tvMessageAlertDialog"
        self.deviceUnbindDialogYesButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
        self.deviceUnbindDialogNoButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"


        '''Location and Time Zone List'''
        self.list_classname = "android.widget.ListView"
        self.listOption = "android:id/text1"


    def click_back(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.backButton))
        )
        element = self.driver.find_element("id", self.backButton)
        element.click()

    def click_unbind_device(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.unbindDeviceButton))
        )
        element = self.driver.find_element("id", self.unbindDeviceButton)
        element.click()

    def click_device_info(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceInfo))
        )
        element = self.driver.find_element("id", self.deviceInfo)
        element.click()

    def click_location(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.locationButton))
        )
        element = self.driver.find_element("id", self.locationButton)
        element.click()

    def click_time_zone(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.timeZoneButton))
        )
        element = self.driver.find_element("id", self.timeZoneButton)
        element.click()

    def click_check_update(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.checkUpdateButton))
        )
        element = self.driver.find_element("id", self.checkUpdateButton)
        element.click()

    def click_reboot_device(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.rebootDeviceButton))
        )
        element = self.driver.find_element("id", self.rebootDeviceButton)
        element.click()

    def click_device_info_dialog_ok(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceInfoDialogOkButton))
        )
        element = self.driver.find_element("id", self.deviceInfoDialogOkButton)
        element.click()

    def get_page_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def get_unbind_device_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.unbindDeviceButton))
        )
        element = self.driver.find_element("id", self.unbindDeviceButton)
        return element.text

    def get_device_info_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceInfo))
        )
        element = self.driver.find_element("id", self.deviceInfo)
        return element.text

    def get_location_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.locationTitleText))
        )
        element = self.driver.find_element("id", self.locationTitleText)
        return element.text

    def get_time_zone_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.timeZoneTitleText))
        )
        element = self.driver.find_element("id", self.timeZoneTitleText)
        return element.text

    def get_current_version_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.currentVersionText))
        )
        element = self.driver.find_element("id", self.currentVersionText)
        return element.text

    def get_check_update_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.checkUpdateButton))
        )
        element = self.driver.find_element("id", self.checkUpdateButton)
        return element.text

    def get_reboot_device_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.rebootDeviceButton))
        )
        element = self.driver.find_element("id", self.rebootDeviceButton)
        return element.text

    def select_location(self, number = 0): # Default: baby room = 0
        self.click_location()
        time.sleep(1)
        elements = self.driver.find_elements("id", "android:id/text1")
        if number < len(elements):
            elements[number].click()
        else:
            raise IndexError("IndexError: Location index out of range")

    def select_time_zone(self, number = 44): # Default: Taiwan = 44
        self.click_time_zone()
        time.sleep(1)
        # Slide to the top of the list
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().className("{self.list_classname}")).setAsVerticalList().scrollToBeginning(10)'
        )
        time.sleep(1)

        last_count = 0
        all_items = []
        seen_texts = set()

        while True:
            visible_items = self.driver.find_elements("id", self.listOption)
            new_items = [element for element in visible_items if element.text not in seen_texts]

            for element in new_items:
                text = element.text
                all_items.append(element)
                seen_texts.add(text)

            if len(all_items) > number:
                all_items[number].click()
                return

            if len(all_items) == last_count:
                raise IndexError("IndexError: Time Zone index out of range")
            last_count = len(all_items)

            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().className("{self.list_classname}")).setAsVerticalList().scrollForward();'
            )
            time.sleep(1)


    def has_device_info_dialog(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.dialog))
            )
            self.driver.find_element("id", self.deviceInfoDialogTitleText)
            return True
        except:
            return False

    def is_in_pixsee_profile_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.videoView))
            )
            self.driver.find_element("id", self.videoView)
            return True
        except:
            return False


