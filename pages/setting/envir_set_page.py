from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PixseeFriendsEnvirPage():
	def __init__(self, driver):
		self.driver = driver
		self.Back = "com.compal.bioslab.pixsee.pixm01:id/ibSensorSettingsBack"
		self.Head = "com.compal.bioslab.pixsee.pixm01:id/textView5"
		self.Save = "com.compal.bioslab.pixsee.pixm01:id/tvSensorSettingsSave"
		self.Detection = "com.compal.bioslab.pixsee.pixm01:id/sensor_settings_status_text"
		self.Switch = "com.compal.bioslab.pixsee.pixm01:id/sensor_settings_status_switch"
		self.Sensitivity = "com.compal.bioslab.pixsee.pixm01:id/type_detection_section"
		self.Low = "com.compal.bioslab.pixsee.pixm01:id/rb_low_radio_txt"
		self.LowCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_low_radio"
		self.Medium = "com.compal.bioslab.pixsee.pixm01:id/rb_medium_radio_txt"
		self.MediumCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_medium_radio"
		self.High = "com.compal.bioslab.pixsee.pixm01:id/rb_high_radio_txt"
		self.HighCheckBox = "com.compal.bioslab.pixsee.pixm01:id/rb_high_radio"
		self.TemperatureTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTemperatureLabelSection"
		self.TemperatureSubTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTemperatureUnit"
		self.TemperatureRange = "com.compal.bioslab.pixsee.pixm01:id/tvTemperatureRangeLabel"
		self.TemperatureSwitch = "com.compal.bioslab.pixsee.pixm01:id/switchCompat"
		self.TemperatureMin = "com.compal.bioslab.pixsee.pixm01:id/tvMinTemperatureValue"
		self.TempaeratureMax = "com.compal.bioslab.pixsee.pixm01:id/tvMaxTemperatureValue"
		self.TemperatureBar = "com.compal.bioslab.pixsee.pixm01:id/sbTemperatureRange"
		self.Humidity = "com.compal.bioslab.pixsee.pixm01:id/tvHumidityRangeLabel"
		self.HumidityRange = "com.compal.bioslab.pixsee.pixm01:id/tvHumidityBestRange"
		self.HumidityMin = "com.compal.bioslab.pixsee.pixm01:id/tvMinHumidityValue"
		self.HumidityMax = "com.compal.bioslab.pixsee.pixm01:id/tvMaxHumidityValue"
		self.HumidityBar = "com.compal.bioslab.pixsee.pixm01:id/sbHumidityRange"


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
	def click_temperature_switch(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.TemperatureSwitch))
		)
		element = self.driver.find_element("id", self.TemperatureSwitch)
		element.click()

	def is_in_envir_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Head))
			)
			return True
		except:
			return False







