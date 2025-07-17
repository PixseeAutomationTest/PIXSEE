from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AddBabyProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
        self.cancelButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
        self.babyPhoto = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_picture_img"
        self.babyGenderBoyButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_gender_boy_radio"
        self.babyGenderGirlButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_gender_girl_radio"
        self.nameEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_name_edx"
        self.birthdayEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_birthday_edx"
        self.nationButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_nation_spn"
        self.relativeButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_relative_spn"
        self.nationOrRelativeText = "android:id/text1"
        self.finishButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_finish_btn"
        self.messageText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_message_label"

        '''Discard dialog'''
        self.cancelMessage = "com.compal.bioslab.pixsee.pixm01:id/tvTitleDialog"
        self.cancelYesButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveDialog"
        self.cancelNoButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeDialog"

        '''Calendar'''
        self.calendar = "android:id/content"
        self.calendarDoneButton = "com.compal.bioslab.pixsee.pixm01:id/done_button"
        self.calendarCancelButton = "com.compal.bioslab.pixsee.pixm01:id/cancel_button"

        '''Nation and Relative Spinner'''
        self.list_class_name = "android.widget.ListView"
        self.decisionText = "android:id/text1"

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

    def get_birthday_hint(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.birthdayEditText))
        )
        element = self.driver.find_element("id", self.birthdayEditText)
        return element.get_attribute("hint")

    def get_nation_selected_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.nationOrRelativeText))
        )
        elements = self.driver.find_elements("id", self.nationOrRelativeText)
        return elements[0].text

    def get_relative_selected_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.nationOrRelativeText))
        )
        elements = self.driver.find_elements("id", self.nationOrRelativeText)
        return elements[1].text

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

    def get_list_text(self, number = -1):
        if self.has_list():
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.decisionText))
            )
            elements = self.driver.find_elements("id", self.decisionText)
            return elements[number].text
        else:
            return None

    def is_in_add_baby_profile_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.babyPhoto))
            )
            self.driver.find_element("id", self.babyPhoto)
            return True
        except:
            return False

    def has_calendar(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.calendar))
            )
            self.driver.find_element("id", self.calendar)
            return True
        except:
            return False

    def has_list(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("class name", self.list_class_name))
            )
            self.driver.find_element("class name", self.list_class_name)
            return True
        except:
            return False

    def add_new_baby(self, baby_name = "Test Baby01"):
        self.input_name(baby_name)
        self.click_birthday()
        self.click_calendar_done()
        time.sleep(3)
        self.click_finish()