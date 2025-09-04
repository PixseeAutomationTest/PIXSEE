

---


# 🌟 PIXSEE AUTOMATION

## 🚀 啟動步驟
1. **Clone 專案** → 把這個 GitHub 連結到自己的電腦  
2. **設定裝置名稱** → 到 `base.py` 改 `capabilities.device_name = 你的device`  
   - ✅ 用 `adb devices` 查裝置 ID（在 PowerShell 輸入）  
3. **設定帳號/密碼**  
   - ⚠️ 如果兩台機器同時跑，**不能用同一組帳號**  
4. 打開 **PyCharm Terminal**  
5. 第一次跑的時候輸入：  
   ```bash
   pip install -r requirements.txt
    ```

6. 確認檔案裡面 **沒有紅色波浪線** 🪱
7. 打開 PowerShell，啟動 Appium：

   ```bash
   appium --use-plugins=inspector --allow-cors
   ```
8. 在 PyCharm 選好要執行的檔案並執行：

   * 📌 `subscription_main.py` → 測 **訂閱**（要手動先在手機按訂閱）
   * 📌 `unsubscription_main.py` → 測 **未訂閱**（要確認手機已取消訂閱）
9. 查看 PyCharm 是否有跑出 **第一個 test** ✅

---

## 📖 [說明文件](https://drive.google.com/drive/folders/1aXvqvS8GBj83i1jdijVb5sZESfhnSr2a?usp=drive_link)

---

## 📂 檔案說明

### 📁 `pages/`

每個頁面都有獨立的 **Page Object**，主要提供：

* **點擊功能**（click\_xxx）
* **文字檢查**（get\_xxx\_text）
* **狀態檢查**（is\_xxx, has\_xxx）
* **進階操作**（滑動、日期選取、刪除驗證…）

👉 **新增功能重點：**

#### 🔸 `album_page.py`

* **縮圖操作**

   `click_recent_thumbnails(count)` → 點選多張最新縮圖
  * `click_specific_thumbnail(index)` → 點選特定索引的縮圖
  * `delete_and_verify_thumbnail(index)` → 刪除縮圖並驗證是否消失
* **日期範圍**

  * `find_thumbnails_between_dates(date)` → 找出目標日期的縮圖
  * `find_date_range(date)` → 檢查日期是否在範圍內
  * `count_photos_today()` → 計算今天有幾張照片
* **寶寶生日**

  * `select_baby_birthday(locale, year, month, day)` → 打開日曆並選日期

#### 🔸 `photo_page.py`

* **備註功能**

  * `input_note()` → 輸入備註
  * `get_note_text()` / `note_input_hint()` → 檢查備註文字
  * `get_chart_count()` → 取得字數限制狀態
* **照片操作**

  * `click_trash()` / `click_dialog_delete()` → 刪除照片
  * `click_share()` → 分享
  * `click_download()` → 下載
  * `click_eye()` → 隱藏 / 顯示
* **檢查**

  * `is_in_photo_page()` → 確認是否在單張照片頁面
  * `find_numbers_in_text(text)` → 從字串中抓取數字（例如容量/張數）

#### 🔸 `edit_baby_profile_page.py`

* **基本資訊**

  * `input_baby_name(new_name)` → 修改寶寶名字（自動避免重複）
  * `select_avatar(number)` → 換大頭貼（選擇相簿照片）
  * `select_baby_birthday(locale, year, month, day)` → 設定生日
* **選單操作**

  * `select_nation(number=51)` → 選擇國籍（預設 Taiwan）
  * `select_relative(number=2)` → 選擇關係（預設 Mommy）
* **刪除 / 對話框**

  * `click_delete_baby_profile()` → 按下刪除寶寶資料
  * `get_dialog_title()` / `get_dialog_message()` / `get_dialog_warning_message()` → 取得對話框文字
  * `click_dialog_yes()` / `click_dialog_no()` / `click_dialog_cancel()` → 操作確認對話框
* **檢查**

  * `is_in_edit_baby_profile_page()` → 確認是否在編輯頁
  * `has_calendar()` / `has_selection_list()` / `has_dialog()` → 元素存在檢查

---

### 📁 `tests/`

* 每個測試檔對應一組 **testcase**
* 所有測試都會依序跑：

  * 🛠️ `setUp()` → 測試開始前執行
  * 🧹 `tearDown()` → 測試結束後執行
* ⚠️ **目前無法檢查圖片是否正確顯示**

### 📁 `results/`

* 存放測試結果
* 預設檔名 = **測試日期**（可自行修改）
* 支援 **3 種語言**

### ▶️ `xxx_main.py`

* 測試進入點
* 可調整：

  * **輸出檔案名稱**
  * **測試項目 / 順序**
* 目前有 **2 個 main**

### ⚙️ `base.py`

* 所有 `test.py` **繼承**的核心 class
* 功能：

  * 降低重複 code
  * 提供常用方法（回上一頁、滑動、讀字串表...）

### 📑 `Pixsee App translations - master_202403.csv`

* 字串表 (需與 `pages/`、`tests/`、`results/` 同層)
* 常用 `base.get_string("ID")` 來取字串

---

## 🔍 功能操作小技巧

### 1️⃣ 找不到 ID，用 XPath 的技巧

當 ID 找不到、但 XPath 包含中英文差異時 →
👉 先找「上層 ID」，再往下找子元素 XPath

範例（Pixsee Cloud → 釋出空間）：

```xpath
//android.widget.TextView[@resource-id="com.compal.bioslab.pixsee.pixm01:id/tvPlanDefinition" and @text="清除25%，保留約604.6 MB"]
```

📸 範例截圖： <img width="848" height="371" alt="image" src="https://github.com/user-attachments/assets/5df151f3-9e5c-4dba-bc88-8ee40bd4ac55" />

### 2️⃣ 程式碼示例

```python
def dialog_delete_25_percent_text(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(("id", self.ListUpLayer))
    )
    uplayer = self.driver.find_element("id", self.ListUpLayer)
    elements = uplayer.find_elements("xpath", self.List)
    return elements[0].text
```


