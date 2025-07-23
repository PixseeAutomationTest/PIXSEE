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
            EC.presence_of_element_located(("id", self.emailField))
        )
        element = self.driver.find_element("id", self.emailField)
        element.clear()
        element.send_keys(email)

    def _input_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.passwordField))
        )
        element = self.driver.find_element("id", self.passwordField)
        element.clear()
        element.send_keys(password)

    def _click_signin(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.signInButton))
        )
        element = self.driver.find_element("id", self.signInButton)
        element.click()

    def login(self, email, password):
        self._input_email(email)
        self._input_password(password)
        self._click_signin()

    def get_email_error_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.emailErrorText))
            )
            element = self.driver.find_element("id", self.emailErrorText)
            return element.text
        except AssertionError :
            return None

    def get_password_error_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.passwordErrorText))
            )
            element = self.driver.find_element("id", self.passwordErrorText)
            return element.text
        except AssertionError:
            return None