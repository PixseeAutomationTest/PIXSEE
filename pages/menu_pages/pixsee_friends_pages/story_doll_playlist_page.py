from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages.base as base

class StoryDollPlaylistPage:
	def __init__(self, driver):
		self.driver = driver

		self.musicList = "com.compal.bioslab.pixsee.pixm01:id/rv_dolls_musics"

		self.dollNameText = "com.compal.bioslab.pixsee.pixm01:id/tvCoverTitle"

		self.backButton = "com.compal.bioslab.pixsee.pixm01:id/ibBackToDollsHome"
		self.settingButton = "com.compal.bioslab.pixsee.pixm01:id/ib_doll_toolbar_settings"
		self.playAlbumButton = "com.compal.bioslab.pixsee.pixm01:id/btPlayAlbum"
		self.repeatButton = "com.compal.bioslab.pixsee.pixm01:id/ibRepeatAlbum"


