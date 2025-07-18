from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AreaDetectionPage():
	def __init__(self, driver):
		self.driver = driver
		self.TutorTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTutorialTitle"
		self.TutorRightPageSpot = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[1]'
		self.TutorLeftPageSpot = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[2]'
		self.Skip = "com.compal.bioslab.pixsee.pixm01:id/btSkipTutorial"

		self.Header = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"


	def header_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			element = self.driver.find_element("id", self.Header)
			return element.text
		except:
			return None
	def tutor_title_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TutorTitle))
			)
			element = self.driver.find_element("id", self.TutorTitle)
			return element.text
		except:
			return None

	def is_in_area_detection_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TutorTitle))
			)
			return True
		except:
			return False
	def is_in_tutor_right_page(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("xpath", self.TutorRightPageSpot))
		)
		light = self.driver.find_element(AppiumBy.ID, self.TutorRightPageSpot)
		is_in_right = light.get_attribute("selected")
		return is_in_right == "true"
	def is_in_tutor_left_page(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("xpath", self.TutorLeftPageSpot))
		)
		light = self.driver.find_element(AppiumBy.ID, self.TutorLeftPageSpot)
		is_in_left = light.get_attribute("selected")
		return is_in_left == "true"


