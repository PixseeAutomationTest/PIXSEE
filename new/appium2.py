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
#infornation
email_input = "com.compal.bioslab.pixsee.pixm01:id/signInEmailField"
password_input = "com.compal.bioslab.pixsee.pixm01:id/signInPasswordField"
sign_in_button = "com.compal.bioslab.pixsee.pixm01:id/btSignIn"
baby_monitor = "com.compal.bioslab.pixsee.pixm01:id/videoTextureView"
home_btn="com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome"
#Content
email = "jackypixsee02@gmail.com"
password = "@Aa12345"

class Login(unittest.TestCase):

    def setUp(self):
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
        email = "jackypixsee02@gmail.com"
        password = "@Aa12345"

    def test_login_success(self):
        fun = Function(self.driver)
        print("Login")
        fun.login_email_input(email)
        fun.login_password_input(password)
        fun.click_btn(sign_in_button)

        fun.login_check()

    def test_login_wrong_Email_fail(self):
        fun = Function(self.driver)
        print("wrong email")
        email="japixsee@gmail.com"
        fun.login_email_input(email)
        fun.login_password_input(password)
        fun.click_btn(sign_in_button)

        expected_text = "This account does not exist, Please sign up first"
        hint_text = "com.compal.bioslab.pixsee.pixm01:id/tvSignInEmailError"
        fun.test_text(expected_text,hint_text)
    def test_login_wrong_password_fail(self):
        fun = Function(self.driver)
        print("wrong password")
        password="123456"
        fun.login_email_input(email)
        fun.login_password_input(password)
        fun.click_btn(sign_in_button)

        expected_text = "Wrong password"
        hint_text="com.compal.bioslab.pixsee.pixm01:id/tvSignInPasswordError"
        fun.test_text(expected_text,hint_text)
    def test_login_empty_Email_fail(self):
        fun = Function(self.driver)
        print("empty email")
        email=""
        fun.login_email_input(email)
        fun.login_password_input(password)
        fun.click_btn(sign_in_button)

        expected_text = "Please enter an email"
        hint_text = "com.compal.bioslab.pixsee.pixm01:id/tvSignInEmailError"
        fun.test_text(expected_text,hint_text)
    def test_login_empty_password_fail(self):
        fun = Function(self.driver)
        print("empty password")
        password=""
        fun.login_email_input(email)
        fun.login_password_input(password)
        fun.click_btn(sign_in_button)

        expected_text = "Please enter password."
        hint_text = "com.compal.bioslab.pixsee.pixm01:id/tvSignInPasswordError"
        fun.test_text(expected_text,hint_text)
if __name__=="__main__":
    unittest.main()
