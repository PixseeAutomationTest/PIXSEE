from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MenuPage:
		def __init__(self, driver):
			self.driver = driver

		def tutor_friends(self):
			pass

		def click_profile(self):
			self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome").click()

		def click_name(self):
			self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome").click()

		def click_members(self):
			self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome").click()

		def click_settings(self):
			self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome").click()

		def click_album(self):
			self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome").click()

		def click_faces(self):
			self.driver.find_element(AppiumBy.ID,).click()

		def click_frames(self):
			self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome").click()

		def click_subscription(self):
			self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome").click()

		def click_assistant(self):
			self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome").click()

		def click_about(self):
			self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsAbout").click()

		def click_logout(self):
			self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsLogout").click()



