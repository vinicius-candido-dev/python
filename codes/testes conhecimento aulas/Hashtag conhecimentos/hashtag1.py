import pyautogui
import time
import pandas openpyxl
tkk = 'https://www.tiktok.com/'
pyautogui.PAUSE = 0.8
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(tkk)
pyautogui.press('enter')
time.sleep(8)
pyautogui.click(156 ,1689)

