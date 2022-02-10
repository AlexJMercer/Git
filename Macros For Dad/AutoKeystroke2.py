# import pyautogui

# import time

# n = int(input("Select Number of Entries to fill: "))
# num = int(input("Enter the different keystrokes : "))

# arr = []
# for i in range(num):
#     arr[i] = pyautogui.

# # Need Pynput or something to get the rest of this done


# time.sleep(7)
# for i in range(n):
#     pyautogui.typewrite(["tab", "tab", "space"])

# print(f"{n} entries have been checked !")

import pyautogui
import time

ch = 'y'
while (ch=='y' or ch=='Y'):
    print("Select Number of Entries to fill: ")
    n = int(input())
    time.sleep(7)
    for i in range(n):
        pyautogui.press(["tab", "tab", "tab", "tab", "space"])
    print(f"{n} entries have been checked !")
    ch = input("\n\nDo you want to continue ? (y/n) : ")

print("\nProcess Exited !")