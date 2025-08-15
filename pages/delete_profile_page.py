from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeleteProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/delete_account_baby_tv_title"
        self.warningText = "com.compal.bioslab.pixsee.pixm01:id/delete_account_baby_tv_warning"
        self.checkInfoText = "com.compal.bioslab.pixsee.pixm01:id/delete_account_baby_tv_check_info"

        self.checkButton = "com.compal.bioslab.pixsee.pixm01:id/delete_account_baby_check"
        self.deleteProfileButton = "com.compal.bioslab.pixsee.pixm01:id/delete_account_baby_bt_delete"
        self.cancelButton = "com.compal.bioslab.pixsee.pixm01:id/delete_account_baby_bt_cancel"

    def click_check(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.checkButton))
        )
        element = self.driver.find_element("id", self.checkButton)
        element.click()

    def click_delete_profile(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteProfileButton))
        )
        element = self.driver.find_element("id", self.deleteProfileButton)
        element.click()

    def click_cancel(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelButton))
        )
        element = self.driver.find_element("id", self.cancelButton)
        element.click()

    def get_page_title(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def get_warning_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.warningText))
        )
        element = self.driver.find_element("id", self.warningText)
        return element.text

    def get_check_info_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.checkInfoText))
        )
        element = self.driver.find_element("id", self.checkInfoText)
        return element.text

    def get_delete_profile_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.deleteProfileButton))
        )
        element = self.driver.find_element("id", self.deleteProfileButton)
        return element.text

    def get_cancel_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelButton))
        )
        element = self.driver.find_element("id", self.cancelButton)
        return element.text

    def is_in_delete_profile_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.pageTitleText))
            )
            self.driver.find_element(By.ID, self.pageTitleText)
            return True
        except:
            return False