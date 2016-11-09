## EXECUTIVE SUMMARY
# running this code will give outputs that demonstrate that to resize an
##image to a smaller pixel size the image should first be loaded from the camera
##at normal settings from that camera. Then the image should be resized, then the
##image should be displayed to a named window that is resized to a normal viewing
##size. 


import cv2
import numpy as np

dispWidth_small = 20
dispHeight_small = 20

## proper route: Setting normal capture size (or don't set any and let
## the camera choose a default
dispWidth = 640 ##taken earlier today
dispHeight = 480

cv2.namedWindow("win_normal",cv2.WINDOW_NORMAL)
cv2.resizeWindow("win_normal",640,480)

## proper route: create a named window and set the flag to normal (not autosize)
cv2.namedWindow("win_small",cv2.WINDOW_NORMAL)
cv2.resizeWindow("win_small",640,480)

cv2.namedWindow("win_small_from_cam",cv2.WINDOW_NORMAL)
cv2.resizeWindow("win_small_from_cam",640,480)

## read from camera
camera = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(0)

## setting capture properties, 
camera.set(cv2.CAP_PROP_FRAME_WIDTH, dispWidth)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, dispHeight)

camera2.set(cv2.CAP_PROP_FRAME_WIDTH, dispWidth_small)
camera2.set(cv2.CAP_PROP_FRAME_HEIGHT, dispHeight_small)

try:
    while True:
        ret_1, frame = camera.read()
        ret_2, frame2 = camera2.read()

        ## proper route: resize the image into a new matrix        
        small = cv2.resize(frame, (20,20),0,0) 

                
        print("original size:",np.shape(frame))
        print("small size:", np.shape(small))

        cv2.imshow('frame',frame)
        cv2.imshow('small', small)
        cv2.imshow('win_normal',frame)

        ## proper route: show that new matrix on the normal sized window
        cv2.imshow('win_small',small) 
        
        cv2.imshow('win_small_from_cam',frame2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
except KeyboardInterrupt:
    camera.release()
    cv2.destroyAllWindows()
