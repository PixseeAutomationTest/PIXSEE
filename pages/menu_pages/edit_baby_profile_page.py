from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BabyProfilePage():
    def __init__(self, driver):
        self.driver = driver

        self.pageTitleText = "com.compal.bioslab.pixsee.pixm01:id/toolbar_title"
        self.babyNameEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_name_edx"
        self.returnButton = "com.compal.bioslab.pixsee.pixm01:id/toolbar_back_img"
        self.doneButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_done_tv"
        self.babyPicture = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_picture_img"
        self.genderBoyButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_gender_boy_radio"
        self.genderGirlButton = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_gender_girl_radio"
        self.birthdayEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_birthday_edx"
        self.nationEditText = "com.compal.bioslab.pixsee.pixm01:id/baby_profile_nation_borders"