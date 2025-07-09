from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class MenuPage():
	def __init__(self, driver):
		self.driver = driver
		self.profileButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsProfile"
		self.nameButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsName"
		self.membersButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsMembers"
		self.settingsButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsSettings"
		self.friendsButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsFriends"
		self.albumButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsGallery"
		self.facesButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsFaces"
		self.framesButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsFrames"
		self.subscriptionButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsSubscription"
		self.assistantButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsAssistant"
		self.aboutButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsAbout"
		self.logoutButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsLogout"


	
	def click_profile(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.profileButton))
		)
		self.driver.find_element(AppiumBy.ID, self.profileButton).click()
		time.sleep(1)  # 等待頁面加載完成，必要時可調整時間

	def click_name(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.nameButton))
		)
		self.driver.find_element(AppiumBy.ID, self.nameButton).click()
		time.sleep(1)  # 等待頁面加載完成，必要時可調整時間

	def click_members(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.membersButton))
		)
		self.driver.find_element(AppiumBy.ID, self.membersButton).click()
		time.sleep(1)  # 等待頁面加載完成，必要時可調整時間

	def click_settings(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.settingsButton))
		)
		self.driver.find_element(AppiumBy.ID, self.settingsButton).click()
		time.sleep(1)

	def click_friends(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.friendsButton))
		)
		self.driver.find_element(AppiumBy.ID, self.friendsButton).click()
		time.sleep(1)

	def click_album(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.albumButton))
		)
		self.driver.find_element(AppiumBy.ID, self.albumButton).click()
		time.sleep(1)
	
	def click_faces(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.facesButton))
		)
		self.driver.find_element(AppiumBy.ID, self.facesButton).click()
		time.sleep(1)
	# 	self.driver.find_element(AppiumBy.ID,).click()
	#
	def click_frames(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.framesButton))
		)
		self.driver.find_element(AppiumBy.ID, self.framesButton).click()
		time.sleep(1)

	def click_subscription(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.subscriptionButton))
		)
		self.driver.find_element(AppiumBy.ID, self.subscriptionButton).click()
		time.sleep(1)

	def click_assistant(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.assistantButton))
		)
		self.driver.find_element(AppiumBy.ID, self.assistantButton).click()
		time.sleep(1)

	def click_about(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id",self.aboutButton))
		)
		self.driver.find_element(AppiumBy.ID, self.aboutButton).click()
		time.sleep(1)
	
	def click_logout(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.logoutButton))
		)
		self.driver.find_element(AppiumBy.ID, self.logoutButton).click()
		time.sleep(1)

	

