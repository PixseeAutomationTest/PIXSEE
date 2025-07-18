from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CoveredFaceDetectionPage():
	def __init__(self, driver):
		self.driver = driver
		self.TutorTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTutorialTitle"
		self.Skip = "com.compal.bioslab.pixsee.pixm01:id/btCoverSkipTutorial"
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

	def is_in_covered_face_detection_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TutorTitle))
			)
			return True
		except:
			return False

