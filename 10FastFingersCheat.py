import pytesseract
from PIL import ImageGrab
import pyautogui
import time

time.sleep(3)
while True:
    img = ImageGrab.grab((340, 235, 1240, 285)) # don't forget to modify this !
    text = pytesseract.image_to_string(img)
    arr = text.split(' ')
    for i in arr:
        pyautogui.typewrite(i)
        pyautogui.typewrite(' ')
    time.sleep(0.5)