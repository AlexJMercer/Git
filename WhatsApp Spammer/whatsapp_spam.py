import pyautogui
import time

i=1
num = int(input("Enter number of messages :  "))
text = input("Enter text : ")
time.sleep(5)

while i<=num:
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    i += 1