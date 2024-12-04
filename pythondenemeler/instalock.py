import pyautogui
import time
import keyboard

x, y = 185, 850
a, b = 950, 755

time.sleep(2)

while True:
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(a, b, duration=0.1)
    pyautogui.click()
    
    if keyboard.is_pressed("esc"):
        break