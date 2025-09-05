from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base as base

class DollBoxPage:
	def __init__(self, driver):
		self.driver = driver

		self.backButton = "com.compal.bioslab.pixsee.pixm01:id/ibBack"
		self.dollTypeButton = "com.compal.bioslab.pixsee.pixm01:id/sDollType"
		self.OKButton = "com.compal.bioslab.pixsee.pixm01:id/btnOK"

		'''Doll Type List'''
		self.dollTypeDecisionText = "com.compal.bioslab.pixsee.pixm01:id/text"
		self.dollTypeDecision_xpath = "//android.widget.ListView/android.view.ViewGroup"


