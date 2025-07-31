from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SDcardStatusPage():
	def __init__(self, driver):
		self.driver = driver
		self.Header = "com.compal.bioslab.pixsee.pixm01:id/tvExternalSdCardRoom"
		self.Back = "com.compal.bioslab.pixsee.pixm01:id/ibExternalSDCardStorageClose"
		self.Title = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
		self.Description = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
		self.FormatButton = "com.compal.bioslab.pixsee.pixm01:id/btnExternalSDCardStorageFormat"
		self.Dialog = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
		self.Go = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
		self.No = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"
		self.Formatting = "com.compal.bioslab.pixsee.pixm01:id/tvFormatting"





	def click_back(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.Back))
		)
		element = self.driver.find_element("id", self.Back)
		element.click()
	def click_format(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.FormatButton))
		)
		element = self.driver.find_element("id", self.FormatButton)
		element.click()
	def click_go(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.Go))
		)
		element = self.driver.find_element("id", self.Go)
		element.click()
	def click_no(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.No))
		)
		element = self.driver.find_element("id", self.No)
		element.click()

	def header_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			element = self.driver.find_element("id", self.Header)
			return element.text
		except :
			return None
	def title_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Title))
			)
			element = self.driver.find_element("id", self.Title)
			return element.text
		except :
			return None
	def description_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Description))
			)
			element = self.driver.find_element("id", self.Description)
			return element.text
		except :
			return None
	def format_button_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.FormatButton))
			)
			element = self.driver.find_element("id", self.FormatButton)
			return element.text
		except :
			return None
	def dialog_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Dialog))
			)
			element = self.driver.find_element("id", self.Dialog)
			return element.text
		except :
			return None
	def go_button_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Go))
			)
			element = self.driver.find_element("id", self.Go)
			return element.text
		except :
			return None
	def no_button_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.No))
			)
			element = self.driver.find_element("id", self.No)
			return element.text
		except :
			return None

	def is_in_sdcard_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			return True
		except :
			return False
	def is_in_format_dialog(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Dialog))
			)
			return True
		except :
			return False
	def is_formatting(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Formatting))
			)
			return True
		except :
			return False

	def format_button_enabled(self):
		try:
			WebDriverWait(self.driver, 5).until(
				EC.presence_of_element_located(("id", self.FormatButton))
			)
			self.driver.find_element("id", self.FormatButton)
			return True
		except :
			return False
