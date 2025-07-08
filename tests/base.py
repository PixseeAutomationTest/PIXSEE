import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options


class BaseTestCase(unittest.TestCase):
    def setUp(self, no_reset=True):
        capabilities = UiAutomator2Options()
        capabilities.platform_name = "Android"
        capabilities.device_name = "38161FDJG00DXJ"
        # adb devices
        capabilities.app_package = "com.compal.bioslab.pixsee.pixm01"
        capabilities.app_activity = "com.compal.bioslab.pixsee.pixm01.activities.SplashActivity"
        capabilities.no_reset = no_reset
        capabilities.auto_grant_permissions = True
        capabilities.new_command_timeout = 300

        self.driver = webdriver.Remote("http://localhost:4723", options=capabilities)

    def tearDown(self):
        pass

# for i in range(5):
#         driver.find_element(AppiumBy.ID, videoMonitor).click()
#
# driver.find_element(
#     AppiumBy.ANDROID_UIAUTOMATOR,
#     'new UiScrollable(new UiSelector().resourceId("com.compal.bioslab.pixsee.pixm01:id/svHomeAct")).setAsVerticalList().scrollForward()'
# )
#
# WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((AppiumBy.ID, babycry))
# )
#
# driver.find_element(
#     AppiumBy.ANDROID_UIAUTOMATOR,
#     'new UiScrollable(new UiSelector().resourceId("com.compal.bioslab.pixsee.pixm01:id/vpCryTipsCards")).setAsHorizontalList().scrollForward()'
# )