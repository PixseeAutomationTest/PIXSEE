from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class MenuPage():
	def __init__(self, driver):
		self.driver = driver
		self.buttonText_class_name = "android.widget.TextView"
		self.profileButton = "com.compal.bioslab.pixsee.pixm01:id/civProfileWelcomeAct"
		self.homeButton = "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome"
		self.notificationsButton = "com.compal.bioslab.pixsee.pixm01:id/btNotificationCenter"
		self.babyListButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsBabiesList"

		self.babyEditButton = "com.compal.bioslab.pixsee.pixm01:id/baby_edit_icon"
		self.babyAddButton = "com.compal.bioslab.pixsee.pixm01:id/baby_list_item"
		self.membersButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsMembers"
		self.settingsButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsDevice"
		self.pixseesettingstxt = "com.compal.bioslab.pixsee.pixm01:id/tvPixseeSettings"
		self.friendsButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsFriends"
		self.albumButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsGallery"
		self.facesButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsFamilyFace"
		self.framesButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsSpecialCards"
		self.subscriptionButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsStore"
		self.assistantButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsHelp"
		self.aboutButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsAbout"
		self.logoutButton = "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsLogout"

	def pixsee_settingstxt_text(self):
		try:
			WebDriverWait(self.driver, 20).until(
				EC.presence_of_element_located(("id", self.pixseesettingstxt))
			)
			element = self.driver.find_element("id", self.pixseesettingstxt)
			return element.text
		except:
			return None

	def click_profile(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.profileButton))
		)
		self.driver.find_element(AppiumBy.ID, self.profileButton).click()
		time.sleep(1)  # 等待頁面加載完成，必要時可調整時間

	def click_home(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.homeButton))
		)
		self.driver.find_element(AppiumBy.ID, self.homeButton).click()
		time.sleep(1)

	def click_notification(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.notificationsButton))
		)
		self.driver.find_element(AppiumBy.ID, self.notificationsButton).click()
		time.sleep(1)

	def click_baby_list(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.babyListButton))
		)
		self.driver.find_element(AppiumBy.ID, self.babyListButton).click()
		time.sleep(1)  # 等待頁面加載完成，必要時可調整時間

	def click_baby_edit(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.babyEditButton))
		)
		self.driver.find_element(AppiumBy.ID, self.babyEditButton).click()
		time.sleep(1)

	def click_baby_add(self):
		self.click_baby_list()
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.babyAddButton))
		)
		elements = self.driver.find_elements(AppiumBy.ID, self.babyAddButton)
		elements[-1].click()
		time.sleep(1)

	def click_members(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.membersButton))
		)
		self.driver.find_element(AppiumBy.ID, self.membersButton).click()
		time.sleep(1)  # 等待頁面加載完成，必要時可調整時間

	def click_settings(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located((AppiumBy.ID, self.settingsButton))
		)
		self.driver.find_element(AppiumBy.ID, self.settingsButton).click()
		time.sleep(1)

	def click_friends(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.friendsButton))
		)
		self.driver.find_element(AppiumBy.ID, self.friendsButton).click()
		time.sleep(1)

	def click_album(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.albumButton))
		)
		self.driver.find_element(AppiumBy.ID, self.albumButton).click()
		time.sleep(1)
	
	def click_faces(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.facesButton))
		)
		self.driver.find_element(AppiumBy.ID, self.facesButton).click()
		time.sleep(1)
	# 	self.driver.find_element(AppiumBy.ID,).click()
	#
	def click_frames(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.framesButton))
		)
		self.driver.find_element(AppiumBy.ID, self.framesButton).click()
		time.sleep(1)

	def click_subscription(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.subscriptionButton))
		)
		self.driver.find_element(AppiumBy.ID, self.subscriptionButton).click()
		time.sleep(1)

	def click_assistant(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.assistantButton))
		)
		self.driver.find_element(AppiumBy.ID, self.assistantButton).click()
		time.sleep(1)

	def click_about(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id",self.aboutButton))
		)
		self.driver.find_element(AppiumBy.ID, self.aboutButton).click()
		time.sleep(1)
	
	def click_logout(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.logoutButton))
		)
		self.driver.find_element(AppiumBy.ID, self.logoutButton).click()
		time.sleep(1)

	def get_members_button_text(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.membersButton))
		)
		parent_element = self.driver.find_element(AppiumBy.ID, self.membersButton)
		element = parent_element.find_element(AppiumBy.CLASS_NAME, self.buttonText_class_name)
		return element.text

	def get_settings_button_text(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.settingsButton))
		)
		parent_element = self.driver.find_element(AppiumBy.ID, self.settingsButton)
		element = parent_element.find_element(AppiumBy.CLASS_NAME, self.buttonText_class_name)
		return element.text

	def get_friends_button_text(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.friendsButton))
		)
		parent_element = self.driver.find_element(AppiumBy.ID, self.friendsButton)
		element = parent_element.find_element(AppiumBy.CLASS_NAME, self.buttonText_class_name)
		return element.text

	def get_album_button_text(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.albumButton))
		)
		parent_element = self.driver.find_element(AppiumBy.ID, self.albumButton)
		element = parent_element.find_element(AppiumBy.CLASS_NAME, self.buttonText_class_name)
		return element.text

	def get_faces_button_text(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.facesButton))
		)
		parent_element = self.driver.find_element(AppiumBy.ID, self.facesButton)
		element = parent_element.find_element(AppiumBy.CLASS_NAME, self.buttonText_class_name)
		return element.text

	def get_frames_button_text(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.framesButton))
		)
		parent_element = self.driver.find_element(AppiumBy.ID, self.framesButton)
		element = parent_element.find_element(AppiumBy.CLASS_NAME, self.buttonText_class_name)
		return element.text

	def get_subscription_button_text(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.subscriptionButton))
		)
		parent_element = self.driver.find_element(AppiumBy.ID, self.subscriptionButton)
		element = parent_element.find_element(AppiumBy.CLASS_NAME, self.buttonText_class_name)
		return element

	def get_assistant_button_text(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.assistantButton))
		)
		parent_element = self.driver.find_element(AppiumBy.ID, self.assistantButton)
		element = parent_element.find_element(AppiumBy.CLASS_NAME, self.buttonText_class_name)
		return element.text

	def get_about_button_text(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.aboutButton))
		)
		parent_element = self.driver.find_element(AppiumBy.ID, self.aboutButton)
		element = parent_element.find_element(AppiumBy.CLASS_NAME, self.buttonText_class_name)
		return element.text

	def get_logout_button_text(self):
		WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located(("id", self.logoutButton))
		)
		parent_element = self.driver.find_element(AppiumBy.ID, self.logoutButton)
		element = parent_element.find_element(AppiumBy.CLASS_NAME, self.buttonText_class_name)
		return element.text

	def is_in_menu_page(self):
		try:
			WebDriverWait(self.driver, 20).until(
				EC.presence_of_element_located(("id", self.profileButton))
			)
			self.driver.find_element(AppiumBy.ID, self.profileButton)
			return True
		except:
			return False

	

