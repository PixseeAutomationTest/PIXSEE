from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PixseeSettingsPage():
	def __init__(self, driver):
		self.driver = driver

		# pixsee settings page elements
		self.backButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"

		self.locationNametxt = "com.compal.bioslab.pixsee.pixm01:id/tvRoomName"
		self.PixseeProfile = "com.compal.bioslab.pixsee.pixm01:id/clProfileSettings"
		self.PixseeProfiletxt = "com.compal.bioslab.pixsee.pixm01:id/tvProfileSettings"

		self.WifiSettings = "com.compal.bioslab.pixsee.pixm01:id/clWifiSettings"
		self.WifiSettingstxt = "com.compal.bioslab.pixsee.pixm01:id/tvWifiSettings"

		self.PixseeFriendsDetection = "com.compal.bioslab.pixsee.pixm01:id/clPixseeFriendsDetection"
		self.PixseeFriendsDetectiontxt = "com.compal.bioslab.pixsee.pixm01:id/tvPixseeFriendsDetection"
		self.PixseeFriendsDetectionStatus = "com.compal.bioslab.pixsee.pixm01:id/tvPixseeFriendsDetectionStatus"

		self.EnvironmentSettings = "com.compal.bioslab.pixsee.pixm01:id/clEnvironmentDetection"
		self.EnvironmentSettingstxt = "com.compal.bioslab.pixsee.pixm01:id/tvEnvironmentDetection"
		self.EnvironmentSettingsStatus = "com.compal.bioslab.pixsee.pixm01:id/tvEnvironmentDetectionStatus"

		self.CryDetection = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_crying_container"
		self.CryDetectiontxt = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_crying_label"
		self.CryDetectionStatus = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_crying_txt"

		self.AreaDetection = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_efence_container"
		self.AreaDetectiontxt = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_efence_label"
		self.AreaDetectionStatus = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_efence_txt"

		self.CoveredFaceDetection = "com.compal.bioslab.pixsee.pixm01:id/cover_detection_settings_container"
		self.CoveredFaceDetectiontxt = "com.compal.bioslab.pixsee.pixm01:id/cover_detection_settings_label"
		self.CoveredFaceDetectionStatus = "com.compal.bioslab.pixsee.pixm01:id/cover_detection_settings_on_off_text"

		self.TimeLapseVideo = "com.compal.bioslab.pixsee.pixm01:id/time_lapse_settings_container"
		self.TimeLapseVideotxt = "com.compal.bioslab.pixsee.pixm01:id/time_lapse_settings_label"
		self.TimeLapseVideoStatus = "com.compal.bioslab.pixsee.pixm01:id/time_lapse_settings_on_off_text"

		self.VoiceService = "com.compal.bioslab.pixsee.pixm01:id/clVoiceCommand"
		self.VoiceServicetxt = "com.compal.bioslab.pixsee.pixm01:id/tvVoiceCommand"

		self.ShutterSoundSwitch = "com.compal.bioslab.pixsee.pixm01:id/capture_sound_switch"
		# self.ShutterSoundTitle = "com.compal.bioslab.pixsee.pixm01:id/clCaptureSound"
		self.ShutterSoundtxt = "com.compal.bioslab.pixsee.pixm01:id/tvCaptureSound"

		self.LEDindicatorSwitch = "com.compal.bioslab.pixsee.pixm01:id/led_switch"
		# self.LEDindicatorTitle = "com.compal.bioslab.pixsee.pixm01:id/clIndicatorLed"
		self.LEDindicatortxt = "com.compal.bioslab.pixsee.pixm01:id/tvIndicatorLedSettings"

		self.NightModeSwitch = "com.compal.bioslab.pixsee.pixm01:id/night_vision_switch"
		# self.NightModeTitle = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_night_vision_label"
		self.NightModetxt = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_night_vision_text"
		self.NightModeSubtext = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_night_vision_subtext"

		self.PrivacySettingsSwitch = "com.compal.bioslab.pixsee.pixm01:id/privacy_control_switch"
		# self.PrivacySettingsTitle = "com.compal.bioslab.pixsee.pixm01:id/privacy_control_label"
		self.PrivacySettingstxt = "com.compal.bioslab.pixsee.pixm01:id/privacy_control_text"
		self.PrivacySettingsSubtext = "com.compal.bioslab.pixsee.pixm01:id/privacy_control_subtext"

		self.SDcard = "com.compal.bioslab.pixsee.pixm01:id/clSDCardStatus"
		self.SDcardStatustxt = "com.compal.bioslab.pixsee.pixm01:id/tvSDCardStatus"







	def is_in_settings(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.AreaDetection))
			)
			self.driver.find_element("id", self.AreaDetection)
			return True
		except :
			return False

	# click

	def click_back(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.backButton))
		)
		element = self.driver.find_element("id", self.backButton)
		element.click()
		time.sleep(1)

	def click_pixsee_profile(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.PixseeProfile))
		)
		element = self.driver.find_element("id", self.PixseeProfile)
		element.click()
		time.sleep(1)

	def click_wifi_settings(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.WifiSettings))
		)
		element = self.driver.find_element("id", self.WifiSettings)
		element.click()
		time.sleep(1)

	def click_pixsee_friends_detection(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.PixseeFriendsDetection))
		)
		element = self.driver.find_element("id", self.PixseeFriendsDetection)
		element.click()
		time.sleep(1)

	def click_environment_settings(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.EnvironmentSettings))
		)
		element = self.driver.find_element("id", self.EnvironmentSettings)
		element.click()
		time.sleep(1)

	def click_cry_detection(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.CryDetection))
		)
		element = self.driver.find_element("id", self.CryDetection)
		element.click()
		time.sleep(1)

	def click_area_detection(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.AreaDetection))
		)
		element = self.driver.find_element("id", self.AreaDetection)
		element.click()
		time.sleep(1)

	def click_covered_face_detection(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.CoveredFaceDetection))
		)
		element = self.driver.find_element("id", self.CoveredFaceDetection)
		element.click()
		time.sleep(1)

	def click_time_lapse_video(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.TimeLapseVideo))
		)
		element = self.driver.find_element("id", self.TimeLapseVideo)
		element.click()
		time.sleep(1)

	def click_voice_service(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.VoiceService))
		)
		element = self.driver.find_element("id", self.VoiceService)
		element.click()
		time.sleep(1)

	def click_shutter_sound_switch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.ShutterSoundSwitch))
		)
		element = self.driver.find_element("id", self.ShutterSoundSwitch)
		element.click()
		time.sleep(1)

	def click_led_indicator_switch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.LEDindicatorSwitch))
		)
		element = self.driver.find_element("id", self.LEDindicatorSwitch)
		element.click()
		time.sleep(1)

	def click_night_mode_switch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.NightModeSwitch))
		)
		element = self.driver.find_element("id", self.NightModeSwitch)
		element.click()
		time.sleep(1)

	def click_privacy_mode_switch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.PrivacySettingsSwitch))
		)
		element = self.driver.find_element("id", self.PrivacySettingsSwitch)
		element.click()
		time.sleep(1)

	def click_sd_card(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.SDcard))
		)
		element = self.driver.find_element("id", self.SDcard)
		element.click()
		time.sleep(1)

	# text
	def location_name_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.locationNametxt))
			)
			element = self.driver.find_element("id", self.locationNametxt)
			return element.text
		except :
			return None

	def profile_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.PixseeProfiletxt))
			)
			element = self.driver.find_element("id", self.PixseeProfiletxt)
			return element.text
		except :
			return None

	def wifi_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.WifiSettingstxt))
			)
			element = self.driver.find_element("id", self.WifiSettingstxt)
			return element.text
		except :
			return None

	def pixsee_friends_detection_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.PixseeFriendsDetectiontxt))
			)
			element = self.driver.find_element("id", self.PixseeFriendsDetectiontxt)
			return element.text
		except :
			return None

	def pixsee_friends_detection_status_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.PixseeFriendsDetectionStatus))
			)
			element = self.driver.find_element("id", self.PixseeFriendsDetectionStatus)
			return element.text
		except :
			return None

	def environment_settings_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.EnvironmentSettingstxt))
			)
			element = self.driver.find_element("id", self.EnvironmentSettingstxt)
			return element.text
		except :
			return None

	def environment_settings_status_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.EnvironmentSettingsStatus))
			)
			element = self.driver.find_element("id", self.EnvironmentSettingsStatus)
			return element.text
		except :
			return None

	def cry_detection_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.CryDetectiontxt))
			)
			element = self.driver.find_element("id", self.CryDetectiontxt)
			return element.text
		except :
			return None

	def cry_detection_status_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.CryDetectionStatus))
			)
			element = self.driver.find_element("id", self.CryDetectionStatus)
			return element.text
		except :
			return None

	def area_detection_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.AreaDetectiontxt))
			)
			element = self.driver.find_element("id", self.AreaDetectiontxt)
			return element.text
		except :
			return None

	def area_detection_status_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.AreaDetectionStatus))
			)
			element = self.driver.find_element("id", self.AreaDetectionStatus)
			return element.text
		except :
			return None

	def covered_face_detection_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.CoveredFaceDetectiontxt))
			)
			element = self.driver.find_element("id", self.CoveredFaceDetectiontxt)
			return element.text
		except :
			return None

	def covered_face_detection_status_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.CoveredFaceDetectionStatus))
			)
			element = self.driver.find_element("id", self.CoveredFaceDetectionStatus)
			return element.text
		except :
			return None

	def time_lapse_video_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TimeLapseVideotxt))
			)
			element = self.driver.find_element("id", self.TimeLapseVideotxt)
			return element.text
		except :
			return None

	def time_lapse_video_status_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TimeLapseVideoStatus))
			)
			element = self.driver.find_element("id", self.TimeLapseVideoStatus)
			return element.text
		except :
			return None

	def voice_service_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.VoiceServicetxt))
			)
			element = self.driver.find_element("id", self.VoiceServicetxt)
			return element.text
		except :
			return None

	def shutter_sound_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.ShutterSoundtxt))
			)
			element = self.driver.find_element("id", self.ShutterSoundtxt)
			return element.text
		except :
			return None

	def led_indicator_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.LEDindicatortxt))
			)
			element = self.driver.find_element("id", self.LEDindicatortxt)
			return element.text
		except :
			return None

	def night_mode_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.NightModetxt))
			)
			element = self.driver.find_element("id", self.NightModetxt)
			return element.text
		except :
			return None

	def night_mode_subtext(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.NightModeSubtext))
			)
			element = self.driver.find_element("id", self.NightModeSubtext)
			return element.text
		except :
			return None

	def privacy_mode_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.PrivacySettingstxt))
			)
			element = self.driver.find_element("id", self.PrivacySettingstxt)
			return element.text
		except :
			return None

	def privacy_mode_subtext(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.PrivacySettingsSubtext))
			)
			element = self.driver.find_element("id", self.PrivacySettingsSubtext)
			return element.text
		except :
			return None

	def sdcard_status_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.SDcardStatustxt))
			)
			element = self.driver.find_element("id", self.SDcardStatustxt)
			return element.text
		except :
			return None

	# switch
	def shutter_sound_switch_status(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.ShutterSoundSwitch))
			)
			element = self.driver.find_element("id", self.ShutterSoundSwitch)
			return element.get_attribute("checked") == "true"
		except :
			return None

	def led_indicator_switch_status(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.LEDindicatorSwitch))
			)
			element = self.driver.find_element("id", self.LEDindicatorSwitch)
			return element.get_attribute("checked") == "true"
		except :
			return None

	def night_mode_switch_status(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.NightModeSwitch))
			)
			element = self.driver.find_element("id", self.NightModeSwitch)
			return element.get_attribute("checked") == "true"
		except :
			return None

	def privacy_mode_switch_status(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.PrivacySettingsSwitch))
			)
			element = self.driver.find_element("id", self.PrivacySettingsSwitch)
			return element.get_attribute("checked") == "true"
		except :
			return None

	def is_cry_detection_able_to_click(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.CryDetection))
		)
		button = self.driver.find_element("id", self.CryDetection)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"

	def is_area_detection_able_to_click (self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.AreaDetection))
		)
		button = self.driver.find_element("id", self.AreaDetection)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"

	def is_covered_face_detection_able_to_click(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.CoveredFaceDetection))
		)
		button = self.driver.find_element("id", self.CoveredFaceDetection)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"

	def is_time_lapse_video_able_to_click(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.TimeLapseVideo))
		)
		button = self.driver.find_element("id", self.TimeLapseVideo)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"


