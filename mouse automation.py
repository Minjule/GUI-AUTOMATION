import pyautogui
import time
print(pyautogui.size())

#pyautogui.moveTo(100, 100, duration = 1)
while(1):
    time.sleep(20)
    print(pyautogui.size())
    pyautogui.scroll(-3500)