from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():
    def __init__(self, driver):
        self.driver = driver


        self.emailField = "com.compal.bioslab.pixsee.pixm01:id/signInEmailField"
        self.passwordField = "com.compal.bioslab.pixsee.pixm01:id/signInPasswordField"
        self.signInButton = "com.compal.bioslab.pixsee.pixm01:id/btSignIn"
        self.emailErrorText = "com.compal.bioslab.pixsee.pixm01:id/tvSignInEmailError"
        self.passwordErrorText = "com.compal.bioslab.pixsee.pixm01:id/tvSignInPasswordError"

    def _input_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.emailField))
        )
        element = self.driver.find_element(AppiumBy.ID, self.emailField)
        element.clear()
        element.send_keys(email)

    def _input_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.passwordField))
        )
        element = self.driver.find_element(AppiumBy.ID, self.passwordField)
        element.clear()
        element.send_keys(password)

    def _click_signin(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, self.signInButton))
        )
        element = self.driver.find_element(AppiumBy.ID, self.signInButton)
        element.click()

    def login(self, email, password):
        self._input_email(email)
        self._input_password(password)
        self._click_signin()

    def get_email_error_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, self.emailErrorText))
            )
            element = self.driver.find_element("id", self.emailErrorText)
            return element.text
        except:
            return None

    def get_password_error_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, self.passwordErrorText))
            )
            element = self.driver.find_element("id", self.passwordErrorText)
            return element.text
        except:
            return None