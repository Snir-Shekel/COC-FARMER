import pygetwindow
import pyautogui
from PIL import Image
from time import time, sleep
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\kalab\Documents\MEGAsync Downloads\Tesseract-OCR\tesseract.exe"

sleep(3)
path = 'C:/Users/kalab/Pictures/result.jpg'



x1 = 730
y1 = 70
width = 100
height = 100


x2 = x1 + width
y2 = y1 + height



pyautogui.screenshot(path)

im = Image.open(path)
im = im.crop((x1,y1,x2,y2))
im.save(path)
im.show(path)


bruh = pytesseract.image_to_string(path, config="-c tessedit_char_whitelist=0123456789")
print(bruh)
bruh = bruh.split("\n")[0]
bruh = bruh.replace(" ","")
print("-----------------------")
print(bruh)
if bool(re.search(r'\d', bruh)):
    bruh = int(bruh)
    if bruh > 99:
        print("lol")





