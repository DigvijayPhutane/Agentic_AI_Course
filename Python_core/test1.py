import pyautogui
import time

TEXT = "AAJA NA"
COUNT = 2000          # reduce this for safety
DELAY_BETWEEN = 0.1   # seconds between messages

print("You have 10 seconds to click the input box...")
# time.sleep(10)

for i in range(COUNT):
    pyautogui.typewrite(TEXT)
    pyautogui.press("enter")
    time.sleep(DELAY_BETWEEN)
 
