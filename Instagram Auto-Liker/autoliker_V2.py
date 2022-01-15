import pyautogui
import time

n = int(input("Number of Posts to like : "))

time.sleep(7)

for i in range(n):
    position = pyautogui.locateOnScreen("pic.png", confidence=0.95)
    print(position)
    if position is not None:
        pyautogui.moveTo(position[0]+13, position[1]+7)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.press("right")
        time.sleep(0.5)
    else:
        time.sleep(3)