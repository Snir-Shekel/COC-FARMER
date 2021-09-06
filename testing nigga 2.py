import cv2
import numpy as np
from windowcapture import WindowCapture
from hsvfilter import HsvFilter



wincap = WindowCapture()


while (1):
    frame = wincap.get_screenshot()



    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)  # modify your thresholds
    inv_mask = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(frame, frame, mask=inv_mask)

    #mask = cv2.inRange(hsv, lower_red, upper_red)
    #inv_mask = cv2.bitwise_not(mask)
    #res = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
    imS1 = cv2.resize(frame, (960, 540))  # Resize image



    cv2.namedWindow("mask", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
    imS2 = cv2.resize(mask, (960, 540))  # Resize image



    cv2.namedWindow("res", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
    imS3 = cv2.resize(res, (960, 540))  # Resize image



    cv2.imshow("frame", imS1)  # Show image
    cv2.imshow("mask", imS2)  # Show image
    cv2.imshow("res", imS3)  # Show image



    #cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    #cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
wincap.release()