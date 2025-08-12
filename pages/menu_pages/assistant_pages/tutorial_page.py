from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TutorialPage():
    def __init__(self, driver):
        self.driver = driver
        self.Text = "com.compal.bioslab.pixsee.pixm01:id/tvTutorialTitle"
        self.Skip = "com.compal.bioslab.pixsee.pixm01:id/btSkipTutorial"
        self.Indicator1 = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[1]'
        self.Indicator2 = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[2]'
        self.Indicator3 = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[3]'
        self.Indicator4 = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[4]'
        self.Indicator5 = '//android.widget.HorizontalScrollView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tlTutorial"]/android.widget.LinearLayout/android.widget.LinearLayout[5]'

    def title_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Text))
        )
        element = self.driver.find_element("id", self.Text)
        return element.text
    def skip_button_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Skip))
        )
        element = self.driver.find_element("id", self.Skip)
        return element.text

    def click_skip(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Skip))
        )
        element = self.driver.find_element("id", self.Skip)
        element.click()
    def is_in_tutorial_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Text))
            )
            return True
        except Exception as e:
            print(f"Tutorial Page not found: {e}")
            return False

    def is_in_tutor_first_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("xpath", self.Indicator1))
        )
        light = self.driver.find_element("xpath", self.Indicator1)
        is_in_right = light.get_attribute("selected")
        return is_in_right == "true"
    def is_in_tutor_second_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("xpath", self.Indicator2))
        )
        light = self.driver.find_element("xpath", self.Indicator2)
        is_in_right = light.get_attribute("selected")
        return is_in_right == "true"
    def is_in_tutor_third_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("xpath", self.Indicator3))
        )
        light = self.driver.find_element("xpath", self.Indicator3)
        is_in_right = light.get_attribute("selected")
        return is_in_right == "true"
    def is_in_tutor_fourth_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("xpath", self.Indicator4))
        )
        light = self.driver.find_element("xpath", self.Indicator4)
        is_in_right = light.get_attribute("selected")
        return is_in_right == "true"
    def is_in_tutor_fifth_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("xpath", self.Indicator5))
        )
        light = self.driver.find_element("xpath", self.Indicator5)
        is_in_right = light.get_attribute("selected")
        return is_in_right == "true"
















