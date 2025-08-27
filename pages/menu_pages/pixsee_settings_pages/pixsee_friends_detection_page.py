from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import base as base

class PixseeFriendsDetPage():
	def __init__(self, driver):
		self.driver = driver

		# Pixsee Friends Detection page elements
		self.Header = "com.compal.bioslab.pixsee.pixm01:id/textViewPixseeFriendsDetection"
		self.Save = "com.compal.bioslab.pixsee.pixm01:id/tvPixseeFriendsDetectionSettingsSave"
		self.Title = "com.compal.bioslab.pixsee.pixm01:id/tv_pixsee_friends_detection_status_text"
		self.Description = "com.compal.bioslab.pixsee.pixm01:id/tv_pixsee_friends_detection_subtext"
		self.Switch = "com.compal.bioslab.pixsee.pixm01:id/sw_pixsee_friends_detection_status_switch"
		self.Back = "com.compal.bioslab.pixsee.pixm01:id/ibPixseeFriendsDetectionBack"
		self.DetectionType = "com.compal.bioslab.pixsee.pixm01:id/tv_type_pixsee_friends_detection_text"
		self.TimeSpan = "com.compal.bioslab.pixsee.pixm01:id/tv_pixsee_friends_detection_time_span_text"
		self.AllDay = "com.compal.bioslab.pixsee.pixm01:id/rb_pixsee_friends_detection_all_day"
		self.AllDaytxt = "com.compal.bioslab.pixsee.pixm01:id/rb_pixsee_friends_detection_all_day_txt"
		self.SetTime = "com.compal.bioslab.pixsee.pixm01:id/rb_pixsee_friends_detection_set_time"
		self.SetTimetxt = "com.compal.bioslab.pixsee.pixm01:id/rb_pixsee_friends_detection_set_time_txt"
		self.StartTime = "com.compal.bioslab.pixsee.pixm01:id/tv_pixsee_friends_detection_start_time_span"
		self.EndTime = "com.compal.bioslab.pixsee.pixm01:id/tv_pixsee_friends_detection_ending_time_span"
		self.StartTimeBlock = "com.compal.bioslab.pixsee.pixm01:id/tv_pixsee_friends_detection_starting_time"
		self.EndTimeBlock = "com.compal.bioslab.pixsee.pixm01:id/tv_pixsee_friends_detection_ending_time"
		self.Hours = "com.compal.bioslab.pixsee.pixm01:id/rvHours"
		self.Minutes = "com.compal.bioslab.pixsee.pixm01:id/rvMinutes"
		self.AmPm = "com.compal.bioslab.pixsee.pixm01:id/rvAmPm"
		self.Cancel = "com.compal.bioslab.pixsee.pixm01:id/cancel"
		self.Confirm = "com.compal.bioslab.pixsee.pixm01:id/confirm"
		self.DiscardMessage = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
		self.DiscardYes = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
		self.DiscardNo = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"
	# status
	def is_switch_on(self):
		WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located((AppiumBy.ID, self.Switch))
		)
		switch = self.driver.find_element(AppiumBy.ID, self.Switch)
		return switch.get_attribute("checked") == "true"
	def is_in_pixsee_friends_det_page(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located((AppiumBy.ID, self.Switch))
			)
			return True
		except :
			return False
	def is_in_timer(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located((AppiumBy.ID, self.Cancel))
			)
			self.driver.find_element(AppiumBy.ID, self.Cancel)
			return True

		except :
			return False
	def is_in_discard_dialog(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located((AppiumBy.ID, self.DiscardMessage))
			)
			self.driver.find_element(AppiumBy.ID, self.DiscardMessage)
			return True

		except :
			return False

	# click
	def click_all_day(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.AllDay))
		)
		self.driver.find_element(AppiumBy.ID, self.AllDay).click()
	def click_set_time(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.SetTime))
		)
		self.driver.find_element(AppiumBy.ID, self.SetTime).click()
	def click_save(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Save))
		)
		self.driver.find_element(AppiumBy.ID, self.Save).click()
	def click_switch(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Switch))
		)
		self.driver.find_element(AppiumBy.ID, self.Switch).click()
	def click_back(self):
		self.driver.find_element(AppiumBy.ID, self.Back).click()
	def click_start_time_block(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.StartTimeBlock))
		)
		self.driver.find_element(AppiumBy.ID, self.StartTimeBlock).click()
	def click_end_time_block(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.EndTimeBlock))
		)
		self.driver.find_element(AppiumBy.ID, self.EndTimeBlock).click()
	def click_cancel(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Cancel))
		)
		self.driver.find_element(AppiumBy.ID, self.Cancel).click()
	def click_confirm(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Confirm))
		)
		self.driver.find_element(AppiumBy.ID, self.Confirm).click()
	def click_discard_yes(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DiscardYes))
		)
		self.driver.find_element(AppiumBy.ID, self.DiscardYes).click()
	def click_discard_no(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DiscardNo))
		)
		self.driver.find_element(AppiumBy.ID, self.DiscardNo).click()
	# text
	def title(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Header))
		)
		return self.driver.find_element(AppiumBy.ID, self.Header).text
	def description(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Title))
		)
		return self.driver.find_element(AppiumBy.ID, self.Title).text
	def description_subtitle(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Description))
		)
		return self.driver.find_element(AppiumBy.ID, self.Description).text
	def dettype_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DetectionType))
		)
		return self.driver.find_element(AppiumBy.ID, self.DetectionType).text
	def time_span_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TimeSpan))
		)
		return self.driver.find_element(AppiumBy.ID, self.TimeSpan).text
	def all_day_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.AllDaytxt))
		)
		return self.driver.find_element(AppiumBy.ID, self.AllDaytxt).text
	def set_time_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.SetTimetxt))
		)
		return self.driver.find_element(AppiumBy.ID, self.SetTimetxt).text
	def start_time_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.StartTime))
		)
		return self.driver.find_element(AppiumBy.ID, self.StartTime).text
	def end_time_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.EndTime))
		)
		return self.driver.find_element(AppiumBy.ID, self.EndTime).text
	def start_time_block_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.StartTimeBlock))
		)
		return self.driver.find_element(AppiumBy.ID, self.StartTimeBlock).text
	def end_time_block_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.EndTimeBlock))
		)
		return self.driver.find_element(AppiumBy.ID, self.EndTimeBlock).text
	def cancel_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Cancel))
		)
		return self.driver.find_element(AppiumBy.ID, self.Cancel).text
	def confirm_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Confirm))
		)
		return self.driver.find_element(AppiumBy.ID, self.Confirm).text
	def discard_message_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DiscardMessage))
		)
		return self.driver.find_element(AppiumBy.ID, self.DiscardMessage).text
	def discard_yes_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DiscardYes))
		)
		return self.driver.find_element(AppiumBy.ID, self.DiscardYes).text
	def discard_no_txt(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DiscardNo))
		)
		return self.driver.find_element(AppiumBy.ID, self.DiscardNo).text


	# check if the checkbox is clicked
	def all_day_status(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.AllDay))
		)
		return self.driver.find_element(AppiumBy.ID, self.AllDay).get_attribute("checked")
	def set_time_status(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.SetTime))
		)
		return self.driver.find_element(AppiumBy.ID, self.SetTime).get_attribute("checked")
	# change by scroll on android
	def change_hour_by_scroll(self):
		window = self.driver.get_window_size()
		x = window["width"] // 2.5 # number should be changed when on ios
		start_y = int(window["height"] * 0.6) # number should be changed when on ios
		end_y = int(window["height"] * 0.5) # number should be changed when on ios

		self.driver.swipe(x, start_y, x, end_y, 500)  # 500 毫秒完成滑動
		time.sleep(1)
	def change_minutes_by_scroll(self):
		window = self.driver.get_window_size()
		x = window["width"] // 2 # this might not be changed on ios
		start_y = int(window["height"] * 0.6) # number should be changed when on ios
		end_y = int(window["height"] * 0.5) # number should be changed when on ios

		self.driver.swipe(x, start_y, x, end_y, 500)  # 500 毫秒完成滑動
		time.sleep(1)
	def change_am_to_pm_by_scroll(self):
		window = self.driver.get_window_size()
		x = window["width"] // 6 * 5 # number should be changed when on ios
		start_y = int(window["height"] * 0.6) # number should be changed when on ios
		end_y = int(window["height"] * 0.5) # number should be changed when on ios

		self.driver.swipe(x, start_y, x, end_y, 500)  # 500 毫秒完成滑動
		time.sleep(1)

	def is_save_enable(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Save))
		)
		button = self.driver.find_element(AppiumBy.ID, self.Save)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"



