import cv2
import numpy as np
import os


camera = cv2.VideoCapture(0) # this captures your default webcam
##camera = cv2.VideoCapture('rtsp://192.168.1.64/1') # this is for an ip camera without a username & password
##camera = cv2.VideoCapture('rtsp://username:password@192.168.1.64/1') # this would be ip cam with user & pass

## toggle to save or just display video
SaveVideo = True
##SaveVideo = False


Video_Title = "GroundWatch_vid_"
num = 0

# updates file name so as not to overwrite videos
for i in range(300):
    title = Video_Title + str(num)+".avi"
    if not os.path.exists(title):
        break
    else:
        num += 1

fourcc = cv2.VideoWriter_fourcc(*'XVID')

ret, frame = camera.read() 
im_ht,im_wdt,im_chan = frame.shape
dispWidth = im_wdt
dispHeight = im_ht

FPS = 20 #this should be experimented with
VidOutput = cv2.VideoWriter(title, fourcc, FPS, (dispWidth,dispHeight))

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
