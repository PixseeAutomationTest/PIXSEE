
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime



class PhotoPage():
	def __init__(self, driver):
		self.driver = driver
		self.iknowButton = "com.compal.bioslab.pixsee.pixm01:id/btnPositive"
		# self.plusButton =
		self.backButton = "//android.widget.ImageButton[@content-desc=\"Navigate up\"]"

	def click_back_button(self):
		# WebDriverWait(self.driver, 10).until(
		# 	EC.presence_of_element_located((AppiumBy.XPATH, self.backButton))
		# )
		element = self.driver.find_element(AppiumBy.XPATH, self.backButton)
		element.click()
		time.sleep(1)

	def click_iknow_button(self):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((AppiumBy.ID, self.iknowButton))
		)
		element = self.driver.find_element(AppiumBy.ID, self.iknowButton)
		element.click()
		time.sleep(1)


	def scroll_down_photo(self):
		window = self.driver.get_window_size()
		x = window["width"] // 2
		start_y = int(window["height"] * 0.8)
		end_y = int(window["height"] * 0.3)

		self.driver.swipe(x, start_y, x, end_y, 500)  # 500 毫秒完成滑動
		time.sleep(1)




	def find_thumbnails_between_dates(self, target_date_str):
		target_date = datetime.strptime(target_date_str, "%Y/%m/%d")
		collected_thumbnails = []
		seen_blocks = set()

		try:  # 先檢查有沒有今天的資料，如果沒有代表沒照片
			top_date_el = self.driver.find_element(AppiumBy.ID,
												   "com.compal.bioslab.pixsee.pixm01:id/gallery_item_date_txt")
			top_date_txt = top_date_el.text.strip().replace(" ", "").replace("／", "/").replace(" / ", "/")
			top_date = datetime.strptime(top_date_txt, "%Y/%m/%d")

			if top_date != target_date:
				print(f"今天{target_date_str}沒有照片")
				return []

		except:
			print("畫面上找不到任何日期，可能畫面尚未載入或元素不存在")
			return []

		collecting = False
		found_new_date = False

		while not found_new_date:
			all_blocks = self.driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup")

			for block in all_blocks:
				if block.id in seen_blocks:
					continue
				seen_blocks.add(block.id)

				try:
					date_txt = block.find_element(AppiumBy.ID,
												  "com.compal.bioslab.pixsee.pixm01:id/gallery_item_date_txt").text
					date_clean = date_txt.strip().replace(" ", "").replace("／", "/").replace(" / ", "/")
					current_date = datetime.strptime(date_clean, "%Y/%m/%d")

					if current_date == target_date:
						collecting = True
						continue

					if collecting and current_date != target_date:
						found_new_date = True
						break

				except:
					if collecting:
						thumbs = block.find_elements(AppiumBy.ID,
													 "com.compal.bioslab.pixsee.pixm01:id/gallery_thumbnail")
						collected_thumbnails.extend(thumbs)

			if not found_new_date:
				self.scroll_down_photo()

		# print(f"共找到 {len(collected_thumbnails)} 張圖片")
		return collected_thumbnails


	def count_photos_today(self):
		today_str = datetime.today().strftime("%Y/%m/%d")
		print("今天是" + today_str)
		thumbnails = self.find_thumbnails_between_dates(today_str)
		return int(len(thumbnails) / 2)

