import pyautogui, time

pyautogui.FAILSAFE = False


time.sleep(5)

f = open("text", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
