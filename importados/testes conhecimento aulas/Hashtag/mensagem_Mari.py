import pyautogui
import time
wtt = 'https://web.whatsapp.com/'
msg = 'hiiii Marina, irmã de Vini'
pyautogui.PAUSE = 1
#abrir chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(wtt)
pyautogui.press('enter')
time.sleep(8)
pyautogui.click(338,740)
for i in range(0,10):
    time.sleep(1)
    pyautogui.write(msg)
    pyautogui.press('enter')
