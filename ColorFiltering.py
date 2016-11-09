import cv2
import numpy as np

# used a yellow sticky note on my cheek
cap = cv2.VideoCapture(0) 

while True:
    _, frame = cap.read() # the underscore is just a useful to notate that we don't care about that value
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_yel = np.array([30,30,100]) #[0-179, 0-255, 0-255]
    upper_yel = np.array([90,200,200]) 

    mask = cv2.inRange(hsv, lower_yel, upper_yel)# mask will result in a 1 or 0
    res = cv2.bitwise_and(frame, frame, mask = mask)# bitwise and is saying where there are colors in the
    # frame and the mask is 1 show the colors in the frame

    cv2.imshow('frame',frame)
##    cv2.imshow('hsv', hsv)
    cv2.imshow('res',res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
