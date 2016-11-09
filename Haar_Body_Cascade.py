import cv2
import numpy as np

# private vars
scale = 1.05


body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')


cap = cv2.VideoCapture('Shop_Test_7_12_16.avi')

while True:
    ret,frame = cap.read()
    if (cv2.waitKey(50) & 0xFF == ord('q')) or ret ==False:
        break

    body = body_cascade.detectMultiScale(frame, scale, 3, 0,(100,150))
    for (x,y,w,h) in body:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.rectangle(frame, (0,0), (639,479), (255,0,0),2)

        
##        roi_gray = gray[y:y+h, x:x+w] # roi is y then x instead of x then y
##        roi_color = frame[y:y+h, x:x+w]

    
    cv2.imshow('Color', frame)

cap.release()
cv2.destroyAllWindows()
