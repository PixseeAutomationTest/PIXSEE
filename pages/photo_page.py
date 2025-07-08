
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime



class PhotoPage:
	def __init__(self, driver):
		self.driver = driver

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