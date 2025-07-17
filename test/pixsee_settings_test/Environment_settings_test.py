

from pages.menu_page import MenuPage
from pages.pixsee_settings.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.pixsee_settings.enviroment_settings_page import EnvironmentSettingsPage





class EnvironmentSettingsCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=False)
	def test_01_environment_set_switch(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(),self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		pixsee_settings_page.click_EnvironmentSettings()
		# check detection title
		try:
			title = environment_settings_page.detection_text()
			hint = self.get_string("pixsee_environment_set_title")
			self.assertEqual(title, hint)
			print("Friends detection title right")
		except AssertionError:
			print("Friends detection title wrong")
			raise AssertionError("Friends detection title mismatch")
		# switch status
		current_status = environment_settings_page.is_switch_on()
		self.check_switch_and_content(current_status, environment_settings_page.Sensitivity)
		environment_settings_page.click_switch()
		after_status = environment_settings_page.is_switch_on()
		self.check_switch_and_content(after_status, environment_settings_page.Sensitivity)
	def test_02_environment_set_save(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()

		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		origin_status = pixsee_settings_page.environment_settings_status_text()
		pixsee_settings_page.click_EnvironmentSettings()
		# turn on switch
		environment_settings_page.click_switch()
		environment_settings_page.click_save()
		new_status = pixsee_settings_page.environment_settings_status_text()
		if origin_status != new_status:
			print("save function success")
		else:
			print("save function failed")
			raise AssertionError("save function failed, status not changed")
	def test_03_environment_set_back(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()

		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		pixsee_settings_page.click_EnvironmentSettings()
		# back to settings page
		environment_settings_page.click_back()
		try:
			self.assertTrue(pixsee_settings_page.is_in_settings())
			print("Back to Pixsee Settings page")
		except AssertionError:
			print("Not in Pixsee Settings page")
			raise AssertionError("Not in Pixsee Settings page")
	def test_04_environment_set_tap_checkbox(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		pixsee_settings_page.click_EnvironmentSettings()
		# ensure switch is on
		if environment_settings_page.is_switch_on() == "true":
			pass
		else:
			environment_settings_page.click_switch()
		# check group titles
		try:
			sensitivity = environment_settings_page.sensitivity_text()
			hint = self.get_string("sensitivity_level")
			self.assertEqual(sensitivity, hint)
			print("Sensitivity title is correct")
		except AssertionError:
			print("Sensitivity title is wrong")
			raise AssertionError("sensitivity doesn't show up after switch on")
		try:
			temp = environment_settings_page.temperature_title_text()
			hint = self.get_string("temperature")
			self.assertEqual(temp, hint)
			print("Temperature title is correct")
		except AssertionError:
			print("Temperature title is wrong")
			raise AssertionError("temperature doesn't show up after switch on")
		try:
			temp_unit = environment_settings_page.temperature_subtitle_text()
			hint = self.get_string("temperature_unit_label")
			self.assertEqual(temp_unit, hint)
			print("Temperature unit title is correct")
		except AssertionError:
			print("Temperature unit title is wrong")
			raise AssertionError("temperature unit doesn't show up after switch on")
		try:
			humidity = environment_settings_page.humidity_text()
			hint = self.get_string("humidity")
			self.assertEqual(humidity, hint)
			print("Humidity title is correct")
		except AssertionError:
			print("Humidity title is wrong")
			raise AssertionError("humidity doesn't show up after switch on")
		# check box name
		try:
			low = environment_settings_page.low_text()
			hint = self.get_string("sensitivity_low")
			self.assertEqual(low, hint)
			print("Low checkbox text is correct")
		except AssertionError:
			print("Low checkbox text is wrong")
			raise AssertionError("low checkbox text mismatch")
		try:
			medium = environment_settings_page.medium_text()
			hint = self.get_string("sensitivity_medium")
			self.assertEqual(medium, hint)
			print("Medium checkbox text is correct")
		except AssertionError:
			print("Medium checkbox text is wrong")
			raise AssertionError("medium checkbox text mismatch")
		try:
			high = environment_settings_page.high_text()
			hint = self.get_string("sensitivity_high")
			self.assertEqual(high, hint)
			print("High checkbox text is correct")
		except AssertionError:
			print("High checkbox text is wrong")
			raise AssertionError("high checkbox text mismatch")
		# check clickable
		try:
			self.assertTrue(environment_settings_page.is_low_clickable())
			print("Low checkbox is clickable")
		except AssertionError:
			print("Low checkbox is not clickable")
			raise AssertionError("Low checkbox is not clickable")
		try:
			self.assertTrue(environment_settings_page.is_medium_clickable())
			print("Medium checkbox is clickable")
		except AssertionError:
			print("Medium checkbox is not clickable")
			raise AssertionError("Medium checkbox is not clickable")
		try:
			self.assertTrue(environment_settings_page.is_high_clickable())
			print("High checkbox is clickable")
		except AssertionError:
			print("High checkbox is not clickable")
			raise AssertionError("High checkbox is not clickable")
	def test_05_environment_celsius_fahrenheit(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()

		menu_page.click_settings()

		pixsee_settings_page.click_EnvironmentSettings()
		if environment_settings_page.is_switch_on() == "true":
			pass
		else:
			environment_settings_page.click_switch()
		# check celsius and fahrenheit text
		try:
			celsius = environment_settings_page.celsius_text()
			hint = "°C"
			self.assertEqual(celsius, hint)
			print("Celsius text right")
		except AssertionError:
			print("Celsius text wrong")
			raise AssertionError("Celsius text mismatch")
		try:
			fahrenheit = environment_settings_page.fahrenheit_text()
			hint = "°F"
			self.assertEqual(fahrenheit, hint)
			print("Fahrenheit text right")
		except AssertionError:
			print("Fahrenheit text wrong")
			raise AssertionError("Fahrenheit text mismatch")
		# check celsius clickable
		try:
			environment_settings_page.click_celsius()
			self.assertEqual(environment_settings_page.temperature_min_text(),"10")
			self.assertEqual(environment_settings_page.temperature_max_text(),"35")
			print("Celsius is clickable")
		except AssertionError:
			print("Celsius is not clickable")
			raise AssertionError("Celsius is not clickable")
		# check fahrenheit clickable
		try:
			environment_settings_page.click_fahrenheit()
			self.assertEqual(environment_settings_page.temperature_min_text(), "50")
			self.assertEqual(environment_settings_page.temperature_max_text(), "95")
			print("Fahrenheit is clickable")
		except AssertionError:
			print("Fahrenheit is not clickable")
			raise AssertionError("Fahrenheit is not clickable")
	def test_06_environment_set_back_discard(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)
		login_page = LoginPage(self.driver)

		login_page.login(self.account(), self.password())
		baby_monitor_page.is_in_baby_monitor_page()
		baby_monitor_page.skip_first_four_tutor()
		baby_monitor_page.click_home()
		# skip menu tutor
		self.click_middle()
		menu_page.click_settings()
		origin_status = pixsee_settings_page.environment_settings_status_text()
		pixsee_settings_page.click_EnvironmentSettings()
		environment_settings_page.click_switch()
		environment_settings_page.click_back()
		# check if is in discard dialog
		try:
			self.assertTrue(environment_settings_page.is_in_discard_dialog())
			print("In discard dialog")
			# check discard dialog text
			try:
				discard = environment_settings_page.discard_message_txt()
				hint = self.get_string("pixsee_environment_set_popup_discard_changes")
				self.assertEqual(discard, hint)
				print("Discard dialog title right")
			except AssertionError:
				print("Discard dialog title wrong")
				raise AssertionError("Discard dialog title mismatch")
			try:
				yes = environment_settings_page.discard_yes_txt()
				hint = self.get_string("yes")
				self.assertEqual(yes, hint)
				print("Discard dialog yes text right")
			except AssertionError:
				print("Discard dialog yes text wrong")
				raise AssertionError("Discard dialog yes text mismatch")
			try:
				no = environment_settings_page.discard_no_txt()
				hint = self.get_string("no")
				self.assertEqual(no, hint)
				print("Discard dialog no text right")
			except AssertionError:
				print("Discard dialog no text wrong")
				raise AssertionError("Discard dialog no text mismatch")
			# click yes
			environment_settings_page.click_discard_yes()
			new_status = pixsee_settings_page.pixsee_environment_set_status_text()
			try:
				self.assertEqual(origin_status, new_status)
				print("Discard function success")
			except AssertionError:
				print("Discard function failed")
				raise AssertionError("Discard function failed, status changed")
		except AssertionError:
			print("Not in discard dialog")
			raise AssertionError("Not in discard dialog")




















