from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
        self.saveStatusButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_tvDone"
        self.returnButton = "com.compal.bioslab.pixsee.pixm01:id/user_profile_edit_toolbar_back_img"
        self.userPhoto = "com.compal.bioslab.pixsee.pixm01:id/civProfileImageUserProfileEditAct"
        self.userNameEditText = "com.compal.bioslab.pixsee.pixm01:id/tvNameUserProfileEditAct"
        self.changePasswordButton = "com.compal.bioslab.pixsee.pixm01:id/tvForgotPasswordUserProfileEditAct"
        self.birthdayEditText = "com.compal.bioslab.pixsee.pixm01:id/etBirthdayUserProfileEditAct"
        self.addBackupEmailButton = "com.compal.bioslab.pixsee.pixm01:id/btAddBackupEmail"
        self.changeBackupEmailButton = "com.compal.bioslab.pixsee.pixm01:id/etBackupEmail"
        self.deleteAccountButton = "com.compal.bioslab.pixsee.pixm01:id/btDeleteAccountProfileEditAct"

        self.calendar_xpath = "/hierarchy/android.widget.FrameLayout"

    def click_user_photo(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.userPhoto))
        )
        element = self.driver.find_element("id", self.userPhoto)
        element.click()


    def click_save_status(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.saveStatusButton))
        )
        element = self.driver.find_element("id", self.saveStatusButton)
        element.click()

    def click_return(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.returnButton))
        )
        element = self.driver.find_element("id", self.returnButton)
        element.click()

    def click_change_password(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.changePasswordButton))
        )
        element = self.driver.find_element("id", self.changePasswordButton)
        element.click()

    def click_birthday_edit(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.birthdayEditText))
        )
        element = self.driver.find_element("id", self.birthdayEditText)
        element.click()

    def click_add_backup_email(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.addBackupEmailButton))
        )
        element = self.driver.find_element("id", self.addBackupEmailButton)
        element.click()

    def click_change_backup_email(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.changeBackupEmailButton))
        )
        element = self.driver.find_element("id", self.changeBackupEmailButton)
        element.click()

    def click_delete_account(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteAccountButton))
        )
        element = self.driver.find_element("id", self.deleteAccountButton)
        element.click()

    def input_user_name(self, new_name):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.userNameEditText))
        )
        element = self.driver.find_element("id", self.userNameEditText)
        element.clear()
        element.send_keys(new_name)

    def get_page_title(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def is_in_user_profile_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.userPhoto))
            )
            self.driver.find_element("id", self.userPhoto)
            return True
        except:
            return False


