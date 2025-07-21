from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CoveredFaceDetectionPage():
	def __init__(self, driver):
		self.driver = driver
		self.TutorTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTutorialTitle"
		self.Skip = "com.compal.bioslab.pixsee.pixm01:id/btCoverSkipTutorial"
		self.Header = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
		self.Save = "com.compal.bioslab.pixsee.pixm01:id/covered_face_detection_menu_save"
		self.Back = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
		self.Detection = "com.compal.bioslab.pixsee.pixm01:id/covered_face_detection_status_label"
		self.DetectionSubtitle = "com.compal.bioslab.pixsee.pixm01:id/tvDetectionSubs"
		self.Switch = "com.compal.bioslab.pixsee.pixm01:id/covered_face_detection_status_switch"
		self.Sensitivity = "com.compal.bioslab.pixsee.pixm01:id/type_detection_section"
		self.Low = "com.compal.bioslab.pixsee.pixm01:id/rb_low_radio_txt"
		self.LowCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_low_radio"
		self.Medium = "com.compal.bioslab.pixsee.pixm01:id/rb_medium_radio_txt"
		self.MediumCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_medium_radio"
		self.High = "com.compal.bioslab.pixsee.pixm01:id/rb_high_radio_txt"
		self.HighCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_high_radio"
		self.DragDescription = "com.compal.bioslab.pixsee.pixm01:id/covered_face_detection_define_area_text_view"
		self.TurnOffDialog = "com.compal.bioslab.pixsee.pixm01:id/tvTurnOffDetectionTitle"
		self.TurnOff15Button = "com.compal.bioslab.pixsee.pixm01:id/btnSnoozeFifteen"
		self.TurnOff30Button = "com.compal.bioslab.pixsee.pixm01:id/btnSnoozeThirty"
		self.TurnOffButton = "com.compal.bioslab.pixsee.pixm01:id/btnTurnOffDetection"
		self.TurnOffCancelButton = "com.compal.bioslab.pixsee.pixm01:id/btnCancel"
		self.Snooze = "com.compal.bioslab.pixsee.pixm01:id/tvSnooze"
		self.DiscardTitle = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
		self.DiscardNo = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"
		self.DiscardYes = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"

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
	def skip_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Skip))
			)
			element = self.driver.find_element("id", self.Skip)
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
	def turn_off_dialog_title(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TurnOffDialog))
		)
		return self.driver.find_element(AppiumBy.ID, self.TurnOffDialog).text
	def turn_off_15_min_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TurnOff15Button))
		)
		return self.driver.find_element(AppiumBy.ID, self.TurnOff15Button).text
	def turn_off_30_min_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TurnOff30Button))
		)
		return self.driver.find_element(AppiumBy.ID, self.TurnOff30Button).text
	def turn_off_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TurnOffButton))
		)
		return self.driver.find_element(AppiumBy.ID, self.TurnOffButton).text
	def turn_off_cancel_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TurnOffCancelButton))
		)
		return self.driver.find_element(AppiumBy.ID, self.TurnOffCancelButton).text
	def drag_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DragDescription))
		)
		return self.driver.find_element(AppiumBy.ID, self.DragDescription).text
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
	def click_turn_off_15_min(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.TurnOff15Button))
		)
		element = self.driver.find_element("id", self.TurnOff15Button)
		element.click()
	def click_turn_off_30_min(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.TurnOff30Button))
		)
		element = self.driver.find_element("id", self.TurnOff30Button)
		element.click()
	def click_turn_off(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.TurnOffButton))
		)
		element = self.driver.find_element("id", self.TurnOffButton)
		element.click()
	def click_turn_off_cancel(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.TurnOffCancelButton))
		)
		element = self.driver.find_element("id", self.TurnOffCancelButton)
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

	def is_in_covered_face_detection_tutor_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TutorTitle))
			)
			return True
		except:
			return False
	def is_in_covered_face_detection_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			return True
		except:
			return False
	def is_in_turn_off_dialog(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TurnOffDialog))
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
	def is_save_enable(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Save))
		)
		button = self.driver.find_element(AppiumBy.ID, self.Save)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"
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

	def snooze_shows(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Snooze))
			)
			return True
		except:
			return False

