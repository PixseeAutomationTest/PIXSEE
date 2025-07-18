from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CryDetectionPage():
	def __init__(self, driver):
		self.driver = driver
		self.Header = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
		self.Back = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
		self.Save = "com.compal.bioslab.pixsee.pixm01:id/tv_save"
		self.Switch = "com.compal.bioslab.pixsee.pixm01:id/crying_settings_status_switch"
		self.Title = "com.compal.bioslab.pixsee.pixm01:id/crying_settings_status_text"

	def header_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			element = self.driver.find_element("id", self.Header)
			return element.text
		except:
			return None
	def title_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Title))
			)
			element = self.driver.find_element("id", self.Title)
			return element.text
		except:
			return None

	def click_back(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.Back))
		)
		element = self.driver.find_element("id", self.Back)
		element.click()
	def click_save(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.Save))
		)
		element = self.driver.find_element("id", self.Save)
		element.click()
	def click_switch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.Switch))
		)
		element = self.driver.find_element("id", self.Switch)
		element.click()





	def is_in_cry_detection_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			return True
		except:
			return False