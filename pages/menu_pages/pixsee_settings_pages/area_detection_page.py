from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image


class AreaDetectionPage():
	def __init__(self, driver):
		self.driver = driver
		self.TutorTitle1 = "com.compal.bioslab.pixsee.pixm01:id/tvTutorialTitle"
		self.TutorTitle2 = "com.compal.bioslab.pixsee.pixm01:id/tvTutorialTitle"
		self.TutorFirstPageIndicator = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[1]'
		self.TutorSecondPageIndicator = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[2]'
		self.Skip = "com.compal.bioslab.pixsee.pixm01:id/btSkipTutorial"

		self.Header = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
		self.Save = "com.compal.bioslab.pixsee.pixm01:id/efence_menu_save"
		self.Back = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
		self.Detection = "com.compal.bioslab.pixsee.pixm01:id/efence_status_label"
		self.DetectionSubtitle = "com.compal.bioslab.pixsee.pixm01:id/tvDetectionSubs"
		self.Switch = "com.compal.bioslab.pixsee.pixm01:id/efence_status_switch"
		self.Sensitivity = "com.compal.bioslab.pixsee.pixm01:id/type_detection_section"
		self.Low = "com.compal.bioslab.pixsee.pixm01:id/rb_low_radio_txt"
		self.LowCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_low_radio"
		self.Medium = "com.compal.bioslab.pixsee.pixm01:id/rb_medium_radio_txt"
		self.MediumCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_medium_radio"
		self.High = "com.compal.bioslab.pixsee.pixm01:id/rb_high_radio_txt"
		self.HighCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_high_radio"
		self.DetectionType = "com.compal.bioslab.pixsee.pixm01:id/efence_type_detection_section"
		self.BabyIn = "com.compal.bioslab.pixsee.pixm01:id/efence_type_safety_txt"
		self.BabyInCheckBox = "com.compal.bioslab.pixsee.pixm01:id/efence_type_safety_radio"
		self.BabyOut = "com.compal.bioslab.pixsee.pixm01:id/efence_type_dangerous_txt"
		self.Baby0utCheckBox = "com.compal.bioslab.pixsee.pixm01:id/efence_type_dangerous_radio"
		self.DragDescription = "com.compal.bioslab.pixsee.pixm01:id/efence_define_area_txt"
		self.TurnOffDialog = "com.compal.bioslab.pixsee.pixm01:id/tvTurnOffDetectionTitle"
		self.TurnOff15Button = "com.compal.bioslab.pixsee.pixm01:id/btnSnoozeFifteen"
		self.TurnOff30Button = "com.compal.bioslab.pixsee.pixm01:id/btnSnoozeThirty"
		self.TurnOffButton =  "com.compal.bioslab.pixsee.pixm01:id/btnTurnOffDetection"
		self.TurnOffCancelButton = "com.compal.bioslab.pixsee.pixm01:id/btnCancel"
		self.Snooze = "com.compal.bioslab.pixsee.pixm01:id/tvSnooze"
		self.DiscardTitle = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
		self.DiscardNo = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"
		self.DiscardYes = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
		self.information = "com.compal.bioslab.pixsee.pixm01:id/btEffenceInformation"
		self.Stream = "com.compal.bioslab.pixsee.pixm01:id/area_stream"
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
			EC.presence_of_element_located((AppiumBy.ID, self.Switch))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Switch)
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
	def click_baby_out(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.Baby0utCheckBox))
		)
		element = self.driver.find_element("id", self.Baby0utCheckBox)
		element.click()
	def click_baby_in(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.BabyInCheckBox))
		)
		element = self.driver.find_element("id", self.BabyInCheckBox)
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
	def click_information(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.information))
		)
		element = self.driver.find_element("id", self.information)
		element.click()

	def discard_message_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DiscardTitle))
			)
			element = self.driver.find_element("id", self.DiscardTitle)
			return element.text
		except AssertionError:
			return None
	def discard_no_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DiscardNo))
			)
			element = self.driver.find_element("id", self.DiscardNo)
			return element.text
		except AssertionError:
			return None
	def discard_yes_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DiscardYes))
			)
			element = self.driver.find_element("id", self.DiscardYes)
			return element.text
		except AssertionError:
			return None
	def header_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			element = self.driver.find_element("id", self.Header)
			return element.text
		except AssertionError:
			return None
	def tutor_first_title_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TutorTitle1))
			)
			element = self.driver.find_element("id", self.TutorTitle1)
			return element.text
		except AssertionError:
			return None
	def tutor_second_title_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TutorTitle2))
			)
			element = self.driver.find_element("id", self.TutorTitle2)
			return element.text
		except AssertionError:
			return None
	def skip_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Skip))
			)
			element = self.driver.find_element("id", self.Skip)
			return element.text
		except AssertionError:
			return None
	def title(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Detection))
			)
			element = self.driver.find_element("id", self.Detection)
			return element.text
		except AssertionError:
			return None
	def detection_description(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DetectionSubtitle))
			)
			element = self.driver.find_element("id", self.DetectionSubtitle)
			return element.text
		except AssertionError:
			return None
	def sensitivity_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Sensitivity))
			)
			element = self.driver.find_element("id", self.Sensitivity)
			return element.text
		except AssertionError:
			return None
	def dettype_txt(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DetectionType))
		)
		return self.driver.find_element(AppiumBy.ID, self.DetectionType).text
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
		except AssertionError:
			return None
	def medium_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Medium))
			)
			element = self.driver.find_element("id", self.Medium)
			return element.text
		except AssertionError:
			return None
	def high_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.High))
			)
			element = self.driver.find_element("id", self.High)
			return element.text
		except AssertionError:
			return None
	def baby_in_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.BabyIn))
			)
			element = self.driver.find_element("id", self.BabyIn)
			return element.text
		except AssertionError:
			return None
	def baby_out_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.BabyOut))
			)
			element = self.driver.find_element("id", self.BabyOut)
			return element.text
		except AssertionError:
			return None

	def is_in_area_detection_tutor_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TutorTitle1))
			)
			return True
		except AssertionError:
			return False
	def is_in_area_detection_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			return True
		except AssertionError:
			return False
	def is_in_tutor_first_page(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("xpath", self.TutorFirstPageIndicator))
		)
		light = self.driver.find_element("xpath", self.TutorFirstPageIndicator)
		is_in_right = light.get_attribute("selected")
		return is_in_right == "true"
	def is_in_tutor_second_page(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("xpath", self.TutorSecondPageIndicator))
		)
		light = self.driver.find_element("xpath", self.TutorSecondPageIndicator)
		is_in_left = light.get_attribute("selected")
		return is_in_left == "true"
	def is_in_turn_off_dialog(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TurnOffDialog))
			)
			return True
		except AssertionError:
			return False
	def is_in_discard_dialog(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DiscardTitle))
			)
			return True
		except AssertionError:
			return False

	def is_save_enable(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Save))
		)
		button = self.driver.find_element(AppiumBy.ID, self.Save)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"
	def is_switch_on(self):
		WebDriverWait(self.driver, 3).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Switch))
		)
		switch = self.driver.find_element(AppiumBy.ID, self.Switch)
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

	def snooze_shows(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Snooze))
			)
			return True
		except AssertionError:
			return False

	def find_stream_left_top(self):
		element_color = self.driver.find_element(AppiumBy.ID, self.Stream)
		x = element_color.location['x']
		y = element_color.location['y']
		'''
		w = element_color.size['width']
		h = element_color.size['height']
		center_x = x + w // 2
		center_y = y + h // 2
		'''
		return x, y

	def is_color_in_range(self, x, y, color_range):
		"""
		Take a screenshot and check if the pixel at coordinates (x, y) is within the given RGB color range.。

		:param y: vertical coordinate of the pixel to check
		:param x: horizontal coordinate of the pixel to check
		:param color_range: color range, ((R_min, G_min, B_min), (R_max, G_max, B_max))
		:return: True or False
		"""
		screenshot_path = "screen.png"
		self.driver.save_screenshot(screenshot_path)

		img = Image.open(screenshot_path)
		pixel = img.getpixel((x, y))  # send back (R, G, B)

		(r_min, g_min, b_min), (r_max, g_max, b_max) = color_range
		r, g, b = pixel[:3]

		in_range = (r_min <= r <= r_max) and (g_min <= g <= g_max) and (b_min <= b <= b_max)
		print(f"Pixel at ({x},{y}) = {pixel}, in range: {in_range}")
		return in_range

