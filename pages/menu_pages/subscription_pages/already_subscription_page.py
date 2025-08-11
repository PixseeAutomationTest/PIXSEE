from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pages.base as base

class SubscriptionPage2():
    def __init__(self, driver):
        self.driver = driver
        self.Back = "com.compal.bioslab.pixsee.pixm01:id/ibBackButton"
        self.Info = "com.compal.bioslab.pixsee.pixm01:id/btnNewSubscribedInformation"
        self.ChangeButton = "com.compal.bioslab.pixsee.pixm01:id/btChangeSubscription"
        self.CouponButton = "com.compal.bioslab.pixsee.pixm01:id/btnCoupon"
        self.CouponTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"
        self.CouponInfo = "com.compal.bioslab.pixsee.pixm01:id/ivInfo"
        self.CouponCodeField = "com.compal.bioslab.pixsee.pixm01:id/etCoupon"
        self.CouponCancel = "com.compal.bioslab.pixsee.pixm01:id/btCancel"
        self.CouponOk = "com.compal.bioslab.pixsee.pixm01:id/btOK"
        self.CouponWrongCode = "com.compal.bioslab.pixsee.pixm01:id/tvError"
        self.Chrome = "com.android.chrome:id/compositor_view_holder"
        self.Ok = "com.compal.bioslab.pixsee.pixm01:id/btnNewSubscribedOk"
        self.PayButton = '//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]'
        self.Chrome = "com.android.chrome:id/compositor_view_holder"
        self.Promotion = "com.compal.bioslab.pixsee.pixm01:id/tvNewsAndPromotions"
        self.CurrentPlan = "com.compal.bioslab.pixsee.pixm01:id/tvCurrentPlan"
        self.PaymentMethod = "com.compal.bioslab.pixsee.pixm01:id/tvPaymentMethodTitle"
        self.Method = "com.compal.bioslab.pixsee.pixm01:id/tvPaymentMethod"
        self.Expiration = "com.compal.bioslab.pixsee.pixm01:id/tvExpirationDate"
        self.Plan2Button = '(//android.widget.RadioButton[@resource-id="com.compal.bioslab.pixsee.pixm01:id/rb"])[2]'
        self.Checkbox = "com.compal.bioslab.pixsee.pixm01:id/cbPromotionsAndNews"

    def is_in_subscription_page(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.ChangeButton))
            )
            return True
        except :
            return False
    def is_in_coupon_dialog(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.CouponTitle))
            )
            return True
        except :
            return False
    def is_in_info_dialog(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.Chrome))
            )
            return True
        except :
            return False
    def is_in_price_plan_dialog(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.CouponTitle))
            )
            return True
        except :
            return False
    def is_in_chrome(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.Chrome))
            )
            return True
        except :
            return False

    def coupon_title_txt(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.CouponTitle))
            )
            element = self.driver.find_element("id", self.CouponTitle)
            return element.text
        except :
            return None
    def coupon_cancel_txt(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.CouponCancel))
            )
            element = self.driver.find_element("id", self.CouponCancel)
            return element.text
        except :
            return None
    def coupon_ok_txt(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.CouponOk))
            )
            element = self.driver.find_element("id", self.CouponOk)
            return element.text
        except :
            return None
    def coupon_code_hint(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.CouponCodeField))
            )
            element = self.driver.find_element("id", self.CouponCodeField)
            return element.get_attribute("hint")
        except :
            return None
    def coupon_wrong_code_text(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.CouponWrongCode))
            )
            element = self.driver.find_element("id", self.CouponWrongCode)
            return element.text
        except :
            return None
    def current_plan_text(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.CurrentPlan))
            )
            element = self.driver.find_element("id", self.CurrentPlan)
            return element.text
        except :
            return None
    def payment_method_text(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.PaymentMethod))
            )
            element = self.driver.find_element("id", self.PaymentMethod)
            return element.text
        except :
            return None
    def in_app_purchase_text(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.Method))
            )
            element = self.driver.find_element("id", self.Method)
            return element.text
        except :
            return None
    def expiration_text(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.Expiration))
            )
            element = self.driver.find_element("id", self.Expiration)
            return element.text
        except :
            return None
    def promotion_text(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.Promotion))
            )
            element = self.driver.find_element("id", self.Promotion)
            return element.text
        except :
            return None
    def ok_button_text(self):
        try:
            WebDriverWait(self.driver, base.wait_time).until(
                EC.presence_of_element_located(("id", self.Ok))
            )
            element = self.driver.find_element("id", self.Ok)
            return element.text
        except :
            return None

    def click_back(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.Back))
        )
        element = self.driver.find_element("id", self.Back)
        element.click()
    def click_info(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.Info))
        )
        element = self.driver.find_element("id", self.Info)
        element.click()
    def click_coupon(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.CouponButton))
        )
        element = self.driver.find_element("id", self.CouponButton)
        element.click()
    def click_coupon_cancel(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.CouponCancel))
        )
        element = self.driver.find_element("id", self.CouponCancel)
        element.click()
    def click_coupon_ok(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.CouponOk))
        )
        element = self.driver.find_element("id", self.CouponOk)
        element.click()
    def click_coupon_info(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.CouponInfo))
        )
        element = self.driver.find_element("id", self.CouponInfo)
        element.click()
    def click_change(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.ChangeButton))
        )
        element = self.driver.find_element("id", self.ChangeButton)
        element.click()
    def click_plan2(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("xpath", self.Plan2Button))
        )
        element = self.driver.find_element("xpath", self.Plan2Button)
        element.click()
    def click_pay(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("xpath", self.PayButton))
        )
        element = self.driver.find_element("xpath", self.PayButton)
        element.click()
    def click_ok(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.Ok))
        )
        element = self.driver.find_element("id", self.Ok)
        element.click()


    def enter_coupon_code(self, code):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.CouponCodeField))
        )
        element = self.driver.find_element("id", self. CouponCodeField)
        element.clear()
        element.send_keys(code)

    def is_coupon_ok_enabled(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located((AppiumBy.ID, self.CouponOk))
        )
        button = self.driver.find_element(AppiumBy.ID, self.CouponOk)
        is_enable = button.get_attribute("enabled")
        return is_enable == "true"

    def is_checkbox_checkable(self):
        WebDriverWait(self.driver, base.wait_time).until(
            EC.presence_of_element_located(("id", self.Checkbox))
        )
        element = self.driver.find_element("id", self.Checkbox)
        is_clickable = element.get_attribute("checkable")
        return is_clickable == "true"