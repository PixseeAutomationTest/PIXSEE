from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import datetime
import time

class EditBabyProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"

        self.babyPicture = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_picture_img"
        self.babyNameEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_name_edx"
        self.birthdayEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_birthday_edx"

        self.cancelButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
        self.genderBoyButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_gender_boy_radio"
        self.genderGirlButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_gender_girl_radio"
        self.nationButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_nation_spn"
        self.relativeButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_relative_spn"
        self.doneButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_done_tv"
        self.deleteBabyProfileButton = "com.compal.bioslab.pixsee.pixm01:id/deleteBabyProfileEditAct"


        '''Alert dialog (Delete baby profile or Change baby's birthday too much)'''
        self.dialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"
        self.dialogTitle = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
        self.dialogMessage = "com.compal.bioslab.pixsee.pixm01:id/tvMessageAlertDialog"
        self.dialogWarningMessage = "com.compal.bioslab.pixsee.pixm01:id/tvWarningMessage" # Only for "delete baby profile" dialog
        self.dialogNoButton = "com.compal.bioslab.pixsee.pixm01:id/btnCustomAction" # Only for "delete baby profile" dialog
        self.dialogYesButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
        self.dialogCancelButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"

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

        '''Nation and Relative list'''
        self.list_classname = "android.widget.ListView"
        self.listOption = "android:id/text1"

    def click_cancel(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelButton))
        )
        element = self.driver.find_element("id", self.cancelButton)
        element.click()

    def click_done(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.doneButton))
        )
        element = self.driver.find_element("id", self.doneButton)
        element.click()
        time.sleep(1)

    def click_baby_picture(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.babyPicture))
        )
        element = self.driver.find_element("id", self.babyPicture)
        element.click()

    def click_gender_boy(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.genderBoyButton))
        )
        element = self.driver.find_element("id", self.genderBoyButton)
        element.click()

    def click_gender_girl(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.genderGirlButton))
        )
        element = self.driver.find_element("id", self.genderGirlButton)
        element.click()

    def edit_baby_name(self, new_name):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.babyNameEditText))
        )
        element = self.driver.find_element("id", self.babyNameEditText)
        element.clear()
        element.send_keys(new_name)

    def click_baby_birthday(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.birthdayEditText))
        )
        element = self.driver.find_element("id", self.birthdayEditText)
        element.click()

    def click_nation(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.nationButton))
        )
        element = self.driver.find_element("id", self.nationButton)
        element.click()

    def click_relative(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.relativeButton))
        )
        element = self.driver.find_element("id", self.relativeButton)
        element.click()

    def click_delete_baby_profile(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteBabyProfileButton))
        )
        element = self.driver.find_element("id", self.deleteBabyProfileButton)
        element.click()

    def click_dialog_no(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogNoButton))
        )
        element = self.driver.find_element("id", self.dialogNoButton)
        element.click()

    def click_dialog_yes(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogYesButton))
        )
        element = self.driver.find_element("id", self.dialogYesButton)
        element.click()

    def click_dialog_cancel(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogCancelButton))
        )
        element = self.driver.find_element("id", self.dialogCancelButton)
        element.click()

    def get_page_title(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def get_done_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.doneButton))
        )
        element = self.driver.find_element("id", self.doneButton)
        return element.text

    def get_gender_boy_status(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.genderBoyButton))
        )
        element = self.driver.find_element("id", self.genderBoyButton)
        return element.get_attribute("checked") == "true"

    def get_gender_girl_status(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.genderGirlButton))
        )
        element = self.driver.find_element("id", self.genderGirlButton)
        return element.get_attribute("checked") == "true"

    def get_baby_name_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.babyNameEditText))
        )
        element = self.driver.find_element("id", self.babyNameEditText)
        return element.text

    def get_baby_birthday_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.birthdayEditText))
        )
        element = self.driver.find_element("id", self.birthdayEditText)
        return element.text

    def get_nation_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.nationButton))
        )
        parent_element = self.driver.find_element("id", self.nationButton)
        element = parent_element.find_element("id", self.listOption)
        return element.text

    def get_relative_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.relativeButton))
        )
        parent_element = self.driver.find_element("id", self.relativeButton)
        element = parent_element.find_element("id", self.listOption)
        return element.text

    def get_delete_baby_profile_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteBabyProfileButton))
        )
        element = self.driver.find_element("id", self.deleteBabyProfileButton)
        return element.text

    def get_dialog_title(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogTitle))
        )
        element = self.driver.find_element("id", self.dialogTitle)
        return element.text

    def get_dialog_message(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogMessage))
        )
        element = self.driver.find_element("id", self.dialogMessage)
        return element.text

    def get_dialog_warning_message(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogWarningMessage))
        )
        element = self.driver.find_element("id", self.dialogWarningMessage)
        return element.text.removeprefix("ICON_WARNING").strip() # Warning message has an icon prefix needs to remove it

    def get_dialog_no_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogNoButton))
        )
        element = self.driver.find_element("id", self.dialogNoButton)
        return element.text

    def get_dialog_yes_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogYesButton))
        )
        element = self.driver.find_element("id", self.dialogYesButton)
        return element.text

    def get_dialog_cancel_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogCancelButton))
        )
        element = self.driver.find_element("id", self.dialogCancelButton)
        return element.text

    def select_baby_birthday(self, year = datetime.date.today().year, month = datetime.date.today().month, day = datetime.date.today().day):
        # Validate the input date
        try:
            target_date = datetime.date(year, month, day)
            if year < 1900 or target_date > datetime.date.today():
                raise ValueError("Year must be between 1900 and the current year, and the date must not be in the future.")
        except ValueError as e:
            raise ValueError(f"Invalid date: {e}")

        self.click_baby_birthday()
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

    def select_nation(self, number = 51): # Default: Taiwan = 51
        self.click_nation()
        time.sleep(1)
        if not self.has_selection_list():
            raise AssertionError("Can't find selection list for nation")
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
                raise IndexError("IndexError: Nation index out of range")
            last_count = len(all_items)

            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().className("{self.list_classname}")).setAsVerticalList().scrollForward();'
            )
            time.sleep(1)

    def select_relative(self, number = 2): # Default: Mommy = 2
        self.click_relative()
        time.sleep(1)
        if not self.has_selection_list():
            raise AssertionError("Can't find selection list for relative")
        elements = self.driver.find_elements("id", self.listOption)
        if number < len(elements):
            elements[number].click()
        else:
            raise IndexError("IndexError: Relative index out of range")

    def has_calendar(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.calendar))
            )
            self.driver.find_element("id", self.calendar)
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

    def has_dialog(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.dialog))
            )
            self.driver.find_element("id", self.dialog)
            return True
        except:
            return False

    def is_in_edit_baby_profile_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.babyPicture))
            )
            self.driver.find_element("id", self.babyPicture)
            return True
        except:
            return False
