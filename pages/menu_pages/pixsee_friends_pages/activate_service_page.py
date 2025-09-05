from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base as base

class ActivateServicePage:
	def __init__(self, driver):
		self.driver = driver

		self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/tvBarTitle"
		self.labelText = "com.compal.bioslab.pixsee.pixm01:id/tvTitleDolls"
		self.messageText = "com.compal.bioslab.pixsee.pixm01:id/tvScanLabel"
		self.dollSNCodeEditText = "com.compal.bioslab.pixsee.pixm01:id/tieActivateCodeDoll"
		self.text_classname = "android.widget.TextView"

		self.closeButton = "com.compal.bioslab.pixsee.pixm01:id/ibClose"
		self.codeTipButton = "com.compal.bioslab.pixsee.pixm01:id/ivTipActivationNumber"
		self.OKButton = "com.compal.bioslab.pixsee.pixm01:id/btnOK"

		'''Code Tip Dialog'''
		self.dialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"
		self.dialogMessageText = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
		self.dialogIGotItButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"

	def click_close_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.closeButton))
		)
		element = self.driver.find_element("id", self.closeButton)
		element.click()

	def input_doll_sn_code(self, sn_code):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.dollSNCodeEditText))
		)
		element = self.driver.find_element("id", self.dollSNCodeEditText)
		element.clear()
		element.send_keys(sn_code)

	def click_code_tip_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.codeTipButton))
		)
		element = self.driver.find_element("id", self.codeTipButton)
		element.click()

	def click_OK_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.OKButton))
		)
		element = self.driver.find_element("id", self.OKButton)
		element.click()

	def click_dialog_i_got_it_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.dialogIGotItButton))
		)
		element = self.driver.find_element("id", self.dialogIGotItButton)
		element.click()

	def get_page_title_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.pageTitleText))
		)
		element = self.driver.find_element("id", self.pageTitleText)
		return element.text

	def get_label_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.labelText))
		)
		element = self.driver.find_element("id", self.labelText)
		return element.text

	def get_message_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.messageText))
		)
		element = self.driver.find_element("id", self.messageText)
		return element.text

	def get_doll_sn_code_hint(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.dollSNCodeEditText))
		)
		element = self.driver.find_element("id", self.dollSNCodeEditText)
		return element.get_attribute("hint")

	def get_error_message_text(self):
		if not self.has_error_message():
			return None
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("class name", self.text_classname))
		)
		elements = self.driver.find_elements("class name", self.text_classname)
		return elements[-1].text

	def get_OK_button_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.OKButton))
		)
		element = self.driver.find_element("id", self.OKButton)
		return element.text

	def get_dialog_message_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.dialogMessageText))
		)
		element = self.driver.find_element("id", self.dialogMessageText)
		return element.text

	def get_dialog_i_got_it_button_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.dialogIGotItButton))
		)
		element = self.driver.find_element("id", self.dialogIGotItButton)
		return element.text

	def has_error_message(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("class name", self.text_classname))
		)
		elements = self.driver.find_elements("class name", self.text_classname)
		if len(elements) > 3:
			return True
		return False

	def has_dialog(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("id", self.dialog))
			)
			return True
		except:
			return False

	def is_in_activate_service_page(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("id", self.labelText))
			)
			self.driver.find_element("id", self.labelText)
			return True
		except:
			return False