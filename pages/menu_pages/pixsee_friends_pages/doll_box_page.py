from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages.base as base

class PixseeFriendsPage:
	def __init__(self, driver):
		self.driver = driver
		self.

		self.backButton = "com.compal.bioslab.pixsee.pixm01:id/ibBack"
		self.dollTypeButton = "com.compal.bioslab.pixsee.pixm01:id/sDollType"
		self.OKButton = "com.compal.bioslab.pixsee.pixm01:id/btnOK"

		'''Doll Type List'''
		self.dollTypeDecisionText = "com.compal.bioslab.pixsee.pixm01:id/text"
		self.dollTypeDecision_xpath = "//android.widget.ListView/android.view.ViewGroup"


