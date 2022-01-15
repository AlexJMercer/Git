import pyautogui as pt
from time import sleep

# Point(x=512, y=468)

class Command:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def nav_to_heart(self, speed):
        position = pt.locateOnScreen("pic.png", confidence=0.8)
        self.x = position[0] - 547
        self.y = position[1] + 10
        pt.moveTo(self.x, self.y, duration=speed)
        print("Navigating...")
        sleep(0.1)


commands = Command(0, 0)

for i in range(40):
    try:
        commands.nav_to_heart(1)
        if pt.pixelMatchesColor(pt.position().x, pt.position().y, (237, 73, 86), tolerance=10):
            pt.scroll(-800)
            sleep(2)
        else:
            pt.click()
            sleep(0.5)
    except Exception as e:
        print(e)
        pt.scroll(-800)
        sleep(0.2)