import cv2
import numpy as np


img = cv2.imread('soccerball.jpg',cv2.IMREAD_COLOR) 

img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
# (image, greater than 220, then converted to 255, if less than then converted to black


cv2.imshow('gray',img2gray)
cv2.imshow('img',img)
cv2.imshow('mask',mask)


cv2.waitKey(0)
##    cv2.imshow('gray', gray)
    

cv2.destroyAllWindows()
