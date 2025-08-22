from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PlayBackPage():
	def __init__(self, driver):
		self.driver = driver
		self.TutorTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
		self.TutorDescription = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
		self.CalenderButton = "com.compal.bioslab.pixsee.pixm01:id/ib_playback_calendar"
		self.LiveButton = "com.compal.bioslab.pixsee.pixm01:id/ibLiveButton"


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