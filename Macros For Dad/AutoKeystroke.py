import pyautogui
import time
print("Select Number of Entries to fill: ")
n = int(input())
time.sleep(7)
for i in range(n):
    pyautogui.press(["tab", "tab", "space"])
print(f"{n} entries have been checked !")
