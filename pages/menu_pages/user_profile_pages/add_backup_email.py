from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages.base as base

class AddBackupEmailPage():
		def __init__(self, driver):
			self.driver = driver

			self.activity_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View"
			self.text_classname = "android.widget.TextView"
			self.emailEdit_classname = "android.widget.EditText"
			self.nextButton_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]"
			self.closeButton_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]"

		def click_close(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.closeButton_xpath))
			)
			element = self.driver.find_element("xpath", self.closeButton_xpath)
			element.click()

		def click_next(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.nextButton_xpath))
			)
			element = self.driver.find_element("xpath", self.nextButton_xpath)
			element.click()

		def input_email(self, email):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.emailEdit_classname))
			)
			element = self.driver.find_element("class name", self.emailEdit_classname)
			element.send_keys(email)

		def get_title_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.text_classname))
			)
			elements = self.driver.find_elements("class name", self.text_classname)
			return elements[0].text # The first element is the title text

		def get_edit_email_hint(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("class name", self.emailEdit_classname))
			)
			email_edittext = self.driver.find_element("class name", self.emailEdit_classname)
			element = email_edittext.find_element("class name", self.text_classname)
			return element.text

		def get_next_button_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.nextButton_xpath))
			)
			next_button = self.driver.find_element("xpath", self.nextButton_xpath)
			element = next_button.find_element("class name", self.text_classname)
			return element.text

		def has_error_message_text(self):
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("xpath", self.activity_xpath))
			)
			activity = self.driver.find_element("xpath", self.activity_xpath)
			elements = activity.find_elements("xpath", "./*")
			print("Number of elements found:", len(elements))
			for element in elements:
				print("Element class name:", element)
			# if elements[3] and elements[3].get_attribute("class name") == self.text_classname:
			# 	return True
			return False
