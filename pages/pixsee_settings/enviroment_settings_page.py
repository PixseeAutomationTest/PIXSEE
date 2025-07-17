from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class EnvironmentSettingsPage():
	def __init__(self, driver):
		self.driver = driver
		self.Back = "com.compal.bioslab.pixsee.pixm01:id/ibSensorSettingsBack"
		self.Header = "com.compal.bioslab.pixsee.pixm01:id/textView5"
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
		self.Celsius = "com.compal.bioslab.pixsee.pixm01:id/tvCelsiusTemperature"
		self.Fahrenheit = "com.compal.bioslab.pixsee.pixm01:id/tvFahrenheitTemperature"
		self.DiscardTitle = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"

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
	def click_celsius(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.Celsius))
		)
		element = self.driver.find_element("id", self.Celsius)
		element.click()
	def click_fahrenheit(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located(("id", self.Fahrenheit))
		)
		element = self.driver.find_element("id", self.Fahrenheit)
		element.click()

	def header_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			element = self.driver.find_element("id", self.Header)
			return element.text
		except:
			return None
	def detection_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Detection))
			)
			element = self.driver.find_element("id", self.Detection)
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
	def temperature_title_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TemperatureTitle))
			)
			element = self.driver.find_element("id", self.TemperatureTitle)
			return element.text
		except:
			return None
	def temperature_subtitle_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TemperatureSubTitle))
			)
			element = self.driver.find_element("id", self.TemperatureSubTitle)
			return element.text
		except:
			return None
	def temperature_range_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TemperatureRange))
			)
			element = self.driver.find_element("id", self.TemperatureRange)
			return element.text
		except:
			return None
	def humidity_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Humidity))
			)
			element = self.driver.find_element("id", self.Humidity)
			return element.text
		except:
			return None
	def humidity_range_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.HumidityRange))
			)
			element = self.driver.find_element("id", self.HumidityRange)
			return element.text
		except:
			return None
	def temperature_min_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TemperatureMin))
			)
			element = self.driver.find_element("id", self.TemperatureMin)
			return element.text
		except:
			return None
	def temperature_max_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.TempaeratureMax))
			)
			element = self.driver.find_element("id", self.TempaeratureMax)
			return element.text
		except:
			return None
	def humidity_min_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.HumidityMin))
			)
			element = self.driver.find_element("id", self.HumidityMin)
			return element.text
		except:
			return None
	def humidity_max_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.HumidityMax))
			)
			element = self.driver.find_element("id", self.HumidityMax)
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
	def celsius_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Celsius))
			)
			element = self.driver.find_element("id", self.Celsius)
			return element.text
		except:
			return None
	def fahrenheit_text(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Fahrenheit))
			)
			element = self.driver.find_element("id", self.Fahrenheit)
			return element.text
		except:
			return None





	def is_in_envir_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.Header))
			)
			return True
		except:
			return False
	def is_switch_on(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Sensitivity))
		)
		switch = self.driver.find_element(AppiumBy.ID, self.Sensitivity)
		return switch.get_attribute("checked") == "true"
	def is_in_discard_dialog(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(("id", self.DiscardTitle))
			)
			return True
		except:
			return False


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







