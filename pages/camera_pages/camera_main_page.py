from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CameraMainPage():
	def __init__(self, driver):
		self.driver = driver
		self.TutorTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
		self.TutorDescription = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
		self.CameraButton = "com.compal.bioslab.pixsee.pixm01:id/ibCamera"
		self.VideoButton = "com.compal.bioslab.pixsee.pixm01:id/ibLandscapeLiveFeaturesRecordVideo"
		self.MusicAlbumButton = "com.compal.bioslab.pixsee.pixm01:id/ibLandscapeLiveFeaturesPlayMusic"
		self.TwoWayTalkButton = "com.compal.bioslab.pixsee.pixm01:id/ibPushToTalk"
		self.ResolutionButton = "com.compal.bioslab.pixsee.pixm01:id/ibLandscapeLiveFeaturesVideoResolution"
		self.PlayBackButton = "com.compal.bioslab.pixsee.pixm01:id/tempPlaybackButton"
		self.HomeButton = "com.compal.bioslab.pixsee.pixm01:id/ibHome"

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
			EC.presence_of_element_located((AppiumBy.ID, self.HomeButton))
		)
		self.driver.find_element(AppiumBy.ID, self.HomeButton).click()
	def click_camera(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.CameraButton))
		)
		self.driver.find_element(AppiumBy.ID, self.CameraButton).click()
	def click_video(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.VideoButton))
		)
		self.driver.find_element(AppiumBy.ID, self.VideoButton).click()
	def click_music_album(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.MusicAlbumButton))
		)
		self.driver.find_element(AppiumBy.ID, self.MusicAlbumButton).click()
	def click_two_way_talk(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TwoWayTalkButton))
		)
		self.driver.find_element(AppiumBy.ID, self.TwoWayTalkButton).click()
	def click_resolution(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.ResolutionButton))
		)
		self.driver.find_element(AppiumBy.ID, self.ResolutionButton).click()
	def click_play_back(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.PlayBackButton))
		)
		self.driver.find_element(AppiumBy.ID, self.PlayBackButton).click()

