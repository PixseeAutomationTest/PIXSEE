from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PixseeSettingsPage():
	def __init__(self, driver):
		self.driver = driver

		self.PixseeProfile = "com.compal.bioslab.pixsee.pixm01:id/clProfileSettings"
		self.PixseeProfiletxt = "com.compal.bioslab.pixsee.pixm01:id/tvProfileSettings"
		self.WifiSettings = "com.compal.bioslab.pixsee.pixm01:id/clWifiSettings"
		self.WifiSettingstxt = "com.compal.bioslab.pixsee.pixm01:id/tvWifiSettings"
		self.PixseeFriendsDetection = "com.compal.bioslab.pixsee.pixm01:id/clPixseeFriendsDetection"
		self.FixseeFriendsDetectiontxt = "com.compal.bioslab.pixsee.pixm01:id/tvPixseeFriendsDetection"
		self.EviromentSettings = "com.compal.bioslab.pixsee.pixm01:id/clEnvironmentDetection"
		self.EviromentSettingstxt = "com.compal.bioslab.pixsee.pixm01:id/tvEnvironmentDetection"
		self.CryDetection = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_crying_container"
		self.CryDetectiontxt = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_crying_label"
		self.AreaDetection = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_efence_container"
		self.AreaDetectiontxt = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_efence_label"
		self.CoveredFaceDetection = "com.compal.bioslab.pixsee.pixm01:id/cover_detection_settings_container"
		self.CoveredFaceDetectiontxt = "com.compal.bioslab.pixsee.pixm01:id/cover_detection_settings_label"
		self.TimeLapseVideo = "com.compal.bioslab.pixsee.pixm01:id/cover_detection_settings_container"
		self.TimeLapseVideotxt = "com.compal.bioslab.pixsee.pixm01:id/cover_detection_settings_label"
		self.VoiceService = "com.compal.bioslab.pixsee.pixm01:id/clVoiceCommand"
		self.VoiceServicetxt = "com.compal.bioslab.pixsee.pixm01:id/tvVoiceCommand"
		self.ShutterSoundSwitch = "com.compal.bioslab.pixsee.pixm01:id/capture_sound_switch"
		self.ShutterSoundTitle = "com.compal.bioslab.pixsee.pixm01:id/clCaptureSound"
		self.ShutterSoundtxt = "com.compal.bioslab.pixsee.pixm01:id/tvCaptureSound"
		self.LEDindicatorSwitch = "com.compal.bioslab.pixsee.pixm01:id/led_switch"
		self.LEDindicatorTitle = "com.compal.bioslab.pixsee.pixm01:id/clIndicatorLed"
		self.LEDindicatortxt = "com.compal.bioslab.pixsee.pixm01:id/tvIndicatorLedSettings"
		self.NightModeSwitch = "com.compal.bioslab.pixsee.pixm01:id/night_vision_switch"
		self.NightModeTitle = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_night_vision_label"
		self.NightModetxt = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_night_vision_text"
		self.NightModeSubtext = "com.compal.bioslab.pixsee.pixm01:id/detection_settings_night_vision_subtitle"
		self.PrivacySettingsSwitch = "com.compal.bioslab.pixsee.pixm01:id/privacy_control_switch"
		self.PrivacySettingsTitle = "com.compal.bioslab.pixsee.pixm01:id/privacy_control_label"
		self.PrivacySettingstxt = "com.compal.bioslab.pixsee.pixm01:id/privacy_control_text"
		self.PrivacySettingsSubtext = "com.compal.bioslab.pixsee.pixm01:id/privacy_control_subtitle"
		self.SDcardStatus = "com.compal.bioslab.pixsee.pixm01:id/clSDCardStatus"
		self.SDcardStatustxt = "com.compal.bioslab.pixsee.pixm01:id/tvSDCardStatus"
		self.in_settings = "com.compal.bioslab.pixsee.pixm01:id/tvRoomName"

	def is_in_settings(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.in_settings))
			)
			element = self.driver.find_element("id", self.in_settings)
			return True
		except:
			return False

	def click_PixseeProfile(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.PixseeProfile))
		)
		element = self.driver.find_element("id", self.PixseeProfile)
		element.click()
		time.sleep(1)

	def click_WifiSettings(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.WifiSettings))
		)
		element = self.driver.find_element("id", self.WifiSettings)
		element.click()
		time.sleep(1)

	def click_PixseeFriendsDetection(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.PixseeFriendsDetection))
		)
		element = self.driver.find_element("id", self.PixseeFriendsDetection)
		element.click()
		time.sleep(1)

	def click_EviromentSettings(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.EviromentSettings))
		)
		element = self.driver.find_element("id", self.EviromentSettings)
		element.click()
		time.sleep(1)

	def click_CryDetection(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.CryDetection))
		)
		element = self.driver.find_element("id", self.CryDetection)
		element.click()
		time.sleep(1)

	def click_AreaDetection(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.AreaDetection))
		)
		element = self.driver.find_element("id", self.AreaDetection)
		element.click()
		time.sleep(1)

	def click_CoveredFaceDetection(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.CoveredFaceDetection))
		)
		element = self.driver.find_element("id", self.CoveredFaceDetection)
		element.click()
		time.sleep(1)

	def click_TimeLapseVideo(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.TimeLapseVideo))
		)
		element = self.driver.find_element("id", self.TimeLapseVideo)
		element.click()
		time.sleep(1)

	def click_VoiceService(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.VoiceService))
		)
		element = self.driver.find_element("id", self.VoiceService)
		element.click()
		time.sleep(1)

	def click_ShutterSoundSwitch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.ShutterSoundSwitch))
		)
		element = self.driver.find_element("id", self.ShutterSoundSwitch)
		element.click()
		time.sleep(1)

	def click_LEDindicatorSwitch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.LEDindicatorSwitch))
		)
		element = self.driver.find_element("id", self.LEDindicatorSwitch)
		element.click()
		time.sleep(1)

	def click_NightModeSwitch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.NightModeSwitch))
		)
		element = self.driver.find_element("id", self.NightModeSwitch)
		element.click()
		time.sleep(1)

	def click_PrivacySettingsSwitch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.PrivacySettingsSwitch))
		)
		element = self.driver.find_element("id", self.PrivacySettingsSwitch)
		element.click()
		time.sleep(1)

	def SDcardStatus(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.SDcardStatus))
		)
		element = self.driver.find_element("id", self.SDcardStatus)
		element.click()
		time.sleep(1)



