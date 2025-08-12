from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SendErrorPage():
    def __init__(self, driver):
        self.driver = driver
        self.Title = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
        self.Text = "com.compal.bioslab.pixsee.pixm01:id/tvMessageAlertDialog"
        self.SendButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
        self.CancelButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"

    def click_send(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.SendButton))
        )
        element = self.driver.find_element("id", self.SendButton)
        element.click()
    def click_cancel(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.CancelButton))
        )
        element = self.driver.find_element("id", self.CancelButton)
        element.click()

    def title_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Title))
        )
        element = self.driver.find_element("id", self.Title)
        return element.text
    def text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Text))
        )
        element = self.driver.find_element("id", self.Text)
        return element.text
    def send_button_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.SendButton))
        )
        element = self.driver.find_element("id", self.SendButton)
        return element.text
    def cancel_button_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.CancelButton))
        )
        element = self.driver.find_element("id", self.CancelButton)
        return element.text

    def is_in_send_error_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Title))
            )
            return True
        except Exception as e:
            print(f"Send Error Dialog not found: {e}")
            return False