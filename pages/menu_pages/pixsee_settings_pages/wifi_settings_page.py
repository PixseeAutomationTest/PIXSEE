from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class WifiSettingsPage():
    def __init__(self, driver):
        self.driver = driver
        self.PopUpTitle = "com.compal.bioslab.pixsee.pixm01:id/tvTitleResetWifiAct"
        self.PopUpOk = "com.compal.bioslab.pixsee.pixm01:id/btnResetWifiOk"
        self.PopUpCancel = "com.compal.bioslab.pixsee.pixm01:id/btnResetWifiCancel"
        self.X = "com.compal.bioslab.pixsee.pixm01:id/ibCloseConnectWifiAct"
        self.Header = "com.compal.bioslab.pixsee.pixm01:id/tvTitleConnectWifiAct"
        self.WifiName = "com.compal.bioslab.pixsee.pixm01:id/etNetworkName"
        self.Description = "com.compal.bioslab.pixsee.pixm01:id/tvNetworkLegend"
        self.Password = "com.compal.bioslab.pixsee.pixm01:id/tieNetworkPassword"
        self.Next = "com.compal.bioslab.pixsee.pixm01:id/btnConnectWifi"
        self.QuitDialog = "com.compal.bioslab.pixsee.pixm01:id/tvTitleDialog"
        self.Yes = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveDialog"
        self.No = "com.compal.bioslab.pixsee.pixm01:id/btnNegativeDialog"
        self.EmptyDialog = "com.compal.bioslab.pixsee.pixm01:id/tvtitleAlertDialog"
        self.EmptyDialogYes = "com.compal.bioslab.pixsee.pixm01:id/btnPositiveAlertDialog"
        self.SearchingDevice = "com.compal.bioslab.pixsee.pixm01:id/tvTitle"

    def is_in_wifi_popup_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.PopUpTitle))
            )
            return True
        except :
            return False
    def is_in_wifi_settings_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Header))
            )
            return True
        except  :
            return False
    def is_in_wifi_quit_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.QuitDialog))
            )
            return True
        except :
            return False
    def is_in_wifi_password_empty_dialog(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.EmptyDialog))
            )
            return True
        except :
            return False
    def is_in_wifi_searching_device(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.SearchingDevice))
            )
            return True
        except :
            return False

    def header_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Header))
            )
            element = self.driver.find_element("id", self.Header)
            return element.text
        except :
            return None
    def description(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Description))
            )
            element = self.driver.find_element("id", self.Description)
            return element.text
        except :
            return None
    def pop_up_title_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.PopUpTitle))
            )
            element = self.driver.find_element("id", self.PopUpTitle)
            return element.text
        except :
            return None
    def pop_up_ok_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.PopUpOk))
            )
            element = self.driver.find_element("id", self.PopUpOk)
            return element.text
        except :
            return None
    def pop_up_cancel_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.PopUpCancel))
            )
            element = self.driver.find_element("id", self.PopUpCancel)
            return element.text
        except :
            return None
    def quit_dialog_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.QuitDialog))
            )
            element = self.driver.find_element("id", self.QuitDialog)
            return element.text
        except :
            return None
    def quit_dialog_yes_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.Yes))
            )
            element = self.driver.find_element("id", self.Yes)
            return element.text
        except :
            return None
    def quit_dialog_no_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.No))
            )
            element = self.driver.find_element("id", self.No)
            return element.text
        except :
            return None
    def empty_dialog_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.EmptyDialog))
            )
            element = self.driver.find_element("id", self.EmptyDialog)
            return element.text
        except :
            return None
    def empty_dialog_yes_text(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("id", self.EmptyDialogYes))
            )
            element = self.driver.find_element("id", self.EmptyDialogYes)
            return element.text
        except :
            return None

    def click_x(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.X))
        )
        element = self.driver.find_element("id", self.X)
        element.click()
    def click_next(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Next))
        )
        element = self.driver.find_element("id", self.Next)
        element.click()
    def click_wifi_name(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.WifiName))
        )
        element = self.driver.find_element("id", self.WifiName)
        element.click()
    def click_pop_up_ok(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.PopUpOk))
        )
        element = self.driver.find_element("id", self.PopUpOk)
        element.click()
    def click_pop_up_cancel(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.PopUpCancel))
        )
        element = self.driver.find_element("id", self.PopUpCancel)
        element.click()
    def click_quit_yes(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Yes))
        )
        element = self.driver.find_element("id", self.Yes)
        element.click()
    def click_quit_no(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.No))
        )
        element = self.driver.find_element("id", self.No)
        element.click()
    def click_empty_dialog_yes(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.EmptyDialogYes))
        )
        element = self.driver.find_element("id", self.EmptyDialogYes)
        element.click()


    def input_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.Password))
        )
        element = self.driver.find_element("id", self.Password)
        element.clear()
        element.send_keys(password)




