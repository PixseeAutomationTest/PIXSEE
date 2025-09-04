import re

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import base as base
import datetime


class PhotoPage():
	def __init__(self, driver):
		self.driver = driver
		self.Eye = "com.compal.bioslab.pixsee.pixm01:id/ibGalleryMediaFullscreenHide"
		self.UserName = "com.compal.bioslab.pixsee.pixm01:id/tvParentGalleryMediaFullAct"
		self.NoteText = "com.compal.bioslab.pixsee.pixm01:id/tvNoteGalleryMediaFullAct"
		self.Trash = "com.compal.bioslab.pixsee.pixm01:id/ibDeleteGalleryMediaFullAct"
		self.Share = "com.compal.bioslab.pixsee.pixm01:id/ibShareGalleryMediaFullAct"
		self.Download = "com.compal.bioslab.pixsee.pixm01:id/ibSaveGalleryMediaFullAct"
		self.NoteButton = "com.compal.bioslab.pixsee.pixm01:id/ibNoteGalleryMediaFullAct"
		self.Time = "com.compal.bioslab.pixsee.pixm01:id/tvDateGalleryMediaFullAct"
		self.Dialog = "com.compal.bioslab.pixsee.pixm01:id/tvTitleDialog"
		self.Dialog_Delete = "com.compal.bioslab.pixsee.pixm01:id/btnDelete"
		self.Dialog_Cancel = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeDialog"
		self.ChartCount = "com.compal.bioslab.pixsee.pixm01:id/tvMediaNoteCharCount"
		self.NoteInput = "com.compal.bioslab.pixsee.pixm01:id/etNoteAreaDialog"
		self.DiaryHead = "com.compal.bioslab.pixsee.pixm01:id/textView"
		self.CompleteButton = "com.compal.bioslab.pixsee.pixm01:id/ibConfirmMediaNoteEdit"

	def get_note_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.NoteText))
		)
		element = self.driver.find_element(AppiumBy.ID, self.NoteText)
		return element.text
	def get_time_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Time))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Time)
		return element.text
	def get_dialog_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Dialog))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Dialog)
		return element.text
	def dialog_delete_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Dialog_Delete))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Dialog_Delete)
		return element.text
	def dialog_cancel_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Dialog_Cancel))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Dialog_Cancel)
		return element.text
	def get_chart_count(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.ChartCount))
		)
		element = self.driver.find_element(AppiumBy.ID, self.ChartCount)
		return element.text
	def get_diary_head(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DiaryHead))
		)
		element = self.driver.find_element(AppiumBy.ID, self.DiaryHead)
		return element.text
	def complete_button_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.CompleteButton))
		)
		element = self.driver.find_element(AppiumBy.ID, self.CompleteButton)
		return element.text
	def note_input_hint(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.NoteInput))
		)
		element = self.driver.find_element(AppiumBy.ID, self.NoteInput)
		return element.get_attribute("text")


	def input_note(self, note):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.NoteInput))
		)
		element = self.driver.find_element(AppiumBy.ID, self.NoteInput)
		element.clear()
		element.send_keys(note)
		time.sleep(1)

	def find_numbers_in_text(self, text):
		# find numbers in the text
		numbers = re.findall(r"[\d.]+", text)
		if len(numbers) >= 2:
			used = int(numbers[0])  # first number
			total = int(numbers[1])  # second number
			return used,total
		else:
			num = int(numbers[0])  # if only one number is found
			return num

	def click_trash(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Trash))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Trash)
		element.click()
		time.sleep(1)
	def click_eye(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Eye))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Eye)
		element.click()
		time.sleep(1)
	def click_share(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Share))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Share)
		element.click()
		time.sleep(1)
	def click_download(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Download))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Download)
		element.click()
		time.sleep(1)
	def click_note(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.NoteButton))
		)
		element = self.driver.find_element(AppiumBy.ID, self.NoteButton)
		element.click()
		time.sleep(1)
	def click_dialog_delete(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Dialog_Delete))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Dialog_Delete)
		element.click()
		time.sleep(1)
	def click_dialog_cancel(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Dialog_Cancel))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Dialog_Cancel)
		element.click()
		time.sleep(1)
	def click_complete(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.CompleteButton))
		)
		element = self.driver.find_element(AppiumBy.ID, self.CompleteButton)
		element.click()
		time.sleep(1)

	def is_in_photo_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((AppiumBy.ID, self.Time))
			)
			return True
		except:
			return False
