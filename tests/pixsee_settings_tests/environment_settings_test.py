from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from pages.menu_pages.menu_page import MenuPage
from pages.menu_pages.pixsee_settings_pages.pixsee_settings_page import PixseeSettingsPage
from pages.base import BaseTestCase
from pages.baby_monitor_page import BabyMonitorPage
from pages.login_page import LoginPage
from pages.menu_pages.pixsee_settings_pages.enviroment_settings_page import EnvironmentSettingsPage
import time
import re


class EnvironmentSettingsCase(BaseTestCase):
	def setUp(self):
		super().setUp(no_reset=True)

	# start from the Pixsee Settings page
	def test_01_environment_set_back(self):
			environment_settings_page = EnvironmentSettingsPage(self.driver)
			menu_page = MenuPage(self.driver)
			baby_monitor_page = BabyMonitorPage(self.driver)
			pixsee_settings_page = PixseeSettingsPage(self.driver)

			pixsee_settings_page.click_environment_settings()
			# back to settings page
			environment_settings_page.click_back()
			try:
				self.assertTrue(pixsee_settings_page.is_in_settings())
				print("Back to Pixsee Settings page")
			except AssertionError:
				raise AssertionError("Not in Pixsee Settings page")
	# start from the Pixsee Settings page
	def test_02_environment_set_save(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		origin_status = pixsee_settings_page.environment_settings_status_text()
		pixsee_settings_page.click_environment_settings()
		# check save enable = false
		try:
			self.assertFalse(environment_settings_page.is_save_enable())
			print("Save diable test pass")
		except AssertionError:
			raise AssertionError("Save disable test failed")

		# turn on switch
		environment_settings_page.click_switch()
		environment_settings_page.click_save()
		new_status = pixsee_settings_page.environment_settings_status_text()
		if origin_status != new_status:
			print("save function success")
		else:
			print("save function failed")
			raise AssertionError("save function failed, status not changed")
	# start from the Pixsee Settings page
	def test_03_environment_set_back_discard(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		origin_status = pixsee_settings_page.environment_settings_status_text()
		pixsee_settings_page.click_environment_settings()
		environment_settings_page.click_switch()
		environment_settings_page.click_back()
		# check if is in discard dialog
		try:
			self.assertTrue(environment_settings_page.is_in_discard_dialog())
			print("In discard dialog")
			# check discard dialog text
			try:
				discard = environment_settings_page.discard_message_text()
				hint = self.get_string("discard_environment_detection_confirmation_message")
				self.assertEqual(discard, hint)
			except AssertionError:
				raise AssertionError("Discard dialog title wrong")
			try:
				yes = environment_settings_page.discard_yes_text()
				hint = self.get_string("yes")
				self.assertEqual(yes, hint)
			except AssertionError:
				raise AssertionError("Discard dialog yes text wrong")
			try:
				no = environment_settings_page.discard_no_text()
				hint = self.get_string("no")
				self.assertEqual(no, hint)
			except AssertionError:
				raise AssertionError("Discard dialog no text wrong")
			# click yes
			environment_settings_page.click_discard_yes()
			new_status = pixsee_settings_page.environment_settings_status_text()
			try:
				self.assertEqual(origin_status, new_status)
			except AssertionError:
				raise AssertionError("Discard function failed, status changed")
		except AssertionError:
			print("Not in discard dialog")
			raise AssertionError("Not in discard dialog")
	# start from the Pixsee Settings page
	def test_04_environment_set_switch(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		pixsee_settings_page.click_environment_settings()
		# check header text
		try:
			header = environment_settings_page.header_text()
			hint = self.get_string("sensor_settings_toolbar_title")
			self.assertEqual(header, hint)
			print("Environment detection header text right")
		except AssertionError:
			raise AssertionError("Environment detection header text wrong")
		# check detection title
		try:
			title = environment_settings_page.detection_text()
			hint = self.get_string("detection")
			self.assertEqual(title, hint)
			print("Friends detection title right")
		except AssertionError:
			raise AssertionError("Friends detection title wrong")
		# switch status
		current_status = environment_settings_page.is_switch_on()
		self.check_switch_and_content(current_status, environment_settings_page.Sensitivity)
		environment_settings_page.click_switch()
		time.sleep(1)
		after_status = environment_settings_page.is_switch_on()
		self.check_switch_and_content(after_status, environment_settings_page.Sensitivity)
	# start from environment page
	def test_05_environment_set_tap_checkbox(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		# ensure switch is on
		if environment_settings_page.is_switch_on():
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
			raise AssertionError("Sensitivity title is wrong")
		try:
			temp = environment_settings_page.temperature_title_text()
			hint = self.get_string("temperature")
			self.assertEqual(temp, hint)
			print("Temperature title is correct")
		except AssertionError:
			raise AssertionError("Temperature title is wrong")
		try:
			temp_unit = environment_settings_page.temperature_subtitle_text()
			hint = self.get_string("temperature_unit_label")
			self.assertEqual(temp_unit, hint)
			print("Temperature unit title is correct")
		except AssertionError:
			raise AssertionError("Temperature unit title is wrong")
		try:
			humidity = environment_settings_page.humidity_text()
			hint = self.get_string("humidity")
			self.assertEqual(humidity, hint)
			print("Humidity title is correct")
		except AssertionError:
			raise AssertionError("Humidity title is wrong")
		# check box name
		try:
			low = environment_settings_page.low_text()
			hint = self.get_string("sensitivity_low")
			self.assertEqual(low, hint)
			print("Low checkbox text is correct")
		except AssertionError:
			raise AssertionError("Low checkbox text is wrong")
		try:
			medium = environment_settings_page.medium_text()
			hint = self.get_string("sensitivity_medium")
			self.assertEqual(medium, hint)
			print("Medium checkbox text is correct")
		except AssertionError:
			raise AssertionError("Medium checkbox text is wrong")
		try:
			high = environment_settings_page.high_text()
			hint = self.get_string("sensitivity_high")
			self.assertEqual(high, hint)
			print("High checkbox text is correct")
		except AssertionError:
			raise AssertionError("High checkbox text is wrong")
		# check clickable
		try:
			self.assertTrue(environment_settings_page.is_low_clickable())
			print("Low checkbox is clickable")
		except AssertionError:
			raise AssertionError("Low checkbox is not clickable")
		try:
			self.assertTrue(environment_settings_page.is_medium_clickable())
			print("Medium checkbox is clickable")
		except AssertionError:
			raise AssertionError("Medium checkbox is not clickable")
		try:
			self.assertTrue(environment_settings_page.is_high_clickable())
			print("High checkbox is clickable")
		except AssertionError:
			raise AssertionError("High checkbox is not clickable")
	# stay
	def test_06_environment_celsius_fahrenheit(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		if environment_settings_page.is_switch_on() :
			pass
		else:
			environment_settings_page.click_switch()
		try:
			celsius = environment_settings_page.celsius_text()
			hint = "℃"
			self.assertEqual(celsius, hint)
			print("Celsius text right")
		except AssertionError:
			raise AssertionError("Celsius text wrong")
		if environment_settings_page.temperature_min_text() == "10":
			# check celsius clickable
			try:
				self.assertEqual(environment_settings_page.temperature_max_text(), "35")
				print("Celsius is clickable")
			except AssertionError:
				raise AssertionError("Celsius is not clickable")
		else:
			try:
				fahrenheit = environment_settings_page.fahrenheit_text()
				hint = "℉"
				self.assertEqual(fahrenheit, hint)
				print("Fahrenheit text right")
			except AssertionError:
				raise AssertionError("Fahrenheit text wrong")
			# check fahrenheit clickable
			try:
				self.assertEqual(environment_settings_page.temperature_min_text(), "50")
				self.assertEqual(environment_settings_page.temperature_max_text(), "95")
				print("Fahrenheit is clickable")
			except AssertionError:
				raise AssertionError("Fahrenheit is not clickable")
		environment_settings_page.click_celsius()
		if environment_settings_page.temperature_min_text() == "10":
			# check celsius clickable
			try:
				self.assertEqual(environment_settings_page.temperature_max_text(), "35")
				print("Celsius is clickable")
			except AssertionError:
				raise AssertionError("Celsius is not clickable")
		else:
			# check fahrenheit clickable
			try:
				self.assertEqual(environment_settings_page.temperature_min_text(), "50")
				self.assertEqual(environment_settings_page.temperature_max_text(), "95")
				print("Fahrenheit is clickable")
			except AssertionError:
				raise AssertionError("Fahrenheit is not clickable")
	# stay
	def test_07_environment_set_temperature_scrolling_bar(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		if environment_settings_page.is_switch_on() :
			pass
		else:
			environment_settings_page.click_switch()
			# number before scrolling
			text_before = environment_settings_page.temperature_range_text()
			# find numbers in the text
			numbers_before = re.findall(r'\d+', text_before)
			# convert the found numbers str list to integers list
			numbers_before = list(map(int, numbers_before))
			print(numbers_before)
			highnum_before = numbers_before[1]
			lownum_before = numbers_before[0]

			# scroll
			finger = PointerInput(kind="touch", name="finger")
			action_builder = ActionBuilder(self.driver, mouse=finger)
			xy = environment_settings_page.temperature_bar_location()
			size = environment_settings_page.temperature_bar_size()
			size_height = size["height"] / 2
			y = xy["y"] + size_height  # Adjust y to the middle of the element
			x_start = xy["x"] + 10
			x_end = 300
			print(xy["x"], xy["y"])
			print(size)
			action_builder.pointer_action.move_to_location(x_start, y)
			action_builder.pointer_action.pointer_down()
			action_builder.pointer_action.pause(0.2)
			action_builder.pointer_action.move_to_location(x_end, y)
			action_builder.pointer_action.pointer_up()
			action_builder.perform()

			# number after scrolling
			text_after = environment_settings_page.temperature_range_text()  # 假設抓取的文字是 "Temperature range: ?-?℃"
			numbers_after = re.findall(r'\d+', text_after)
			numbers_after = list(map(int, numbers_after))
			print(numbers_after)
			highnum_after = numbers_after[1]
			lownum_after = numbers_after[0]

			# compare before and after values
			if highnum_after != highnum_before or lownum_after != lownum_before:
				print("Scrolling bar works")
			else:
				raise AssertionError("Scrolling bar doesn't work, values not changed")
	# stay
	def test_08_environment_set_humidity_scrolling_bar(self):
		environment_settings_page = EnvironmentSettingsPage(self.driver)
		menu_page = MenuPage(self.driver)
		baby_monitor_page = BabyMonitorPage(self.driver)
		pixsee_settings_page = PixseeSettingsPage(self.driver)

		# ensure switch is on
		if environment_settings_page.is_switch_on() :
			pass
		else:
			environment_settings_page.click_switch()
		# number before scrolling
		text_before = environment_settings_page.humidity_range_text()
		# find numbers in the text
		numbers_before = re.findall(r'\d+', text_before)
		# convert the found numbers str list to integers list
		numbers_before = list(map(int, numbers_before))
		highnum_before = numbers_before[1]
		lownum_before = numbers_before[0]

		# scroll
		finger = PointerInput(kind="touch", name="finger")
		action_builder = ActionBuilder(self.driver, mouse=finger)
		xy = environment_settings_page.humidity_bar_location()
		size = environment_settings_page.humidity_bar_size()
		size_height = size["height"] / 2
		y = xy["y"] + size_height  # Adjust y to the middle of the element
		x_start = xy["x"] + 10
		x_end = 300
		print(xy["x"], xy["y"])
		print(size)
		action_builder.pointer_action.move_to_location(x_start, y)
		action_builder.pointer_action.pointer_down()
		action_builder.pointer_action.pause(0.2)
		action_builder.pointer_action.move_to_location(x_end, y)
		action_builder.pointer_action.pointer_up()
		action_builder.perform()

		# number after scrolling
		text_after = environment_settings_page.humidity_range_text()
		numbers_after = re.findall(r'\d+', text_after)
		numbers_after = list(map(int, numbers_after))
		highnum_after = numbers_after[1]
		lownum_after = numbers_after[0]

		# compare before and after values
		if highnum_after != highnum_before or lownum_after != lownum_before:
			print("Scrolling bar works")
		else:
			raise AssertionError("Scrolling bar doesn't work, values not changed")
		environment_settings_page.click_back()
		environment_settings_page.click_discard_yes()
	# back to Pixsee Settings page




















