from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages.base as base

class VoiceServicePage():
	def __init__(self, driver):
		self.driver = driver

		self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
		self.detectionNotificationText = "com.compal.bioslab.pixsee.pixm01:id/cl_voice_command_detection_label"
		self.serviceSectionParent = "com.compal.bioslab.pixsee.pixm01:id/clServiceSection"
		self.serviceSectionText_classname = "android.widget.TextView"
		self.voiceCommandText = "com.compal.bioslab.pixsee.pixm01:id/tvVoiceCommand"

		self.backButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back"
		self.saveButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_save"
		self.detectionSwitch = "com.compal.bioslab.pixsee.pixm01:id/switchVoiceService"
		self.voiceCommandButton = "com.compal.bioslab.pixsee.pixm01:id/clVoiceCommand"

		'''Discard dialog'''
		self.discardDialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"
		self.discardDialogTitle = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
		self.discardDialogYesButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
		self.discardDialogNoButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"

	def click_back(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.backButton))
		)
		element = self.driver.find_element("id", self.backButton)
		element.click()

	def click_save(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.saveButton))
		)
		element = self.driver.find_element("id", self.saveButton)
		element.click()

	def click_detection_switch(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.detectionSwitch))
		)
		element = self.driver.find_element("id", self.detectionSwitch)
		element.click()

	def click_voice_command_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.voiceCommandButton))
		)
		element = self.driver.find_element("id", self.voiceCommandButton)
		element.click()

	def click_discard_dialog_yes(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.discardDialogYesButton))
		)
		element = self.driver.find_element("id", self.discardDialogYesButton)
		element.click()

	def click_discard_dialog_no(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.discardDialogNoButton))
		)
		element = self.driver.find_element("id", self.discardDialogNoButton)
		element.click()

	def get_page_title(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.pageTitleText))
		)
		element = self.driver.find_element("id", self.pageTitleText)
		return element.text

	def get_save_button_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.saveButton))
		)
		element = self.driver.find_element("id", self.saveButton)
		return element.text

	def get_detection_notification(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.detectionNotificationText))
		)
		element = self.driver.find_element("id", self.detectionNotificationText)
		return element.text

	def get_service_section(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.serviceSectionParent))
		)
		parent_element = self.driver.find_element("id", self.serviceSectionParent)
		element = parent_element.find_element("class name", self.serviceSectionText_classname)
		return element.text

	def get_voice_command_button_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.voiceCommandText))
		)
		element = self.driver.find_element("id", self.voiceCommandText)
		return element.text

	def get_detection_switch_status(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.detectionSwitch))
		)
		element = self.driver.find_element("id", self.detectionSwitch)
		return element.get_attribute("checked") == "true"

	def get_save_button_enabled(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.saveButton))
		)
		element = self.driver.find_element("id", self.saveButton)
		return element.get_attribute("enabled") == "true"

	def get_discard_dialog_title(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.discardDialogTitle))
		)
		element = self.driver.find_element("id", self.discardDialogTitle)
		return element.text

	def get_discard_dialog_yes_button_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.discardDialogYesButton))
		)
		element = self.driver.find_element("id", self.discardDialogYesButton)
		return element.text

	def get_discard_dialog_no_button_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.discardDialogNoButton))
		)
		element = self.driver.find_element("id", self.discardDialogNoButton)
		return element.text

	def has_discard_dialog(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("id", self.discardDialog))
			)
			find_element = self.driver.find_element("id", self.discardDialog)
			return True
		except:
			return False

	def is_in_voice_service_page(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("id", self.detectionNotificationText))
			)
			self.driver.find_element("id", self.detectionNotificationText)
			return True
		except:
			return False

