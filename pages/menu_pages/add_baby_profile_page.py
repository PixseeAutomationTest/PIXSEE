from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time
import random

class AddBabyProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
        self.messageText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_message_label"

        self.babyPhoto = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_picture_img"
        self.nameEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_name_edx"
        self.birthdayEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_birthday_edx"

        self.cancelButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
        self.babyGenderBoyButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_gender_boy_radio"
        self.babyGenderGirlButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_gender_girl_radio"
        self.nationButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_nation_spn"
        self.relativeButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_relative_spn"
        self.finishButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_finish_btn"

        '''Discard dialog'''
        self.cancelMessage = "com.compal.bioslab.pixsee.pixm01:id/tvTitleDialog"
        self.cancelYesButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveDialog"
        self.cancelNoButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeDialog"

        '''Calendar'''
        self.calendar = "android:id/content"
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

    def click_baby_photo(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.babyPhoto))
        )
        element = self.driver.find_element("id", self.babyPhoto)
        element.click()

    def click_gender_boy(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.babyGenderBoyButton))
        )
        element = self.driver.find_element("id", self.babyGenderBoyButton)
        element.click()

    def click_gender_girl(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.babyGenderGirlButton))
        )
        element = self.driver.find_element("id", self.babyGenderGirlButton)
        element.click()

    def input_name(self, name):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.nameEditText))
        )
        element = self.driver.find_element("id", self.nameEditText)
        element.clear()
        element.send_keys(name)

    def click_birthday(self):
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

    def click_finish(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.finishButton))
        )
        element = self.driver.find_element("id", self.finishButton)
        element.click()

    def click_cancel_yes(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelYesButton))
        )
        element = self.driver.find_element("id", self.cancelYesButton)
        element.click()

    def click_cancel_no(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelNoButton))
        )
        element = self.driver.find_element("id", self.cancelNoButton)
        element.click()

    def click_calendar_done(self):
        if self.has_calendar():
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.calendarDoneButton))
            )
            element = self.driver.find_element("id", self.calendarDoneButton)
            element.click()

    def click_calendar_cancel(self):
        if self.has_calendar():
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.calendarCancelButton))
            )
            element = self.driver.find_element("id", self.calendarCancelButton)
            element.click()


    def get_page_title(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def get_gender_boy_status(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.babyGenderBoyButton))
        )
        element = self.driver.find_element("id", self.babyGenderBoyButton)
        return element.get_attribute("checked") == "true"

    def get_gender_girl_status(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.babyGenderGirlButton))
        )
        element = self.driver.find_element("id", self.babyGenderGirlButton)
        return element.get_attribute("checked") == "true"

    def get_name_hint(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.nameEditText))
        )
        element = self.driver.find_element("id", self.nameEditText)
        return element.get_attribute("hint")

    def get_name_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.nameEditText))
        )
        element = self.driver.find_element("id", self.nameEditText)
        return element.text

    def get_birthday_hint(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.birthdayEditText))
        )
        element = self.driver.find_element("id", self.birthdayEditText)
        return element.get_attribute("hint")

    def get_birthday_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.birthdayEditText))
        )
        element = self.driver.find_element("id", self.birthdayEditText)
        return element.text

    def get_nation_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.nationButton))
        )
        parent_element = self.driver.find_elements("id", self.nationButton)
        element = parent_element.find_element("id", self.listOption)
        return element.text

    def get_relative_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.relativeButton))
        )
        parent_element = self.driver.find_elements("id", self.relativeButton)
        element = parent_element.find_element("id", self.listOption)
        return element.text

    def get_finish_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.finishButton))
        )
        element = self.driver.find_element("id", self.finishButton)
        return element.text

    def get_message_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.messageText))
        )
        element = self.driver.find_element("id", self.messageText)
        return element.text

    def get_cancel_message(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelMessage))
        )
        element = self.driver.find_element("id", self.cancelMessage)
        return element.text

    def get_cancel_yes_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelYesButton))
        )
        element = self.driver.find_element("id", self.cancelYesButton)
        return element.text

    def get_cancel_no_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelNoButton))
        )
        element = self.driver.find_element("id", self.cancelNoButton)
        return element.text

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

    def is_in_add_baby_profile_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.babyPhoto))
            )
            self.driver.find_element("id", self.babyPhoto)
            return True
        except:
            return False

    def add_new_baby(self, baby_name = "Test_Baby 01"):
        self.input_name(baby_name)
        self.click_birthday()
        self.click_calendar_done()
        time.sleep(3)
        self.select_nation(random.randint(1, 58))
        self.select_relative(random.randint(1, 10))
        self.click_finish()