from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AreaDetectionPage():
	def __init__(self, driver):
		self.driver = driver
		self.TutorTitle1 = "com.compal.bioslab.pixsee.pixm01:id/tvTutorialTitle"
		self.TutorTitle2 = "com.compal.bioslab.pixsee.pixm01:id/tvTutorialTitle"
		self.TutorFirstPageIndicator = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[1]'
		self.TutorSecondPageIndicator = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[2]'
		self.Skip = "com.compal.bioslab.pixsee.pixm01:id/btSkipTutorial"

		self.Header = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"

	def click_skip(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.Skip))
		)
		element = self.driver.find_element("id", self.Skip)
		element.click()
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

	def header_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			element = self.driver.find_element("id", self.Header)
			return element.text
		except:
			return None
	def tutor_first_title_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TutorTitle1))
			)
			element = self.driver.find_element("id", self.TutorTitle1)
			return element.text
		except:
			return None
	def tutor_second_title_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TutorTitle2))
			)
			element = self.driver.find_element("id", self.TutorTitle2)
			return element.text
		except:
			return None
	def skip_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Skip))
			)
			element = self.driver.find_element("id", self.Skip)
			return element.text
		except:
			return None

	def is_in_area_detection_tutor_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TutorTitle1))
			)
			return True
		except:
			return False
	def is_in_area_detection_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			return True
		except:
			return False
	def is_in_tutor_first_page(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("xpath", self.TutorFirstPageIndicator))
		)
		light = self.driver.find_element(AppiumBy.ID, self.TutorFirstPageIndicator)
		is_in_right = light.get_attribute("selected")
		return is_in_right == "true"
	def is_in_tutor_second_page(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("xpath", self.TutorSecondPageIndicator))
		)
		light = self.driver.find_element(AppiumBy.ID, self.TutorSecondPageIndicator)
		is_in_left = light.get_attribute("selected")
		return is_in_left == "true"


