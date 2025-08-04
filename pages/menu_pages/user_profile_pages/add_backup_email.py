from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddBackupEmailPage():
		def __init__(self, driver):
				self.driver = driver

				self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/tvAddBackupEmailTitle"
				self.emailEditText = "com.compal.bioslab.pixsee.pixm01:id/sietBackupEmailField"
				self.doneButton = "com.compal.bioslab.pixsee.pixm01:id/btConfirmAddBackupEmail"
				self.cancelButton = "com.compal.bioslab.pixsee.pixm01:id/btCancelAddBackupEmail"