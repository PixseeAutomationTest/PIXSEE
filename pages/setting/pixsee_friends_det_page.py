from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PixseeFriendsDetPage():
	def __init__(self, driver):
		self.driver = driver

		# Pixsee Friends Detection page elements
		self.PixseeFriendsDetTitle = "com.compal.bioslab.pixsee.pixm01:id/textViewPixseeFriendsDetection"
		self.save = "com.compal.bioslab.pixsee.pixm01:id/tvPixseeFriendsDetectionSettingsSave"
		self.PixseeFriendsDetDesc = "com.compal.bioslab.pixsee.pixm01:id/tv_pixsee_friends_detection_status_text"
		self.PixseeFriendsDetDescSubtitle = "com.compal.bioslab.pixsee.pixm01:id/tv_pixsee_friends_detection_subtext"
		self.PixseeFriendsDetSwitch = "com.compal.bioslab.pixsee.pixm01:id/sw_pixsee_friends_detection_status_switch"
		self.back = "com.compal.bioslab.pixsee.pixm01:id/ibPixseeFriendsDetectionBack"
		self.DetectionType = "com.compal.bioslab.pixsee.pixm01:id/ibPixseeFriendsDetectionBack"
		self.TimeSpan = "com.compal.bioslab.pixsee.pixm01:id/tv_type_pixsee_friends_detection_text"
		self.AllDay = "com.compal.bioslab.pixsee.pixm01:id/rb_pixsee_friends_detection_all_day"
		self.AllDaytxt = "com.compal.bioslab.pixsee.pixm01:id/rb_pixsee_friends_detection_all_day_txt"
		self.SetTime = "com.compal.bioslab.pixsee.pixm01:id/rb_pixsee_friends_detection_set_time"
		self.SetTimetxt = "com.compal.bioslab.pixsee.pixm01:id/rb_pixsee_friends_detection_set_time_txt"



	def click_save(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.save))
		)
		self.driver.find_element(AppiumBy.ID, self.save).click()

	def click_switch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.PixseeFriendsDetSwitch))
		)
		self.driver.find_element(AppiumBy.ID, self.PixseeFriendsDetSwitch).click()

	def is_in_pixsee_friends_det_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((AppiumBy.ID, self.PixseeFriendsDetTitle))
			)
			return True
		except:
			return False

	def title(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.PixseeFriendsDetTitle))
		)
		return self.driver.find_element(AppiumBy.ID, self.PixseeFriendsDetTitle).text

	def description(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.PixseeFriendsDetDesc))
		)
		return self.driver.find_element(AppiumBy.ID, self.PixseeFriendsDetDesc).text

	def description_subtitle(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.PixseeFriendsDetDescSubtitle))
		)
		return self.driver.find_element(AppiumBy.ID, self.PixseeFriendsDetDescSubtitle).text

	def dettype(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DetectionType))
		)
		return self.driver.find_element(AppiumBy.ID, self.DetectionType).text

	def is_switch_on(self):
		WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((AppiumBy.ID, self.DetectionType))
		)
		switch = self.driver.find_element(AppiumBy.ID, self.DetectionType)
		return switch.get_attribute("checked") == "true"
	def time_span(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TimeSpan))
		)
		return self.driver.find_element(AppiumBy.ID, self.TimeSpan).text

	def click_all_day(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.AllDay))
		)
		self.driver.find_element(AppiumBy.ID, self.AllDay).click()
	def all_day_txt(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.AllDaytxt))
		)
		return self.driver.find_element(AppiumBy.ID, self.AllDaytxt).text

	def click_set_time(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.SetTime))
		)
		self.driver.find_element(AppiumBy.ID, self.SetTime).click()
	def set_time_txt(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.SetTimetxt))
		)
		return self.driver.find_element(AppiumBy.ID, self.SetTimetxt).text

	def click_back(self):
		self.driver.find_element(AppiumBy.ID, self.back).click()