from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class EditBabyProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"

        self.babyPicture = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_picture_img"
        self.babyNameEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_name_edx"
        self.birthdayEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_birthday_edx"

        self.returnButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
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

    def click_baby_profile(self):
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
        element = self.driver.find_element("id", self.nationButton)
        return element.text

    def get_relative_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.relativeButton))
        )
        element = self.driver.find_element("id", self.relativeButton)
        return element.text

    def get_baby_profile_button_text(self):
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
