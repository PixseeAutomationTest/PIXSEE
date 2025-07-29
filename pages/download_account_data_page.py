from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DownloadAccountDataPage():
    def __init__(self, driver):
        self.driver = driver

        self.titleText = "com.compal.bioslab.pixsee.pixm01:id/tvTitle" # for page and dialog
        self.infoText = "com.compal.bioslab.pixsee.pixm01:id/tvInfo"
        self.mailEditText = "com.compal.bioslab.pixsee.pixm01:id/etMail"
        self.confirmMailEditText = "com.compal.bioslab.pixsee.pixm01:id/etConfirmMail"

        self.closeButton = "com.compal.bioslab.pixsee.pixm01:id/ibClose"
        self.submitButton = "com.compal.bioslab.pixsee.pixm01:id/btSubmit"
        self.cancelButton = "com.compal.bioslab.pixsee.pixm01:id/btCancel" # for page and dialog

        ''' Select download dialog'''
        self.dialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"

        self.allDataText = "com.compal.bioslab.pixsee.pixm01:id/tvAllData"
        self.babyNameText = "com.compal.bioslab.pixsee.pixm01:id/tvBabyName"

        self.allDataButton = "com.compal.bioslab.pixsee.pixm01:id/viewCbAllData"
        self.selectBabyButton = "com.compal.bioslab.pixsee.pixm01:id/ckBaby"
        self.dialogOkButton = "com.compal.bioslab.pixsee.pixm01:id/btnOK"
        self.dialogCancelButton = "com.compal.bioslab.pixsee.pixm01:id/btnCancel"

    def click_close(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.closeButton))
        )
        element = self.driver.find_element("id", self.closeButton)
        element.click()

    def click_submit(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.submitButton))
        )
        element = self.driver.find_element("id", self.submitButton)
        element.click()

    def click_cancel(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelButton))
        )
        element = self.driver.find_element("id", self.cancelButton)
        element.click()

    def click_all_data(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.allDataButton))
        )
        element = self.driver.find_element("id", self.allDataButton)
        element.click()

    def click_select_baby(self, number = 0):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.selectBabyButton))
        )
        elements = self.driver.find_elements("id", self.selectBabyButton)
        if number < len(elements) and number >= 0:
            elements[number].click()
        else:
            raise IndexError("Baby index out of range")

    def click_dialog_ok(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogOkButton))
        )
        element = self.driver.find_element("id", self.dialogOkButton)
        element.click()

    def click_dialog_cancel(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogCancelButton))
        )
        element = self.driver.find_element("id", self.dialogCancelButton)
        element.click()

    def get_title_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.titleText))
        )
        element = self.driver.find_element("id", self.titleText)
        return element.text

    def get_info_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.infoText))
        )
        element = self.driver.find_element("id", self.infoText)
        return element.text

    def get_mail_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.mailEditText))
        )
        element = self.driver.find_element("id", self.mailEditText)
        return element.text

    def get_confirm_mail_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.confirmMailEditText))
        )
        element = self.driver.find_element("id", self.confirmMailEditText)
        return element.text

    def get_submit_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.submitButton))
        )
        element = self.driver.find_element("id", self.submitButton)
        return element.text

    def get_cancel_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.cancelButton))
        )
        element = self.driver.find_element("id", self.cancelButton)
        return element.text

    def get_all_data_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.allDataText))
        )
        element = self.driver.find_element("id", self.allDataText)
        return element.text

    def get_baby_name_text(self, number = 0):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.babyNameText))
        )
        elements = self.driver.find_elements("id", self.babyNameText)
        if number < len(elements) and number >= 0:
            return elements[number].text
        else:
            raise IndexError("Baby index out of range")

    def get_dialog_ok_button_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(("id", self.dialogOkButton))
        )
        element = self.driver.find_element("id", self.dialogOkButton)
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
        except Exception:
            return False

    def is_in_download_account_data_page(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(("id", self.infoText))
            )
            self.driver.find_element("id", self.infoText)
            return True
        except Exception:
            return False
