import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows, cols,_ = frame.shape

x_medium = int(cols/2)
center = int(cols/2)

position = 90

while True:
    ret, frame = cap.read()
    image = cv2.rotate(frame,cv2.cv2.ROTATE_180)

    hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #red color
    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv_frame,low_red,high_red)
    (contours,_)  =  cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted (contours, key=lambda x:cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        cv2.rectangle (image, (x , y), (x + w, y + h), (0, 255, 0), 2)
        x_medium = int((x + x + w) / 2)
        cv2.line(image,(x_medium, 0), (x_medium, 480),(0, 255, 0), 2)
        break

    #cv2.imshow("mask",red_mask)
    cv2.imshow("output",image)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.releate()
cv2.destroyAllWindow()