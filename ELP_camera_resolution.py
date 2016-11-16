## very similar to Resizing_test.py except that this is aimed at experimenting
## with the ELP (or other) camera in particular

import cv2
import numpy as np

dispWidth_small = 20
dispHeight_small = 20

## proper route: Setting normal capture size (or don't set any and let
## the camera choose a default
dispWidth = 640 ##taken earlier today
dispHeight = 480

dispWidth_HR = 1920
dispHeight_HR = 1080

dispWidth_LR = 320
dispHeight_LR = 240

cv2.namedWindow("win_high_res",cv2.WINDOW_NORMAL)
##cv2.resizeWindow("win_high_res",640,480)

cv2.namedWindow("win_norm_res",cv2.WINDOW_NORMAL)
##cv2.resizeWindow("win_norm_res",640,480)

## proper route: create a named window and set the flag to normal (not autosize)
##cv2.namedWindow("win_small",cv2.WINDOW_NORMAL)
##cv2.resizeWindow("win_small",640,480)


## read from camera
camera = cv2.VideoCapture(1)
camera2 = cv2.VideoCapture(2)

## setting capture properties, 
camera.set(cv2.CAP_PROP_FRAME_WIDTH, dispWidth_HR)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, dispHeight_HR)

camera2.set(cv2.CAP_PROP_FRAME_WIDTH, dispWidth_LR)
camera2.set(cv2.CAP_PROP_FRAME_HEIGHT, dispHeight_LR)

try:
    while True:
        ret_1, frame = camera2.read()
        ret_2, frame2 = camera.read()

        ## draw a rect of the same pixel size on each image, is one smaller in the display outputs?
        rect_h = rect_w = 100
        mosx = 150
        mosy = 150
        mosx2 = 650
        mosy2 = 450
        rect_v1 = (int(mosx-rect_w/2),int(mosy-rect_h/2))
        rect_v2 = (int(mosx+rect_w/2),int(mosy+rect_h/2))
        rect_v1_2 = (int(mosx2-rect_w/2),int(mosy2-rect_h/2))
        rect_v2_2 = (int(mosx2+rect_w/2),int(mosy2+rect_h/2))
        cv2.rectangle(frame,rect_v1,rect_v2,(0,255,0), 2)
        cv2.rectangle(frame2,rect_v1_2,rect_v2_2,(0,255,0), 2)
        
        ## proper route: resize the image into a new matrix        
        small = cv2.resize(frame, (20,20),0,0) 

                
        print("ELP high res:",np.shape(frame)," ELP normal res:", np.shape(frame2))

        
        cv2.imshow('win_norm_res',frame)
        cv2.imshow('win_high_res',frame2)

        ## proper route: show that new matrix on the normal sized window
##        cv2.imshow('win_small',small) 
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
except KeyboardInterrupt:
    camera.release()
    cv2.destroyAllWindows()
