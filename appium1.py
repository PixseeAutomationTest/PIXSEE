# connecting to device
from asyncio import wait
#appium --use-plugins=inspector --allow-cors
#pip install Appium-Python-Client
import appium
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
#Components
email_input = "com.compal.bioslab.pixsee.pixm01:id/signInEmailField"
password_input = "com.compal.bioslab.pixsee.pixm01:id/signInPasswordField"
sign_in_button = "com.compal.bioslab.pixsee.pixm01:id/btSignIn"
baby_monitor = "com.compal.bioslab.pixsee.pixm01:id/videoTextureView"
home_btn="com.compal.bioslab.pixsee.pixm01:id/ibMenuButtonHome"
#Content
email = "jackypixsee02@gmail.com"
password = "@Aa12345"

#actions
# 1. tap email_input
# 2. type email
# 3. tap password_input
# 4. type password
# 5. tap sign_in_button
# 6. wait for baby_monitor to appear

# connecting to device

capabilities = UiAutomator2Options()
capabilities.platform_name = "Android"
capabilities.device_name = "emulator-5554"
#adb devices
capabilities.app_package = "com.compal.bioslab.pixsee.pixm01"
capabilities.app_activity = "com.compal.bioslab.pixsee.pixm01.activities.SplashActivity"
capabilities.no_reset = False
capabilities.auto_grant_permissions = True
capabilities.new_command_timeout = 3000

driver = webdriver.Remote("http://localhost:4723", options=capabilities)


WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, email_input))
)
#email
element=driver.find_element(AppiumBy.ID,email_input)
element.click()
element.send_keys(email)
#password
element=driver.find_element(AppiumBy.ID,password_input)
element.click()
element.send_keys(password)
#sign-in
element=driver.find_element(AppiumBy.ID,sign_in_button); element.click()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, baby_monitor))
    )
    if element.is_displayed():
        print("Login success")
    else:
        print("Login failed: Element not visible")
except TimeoutException:
    print("Login failed: Element not found (timeout)")
for i in range(5):
    element=driver.find_element(AppiumBy.ID,baby_monitor)
    element.click()
'''driver.execute_script("mobile: swipeGesture", {
    "left": 100,
    "top": 500,
    "width": 800,
    "height": 1000,
    "direction": "down",
    "percent": 0.75
})'''
print("job done")
element=driver.find_element(AppiumBy.ID,home_btn); element.click()