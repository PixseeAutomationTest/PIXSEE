from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages.base as base

from appium.webdriver.common.appiumby import AppiumBy

class MusicDollPlaylistPage:
	def __init__(self, driver):
		self.driver = driver

		self.albumBar = "com.compal.bioslab.pixsee.pixm01:id/header"
		self.musicList = "com.compal.bioslab.pixsee.pixm01:id/rv_dolls_musics"

		self.dollNameText = "com.compal.bioslab.pixsee.pixm01:id/tvCoverTitle"

		self.backButton = "com.compal.bioslab.pixsee.pixm01:id/ibBackToDollsHome"
		self.settingButton = "com.compal.bioslab.pixsee.pixm01:id/ib_doll_toolbar_settings"
		self.playAlbumButton = "com.compal.bioslab.pixsee.pixm01:id/btPlayAlbum"
		self.repeatButton = "com.compal.bioslab.pixsee.pixm01:id/ibRepeatAlbum"

		'''Music item'''
		self.musicItemBar = "com.compal.bioslab.pixsee.pixm01:id/clMusicItem"
		self.musicItemNameText = "com.compal.bioslab.pixsee.pixm01:id/tvContentPlayItemName"
		self.musicItemTotalTimeText = "com.compal.bioslab.pixsee.pixm01:id/tvContentPlayItemTime"
		self.musicItemCurrentTimeText = "com.compal.bioslab.pixsee.pixm01:id/tv_doll_media_item_elapsed_time"
		self.musicItemRemainTimeText = "com.compal.bioslab.pixsee.pixm01:id/tv_doll_media_item_remaining_time"
		self.musicItemPlayButton = "com.compal.bioslab.pixsee.pixm01:id/ib_doll_media_play"
		self.musicItemTimeSlider = "com.compal.bioslab.pixsee.pixm01:id/doll_media_item_slider"

	def click_back_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.backButton))
		)
		element = self.driver.find_element("id", self.backButton)
		element.click()

	def click_setting_button(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.settingButton))
		)
		element = self.driver.find_element("id", self.settingButton)
		element.click()

	def click_album_bar(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.albumBar))
		)
		element = self.driver.find_element("id", self.albumBar)
		element.click()

	def click_playAlbum_button(self):
		self.click_album_bar()
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.playAlbumButton))
		)
		element = self.driver.find_element("id", self.playAlbumButton)
		element.click()

	def click_repeat_button(self):
		self.click_album_bar()
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.repeatButton))
		)
		element = self.driver.find_element("id", self.repeatButton)
		element.click()

	def click_music_item_bar(self, index=0, fromBeginning = True):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.musicList))
		)
		if not fromBeginning:
			elements = self.driver.find_elements("id", self.musicItemBar)
			if index >= len(elements):
				raise ValueError("Index out of range for currently loaded music items.")
			elements[index].click()
		else:
			self.driver.find_element(
				AppiumBy.ANDROID_UIAUTOMATOR,
				f'new UiScrollable(new UiSelector().resourceId("{self.musicList}")).setAsVerticalList().scrollToBeginning(10)'
			)
			seen_music = []
			last = None
			while self.driver.find_element("id", self.musicItemBar) != last:
				all_items = self.driver.find_elements("id", self.musicItemBar)
				last = all_items[0]
				for item_bar in all_items:
					try:
						item_text = item_bar.find_element("id", self.musicItemNameText)
					except:
						continue
					if (item_text.text, item_bar) not in seen_music:
						seen_music.append((item_text.text, item_bar))
				if index < len(seen_music):
					seen_music[index][1].click()
					return
				self.driver.find_element(
					AppiumBy.ANDROID_UIAUTOMATOR,
					f'new UiScrollable(new UiSelector().resourceId("{self.musicList}")).setAsVerticalList().scrollForward()'
				)
			raise ValueError("Index out of range for music items.")

	def click_music_item_play_button(self, index=0, fromBeginning = True):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.musicList))
		)
		if not fromBeginning:
			elements = self.driver.find_elements("id", self.musicItemBar)
			if index >= len(elements):
				raise ValueError("Index out of range for currently loaded music items.")
			elements[index].click()
		else:
			self.driver.find_element(
				AppiumBy.ANDROID_UIAUTOMATOR,
				f'new UiScrollable(new UiSelector().resourceId("{self.musicList}")).setAsVerticalList().scrollToBeginning(10)'
			)
			seen_music = []
			last = None
			while self.driver.find_element("id", self.musicItemBar) != last:
				all_items = self.driver.find_elements("id", self.musicItemBar)
				last = all_items[0]
				for item_bar in all_items:
					try:
						item_text = item_bar.find_element("id", self.musicItemNameText)
					except:
						continue
					if (item_text.text, item_bar) not in seen_music:
						seen_music.append((item_text.text, item_bar))
				if index < len(seen_music):
					seen_music[index][1].find_element("id", self.musicItemPlayButton).click()
					return
				self.driver.find_element(
					AppiumBy.ANDROID_UIAUTOMATOR,
					f'new UiScrollable(new UiSelector().resourceId("{self.musicList}")).setAsVerticalList().scrollForward()'
				)
			raise ValueError("Index out of range for music items.")

	def get_doll_name_text(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.dollNameText))
		)
		element = self.driver.find_element("id", self.dollNameText)
		return element.text

	def get_music_item_name_text(self, index=0, fromBeginning = True): # 50 music items on 2025/8/22
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located(("id", self.musicList))
		)
		if not fromBeginning:
			elements = self.driver.find_elements("id", self.musicItemNameText)
			if index >= len(elements):
				raise ValueError("Index out of range for currently loaded music items.")
			return elements[index].text

		else:
			self.driver.find_element(
				AppiumBy.ANDROID_UIAUTOMATOR,
				f'new UiScrollable(new UiSelector().resourceId("{self.musicList}")).setAsVerticalList().scrollToBeginning(10)'
			)
			seen_music = []
			last = None
			while self.driver.find_element("id", self.musicItemNameText) != last:
				all_items = self.driver.find_elements("id", self.musicItemNameText)
				last = all_items[0]
				for item in all_items:
					if item.text not in seen_music:
						seen_music.append(item.text)
				if index < len(seen_music):
					return seen_music[index]
				self.driver.find_element(
					AppiumBy.ANDROID_UIAUTOMATOR,
					f'new UiScrollable(new UiSelector().resourceId("{self.musicList}")).setAsVerticalList().scrollForward()'
				)
			raise ValueError("Index out of range for music items.")

	def is_in_music_doll_playlist_page(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("id", self.musicList))
			)
			self.driver.find_element("id", self.musicList)
			if self.get_doll_name_text() not in ["Trunkee", "Bunee", "Monkee"]:
				return False
			return True
		except:
			return False



