import cv2 as cv
import numpy as np
import os
from PIL import Image
from time import time, sleep
from windowcapture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter
import pyautogui
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pytesseract
import re



def clickeod():
    print("niguz")
    # Change the working directory to the folder this script is in.
    # Doing this because I'll be putting the files from each video in their own folder on GitHub
    # os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # initialize the WindowCapture class
    wincap = WindowCapture('BlueStacks')

    # load the trained model

    boe = 0.5
    banan = r"C:\Users\kalab\Desktop\Screenshot_29.jpg"
    # load an empty Vision class
    vision_gold = Vision(banan)
    # 29-34, 37, 39

    # vision_gold.init_control_gui()
    #hsv_filter = HsvFilter(2, 0, 0, 6, 255, 255, 0, 0, 0, 0)
    hsv_filter = HsvFilter(31, 114, 0, 88, 255, 255, 0, 0, 40, 0)

    loop_time = time()
    can_mine = 1
    while (True):

        screenshot = wincap.get_screenshot()

        processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
        rectanglesi = vision_gold.find(processed_image, boe)
        output_image_gold = vision_gold.draw_rectangles(screenshot, rectanglesi)

        cv.imshow('Processed', processed_image)
        cv.imshow('Matches_gold', output_image_gold)

        if can_mine == 1:
            banan = r"C:\Users\kalab\Desktop\Screenshot_29.jpg"
            vision_gold = Vision(banan)
            boe = 0.5
            screenshot = wincap.get_screenshot()
            processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
            rectanglesi = vision_gold.find(processed_image, boe)
            if len(rectanglesi) > 0:
                targets = vision_gold.get_click_points(rectanglesi)
                target = wincap.get_screen_position(targets[0])
                sleep(3)
                pyautogui.moveTo(x=target[0] + 50, y=target[1])
                pyautogui.moveTo(x=target[0], y=target[1] + 60)
                pyautogui.moveTo(x=target[0] - 50, y=target[1])
                pyautogui.moveTo(x=target[0], y=target[1] - 60)

                attack()



        # debug the loop rate
        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            can_mine = 0
            break

    print('Done.')



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 741, 241))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(clickeod)
        #self.pushButton.clicked.connect(MainWindow.close)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, -40, 761, 121))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 40, 241, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\kalab\\Downloads\\python_test\\Lib\\site-packages\\qt5_applications\\Qt\\bin\\../../Users/kalab/Users/kalab/Downloads/images.png"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "S T A R T"))
        self.label.setText(_translate("MainWindow", "שלום אדון זר ומטריד לידיעתך אתה ממש מפגר שהורדת את הקובץ הזה מאדם זר אחר. קיצר תלחץ על הכפתור יא גיי "))


def attack():
        wincap = WindowCapture('BlueStacks')
        hsv_filter = HsvFilter(31, 114, 0, 88, 255, 255, 0, 0, 40, 0)
        banan = r"C:\Users\kalab\Desktop\Screenshot_30.jpg"
        vision_gold = Vision(banan)
        boe = 0.8
        screenshot = wincap.get_screenshot()
        processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
        rectanglesi = vision_gold.find(processed_image, boe)
        if len(rectanglesi) > 0:
            targets = vision_gold.get_click_points(rectanglesi)
            target = wincap.get_screen_position(targets[0])
            sleep(0.5)
            pyautogui.click(x=target[0], y=target[1])

        banan = r"C:\Users\kalab\Desktop\Screenshot_31.jpg"
        vision_gold = Vision(banan)
        boe = 0.8
        screenshot = wincap.get_screenshot()
        processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
        rectanglesi = vision_gold.find(processed_image, boe)
        if len(rectanglesi) > 0:
            targets = vision_gold.get_click_points(rectanglesi)
            target = wincap.get_screen_position(targets[0])
            sleep(0.5)
            pyautogui.click(x=target[0], y=target[1])

        banan = r"C:\Users\kalab\Desktop\Screenshot_43.jpg"
        vision_gold = Vision(banan)
        boe = 0.8
        sleep(2)
        screenshot = wincap.get_screenshot()
        processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
        rectanglesi = vision_gold.find(processed_image, boe)
        if len(rectanglesi) > 0:
            targets = vision_gold.get_click_points(rectanglesi)
            target = wincap.get_screen_position(targets[0])
            sleep(0.5)
            pyautogui.click(x=target[0], y=target[1])

        banan = r"C:\Users\kalab\Desktop\Screenshot_91.jpg"
        vision_gold = Vision(banan)
        boe = 0.8
        sleep(2)
        screenshot = wincap.get_screenshot()
        processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
        rectanglesi = vision_gold.find(processed_image, boe)
        if len(rectanglesi) > 0:
            targets = vision_gold.get_click_points(rectanglesi)
            target = wincap.get_screen_position(targets[0])
            sleep(0.5)
            pyautogui.click(x=target[0], y=target[1])

        banan = r"C:\Users\kalab\Desktop\Screenshot_90.jpg"
        vision_gold = Vision(banan)
        boe = 0.8
        sleep(2)
        screenshot = wincap.get_screenshot()
        processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
        rectanglesi = vision_gold.find(processed_image, boe)
        if len(rectanglesi) > 0:
            sleep(1560)

        banan = r"C:\Users\kalab\Desktop\Screenshot_33.jpg"
        vision_gold = Vision(banan)
        boe = 0.8
        screenshot = wincap.get_screenshot()
        processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
        rectanglesi = vision_gold.find(processed_image, boe)
        if len(rectanglesi) > 0:
            targets = vision_gold.get_click_points(rectanglesi)
            target = wincap.get_screen_position(targets[0])
            sleep(0.5)
            pyautogui.click(x=target[0], y=target[1])

        banan = r"C:\Users\kalab\Desktop\Screenshot_34.jpg"
        vision_gold = Vision(banan)
        boe = 0.7
        screenshot = wincap.get_screenshot()
        processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
        rectanglesi = vision_gold.find(processed_image, boe)
        if len(rectanglesi) > 0:
            targets = vision_gold.get_click_points(rectanglesi)
            target = wincap.get_screen_position(targets[0])
            sleep(0.5)
            pyautogui.click(x=target[0], y=target[1])


        banan = r"C:\Users\kalab\Desktop\Screenshot_41.jpg"
        vision_gold = Vision(banan)
        boe = 0.7
        sleep(2)
        screenshot = wincap.get_screenshot()
        processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
        rectanglesi = vision_gold.find(processed_image, boe)
        if len(rectanglesi) > 0:
            targets = vision_gold.get_click_points(rectanglesi)
            target = wincap.get_screen_position(targets[0])
            pyautogui.click(x=target[0], y=target[1])
            sleep(6)

            pytesseract.pytesseract.tesseract_cmd = r"C:\Users\kalab\Documents\MEGAsync Downloads\Tesseract-OCR\tesseract.exe"
            path = 'C:/Users/kalab/Pictures/result.jpg'

            x1 = 110
            y1 = 170
            width = 180
            height = 160

            x2 = x1 + width
            y2 = y1 + height

            pyautogui.screenshot(path)

            im = Image.open(path)
            im = im.crop((x1, y1, x2, y2))
            im.save(path)


            bruh = pytesseract.image_to_string(path, config="-c tessedit_char_whitelist=0123456789")
            print(bruh)
            print("-----------------------------")
            if len(bruh.splitlines()) > 2 and len(bruh.splitlines()) < 5:
                bruh = bruh.split("\n")[1]
                bruh = bruh.replace(" ", "")
                if bool(bruh):
                    if bool(re.search(r'\d', bruh)):
                        bruh = int(bruh)
                    print(bruh)
                    print("-----------------------------")
                else:
                    bruh = 0
                    print(bruh)
                    print("-----------------------------")


            else:
                bruh = 0
                print(bruh)
                print("-----------------------------")

            while bruh < 300000:
                banan = r"C:\Users\kalab\Desktop\Screenshot_37.jpg"
                vision_gold = Vision(banan)
                boe = 0.5
                screenshot = wincap.get_screenshot()
                processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
                rectanglesi = vision_gold.find(processed_image, boe)
                if len(rectanglesi) > 0:
                    targets = vision_gold.get_click_points(rectanglesi)
                    target = wincap.get_screen_position(targets[0])
                    sleep(5)
                    pyautogui.click(x=target[0], y=target[1])
                    sleep(6)
                    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\kalab\Documents\MEGAsync Downloads\Tesseract-OCR\tesseract.exe"
                    path = 'C:/Users/kalab/Pictures/result.jpg'

                    x1 = 110
                    y1 = 170
                    width = 180
                    height = 160

                    x2 = x1 + width
                    y2 = y1 + height

                    pyautogui.screenshot(path)

                    im = Image.open(path)
                    im = im.crop((x1, y1, x2, y2))
                    im.save(path)

                    bruh = pytesseract.image_to_string(path, config="-c tessedit_char_whitelist=0123456789")
                    print(bruh)
                    print("-----------------------------")
                    if len(bruh.splitlines()) > 2 and len(bruh.splitlines()) < 5:
                        bruh = bruh.split("\n")[1]
                        bruh = bruh.replace(" ", "")
                        if bool(bruh):
                            if bool(re.search(r'\d', bruh)):
                                bruh = int(bruh)
                            print(bruh)
                            print("-----------------------------")
                        else:
                            bruh = 0
                            print(bruh)
                            print("-----------------------------")


                    else:
                        bruh = 0
                        print(bruh)
                        print("-----------------------------")
            print("we have found the one!!!")
            sleep(1)

            banan = r"C:\Users\kalab\Desktop\Screenshot_42.jpg"
            vision_gold = Vision(banan)
            boe = 0.8
            screenshot = wincap.get_screenshot()
            processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
            rectanglesi = vision_gold.find(processed_image, boe)
            if len(rectanglesi) > 0:
                targets = vision_gold.get_click_points(rectanglesi)
                target = wincap.get_screen_position(targets[0])
                sleep(0.5)
                pyautogui.click(x=target[0], y=target[1])


            banan = r"C:\Users\kalab\Desktop\Screenshot_39.jpg"
            vision_gold = Vision(banan)
            boe = 0.7
            sleep(2)
            screenshot = wincap.get_screenshot()
            processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
            rectanglesi = vision_gold.find(processed_image, boe)
            while len(rectanglesi) < 1:
                pyautogui.click(x=330 + 50, y=111 + 50)
                pyautogui.click(x=1479, y=115 + 100)
                pyautogui.click(x=1661, y=673 - 20)
                pyautogui.click(x=159, y=677)
                screenshot = wincap.get_screenshot()
                processed_image = vision_gold.take_out_color(screenshot, hsv_filter)
                rectanglesi = vision_gold.find(processed_image, boe)

            if len(rectanglesi) > 0:
                targets = vision_gold.get_click_points(rectanglesi)
                target = wincap.get_screen_position(targets[0])
                sleep(0.5)
                pyautogui.click(x=target[0], y=target[1])

def build():
    hsv_filter = HsvFilter(2, 0, 0, 6, 255, 255, 0, 0, 0, 0)








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())








