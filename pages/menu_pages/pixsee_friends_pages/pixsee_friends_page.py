from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import pages.base as base

class PixseeFriendsPage:
	def __init__(self, driver):
		self.driver = driver

		self.titleText = "com.compal.bioslab.pixsee.pixm01:id/tvTitle" # For page and dialogs
		self.dollNameText = "com.compal.bioslab.pixsee.pixm01:id/tv_dolls_list_doll_name"
		self.dollsList = "com.compal.bioslab.pixsee.pixm01:id/cl_name_and_play_mode"

		self.closeButton = "com.compal.bioslab.pixsee.pixm01:id/ibClose"
		self.infoButton = "com.compal.bioslab.pixsee.pixm01:id/ibInfo"
		self.addDollButton = "com.compal.bioslab.pixsee.pixm01:id/ibAdd"

		self.tutorialDialog = "com.compal.bioslab.pixsee.pixm01:id/llLayoutAlertDialog"

		'''Tutorial Dialog'''
		self.tutorialDialogMessageText = "com.compal.bioslab.pixsee.pixm01:id/tvMessage"
		self.tutorialDialogIKnowButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositive"

		'''Add Doll Dialog'''
		self.addDollDialogAlertText = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
		self.addDollDialogMessageText = "com.compal.bioslab.pixsee.pixm01:id/tvMessageAlertDialog"
		self.addDollDialogOkButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
		self.addDollDialogCancelButton = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"

		'''Outside Website'''
		self.url = "com.android.chrome:id/url_bar"

	def click_close_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.closeButton))
		)
		element = self.driver.find_element("id", self.closeButton)
		element.click()

	def click_info_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.infoButton))
		)
		element = self.driver.find_element("id", self.infoButton)
		element.click()

	def click_add_doll_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.addDollButton))
		)
		element = self.driver.find_element("id", self.addDollButton)
		element.click()

	def click_tutorial_dialog_i_know_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.tutorialDialogIKnowButton))
		)
		element = self.driver.find_element("id", self.tutorialDialogIKnowButton)
		element.click()

	def click_add_doll_dialog_ok_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.addDollDialogOkButton))
		)
		element = self.driver.find_element("id", self.addDollDialogOkButton)
		element.click()

	def click_add_doll_dialog_cancel_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.addDollDialogCancelButton))
		)
		element = self.driver.find_element("id", self.addDollDialogCancelButton)
		element.click()

	def scroll_up_dolls_list(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.dollsList))
		)
		element = self.driver.find_element("id", self.dollsList)
		x = element.location['x']
		y = element.location['y']

		w = element.size['width']
		h = element.size['height']
		self.driver.swipe(x + w, y + h, x, y, 300)

	def scroll_down_dolls_list(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.dollsList))
		)
		element = self.driver.find_element("id", self.dollsList)
		x = element.location['x']
		y = element.location['y']

		w = element.size['width']
		h = element.size['height']
		self.driver.swipe(x, y, x + w, y + h, 300)

	# For page and dialogs
	def get_title_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.titleText))
		)
		element = self.driver.find_element("id", self.titleText)
		return element.text

	def get_doll_name_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.dollNameText))
		)
		element = self.driver.find_element("id", self.dollNameText)
		return element.text

	def get_tutorial_dialog_message_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.tutorialDialogMessageText))
		)
		element = self.driver.find_element("id", self.tutorialDialogMessageText)
		return element.text

	def get_tutorial_dialog_i_know_button_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.tutorialDialogIKnowButton))
		)
		element = self.driver.find_element("id", self.tutorialDialogIKnowButton)
		return element.text

	def get_add_doll_dialog_alert_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.addDollDialogAlertText))
		)
		element = self.driver.find_element("id", self.addDollDialogAlertText)
		return element.text

	def get_add_doll_dialog_message_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.addDollDialogMessageText))
		)
		element = self.driver.find_element("id", self.addDollDialogMessageText)
		return element.text

	def get_add_doll_dialog_ok_button_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.addDollDialogOkButton))
		)
		element = self.driver.find_element("id", self.addDollDialogOkButton)
		return element.text

	def get_add_doll_dialog_cancel_button_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.addDollDialogCancelButton))
		)
		element = self.driver.find_element("id", self.addDollDialogCancelButton)
		return element.text

	def get_outside_website_url(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.url))
		)
		element = self.driver.find_element("id", self.url)
		return element.text

	def has_dialog(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("id", self.tutorialDialog))
			)
			self.driver.find_element("id", self.tutorialDialog)
			return True
		except:
			return False

	def is_in_pixsee_friends_page(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("id", self.dollNameText))
			)
			self.driver.find_element("id", self.dollNameText)
			return True
		except:
			return False

	def is_in_outside_website(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("id", self.url))
			)
			self.driver.find_element("id", self.url)
			return True
		except:
			return False