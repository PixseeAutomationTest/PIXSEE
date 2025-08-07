from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import datetime
import time
import pages.base as base

class UserProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
        self.userPhoto = "com.compal.bioslab.pixsee.pixm01:id/civProfileImageUserProfileEditAct"
        self.userNameEditText = "com.compal.bioslab.pixsee.pixm01:id/tvNameUserProfileEditAct"
        self.backupEmailText = "com.compal.bioslab.pixsee.pixm01:id/etBackupEmail"

        self.doneButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_tvDone"
        self.returnButton = "com.compal.bioslab.pixsee.pixm01:id/user_profile_edit_toolbar_back_img"
        self.changePasswordButton = "com.compal.bioslab.pixsee.pixm01:id/tvForgotPasswordUserProfileEditAct"
        self.birthdayButton = "com.compal.bioslab.pixsee.pixm01:id/etBirthdayUserProfileEditAct"
        self.addBackupEmailButton = "com.compal.bioslab.pixsee.pixm01:id/btAddBackupEmail"
        self.changeBackupEmailButton = "com.compal.bioslab.pixsee.pixm01:id/etBackupEmail"
        self.deleteAccountButton = "com.compal.bioslab.pixsee.pixm01:id/btDeleteAccountProfileEditAct"

        '''Calendar'''
        self.calendar = "android:id/content"
        self.calendarScrollableList_classname = "android.widget.ListView"
        self.calendarYearPicker = "com.compal.bioslab.pixsee.pixm01:id/date_picker_year"
        self.calendarMonthPicker = "com.compal.bioslab.pixsee.pixm01:id/date_picker_month"
        self.calendarDayPicker = "com.compal.bioslab.pixsee.pixm01:id/date_picker_day"
        self.calendarOneMonth_xpath = "//android.widget.ListView/android.view.View"
        self.calendarOneDay_classname = "android.view.View"
        self.calendarDoneButton = "com.compal.bioslab.pixsee.pixm01:id/done_button"
        self.calendarCancelButton = "com.compal.bioslab.pixsee.pixm01:id/cancel_button"

        '''Delete Account Alert dialog'''
        self.deleteAccountDialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"
        self.deleteAccountDialogTitle = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
        self.deleteAccountDialogMessage = "com.compal.bioslab.pixsee.pixm01:id/tvMessageAlertDialog"
        self.deleteAccountDialogWarningMessage = "com.compal.bioslab.pixsee.pixm01:id/tvWarningMessage"
        self.deleteAccountDialogNoButton = "com.compal.bioslab.pixsee.pixm01:id/btnCustomAction"
        self.deleteAccountDialogYesButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
        self.deleteAccountDialogCancelButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"

        '''Add Backup Email dialog'''
        self.addBackupEmailDialog_xpath = "//android.view.ViewGroup/android.view.View/android.view.View/android.view.View"
        self.addBackupEmailDialogText_classname = "android.widget.TextView"
        self.addBackupEmailDialogButton_classname = "android.view.View"

        '''Photos (edit page & outside)'''
        self.photosCategory_xpath = "//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]"
        self.photos_classname = "android.widget.ImageView"
        self.editPhotoDoneButton = "com.compal.bioslab.pixsee.pixm01:id/tvImageEditorDone"
        self.editPhotoReturnButton = "com.compal.bioslab.pixsee.pixm01:id/image_editor_toolbar_back_img"

    def click_user_photo(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.userPhoto))
        )
        element = self.driver.find_element("id", self.userPhoto)
        element.click()

    def click_done(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.doneButton))
        )
        element = self.driver.find_element("id", self.doneButton)
        element.click()

    def click_return(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.returnButton))
        )
        element = self.driver.find_element("id", self.returnButton)
        element.click()

    def input_user_name(self, new_name = "Test_User 01"):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.userNameEditText))
        )
        element = self.driver.find_element("id", self.userNameEditText)
        if element.text == new_name:
            new_name = new_name + "(1)"
        element.clear()
        element.send_keys(new_name)

    def click_change_password(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.changePasswordButton))
        )
        element = self.driver.find_element("id", self.changePasswordButton)
        element.click()

    def click_birthday(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.birthdayButton))
        )
        element = self.driver.find_element("id", self.birthdayButton)
        element.click()

    def click_add_backup_email(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.addBackupEmailButton))
        )
        element = self.driver.find_element("id", self.addBackupEmailButton)
        element.click()

    def click_change_backup_email(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.changeBackupEmailButton))
        )
        element = self.driver.find_element("id", self.changeBackupEmailButton)
        element.click()

    def click_delete_account(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.deleteAccountButton))
        )
        element = self.driver.find_element("id", self.deleteAccountButton)
        element.click()

    def click_add_backup_email_dialog_ok(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("xpath", self.addBackupEmailDialog_xpath))
        )
        dialog = self.driver.find_element("xpath", self.addBackupEmailDialog_xpath)
        buttons = dialog.find_elements("class name", self.addBackupEmailDialogButton_classname)
        buttons[0].click()

    def click_add_backup_email_dialog_cancel(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("xpath", self.addBackupEmailDialog_xpath))
        )
        dialog = self.driver.find_element("xpath", self.addBackupEmailDialog_xpath)
        buttons = dialog.find_elements("class name", self.addBackupEmailDialogButton_classname)
        buttons[1].click()

    def click_photos_category(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("xpath", self.photosCategory_xpath))
        )
        element = self.driver.find_element("xpath", self.photosCategory_xpath)
        element.click()

    def click_selected_photo(self, number=0):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("class name", self.photos_classname))
        )
        elements = self.driver.find_elements("class name", self.photos_classname)
        elements[number].click()

    def click_edit_photo_done(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.editPhotoDoneButton))
        )
        element = self.driver.find_element("id", self.editPhotoDoneButton)
        element.click()

    def get_page_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def get_done_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.doneButton))
        )
        element = self.driver.find_element("id", self.doneButton)
        return element.text

    def get_user_name_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.userNameEditText))
        )
        element = self.driver.find_element("id", self.userNameEditText)
        return element.text

    def get_user_birthday_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.birthdayButton))
        )
        element = self.driver.find_element("id", self.birthdayButton)
        return element.text

    def get_change_password_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.changePasswordButton))
        )
        element = self.driver.find_element("id", self.changePasswordButton)
        return element.text

    def get_add_backup_email_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.addBackupEmailButton))
        )
        element = self.driver.find_element("id", self.addBackupEmailButton)
        return element.text

    def get_change_backup_email_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.changeBackupEmailButton))
        )
        element = self.driver.find_element("id", self.changeBackupEmailButton)
        return element.text

    def get_delete_account_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.deleteAccountButton))
        )
        element = self.driver.find_element("id", self.deleteAccountButton)
        return element.text

    def get_add_backup_email_dialog_title_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("xpath", self.addBackupEmailDialog_xpath))
        )
        dialog = self.driver.find_element("xpath", self.addBackupEmailDialog_xpath)
        elements = dialog.find_elements("class name", self.addBackupEmailDialogText_classname)
        return elements[0].text

    def get_add_backup_email_dialog_info_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("xpath", self.addBackupEmailDialog_xpath))
        )
        dialog = self.driver.find_element("xpath", self.addBackupEmailDialog_xpath)
        elements = dialog.find_elements("class name", self.addBackupEmailDialogText_classname)
        return elements[1].text

    def get_add_backup_email_dialog_ok_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("xpath", self.addBackupEmailDialog_xpath))
        )
        dialog = self.driver.find_element("xpath", self.addBackupEmailDialog_xpath)
        buttons = dialog.find_elements("class name", self.addBackupEmailDialogButton_classname)
        element = buttons[0].find_element("class name", self.addBackupEmailDialogText_classname)
        return element.text

    def get_add_backup_email_dialog_cancel_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("xpath", self.addBackupEmailDialog_xpath))
        )
        dialog = self.driver.find_element("xpath", self.addBackupEmailDialog_xpath)
        buttons = dialog.find_elements("class name", self.addBackupEmailDialogButton_classname)
        element = buttons[1].find_element("class name", self.addBackupEmailDialogText_classname)
        return element.text

    def select_avatar(self, number=0):
        self.click_user_photo()
        self.click_photos_category()
        self.click_selected_photo(number)
        time.sleep(1)
        self.click_edit_photo_done()

    def select_birthday(self, year = datetime.date.today().year, month = datetime.date.today().month, day = datetime.date.today().day):
        # Validate the input date
        try:
            target_date = datetime.date(year, month, day)
            if year < 1900 or target_date > datetime.date.today():
                raise ValueError("Year must be between 1900 and the current year, and the date must not be in the future.")
        except ValueError as e:
            raise ValueError(f"Invalid date: {e}")

        self.click_birthday()
        time.sleep(1)
        if not self.has_calendar():
            raise AssertionError("Can't find calendar for birthday selection")
        # Jump to the selected year
        year_picker = self.driver.find_element("id", self.calendarYearPicker)
        month_picker = self.driver.find_element("id", self.calendarMonthPicker)
        day_picker = self.driver.find_element("id", self.calendarDayPicker)
        if year != int(year_picker.text):
            year_picker.click()
            while True:
                try:
                    element = self.driver.find_element("accessibility id", f"{year}")
                    element.click()
                    break
                except:
                    if year < int(year_picker.text):
                        self.driver.find_element(
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            f'new UiScrollable(new UiSelector().className({self.calendarScrollableList_classname})).setAsVerticalList().scrollBackward()'
                        )
                    elif year > int(year_picker.text):
                        self.driver.find_element(
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            f'new UiScrollable(new UiSelector().className({self.calendarScrollableList_classname})).setAsVerticalList().scrollForward()'
                        )
                    time.sleep(0.2)
        # Find the date and click it. Need to swipe up if the date is not visible
        target_date_str = target_date.strftime("%d %B %Y")
        first_days = set()
        while True:
            try:
                if month == datetime.datetime.strptime(month_picker.text, "%b").month and day == int(day_picker.text):
                    element = self.driver.find_element("accessibility id", target_date_str + " selected")
                    element.click()
                else:
                    element = self.driver.find_element("accessibility id", target_date_str)
                    element.click()
                element = self.driver.find_element("id", self.calendarDoneButton)
                element.click()
                return
            except:
                calendar_current_month = self.driver.find_element("xpath", self.calendarOneMonth_xpath)
                element = calendar_current_month.find_element("class name", self.calendarOneDay_classname)
                first_date_str = element.get_attribute("content-desc").split("selected")[0].strip()
                first_date = datetime.datetime.strptime(first_date_str, "%d %B %Y").date()
                if first_date_str in first_days:
                    raise ValueError(f"{year}-{month}-{day} is not found in the calendar. Please check the date and try again.")
                first_days.add(first_date_str)
                if month < first_date.month:
                    self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().className({self.calendarScrollableList_classname})).setAsVerticalList().scrollBackward()'
                    )
                elif month > first_date.month:
                    self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().className({self.calendarScrollableList_classname})).setAsVerticalList().scrollForward()'
                    )
                elif day > first_date.day:
                    window = self.driver.get_window_size()
                    x = window["width"] // 2.5
                    start_y = int(window["height"] * 0.6)
                    end_y = int(window["height"] * 0.5)
                    self.driver.swipe(x, start_y, x, end_y, 3000)
                elif day < first_date.day:
                    window = self.driver.get_window_size()
                    x = window["width"] // 2.5
                    start_y = int(window["height"] * 0.5)
                    end_y = int(window["height"] * 0.6)
                    self.driver.swipe(x, start_y, x, end_y, 3000)
                time.sleep(0.2)

    def has_backup_email(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.backupEmailText))
            )
            self.driver.find_element("id", self.backupEmailText)
            return True
        except:
            return False

    def has_calendar(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.calendar))
            )
            self.driver.find_element("id", self.calendar)
            return True
        except:
            return False

    def has_delete_account_dialog(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.deleteAccountDialog))
            )
            self.driver.find_element("id", self.deleteAccountDialog)
            return True
        except:
            return False

    def has_add_backup_email_dialog(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("xpath", self.addBackupEmailDialog_xpath))
            )
            self.driver.find_element("xpath", self.addBackupEmailDialog_xpath)
            return True
        except:
            return False

    def is_in_user_profile_page(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.userPhoto))
            )
            self.driver.find_element("id", self.userPhoto)
            return True
        except:
            return False


