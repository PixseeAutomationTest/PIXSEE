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
        self.firmwareRelease = "com.compal.bioslab.pixsee.pixm01:id/tvFirmwareReleaseDate"
        self.syncingText = "com.compal.bioslab.pixsee.pixm01:id/tvSnackbarToastLabel"

        self.backButton = "com.compal.bioslab.pixsee.pixm01:id/ibProfileSettingsBackButton"
        self.unbindDeviceButton = "com.compal.bioslab.pixsee.pixm01:id/btnDisconnectDevice"
        self.IQSettingButton = "com.compal.bioslab.pixsee.pixm01:id/ibIQSetting"
        self.rotateButton = "com.compal.bioslab.pixsee.pixm01:id/ibRotateSetting"
        self.deviceInfo = "com.compal.bioslab.pixsee.pixm01:id/deviceInfoTextView"
        self.locationButton = "com.compal.bioslab.pixsee.pixm01:id/msDeviceLocationName"
        self.timeZoneButton = "com.compal.bioslab.pixsee.pixm01:id/msTimezoneName"
        self.checkUpdateButton = "com.compal.bioslab.pixsee.pixm01:id/checkUpdate"
        self.rebootDeviceButton = "com.compal.bioslab.pixsee.pixm01:id/btnRebootDevice"

        self.IQSettingBar = "com.compal.bioslab.pixsee.pixm01:id/llToggleIQSetting"
        self.IQOptions = [
            "com.compal.bioslab.pixsee.pixm01:id/optionIQ1",
            "com.compal.bioslab.pixsee.pixm01:id/optionIQ2",
            "com.compal.bioslab.pixsee.pixm01:id/optionIQ3",
            "com.compal.bioslab.pixsee.pixm01:id/optionIQ4",
        ]
        self.dialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"

        '''Device Info Dialog'''
        self.deviceInfoDialogTitleText = "com.compal.bioslab.pixsee.pixm01:id/alertDialogTitleTextView"
        self.productNameTitleText = "com.compal.bioslab.pixsee.pixm01:id/productNameTitleTextView"
        self.productNameText = "com.compal.bioslab.pixsee.pixm01:id/productNameValueTextView"
        self.productModelTitleText = "com.compal.bioslab.pixsee.pixm01:id/productModelTitleTextView"
        self.productModelText = "com.compal.bioslab.pixsee.pixm01:id/productModelValueTextView"
        self.productSerialNumberTitleText = "com.compal.bioslab.pixsee.pixm01:id/serialNumberTitleTextView"
        self.productSerialNumberText = "com.compal.bioslab.pixsee.pixm01:id/serialNumberValueTextView"
        self.warrantyPeriodTitleText = "com.compal.bioslab.pixsee.pixm01:id/warrantyPeriodTitleTextView"
        self.warrantyPeriodText = "com.compal.bioslab.pixsee.pixm01:id/warrantyPeriodValueTextView"
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

    def click_IQ_setting(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.IQSettingButton))
        )
        element = self.driver.find_element("id", self.IQSettingButton)
        element.click()

    def click_IQ_option(self, option_number = 0):
        if option_number < 0 or option_number >= len(self.IQOptions):
            raise IndexError("IndexError: IQ option index out of range")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.IQOptions[option_number]))
        )
        element = self.driver.find_element("id", self.IQOptions[option_number])
        element.click()

    def click_rotate(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.rotateButton))
        )
        element = self.driver.find_element("id", self.rotateButton)
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

    def click_device_unbind_dialog_yes(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceUnbindDialogYesButton))
        )
        element = self.driver.find_element("id", self.deviceUnbindDialogYesButton)
        element.click()

    def click_device_unbind_dialog_no(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceUnbindDialogNoButton))
        )
        element = self.driver.find_element("id", self.deviceUnbindDialogNoButton)
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

    def get_IQ_setting_bar_len(self):
        find_options = 0
        for i in range(len(self.IQOptions)):
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.IQOptions[i]))
            )
            find_options += 1
        return find_options

    def get_IQ_setting_current_level(self):
        for i in range(4):
            element = self.driver.find_element("id", self.IQOptions[i])
            if element.get_attribute("checked") == "true":
                return i
        return -1

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

    def get_current_location_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.locationButton))
        )
        parent_element = self.driver.find_element("id", self.locationButton)
        element = parent_element.find_element("id", self.listOption)
        return element.text

    def get_time_zone_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.timeZoneTitleText))
        )
        element = self.driver.find_element("id", self.timeZoneTitleText)
        return element.text

    def get_current_time_zone_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.timeZoneButton))
        )
        parent_element = self.driver.find_element("id", self.timeZoneButton)
        element = parent_element.find_element("id", self.listOption)
        return element.text

    # FIXME: Calculate the time zone difference in hours and minutes, but Android doesn't support Daylight saving time
    # def get_time_zone(self):
    #     time_zone_text = self.get_current_time_zone_text()
    #     match = re.search(r"\(GMT([+-])(\d{2}):(\d{2})\)", time_zone_text)
    #     if not match:
    #         raise ValueError("Time zone format parsing failed")
    #     sign, hour_str, minute_str = match.groups()
    #     difference_hours = int(hour_str)
    #     difference_minutes = int(minute_str)
    #     if sign == '-':
    #         difference_minutes = -difference_hours
    #         difference_minutes = -difference_minutes
    #
    #     return difference_hours, difference_minutes

    def get_current_version_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.currentVersionText))
        )
        element = self.driver.find_element("id", self.currentVersionText)
        return element.text

    def get_firmware_release_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.firmwareRelease))
        )
        element = self.driver.find_element("id", self.firmwareRelease)
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

    def get_device_info_dialog_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceInfoDialogTitleText))
        )
        element = self.driver.find_element("id", self.deviceInfoDialogTitleText)
        return element.text

    def get_product_name_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.productNameTitleText))
        )
        element = self.driver.find_element("id", self.productNameTitleText)
        return element.text

    def get_product_name_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.productNameText))
        )
        element = self.driver.find_element("id", self.productNameText)
        return element.text

    def get_product_model_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.productModelTitleText))
        )
        element = self.driver.find_element("id", self.productModelTitleText)
        return element.text

    def get_product_model_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.productModelText))
        )
        element = self.driver.find_element("id", self.productModelText)
        return element.text

    def get_product_serial_number_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.productSerialNumberTitleText))
        )
        element = self.driver.find_element("id", self.productSerialNumberTitleText)
        return element.text

    def get_product_serial_number_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.productSerialNumberText))
        )
        element = self.driver.find_element("id", self.productSerialNumberText)
        return element.text

    def get_warranty_period_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.warrantyPeriodTitleText))
        )
        element = self.driver.find_element("id", self.warrantyPeriodTitleText)
        return element.text

    def get_warranty_period_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.warrantyPeriodText))
        )
        element = self.driver.find_element("id", self.warrantyPeriodText)
        return element.text

    def get_device_info_dialog_ok_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceInfoDialogOkButton))
        )
        element = self.driver.find_element("id", self.deviceInfoDialogOkButton)
        return element.text

    def get_device_unbind_dialog_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceUnbindDialogTitleText))
        )
        element = self.driver.find_element("id", self.deviceUnbindDialogTitleText)
        return element.text

    def get_device_unbind_dialog_description_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceUnbindDialogDescriptionText))
        )
        element = self.driver.find_element("id", self.deviceUnbindDialogDescriptionText)
        return element.text

    def get_device_unbind_dialog_yes_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceUnbindDialogYesButton))
        )
        element = self.driver.find_element("id", self.deviceUnbindDialogYesButton)
        return element.text

    def get_device_unbind_dialog_no_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deviceUnbindDialogNoButton))
        )
        element = self.driver.find_element("id", self.deviceUnbindDialogNoButton)
        return element.text

    def get_syncing_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.syncingText))
        )
        element = self.driver.find_element("id", self.syncingText)
        return element.text

    def select_location(self, number = 0): # Default: baby room = 0
        self.click_location()
        time.sleep(1)
        if not self.has_selection_list():
            raise AssertionError("Can't find selection list for location")
        elements = self.driver.find_elements("id", self.listOption)
        if number < len(elements):
            elements[number].click()
        else:
            raise IndexError("IndexError: Location index out of range")

    def select_time_zone(self, number = 44): # Default: Taiwan = 44
        self.click_time_zone()
        time.sleep(1)
        if not self.has_selection_list():
            raise AssertionError("Can't find selection list for time zone")
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

    def has_IQ_setting_bar(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.IQSettingBar))
            )
            self.driver.find_element("id", self.IQSettingBar)
            return True
        except:
            return False

    def has_syncing_toast(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.syncingText))
            )
            self.driver.find_element("id", self.syncingText)
            return True
        except:
            return False

    def has_selection_list(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("class name", self.list_classname))
            )
            self.driver.find_element("class name", self.list_classname)
            return True
        except:
            return False

    def has_device_info_dialog(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.dialog))
            )
            self.driver.find_element("id", self.deviceInfoDialogTitleText)
            return True
        except:
            return False

    def has_device_unbind_dialog(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.dialog))
            )
            self.driver.find_element("id", self.deviceUnbindDialogTitleText)
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


