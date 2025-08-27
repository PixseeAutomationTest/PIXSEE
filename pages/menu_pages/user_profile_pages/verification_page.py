from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base as base


class VerificationPage():
		def __init__(self, driver):
			self.driver = driver

			self.activity_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View"
			self.text_classname = "android.widget.TextView"
			self.verificationCodeEdit_classname = "android.widget.EditText"
			self.confirmButton_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]"
			self.cancelButton_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]"

			'''Resend code dialog'''
			self.dialog_xpath = "//android.view.ViewGroup/android.view.View/android.view.View/android.view.View"
			self.dialgoOkButton_xpath = "//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View"

		def input_verification_code(self, verification_code):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.verificationCodeEdit_classname))
			)
			element = self.driver.find_element("class name", self.verificationCodeEdit_classname)
			element.send_keys(verification_code)

		def click_resend_code_button(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.text_classname))
			)
			elements = self.driver.find_elements("class name", self.text_classname)
			if self.has_error_message():
				elements[-4].click()
			elements[-3].click()

		def click_confirm(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.confirmButton_xpath))
			)
			element = self.driver.find_element("xpath", self.confirmButton_xpath)
			element.click()


		def click_cancel(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.cancelButton_xpath))
			)
			element = self.driver.find_element("xpath", self.cancelButton_xpath)
			element.click()

		def get_title_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.text_classname))
			)
			elements = self.driver.find_elements("class name", self.text_classname)
			return elements[0].text # The first element is the title text

		def get_info1_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.text_classname))
			)
			elements = self.driver.find_elements("class name", self.text_classname)
			return elements[1].text # The second element is the info1 text

		def get_email_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.text_classname))
			)
			elements = self.driver.find_elements("class name", self.text_classname)
			return elements[2].text # The third element is the email text

		def get_info2_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.text_classname))
			)
			elements = self.driver.find_elements("class name", self.text_classname)
			return elements[3].text # The fourth element is the info2 text

		def get_code_input(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.verificationCodeEdit_classname))
			)
			element = self.driver.find_element("class name", self.verificationCodeEdit_classname)
			return element.text

		def get_resend_code_button_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.text_classname))
			)
			elements = self.driver.find_elements("class name", self.text_classname)
			if self.has_error_message():
				return elements[-4].text
			return elements[-3].text

		def get_confirm_button_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.confirmButton_xpath))
			)
			next_button = self.driver.find_element("xpath", self.confirmButton_xpath)
			element = next_button.find_element("class name", self.text_classname)
			return element.text

		def get_cancel_button_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.cancelButton_xpath))
			)
			next_button = self.driver.find_element("xpath", self.cancelButton_xpath)
			element = next_button.find_element("class name", self.text_classname)
			return element.text

		def get_error_message_text(self):
			if not self.has_error_message():
				return None
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.text_classname))
			)
			elements = self.driver.find_elements("class name", self.text_classname)
			return elements[-3].text

		def has_error_message(self):
			if self.get_number_of_all_texts() - len(self.get_code_input()) <= 7:
				return False
			return True

		def get_number_of_all_texts(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.activity_xpath))
			)
			elements = self.driver.find_elements("class name", self.text_classname)
			return len(elements)

		def click_resend_code_dialog_ok_button(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.dialgoOkButton_xpath))
			)
			element = self.driver.find_element("xpath", self.dialgoOkButton_xpath)
			element.click()

		def get_resend_code_dialog_info_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.dialog_xpath))
			)
			dialog = self.driver.find_element("xpath", self.dialog_xpath)
			elements = dialog.find_elements("class name", self.text_classname)
			return elements[0].text

		def get_resend_code_dialog_ok_button_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.dialgoOkButton_xpath))
			)
			ok_button = self.driver.find_element("xpath", self.dialgoOkButton_xpath)
			element = ok_button.find_element("class name", self.text_classname)
			return element.text
