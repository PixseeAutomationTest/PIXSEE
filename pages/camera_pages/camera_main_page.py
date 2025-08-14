from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CameraMainPage():
	def __init__(self, driver):
		self.driver = driver
		self.TutorTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
		self.TutorDescription = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
		self.cameraButton = "com.compal.bioslab.pixsee.pixm01:id/ibCamera"
		self.videoButton = "com.compal.bioslab.pixsee.pixm01:id/ibVideo"
		self.albumButton = "com.compal.bioslab.pixsee.pixm01:id/ibAlbum"
		self.homeButton = "com.compal.bioslab.pixsee.pixm01:id/ibHome"

	def tutor_title(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TutorTitle))
		)
		element = self.driver.find_element(AppiumBy.ID, self.TutorTitle)
		return element.text
	def tutor_description(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TutorDescription))
		)
		element = self.driver.find_element(AppiumBy.ID, self.TutorDescription)
		return element.text

	def click_home(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.homeButton))
		)
		self.driver.find_element(AppiumBy.ID, self.homeButton).click()

