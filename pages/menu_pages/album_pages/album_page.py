
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import base as base
import datetime


class AlbumPage():
	def __init__(self, driver):
		self.driver = driver
		self.NewFuncTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
		self.NewFuncMsg = "com.compal.bioslab.pixsee.pixm01:id/tvBottomMessage"
		self.iknowButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositive"
		self.TutorTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
		self.TutorDescription = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
		self.Calendar = "com.compal.bioslab.pixsee.pixm01:id/ibDailyCoverGalleryCalendar"
		self.UplayerBack = "com.compal.bioslab.pixsee.pixm01:id/toolbar"
		self.BackButton = "//android.widget.ImageButton"
		'''Select Mode'''
		self.Select = "com.compal.bioslab.pixsee.pixm01:id/ibSelectMode"
		self.Header = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
		self.SelectCancel = "com.compal.bioslab.pixsee.pixm01:id/tv_daily_cover_gallery_cancel"
		self.Garbage = "com.compal.bioslab.pixsee.pixm01:id/toolbar_delete_img"
		self.Share = "com.compal.bioslab.pixsee.pixm01:id/toolbar_share_img"
		self.Download = "com.compal.bioslab.pixsee.pixm01:id/toolbar_save_img"
		self.Visible = "com.compal.bioslab.pixsee.pixm01:id/toolbar_view_img"
		self.DownloadSuccess = "com.compal.bioslab.pixsee.pixm01:id/tvSnackbarToastLabel"
		self.ChooserHeader = "android:id/chooser_header"
		self.HiddenPhoto = "com.compal.bioslab.pixsee.pixm01:id/photo_hidden"
		self.Eye = "//android.widget.ImageView"
		'''Plus Button'''
		self.PlusButton = "com.compal.bioslab.pixsee.pixm01:id/fab_daily_cover_gallery_menu"
		self.SlideButton = "com.compal.bioslab.pixsee.pixm01:id/fab_daily_cover_gallery_slideshow"
		self.SlideButtonText = "com.compal.bioslab.pixsee.pixm01:id/tv_daily_cover_gallery_fab_slideshow"
		self.PhotoButton = "com.compal.bioslab.pixsee.pixm01:id/fab_daily_cover_gallery_menu"
		self.PhotoButtonText = "com.compal.bioslab.pixsee.pixm01:id/tv_daily_cover_gallery_fab_photo"
		self.Dialog ="com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
		self.DialogYes = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
		self.DialogNo = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeAlertDialog"
		'''Calendar'''
		self.calendar = "android:id/content"
		self.calendarScrollableList_classname = "android.widget.ListView"
		self.calendarYearPicker = "com.compal.bioslab.pixsee.pixm01:id/date_picker_year"
		self.calendarMonthPicker = "com.compal.bioslab.pixsee.pixm01:id/date_picker_month"
		self.calendarDayPicker = "com.compal.bioslab.pixsee.pixm01:id/date_picker_day"
		self.calendarOneMonth_xpath = "//android.widget.ListView/android.view.View"
		self.calendarOneDay_classname = "android.view.View"
		self.calendarDoneButton = "com.compal.bioslab.pixsee.pixm01:id/done_button"
		self.calendarCancelButton = "com.compal.bioslab.pixsee.pixm01:id/cancel_button"

		self.gallery_thumbnail = "com.compal.bioslab.pixsee.pixm01:id/gallery_thumbnail"

	def new_function_title(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.NewFuncTitle))
		)
		element = self.driver.find_element(AppiumBy.ID, self.NewFuncTitle)
		return element.text
	def new_function_msg(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.NewFuncMsg))
		)
		element = self.driver.find_element(AppiumBy.ID, self.NewFuncMsg)
		return element.text
	def iknow_button_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.iknowButton))
		)
		element = self.driver.find_element(AppiumBy.ID, self.iknowButton)
		return element.text
	def tutor_title(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TutorTitle))
		)
		element = self.driver.find_element(AppiumBy.ID, self.TutorTitle)
		return element.text
	def tutor_description(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.TutorDescription))
		)
		element = self.driver.find_element(AppiumBy.ID, self.TutorDescription)
		return element.text
	def header_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Header))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Header)
		return element.text
	def select_cancel_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.SelectCancel))
		)
		element = self.driver.find_element(AppiumBy.ID, self.SelectCancel)
		return element.text
	def slide_button_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.SlideButtonText))
		)
		element = self.driver.find_element(AppiumBy.ID, self.SlideButtonText)
		return element.text
	def photo_button_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.PhotoButtonText))
		)
		element = self.driver.find_element(AppiumBy.ID, self.PhotoButtonText)
		return element.text
	def dialog_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Dialog))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Dialog)
		return element.text
	def dialog_yes_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DialogYes))
		)
		element = self.driver.find_element(AppiumBy.ID, self.DialogYes)
		return element.text
	def dialog_no_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DialogNo))
		)
		element = self.driver.find_element(AppiumBy.ID, self.DialogNo)
		return element.text
	def download_success_text(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DownloadSuccess))
		)
		element = self.driver.find_element(AppiumBy.ID, self.DownloadSuccess)
		return element.text

	def click_iknow_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.iknowButton))
		)
		element = self.driver.find_element(AppiumBy.ID, self.iknowButton)
		element.click()
		time.sleep(1)
	def click_calendar_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Calendar))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Calendar)
		element.click()
		time.sleep(1)
	def click_select_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Select))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Select)
		element.click()
		time.sleep(1)
	def click_select_cancel(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.SelectCancel))
		)
		element = self.driver.find_element(AppiumBy.ID, self.SelectCancel)
		element.click()
		time.sleep(1)
	def click_plus_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.PlusButton))
		)
		element = self.driver.find_element(AppiumBy.ID, self.PlusButton)
		element.click()
		time.sleep(1)
	def click_slide_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.SlideButton))
		)
		element = self.driver.find_element(AppiumBy.ID, self.SlideButton)
		element.click()
		time.sleep(1)
	def click_photo_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.PhotoButton))
		)
		element = self.driver.find_element(AppiumBy.ID, self.PhotoButton)
		element.click()
		time.sleep(1)
	def click_dialog_yes(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DialogYes))
		)
		element = self.driver.find_element(AppiumBy.ID, self.DialogYes)
		element.click()
		time.sleep(1)
	def click_dialog_no(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.DialogNo))
		)
		element = self.driver.find_element(AppiumBy.ID, self.DialogNo)
		element.click()
		time.sleep(1)
	def click_garbage_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Garbage))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Garbage)
		element.click()
		time.sleep(1)
	def click_share_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Share))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Share)
		element.click()
		time.sleep(1)
	def click_download_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Download))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Download)
		element.click()
		time.sleep(1)
	def click_visible_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Visible))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Visible)
		element.click()
		time.sleep(1)
	def click_back_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.UplayerBack))
		)
		uplayer = self.driver.find_element(AppiumBy.ID, self.UplayerBack)
		element = uplayer.find_element("xpath", self.BackButton)
		element.click()
		time.sleep(1)

	def is_in_album_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((AppiumBy.ID, self.Calendar))
			)
			return True
		except:
			return False
	def is_in_select_mode(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((AppiumBy.ID, self.SelectCancel))
			)
			return True
		except:
			return False
	def is_in_dialog(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((AppiumBy.ID, self.Dialog))
			)
			return True
		except:
			return False

	def is_garbage_enabled(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Garbage))
		)
		button = self.driver.find_element(AppiumBy.ID, self.Garbage)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"
	def is_share_enabled(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Share))
		)
		button = self.driver.find_element(AppiumBy.ID, self.Share)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"
	def is_download_enabled(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Download))
		)
		button = self.driver.find_element(AppiumBy.ID, self.Download)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"
	def is_visible_enabled(self):
		WebDriverWait(self.driver, base.wait_time).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Visible))
		)
		button = self.driver.find_element(AppiumBy.ID, self.Visible)
		is_enable = button.get_attribute("enabled")
		return is_enable == "true"
	def is_chooser_appeared(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located((AppiumBy.ID, self.ChooserHeader))
			)
			self.driver.find_element(AppiumBy.ID, self.ChooserHeader)
			return True
		except:
			return False

	def has_calendar(self):
		try:
			WebDriverWait(self.driver, base.wait_time).until(
				EC.presence_of_element_located(("id", self.calendar))
			)
			self.driver.find_element("id", self.calendar)
			return True
		except:
			return False

	def scroll_down_photo(self):
		window = self.driver.get_window_size()
		x = window["width"] // 2
		start_y = int(window["height"] * 0.7)
		end_y = int(window["height"] * 0.3)

		self.driver.swipe(x, start_y, x, end_y, 500)  # 500 毫秒完成滑動
		time.sleep(1)

	def scroll_up_photo(self):
		window = self.driver.get_window_size()
		x = window["width"] // 2
		start_y = int(window["height"] * 0.3)
		end_y = int(window["height"] * 0.7)

		self.driver.swipe(x, start_y, x, end_y, 500)  # 500 毫秒完成滑動
		time.sleep(1)
	# find how many photos between two dates
	def find_thumbnails_between_dates(self, target_date_str):
		target_date = datetime.datetime.strptime(target_date_str, "%Y/%m/%d")
		collected_thumbnails = []
		seen_blocks = set()
		seen_thumb_ids = set()  # 用來記錄已經收集過的縮圖 ID

		try:  # 先檢查有沒有今天的資料，如果沒有代表沒照片
			top_date_el = self.driver.find_element(AppiumBy.ID,
												   "com.compal.bioslab.pixsee.pixm01:id/gallery_item_date_txt")
			top_date_txt = top_date_el.text.strip().replace(" ", "").replace("／", "/").replace(" / ", "/")
			top_date = datetime.datetime.strptime(top_date_txt, "%Y/%m/%d")

			if top_date != target_date:
				print(f"no photo today")
				return []

		except:
			print("no elements found, no photos today")
			return []

		collecting = False
		found_new_date = False
		current_date = None
		current_day_num = None

		while not found_new_date:
			all_blocks = self.driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup")

			for block in all_blocks:
				if block.id in seen_blocks:
					continue
				seen_blocks.add(block.id)
				# print(block.id)

				try:
					day_txt = block.find_element(AppiumBy.ID,
												 "com.compal.bioslab.pixsee.pixm01:id/gallery_item_day_number_txt").text
					try:
						date_txt = block.find_element(AppiumBy.ID,
													  "com.compal.bioslab.pixsee.pixm01:id/gallery_item_date_txt").text
						date_clean = date_txt.strip().replace(" ", "").replace("／", "/").replace(" / ",
																								 "/")
						current_date = datetime.datetime.strptime(date_clean, "%Y/%m/%d")
						print(current_date)
						if current_date == target_date:
							collecting = True
							current_day_num = day_txt
							continue
					except:
						pass

					if collecting:
						if current_date != target_date or day_txt != current_day_num:
							found_new_date = True
							break

				except:
					if collecting:
						# thumbs = block.find_element(AppiumBy.ID,"com.compal.bioslab.pixsee.pixm01:id/clContainer")
						thumbs = block.find_elements(AppiumBy.ID,
													 self.gallery_thumbnail)
						for thumb in thumbs:
							if thumb.id not in seen_thumb_ids:
								seen_thumb_ids.add(thumb.id)
								collected_thumbnails.append(thumb)

			if not found_new_date:
				self.scroll_down_photo()

		return collected_thumbnails

	def find_date_range(self, target_date_str):
		target_date = datetime.datetime.strptime(target_date_str, "%Y/%m/%d")
		found_lower = False
		while True:
			all_blocks = self.driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup")

			date_list = []
			for block in all_blocks:
				try:
					date_txt = block.find_element(
						AppiumBy.ID,
						"com.compal.bioslab.pixsee.pixm01:id/gallery_item_date_txt"
					).text
					date_clean = date_txt.strip().replace(" ", "").replace("／", "/").replace(" / ", "/")
					block_date = datetime.datetime.strptime(date_clean, "%Y/%m/%d")
					date_list.append(block_date)
				except:
					continue

			if not date_list:
				self.scroll_up_photo()
				continue

			min_date = min(date_list)
			max_date = max(date_list)

			# 第一步：找到一個 <= target 的日期
			if not found_lower and min_date <= target_date:
				print(f"✅ 找到下界 {min_date} <= {target_date}，準備繼續往上找")
				found_lower = True
				self.scroll_up_photo()
				continue

			# 第二步：找到一個 >= target 的日期
			if found_lower and max_date > target_date:
				print(f"🎯 找到上界 {max_date} >= {target_date}，完成！")
				return True

			# 還沒滿足條件就繼續滑
			self.scroll_up_photo()

	def count_photos_today(self):
		today_str = datetime.datetime.today().strftime("%Y/%m/%d")
		# print("今天是" + today_str)
		thumbnails = self.find_thumbnails_between_dates(today_str)
		return int(len(thumbnails))

	def select_baby_birthday(self, locale, year=datetime.date.today().year, month=datetime.date.today().month,
							 day=datetime.date.today().day):
		# Validate the input date
		try:
			target_date = datetime.date(year, month, day)
			if year < 2020 or target_date > datetime.date.today():
				raise ValueError(
					"Year must be between 2020 and the current year, and the date must not be in the future.")
		except ValueError as e:
			raise ValueError(f"Invalid date: {e}")

		self.click_calendar_button()
		time.sleep(1)
		if not self.has_calendar():
			raise AssertionError("Can't find calendar for birthday selection")

		# Year / Month / Day pickers
		year_picker = self.driver.find_element("id", self.calendarYearPicker)
		month_picker = self.driver.find_element("id", self.calendarMonthPicker)
		day_picker = self.driver.find_element("id", self.calendarDayPicker)

		if year != int(year_picker.text):
			year_picker.click()
			while True:
				try:
					element = self.driver.find_element("accessibility id", f"{year}")
					element.click()
					break
				except:
					if year < int(year_picker.text):
						self.driver.find_element(
							AppiumBy.ANDROID_UIAUTOMATOR,
							f'new UiScrollable(new UiSelector().className({self.calendarScrollableList_classname})).setAsVerticalList().scrollBackward()'
						)
					elif year > int(year_picker.text):
						self.driver.find_element(
							AppiumBy.ANDROID_UIAUTOMATOR,
							f'new UiScrollable(new UiSelector().className({self.calendarScrollableList_classname})).setAsVerticalList().scrollForward()'
						)
					time.sleep(0.2)

		month_text = month_picker.text.strip()
		try:
			current_month_num = datetime.datetime.strptime(month_text, "%b").month  # e.g. Aug
		except ValueError:
			if month_text.startswith("M") and month_text[1:].isdigit():
				current_month_num = int(month_text[1:])  # e.g. M08
			else:
				raise ValueError(f"Unsupported month format: {month_text}")

		first_day_elem = self.driver.find_element("xpath", self.calendarOneMonth_xpath).find_element("class name",
																									 self.calendarOneDay_classname)
		if locale != "CN":
			first_date_str = first_day_elem.get_attribute("content-desc").split("selected")[0].strip()
		else:
			first_date_str = first_day_elem.get_attribute("content-desc").split("已选")[0].strip()
		month_part = first_date_str.split()[1]
		if month_part.startswith("M") and month_part[1:].isdigit():
			target_date_str = f"{day:02d} M{month:02d} {year}"
		else:
			target_date_str = target_date.strftime("%d %B %Y")

		first_days = set()
		while True:
			try:
				if month == current_month_num and day == int(day_picker.text):
					if locale != "CN":
						element = self.driver.find_element("accessibility id", target_date_str + " selected")
					else:
						element = self.driver.find_element("accessibility id", target_date_str + "已选")
					element.click()
				else:
					element = self.driver.find_element("accessibility id", target_date_str)
					element.click()
				element = self.driver.find_element("id", self.calendarDoneButton)
				element.click()
				return
			except:
				calendar_current_month = self.driver.find_element("xpath", self.calendarOneMonth_xpath)
				element = calendar_current_month.find_element("class name", self.calendarOneDay_classname)
				if locale != "CN":
					first_date_str = element.get_attribute("content-desc").split("selected")[0].strip()
				else:
					first_date_str = element.get_attribute("content-desc").split("已选")[0].strip()
				month_part = first_date_str.split()[1]
				if month_part.startswith("M") and month_part[1:].isdigit():
					first_date = datetime.datetime.strptime(first_date_str.replace("M", ""), "%d %m %Y").date()
				else:
					first_date = datetime.datetime.strptime(first_date_str, "%d %B %Y").date()

				if first_date_str in first_days:
					raise ValueError(
						f"{year}-{month}-{day} is not found in the calendar. Please check the date and try again.")
				first_days.add(first_date_str)
				if year < first_date.year:
					self.driver.find_element(
						AppiumBy.ANDROID_UIAUTOMATOR,
						f'new UiScrollable(new UiSelector().className({self.calendarScrollableList_classname})).setAsVerticalList().scrollBackward()'
					)
				elif month < first_date.month:
					self.driver.find_element(
						AppiumBy.ANDROID_UIAUTOMATOR,
						f'new UiScrollable(new UiSelector().className({self.calendarScrollableList_classname})).setAsVerticalList().scrollBackward()'
					)
				elif month > first_date.month:
					self.driver.find_element(
						AppiumBy.ANDROID_UIAUTOMATOR,
						f'new UiScrollable(new UiSelector().className({self.calendarScrollableList_classname})).setAsVerticalList().scrollForward()'
					)
				elif day > first_date.day:
					window = self.driver.get_window_size()
					x = window["width"] // 2.5
					start_y = int(window["height"] * 0.6)
					end_y = int(window["height"] * 0.5)
					self.driver.swipe(x, start_y, x, end_y, 3000)
				elif day < first_date.day:
					window = self.driver.get_window_size()
					x = window["width"] // 2.5
					start_y = int(window["height"] * 0.5)
					end_y = int(window["height"] * 0.6)
					self.driver.swipe(x, start_y, x, end_y, 3000)
				time.sleep(0.2)
	# click 1 or more recent thumbnails
	def click_recent_thumbnails(self, count):
			seen_thumb_ids = set()
			clicked = 0

			while clicked < count:
				# 找到畫面上的所有縮圖
				thumbs = self.driver.find_elements(
					AppiumBy.ID,
					self.gallery_thumbnail
				)

				for thumb in thumbs:
					if thumb.id not in seen_thumb_ids:
						seen_thumb_ids.add(thumb.id)
						try:
							thumb.click()
							clicked += 1
							print(f"✅ 點選第 {clicked} 張照片 (id={thumb.id})")
						except Exception as e:
							print(f"⚠️ 點選失敗: {e}")

						if clicked >= count:
							return  # 已經點到夠的數量，直接結束

				# 如果還不夠張數，就往下滑繼續找
				if clicked < count:
					self.scroll_down_photo()
	# click one pic you want
	def click_specific_thumbnail(self, index: int):
		"""
		點選畫面上的其中一張縮圖 (index 從 0 開始)
		"""
		thumbs = self.driver.find_elements(
			AppiumBy.ID,
			self.gallery_thumbnail
		)

		total = len(thumbs)
		if total == 0:
			print("❌ 畫面上沒有找到任何縮圖")
			return

		if index < 0 or index >= total:
			print(f"❌ index 超出範圍 (目前有 {total} 張縮圖)")
			return

		try:
			thumbs[index].click()
			print(f"✅ 成功點選第 {index + 1} 張縮圖")
		except Exception as e:
			print(f"⚠️ 點選失敗: {e}")

	def numbers_of_photo_hidden(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.HiddenPhoto))
		)
		elements = self.driver.find_elements(AppiumBy.ID, self.HiddenPhoto)
		return len(elements)

	def delete_and_verify_thumbnail(self, index: int):
		"""
		點選指定的縮圖，刪除，並驗證是否真的消失
		"""
		thumbs = self.driver.find_elements(
			AppiumBy.ID,
			self.gallery_thumbnail
		)

		total = len(thumbs)
		if total == 0:
			print("❌ 畫面上沒有任何縮圖")
			return

		if index < 0 or index >= total:
			print(f"❌ index 超出範圍 (目前有 {total} 張縮圖)")
			return

		# 先記住這張縮圖的 element_id
		target_id = thumbs[index].id

		# 點進去
		thumbs[index].click()
		print(f"✅ 進入第 {index + 1} 張縮圖 (id={target_id})")

		# 執行刪除（這裡請換成實際刪除的 locator）
		try:
			delete_btn = self.driver.find_element(
				AppiumBy.ID,
				self.Garbage
			)
			delete_btn.click()
			self.click_dialog_yes()
			print("🗑️ 已經刪除縮圖")
		except Exception as e:
			print(f"❌ 找不到刪除按鈕: {e}")
			return

		# 回到縮圖列表（假設刪除後會自動返回）
		# 如果需要手動返回，可以加 driver.back()

		# 再次取得縮圖列表
		thumbs_after = self.driver.find_elements(
			AppiumBy.ID,
			self.gallery_thumbnail
		)

		# 驗證剛剛刪掉的 id 不存在
		after_ids = [t.id for t in thumbs_after]
		if target_id not in after_ids:
			print(f"✅ 縮圖 (id={target_id}) 已經消失，刪除驗證成功")
		else:
			print(f"❌ 縮圖 (id={target_id}) 還存在，刪除驗證失敗")



