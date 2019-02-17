import pyautogui,pyperclip
from selenium import webdriver
import time

# 한글은 입력안되는 이슈있음
class Sheet:
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get('https://www.google.com')
        enter = input(">>> 로그인후 첫번째 셀에 커서를두고 엔터를 눌러주세요 : ")
        cX, cY = pyautogui.position()
        self.x = cX
        self.y = cY

    def initCursot(self):
        pyautogui.moveTo(self.x, self.y)
        pyautogui.click()

    def write(self,x,y,text):
        self.initCursot()
        for _ in range(x):
            pyautogui.press('right')
        for _ in range(y):
            pyautogui.press('down')
        pyautogui.press('enter')
        #pyautogui.typewrite(text,interval=interval)
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')

    def __del__(self):
        time.sleep(1) # for sheet save time
        self.driver.close()

if __name__ == "__main__":
    S = Sheet()
    S.write(1,2,"반갑다")
    S.write(0, 2, "반갑다22")
    S.write(5, 2, "myname is")



