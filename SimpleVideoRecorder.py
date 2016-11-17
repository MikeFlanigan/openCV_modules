import cv2
import numpy as np
import datetime
import os


camera = cv2.VideoCapture(0) 


## toggle to save or just display video
SaveVideo = True
##SaveVideo = False


Video_Title = "face"
fourcc = cv2.VideoWriter_fourcc(*'XVID')
title = Video_Title + ".avi"

ret, frame = camera.read() 
im_ht,im_wdt,im_chan = frame.shape
dispWidth = im_wdt
dispHeight = im_ht

FPS = 30 #this should be experimented with
VidOutput = cv2.VideoWriter(title,fourcc, FPS, (dispWidth,dispHeight))

while True:

    ret, frame = camera.read() 

    cv2.imshow('frame',frame) # displays the frame

    if SaveVideo:
        VidOutput.write(frame) # save the frames

   
    if cv2.waitKey(1) & 0xFF == ord('q'):  ## exit and close when user presses q key
        break


## cleanup
camera.release()
if SaveVideo:
    VidOutput.release() # release the VidOutputput frame
cv2.destroyAllWindows()
