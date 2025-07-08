#測試機型帶有錯誤SD卡，所以本程式包含關閉SD卡之按鈕，正常機型會比較拖時間
#如果你的機型正常可以註解掉約第70行和其後續
#2025/7/8-新增當日照片判斷，無SD卡通知機型運行，小幅調正等待時間
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from login_page import Function
from search_photo import Search
import datetime
email_input = "com.compal.bioslab.pixsee.pixm01:id/signInEmailField"
password_input = "com.compal.bioslab.pixsee.pixm01:id/signInPasswordField"
sign_in_button = "com.compal.bioslab.pixsee.pixm01:id/btSignIn"
baby_monitor = "com.compal.bioslab.pixsee.pixm01:id/videoTextureView"
home_btn="com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome"
#Content
email = "amypixsee03@gmail.com"
password = "@Aa12345"
class PhotoCheck:
    def __init__(self):
        pass

    '''def disable_app_notifications(package_name="com.compal.bioslab.pixsee.pixm01"):
        import subprocess
        subprocess.run(["adb", "shell", "appops", "set", package_name, "POST_NOTIFICATION", "ignore"])'''

    def start(self):
        capabilities = UiAutomator2Options()
        capabilities.platform_name = "Android"
        capabilities.device_name = "emulator-5554"
        # adb devices
        capabilities.app_package = "com.compal.bioslab.pixsee.pixm01"
        capabilities.app_activity = "com.compal.bioslab.pixsee.pixm01.activities.SplashActivity"
        capabilities.no_reset = False
        capabilities.auto_grant_permissions = True
        capabilities.new_command_timeout = 3000

        self.driver = webdriver.Remote("http://localhost:4723", options=capabilities)

    def test_login_success(self):
        fun = Function(self.driver)
        print("Login")
        time.sleep(5)
        # email
        fun.login_email_input(email)
        # password
        fun.login_password_input(password)
        # sign-in
        fun.click_btn(sign_in_button)
        '''time.sleep(15)
        element = self.driver.find_element(AppiumBy.ID,"com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog");
        element.click()'''
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((AppiumBy.ID, baby_monitor))
            )
            if element.is_displayed():
                print("----Login success")#嗨
            else:
                print("----Login failed")
        except TimeoutException:
            print("----Login failed:time out")
        except Exception as e:
            print(f"其他登入錯誤")

        try:#等待SD卡確認按鈕出現，如果沒有就跳過
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"))
            )
            if element.is_displayed():
                element.click()
                time.sleep(0.5)
        except:
            pass
        for i in range(4):
            fun.click()
            time.sleep(0.5)
    def photo(self):
        fun = Function(self.driver)
        element = self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome");
        element.click()
        fun.click()
        time.sleep(1)
        element = self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsGallery");
        element.click()
        time.sleep(3)
        element = self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/btnPositive");
        element.click()
        time.sleep(0.5)
        fun.click()
    def count(self):
        search=Search(self.driver)
        today_str = datetime.date.today().strftime("%Y/%m/%d")
        print("今天是"+today_str)
        print("正在計算照片數量...")
        thumbnails = search.find_thumbnails_between_dates(today_str)
        count1=str(int(len(thumbnails)/2))
        print("原本共有"+count1+"張照片")
        return count1
    def take_photo(self):
        fun = Function(self.driver)
        time.sleep(1)
        element = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc=\"Navigate up\"]");
        element.click()#回上頁
        time.sleep(1)
        element = self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome");
        element.click()#回主頁
        time.sleep(1)
        element = self.driver.find_element(AppiumBy.XPATH,"//android.widget.RelativeLayout[@resource-id=\"com.compal.bioslab.pixsee.pixm01:id/btnSwipeCapture\"]/android.widget.ImageView[2]");
        element.click()#拍照按鈕
        print("正在拍照")
        time.sleep(5)
        #拍完照
        element = self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome");
        element.click()
        element = self.driver.find_element(AppiumBy.ID, "com.compal.bioslab.pixsee.pixm01:id/llNvSettingsGallery");
        element.click()
        time.sleep(1)
    def count2(self,count1):
        search = Search(self.driver)
        time.sleep(5)#等待照片出現
        today_str = datetime.date.today().strftime("%Y/%m/%d")
        print("正在計算照片數量...")
        thumbnails = search.find_thumbnails_between_dates(today_str)
        count2 = str(int(len(thumbnails) / 2))
        print("拍照後共有" + count2 + "張照片")
        count2=int(count2)
        count1=int(count1)
        if count2==count1+1:
            print("拍照成功")
        else:
            print("拍照失敗，請重試或檢查連線")

go=PhotoCheck()

go.start()
#go.disable_app_notifications()
go.test_login_success()
go.photo()
count1=go.count()
go.take_photo()
go.count2(count1)


