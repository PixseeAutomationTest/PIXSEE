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
		self.Detection = "com.compal.bioslab.pixsee.pixm01:id/crying_settings_status_text"
		self.DetectionSubtitle = "com.compal.bioslab.pixsee.pixm01:id/crying_settings_subtext"
		self.Sensitivity = "com.compal.bioslab.pixsee.pixm01:id/type_detection_section"
		self.Low = "com.compal.bioslab.pixsee.pixm01:id/rb_low_radio_txt"
		self.LowCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_low_radio"
		self.Medium = "com.compal.bioslab.pixsee.pixm01:id/rb_medium_radio_txt"
		self.MediumCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_medium_radio"
		self.High = "com.compal.bioslab.pixsee.pixm01:id/rb_high_radio_txt"
		self.HighCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_high_radio"
		self.MusicSettings = "com.compal.bioslab.pixsee.pixm01:id/crying_settings_smart_soothing_section"
		self.SmartSoothing = "com.compal.bioslab.pixsee.pixm01:id/crying_settings_soothing_text"
		self.SmartSoothingSwitch = "com.compal.bioslab.pixsee.pixm01:id/crying_settings_soothing_switch"
		self.Music = "com.compal.bioslab.pixsee.pixm01:id/crying_settings_music_label"
		self.MusicButton = "com.compal.bioslab.pixsee.pixm01:id/crying_settings_music_container"
		self.MusicRoom = "com.compal.bioslab.pixsee.pixm01:id/tvContentPlayRoom"
		self.DiscardTitle = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
		self.DiscardNo = "com.compal.bioslab.pixsee.pixm01:id/tvNegativeButton"
		self.DiscardYes = "com.compal.bioslab.pixsee.pixm01:id/tvPositiveButton"

	def header_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			element = self.driver.find_element("id", self.Header)
			return element.text
		except:
			return None
	def title(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Detection))
			)
			element = self.driver.find_element("id", self.Detection)
			return element.text
		except:
			return None
	def detection_description(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DetectionSubtitle))
			)
			element = self.driver.find_element("id", self.DetectionSubtitle)
			return element.text
		except:
			return None
	def sensitivity_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Sensitivity))
			)
			element = self.driver.find_element("id", self.Sensitivity)
			return element.text
		except:
			return None
	def music_settings_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.MusicSettings))
			)
			element = self.driver.find_element("id", self.MusicSettings)
			return element.text
		except:
			return None
	def smart_soothing_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.SmartSoothing))
			)
			element = self.driver.find_element("id", self.SmartSoothing)
			return element.text
		except:
			return None
	def low_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Low))
			)
			element = self.driver.find_element("id", self.Low)
			return element.text
		except:
			return None
	def medium_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Medium))
			)
			element = self.driver.find_element("id", self.Medium)
			return element.text
		except:
			return None
	def high_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.High))
			)
			element = self.driver.find_element("id", self.High)
			return element.text
		except:
			return None
	def music_title(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Music))
			)
			element = self.driver.find_element("id", self.Music)
			return element.text
		except:
			return None
	def discard_message_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DiscardTitle))
			)
			element = self.driver.find_element("id", self.DiscardTitle)
			return element.text
		except:
			return None
	def discard_no_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DiscardNo))
			)
			element = self.driver.find_element("id", self.DiscardNo)
			return element.text
		except:
			return None
	def discard_yes_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DiscardYes))
			)
			element = self.driver.find_element("id", self.DiscardYes)
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
	def click_low(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.LowCheckBox))
		)
		element = self.driver.find_element("id", self.LowCheckBox)
		element.click()
	def click_medium(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.MediumCheckBox))
		)
		element = self.driver.find_element("id", self.MediumCheckBox)
		element.click()
	def click_high(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.HighCheckBox))
		)
		element = self.driver.find_element("id", self.HighCheckBox)
		element.click()
	def click_smart_soothing_switch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.SmartSoothing))
		)
		element = self.driver.find_element("id", self.SmartSoothing)
		element.click()
	def click_music(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.MusicButton))
		)
		element = self.driver.find_element("id", self.MusicButton)
		element.click()
	def click_discard_no(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.DiscardNo))
		)
		element = self.driver.find_element("id", self.DiscardNo)
		element.click()
	def click_discard_yes(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.DiscardYes))
		)
		element = self.driver.find_element("id", self.DiscardYes)
		element.click()

	def is_in_music_page(self):
		try:
			WebDriverWait(self.driver, 3).until(
				EC.presence_of_element_located((AppiumBy.ID, self.MusicRoom))
			)
			return True
		except:
			return False
	def is_in_cry_detection_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			return True
		except:
			return False
	def is_in_discard_dialog(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DiscardTitle))
			)
			return True
		except:
			return False

	def is_switch_on(self):
		WebDriverWait(self.driver, 3).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Sensitivity))
		)
		switch = self.driver.find_element(AppiumBy.ID, self.Sensitivity)
		return switch.get_attribute("checked") == "true"
	def is_smart_soothing_switch_on(self):
		WebDriverWait(self.driver, 3).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Music))
		)
		switch = self.driver.find_element(AppiumBy.ID, self.Music)
		return switch.get_attribute("checked") == "true"

	def is_low_clickable(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.LowCheckBox))
		)
		button = self.driver.find_element(AppiumBy.ID, self.LowCheckBox)
		is_clickable = button.get_attribute("clickable")
		return is_clickable == "true"
	def is_medium_clickable(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.MediumCheckBox))
		)
		button = self.driver.find_element(AppiumBy.ID, self.MediumCheckBox)
		is_clickable = button.get_attribute("clickable")
		return is_clickable == "true"
	def is_high_clickable(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.HighCheckBox))
		)
		button = self.driver.find_element(AppiumBy.ID, self.HighCheckBox)
		is_clickable = button.get_attribute("clickable")
		return is_clickable == "true"
