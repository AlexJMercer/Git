import pyautogui

import time

n = int(input("Select Number of Entries to fill: "))
num = int(input("Enter the different keystrokes : "))

arr = []
for i in range(num):
    arr[i] = pyautogui.

# Need Pynput or something to get the rest of this done


time.sleep(7)
for i in range(n):
    pyautogui.typewrite(["tab", "tab", "space"])

print(f"{n} entries have been checked !")
