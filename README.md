# **PIXSEE AUTOMATION** 
## 啟動步驟
1. 把這個github連結到自己的電腦
2. 先到base那邊改capabilities.device_name = 你的device(可以在powershell裡面打adb devices來查)
3. 再滑下去改account和password (如果有兩台機器同時要跑不能用同一個帳號)
4. 打開pycharm terminal
5. 第一次跑的時候要輸入pip install -r requirements.txt
6. 確認檔案裏面都沒有毛毛蟲紅線
7. 打開powershell輸入appium --use-plugins=inspector --allow-cors
8. pycharm 這邊選好要執行的檔案看是要測訂閱或是未訂閱並按下執行，如果是訂閱的話需要手動先在手機按下訂閱，如果是未訂閱需要檢查手機是否取消訂閱了
9. 看pycharm那邊有沒有第一個test出現

### [說明文件](https://drive.google.com/drive/folders/1aXvqvS8GBj83i1jdijVb5sZESfhnSr2a?usp=drive_link)
## 檔案說明
### pages 
此資料夾裡，根據每個頁面分別做成一個 python 檔，裡面的 function 太多，不一一介紹，大部分皆為按特定按鈕或取得某元素的文字，若非此兩類，請看程式註解或 function 名字。

### tests
此資料夾裡，根據 testcase 所撰寫的自動化測試程式檔，測試項目皆為 test_xxx 當作開頭，執行任何一個測試項目前，皆會先執行 setUp() ，執行結束後，皆會執行 tearDown()。目前無法檢查圖片是否顯示正確。

### results
此資料夾裡，存放著每次測試的結果，總共有三個語言，可以自行更改檔名，每次存檔的名字預設為測試當天日期。

### xxx_main.py
執行程式的地方，可在最後改輸出檔的名字，中間調整測試的項目及順序。目前有2個 main

### base.py
為所有 test.py 都繼承了此檔案裡的 class ， 主要是為了減少 code 的重複性，也有一些常用的 function，可以使用在 test.py 裡，如:回上一頁、上下左右滑、從字串表裡取得字串。

### Pixsee App translations - master_202403.csv
此為字串表需要放在專案資料夾裡，跟 pages 、 results 、 tests 同一層。最常用到 base 裡的 get_string(“ID”)，ID 必須對表找。

## 一些功能說明
1.如果找不到id而且xpath又是裡面包含會因為中英文不一樣的時候可以先找上層的id，再往下找之下的xpath前面幾個字
像是pixsee cloud裡面的釋出空間有好幾個項目，但是隨便抓一個xpath會長這樣:
//android.widget.TextView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tvPlanDefinition" and @text="清除25%，保留約604.6 MB"]
<img width="848" height="371" alt="image" src="https://github.com/user-attachments/assets/5df151f3-9e5c-4dba-bc88-8ee40bd4ac55" />
'''python 
    def dialog_delete_25_percent_text(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("id", self.ListUpLayer))
        )
        uplayer = self.driver.find_element("id", self.ListUpLayer)
        elements = uplayer.find_elements("xpath", self.List)
        return elements[0].text
'''

