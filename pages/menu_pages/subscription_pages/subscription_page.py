from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image


class SubscriptionPage():
    def __init__(self, driver):
        self.driver = driver
        self.Header = "com.compal.bioslab.pixsee.pixm01:id/tvBarTitle"
        self.X = "com.compal.bioslab.pixsee.pixm01:id/ibBackButton"
        self.Info = "com.compal.bioslab.pixsee.pixm01:id/ivSubscInfo"
        self.GoldStarButton = "com.compal.bioslab.pixsee.pixm01:id/btNewSubscription"
        self.CouponButton = "com.compal.bioslab.pixsee.pixm01:id/ibCoupon"
        self.Capacity = "com.compal.bioslab.pixsee.pixm01:id/tvPlanTypeTitle"
        self.Coupon = "com.compal.bioslab.pixsee.pixm01:id/btnUpgradeTimeLapseCancel"
        self.Chrome = "com.android.chrome:id/compositor_view_holder"
        self.MoreDetails = "com.compal.bioslab.pixsee.pixm01:id/tvMoreDetail"
        self.Plan1Button= '(//android.widget.RadioButton[@resource-id="com.compal.bioslab.pixsee.pixm01:id/rb"])[1]'
        self.Plan2Button= '(//android.widget.RadioButton[@resource-id="com.compal.bioslab.pixsee.pixm01:id/rb"])[2]'
        self.PayButton = "android.widget.Button"
        self.Chrome = "com.android.chrome:id/compositor_view_holder"

    def is_in_subscription_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Header))
            )
            return True
        except AssertionError:
            return False
    def is_in_coupon_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Coupon))
            )
            return True
        except AssertionError:
            return False
    def is_in_info_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Chrome))
            )
            return True
        except AssertionError:
            return False
    def is_in_prize_plan_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("xpath", self.Plan1Button))
            )
            return True
        except AssertionError:
            return False
    def is_in_pay_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("xpath", self.PayButton))
            )
            return True
        except AssertionError:
            return False
    def is_in_chrome(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Chrome))
            )
            return True
        except AssertionError:
            return False

    def header_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Header))
            )
            element = self.driver.find_element("id", self.Header)
            return element.text
        except AssertionError:
            return None
    def title(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Capacity))
            )
            element = self.driver.find_element("id", self.Capacity)
            return element.text
        except AssertionError:
            return None
    def gold_star_button_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.GoldStarButton))
            )
            element = self.driver.find_element("id", self.GoldStarButton)
            return element.text
        except AssertionError:
            return None
    def more_details_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.MoreDetails))
            )
            element = self.driver.find_element("id", self.MoreDetails)
            return element.text
        except AssertionError:
            return None

    def click_x(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.X))
        )
        element = self.driver.find_element("id", self.X)
        element.click()
    def click_info(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Info))
        )
        element = self.driver.find_element("id", self.Info)
        element.click()
    def click_coupon(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.CouponButton))
        )
        element = self.driver.find_element("id", self.CouponButton)
        element.click()
    def click_gold_star(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.GoldStarButton))
        )
        element = self.driver.find_element("id", self.GoldStarButton)
        element.click()
    def click_plan1(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("xpath", self.Plan1Button))
        )
        element = self.driver.find_element("xpath", self.Plan1Button)
        element.click()
    def click_plan2(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("xpath", self.Plan2Button))
        )
        element = self.driver.find_element("xpath", self.Plan2Button)
        element.click()
    def click_pay(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("xpath", self.PayButton))
        )
        element = self.driver.find_element("xpath", self.PayButton)
        element.click()


    def find_stream_left_top(self):
        element_color = self.driver.find_element(AppiumBy.ID, self.Stream)
        x = element_color.location['x']
        y = element_color.location['y']
        '''
        w = element_color.size['width']
        h = element_color.size['height']
        center_x = x + w // 2
        center_y = y + h // 2
        '''
        return x, y


    def is_color_in_range(self, x, y, color_range):
        """
        Take a screenshot and check if the pixel at coordinates (x, y) is within the given RGB color range.。

        :param y: vertical coordinate of the pixel to check
        :param x: horizontal coordinate of the pixel to check
        :param color_range: color range, ((R_min, G_min, B_min), (R_max, G_max, B_max))
        :return: True or False
        """
        screenshot_path = "screen.png"
        self.driver.save_screenshot(screenshot_path)

        img = Image.open(screenshot_path)
        pixel = img.getpixel((x, y))  # send back (R, G, B)

        (r_min, g_min, b_min), (r_max, g_max, b_max) = color_range
        r, g, b = pixel[:3]

        in_range = (r_min <= r <= r_max) and (g_min <= g <= g_max) and (b_min <= b <= b_max)
        print(f"Pixel at ({x},{y}) = {pixel}, in range: {in_range}")
        return in_range
