import cv2
import numpy as np

camera = cv2.VideoCapture(1)
cv2.namedWindow("cam_display",cv2.WINDOW_NORMAL)

x = 200
y = 200
r = 25

while True:
    ret, frame = camera.read()
    new_im = frame.copy()


    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,255,0), 3)
##    contours0, hierarchy = cv2.findContours( img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
##    moments  = [cv2.moments(cnt) for cnt in contours0]
    
    cv2.circle(frame,(x,y),r,(0,255,0),3)



    cv2.imshow('Adaptive threshold',thresh)
    cv2.imshow('cam_display',frame)
    cv2.imshow('frame copy',new_im)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
