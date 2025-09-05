


# PIXSEE 自動化測試使用者完整操作流程
---
## 這個是跑整體的BAT檔案說明，可以直接先去看[下載篇](https://docs.google.com/document/d/1ItL32rgG6MNTK-BSXAnEmVTSNSz00fPfkFMwrz_ic6Q/edit?tab=t.0)就可以跳過1-4步驟

## 1️⃣ 下載專案

1. 使用者先安裝 **Git**

   * Windows 可下載 [Git for Windows](https://git-scm.com/download/win)
   * 安裝時選擇 **Git Bash** 與 **Git 命令可加入 PATH**

2. 打開 **Git Bash** 或 **PowerShell**，Clone 專案：

   ```bash
   git clone https://github.com/PixseeAutomationTest/PIXSEE.git
   cd PIXSEE
   ```

---

## 2️⃣ 安裝 Python

1. 下載 [Python 3.10+](https://www.python.org/downloads/windows/)
2. 安裝時勾選 **Add Python to PATH**
3. 確認安裝成功：

   ```cmd
   python --version
   pip --version
   ```

---

## 3️⃣ 安裝 Appium

1. 安裝 Node.js（Appium 需要 Node）

   * [Node.js 官網](https://nodejs.org/)
   * 安裝完成後確認：

     ```cmd
     node -v
     npm -v
     ```

2. 安裝 Appium：

   ```cmd
   npm install -g appium
   ```

3. 安裝 Appium Inspector（可選，用於檢查元素）

---

## 4️⃣ 確認 Android 環境

1. 安裝 **ADB（Android SDK Platform Tools）**

   * [下載連結](https://developer.android.com/studio/releases/platform-tools)
   * 把 `platform-tools` 路徑加到 **環境變數 PATH**

2. 連接手機並確認：

   ```cmd
   adb devices
   ```

   * 會看到手機 ID，例如 `2A141FDH2009E8`

---

## 5️⃣ 使用批次檔跑測試

## 可以直接下載整個ZIP在解壓縮

### 執行步驟：

1. 雙擊 `run.bat` 或在 cmd/PowerShell 執行：

   ```cmd
   cd PIXSEE
   run.bat
   ```

2. 批次檔會依序詢問：

   * **裝置名稱（adb devices ID）** → 例如 `2A141FDH2009E8`
   * **帳號** → 例如 `jackypixsee02@gmail.com`記得同時測試多台時不要用同一個帳號
   * **密碼** → 例如 `@Aa12345`

3. 批次檔會檢查是否第一次跑，如果第一次會安裝 `requirements.txt` 裡的套件。

4. 批次檔會啟動 **Appium server**（打開新視窗），**要等appium跑完顯示ACTIVE之後才能做下一步**(這個會在新視窗中看到)下一步再回到原本的視窗

5. 批次檔會詢問：

   ```
   Run (1) Subscription test or (2) Unsubscription test? Enter 1 or 2:
   ```

   * 輸入 `1` → 跑訂閱測試
   * 輸入 `2` → 跑取消訂閱測試

6. 測試開始跑，Python 會自動讀取環境變數，不會改 `base.py`。

7. 測試跑完後批次檔會停在 `pause`，方便查看測試結果。
   
8. 檔案要去results資料夾看(如果要測單項還是要去看[README_PYCHARM](README_PYCHARM.md))

---

## 6️⃣ 注意事項

1. **第一次跑**要確保手機已連線並授權 USB 調試
2. **Appium server** 必須啟動，否則測試無法連線手機
3. **每次跑不同裝置/帳號**只要重新輸入環境變數即可
4. **Python 套件**只需安裝一次，之後就不用重裝


