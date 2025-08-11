from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages.base as base

class ChangePasswordPage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/tvChangePasswordTitle"
        self.currentPasswordEditText = "com.compal.bioslab.pixsee.pixm01:id/sietCurrentPasswordField"
        self.currentPasswordErrorText = "com.compal.bioslab.pixsee.pixm01:id/tvCurrentPasswordFieldError"
        self.newPasswordEditText = "com.compal.bioslab.pixsee.pixm01:id/sietNewPasswordField"
        self.newPasswordErrorText = "com.compal.bioslab.pixsee.pixm01:id/tvNewPasswordFieldError"
        self.confirmPasswordEditText = "com.compal.bioslab.pixsee.pixm01:id/sietConfirmNewPasswordField"
        self.confirmPasswordErrorText = "com.compal.bioslab.pixsee.pixm01:id/tvConfirmNewPasswordFieldError"
        self.wrongBarText = "com.compal.bioslab.pixsee.pixm01:id/tvSnackbarLabel"

        self.doneButton = "com.compal.bioslab.pixsee.pixm01:id/btConfirmChangePassword"
        self.cancelButton = "com.compal.bioslab.pixsee.pixm01:id/btCancel"

    def click_done(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.doneButton))
        )
        element = self.driver.find_element("id", self.doneButton)
        element.click()

    def click_cancel(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.cancelButton))
        )
        element = self.driver.find_element("id", self.cancelButton)
        element.click()

    def input_current_password(self, password):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.currentPasswordEditText))
        )
        element = self.driver.find_element("id", self.currentPasswordEditText)
        element.clear()
        element.send_keys(password)

    def input_new_password(self, password):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.newPasswordEditText))
        )
        element = self.driver.find_element("id", self.newPasswordEditText)
        element.clear()
        element.send_keys(password)

    def input_confirm_password(self, password):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.confirmPasswordEditText))
        )
        element = self.driver.find_element("id", self.confirmPasswordEditText)
        element.clear()
        element.send_keys(password)

    def get_page_title(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.pageTitleText))
        )
        element = self.driver.find_element("id", self.pageTitleText)
        return element.text

    def get_current_password_hint(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.currentPasswordEditText))
        )
        element = self.driver.find_element("id", self.currentPasswordEditText)
        return element.get_attribute("hint")

    def get_current_password_error(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.currentPasswordErrorText))
        )
        element = self.driver.find_element("id", self.currentPasswordErrorText)
        return element.text

    def get_new_password_hint(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.newPasswordEditText))
        )
        element = self.driver.find_element("id", self.newPasswordEditText)
        return element.get_attribute("hint")

    def get_new_password_error(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.newPasswordErrorText))
        )
        element = self.driver.find_element("id", self.newPasswordErrorText)
        return element.text

    def get_confirm_password_hint(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.confirmPasswordEditText))
        )
        element = self.driver.find_element("id", self.confirmPasswordEditText)
        return element.get_attribute("hint")

    def get_confirm_password_error(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.confirmPasswordErrorText))
        )
        element = self.driver.find_element("id", self.confirmPasswordErrorText)
        return element.text

    def get_done_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.doneButton))
        )
        element = self.driver.find_element("id", self.doneButton)
        return element.text

    def get_cancel_button_text(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.cancelButton))
        )
        element = self.driver.find_element("id", self.cancelButton)
        return element.text

    def is_in_change_password_page(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.pageTitleText))
            )
            self.driver.find_element("id", self.pageTitleText)
            return True
        except:
            return False