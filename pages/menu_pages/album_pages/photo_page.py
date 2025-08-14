
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime



class PhotoPage():
	def __init__(self, driver):
		self.driver = driver
		self.NewFuncTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
		self.NewFuncMsg = "com.compal.bioslab.pixsee.pixm01:id/tvBottomMessage"
		self.iknowButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositive"
		self.TutorTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
		self.TutorDescription = "com.compal.bioslab.pixsee.pixm01:id/tvDescription"
		self.Calender = "com.compal.bioslab.pixsee.pixm01:id/ibDailyCoverGalleryCalendar"
		self.Select = "com.compal.bioslab.pixsee.pixm01:id/ibSelectMode"
		self.PlusButton = "com.compal.bioslab.pixsee.pixm01:id/fab_daily_cover_gallery_menu"
		self.SlideButton = "com.compal.bioslab.pixsee.pixm01:id/tv_daily_cover_gallery_fab_slideshow"
		self.SlideButtonText = "com.compal.bioslab.pixsee.pixm01:id/tv_daily_cover_gallery_fab_slideshow"
		self.PhotoButton = "com.compal.bioslab.pixsee.pixm01:id/fab_daily_cover_gallery_menu"
		self.PhotoButtonText = "com.compal.bioslab.pixsee.pixm01:id/tv_daily_cover_gallery_fab_photo"



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

	def click_iknow_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.iknowButton))
		)
		element = self.driver.find_element(AppiumBy.ID, self.iknowButton)
		element.click()
		time.sleep(1)
	def click_calendar_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Calender))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Calender)
		element.click()
		time.sleep(1)
	def click_select_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.Select))
		)
		element = self.driver.find_element(AppiumBy.ID, self.Select)
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

	def is_in_photo_page(self):
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((AppiumBy.ID, self.Calender))
			)
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

	def find_thumbnails_between_dates(self, target_date_str):
		target_date = datetime.strptime(target_date_str, "%Y/%m/%d")
		collected_thumbnails = []
		seen_blocks = set()
		seen_thumb_ids = set()  # 用來記錄已經收集過的縮圖 ID

		try:  # 先檢查有沒有今天的資料，如果沒有代表沒照片
			top_date_el = self.driver.find_element(AppiumBy.ID,
												   "com.compal.bioslab.pixsee.pixm01:id/gallery_item_date_txt")
			top_date_txt = top_date_el.text.strip().replace(" ", "").replace("／", "/").replace(" / ", "/")
			top_date = datetime.strptime(top_date_txt, "%Y/%m/%d")

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
						current_date = datetime.strptime(date_clean, "%Y/%m/%d")

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
													 "com.compal.bioslab.pixsee.pixm01:id/gallery_thumbnail")
						for thumb in thumbs:
							if thumb.id not in seen_thumb_ids:
								seen_thumb_ids.add(thumb.id)
								collected_thumbnails.append(thumb)

			if not found_new_date:
				self.scroll_down_photo()

		return collected_thumbnails

	def count_photos_today(self):
		today_str = datetime.today().strftime("%Y/%m/%d")
		# print("今天是" + today_str)
		thumbnails = self.find_thumbnails_between_dates(today_str)
		return int(len(thumbnails))

