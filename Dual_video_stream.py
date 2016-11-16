import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame',640,480)

cv2.namedWindow('frame2',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame2',640,480)

while True:
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    

    cv2.imshow('frame',frame)
    cv2.imshow('frame2',frame2)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
