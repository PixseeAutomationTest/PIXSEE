from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.user_photo = "com.compal.bioslab.pixsee.pixm01:id/civProfileImageUserProfileEditAct"
        self.user_name_edit_text = "com.compal.bioslab.pixsee.pixm01:id/tvNameUserProfileEditAct"
        self.save_status_button = "com.compal.bioslab.pixsee.pixm01:id/toolbar_tvDone"
        self.return_button = "com.compal.bioslab.pixsee.pixm01:id/user_profile_edit_toolbar_back_img"
        self.page_title_text = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
        self.birthday_edit_text = "com.compal.bioslab.pixsee.pixm01:id/etBirthdayUserProfileEditAct"

        self.calendar_xpath = "/hierarchy/android.widget.FrameLayout"

    def click_user_photo(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.user_photo))
        )
        element = self.driver.find_element("id", self.user_photo)
        element.click()

    def click_save_status(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.save_status_button))
        )
        element = self.driver.find_element("id", self.save_status_button)
        element.click()

    def input_user_name(self, user_name):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.user_name_edit_text))
        )
        element = self.driver.find_element("id", self.user_name_edit_text)
        element.clear()
        element.send_keys(user_name)

    def click_return(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.return_button))
        )
        element = self.driver.find_element("id", self.return_button)
        element.click()

    def click_birthday_edit(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.birthday_edit_text))
        )
        element = self.driver.find_element("id", self.birthday_edit_text)
        element.click()

    def change_birthday(self):
        self.click_birthday_edit()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("xpath", self.calendar_xpath))
        )

    def is_in_user_profile_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.page_title_text))
            )
            self.driver.find_element("id", self.page_title_text)
            return True
        except:
            return False


