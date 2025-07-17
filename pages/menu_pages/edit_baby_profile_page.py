from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class EditBabyProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
        self.babyNameEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_name_edx"
        self.returnButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
        self.doneButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_done_tv"
        self.babyPicture = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_picture_img"
        self.genderBoyButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_gender_boy_radio"
        self.genderGirlButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_gender_girl_radio"
        self.birthdayEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_birthday_edx"
        self.nationButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_nation_spn"
        self.relativeButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_relative_spn"
        self.deleteBabyProfileButton = "com.compal.bioslab.pixsee.pixm01:id/deleteBabyProfileEditAct"

        '''Delete alert dialog'''
        self.deleteDialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"
        self.deleteDialogTitle = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
        self.deleteDialogMessage = "com.compal.bioslab.pixsee.pixm01:id/tvMessageAlertDialog"
        self.deleteDialogWarningMessage = "com.compal.bioslab.pixsee.pixm01:id/tvWarningMessage"
        self.deleteDialogNoButton = "com.compal.bioslab.pixsee.pixm01:id/btnCustomAction"
        self.deleteDialogYesButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
        self.deleteDialogCancelButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"

    def click_return(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.returnButton))
        )
        element = self.driver.find_element("id", self.returnButton)
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

    def click_delete_baby_profile(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteBabyProfileButton))
        )
        element = self.driver.find_element("id", self.deleteBabyProfileButton)
        element.click()

    def click_delete_dialog_no(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteDialogNoButton))
        )
        element = self.driver.find_element("id", self.deleteDialogNoButton)
        element.click()

    def click_delete_dialog_yes(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteDialogYesButton))
        )
        element = self.driver.find_element("id", self.deleteDialogYesButton)
        element.click()

    def click_delete_dialog_cancel(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteDialogCancelButton))
        )
        element = self.driver.find_element("id", self.deleteDialogCancelButton)
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

    def get_delete_baby_profile_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteBabyProfileButton))
        )
        element = self.driver.find_element("id", self.deleteBabyProfileButton)
        return element.text

    def get_delete_dialog_title(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteDialogTitle))
        )
        element = self.driver.find_element("id", self.deleteDialogTitle)
        return element.text

    def get_delete_dialog_message(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteDialogMessage))
        )
        element = self.driver.find_element("id", self.deleteDialogMessage)
        return element.text

    def get_delete_dialog_warning_message(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteDialogWarningMessage))
        )
        element = self.driver.find_element("id", self.deleteDialogWarningMessage)
        return element.text.removeprefix("ICON_WARNING").strip() # Warning message has an icon prefix needs to remove it

    def get_delete_dialog_no_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteDialogNoButton))
        )
        element = self.driver.find_element("id", self.deleteDialogNoButton)
        return element.text

    def get_delete_dialog_yes_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteDialogYesButton))
        )
        element = self.driver.find_element("id", self.deleteDialogYesButton)
        return element.text

    def get_delete_dialog_cancel_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteDialogCancelButton))
        )
        element = self.driver.find_element("id", self.deleteDialogCancelButton)
        return element.text

    def is_in_edit_baby_profile_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.babyPicture))
            )
            self.driver.find_element("id", self.babyPicture)
            return True
        except:
            return False

    def has_delete_dialog(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.deleteDialog))
            )
            self.driver.find_element("id", self.deleteDialog)
            return True
        except:
            return False
