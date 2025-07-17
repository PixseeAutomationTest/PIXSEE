from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VoiceServicePage():
	def __init__(self, driver):
		self.driver = driver
		self.Back = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back"
		self.Header = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
		self.Save = "com.compal.bioslab.pixsee.pixm01:id/toolbar_save"
		self.Detection = "com.compal.bioslab.pixsee.pixm01:id/cl_voice_command_detection_label"
		self.DetectionSwitch = "com.compal.bioslab.pixsee.pixm01:id/switchVoiceService"
		self.Language = "com.compal.bioslab.pixsee.pixm01:id/tvLanguage"
		self.EnglishCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_voice_command_language_english"
		self.ChineseCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_voice_command_language_chinese"
		self.EnglishText = "com.compal.bioslab.pixsee.pixm01:id/rb_voice_command_language_english_txt"
		self.ChineseText = "com.compal.bioslab.pixsee.pixm01:id/rb_voice_command_language_chinese_txt"

