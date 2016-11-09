import cv2
import numpy as np
import datetime
import os

## testing seems to be you should use the valid camera settings
## below settings are for the HD 1080P USB CMOS board camera
##dispWidth = 1920
##dispHeight = 1080
##FPS = 6

##dispWidth = 1280
##dispHeight = 1024
##FPS = 6

##dispWidth = 1280
##dispHeight = 720
##FPS = 9

dispWidth = 800
dispHeight = 600
FPS = 21

##dispWidth = 640 ##taken earlier today
##dispHeight = 480
##FPS = 30

##dispWidth = 320 ##taken earlier today
##dispHeight = 240
##FPS = 30


# can capture video
cap = cv2.VideoCapture(1) # the number is equal to which camera is connected
# OR could load a video file like so
##cap = cv2.VideoCapture('VidOutputput.avi')

## setting capture properties
cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispHeight)

## toggle to save or just display video
SaveVideo = True
##SaveVideo = False

# file saving duration and trigger
SetupNewVideoFile = True # state variable
VidCaptureDuration = 2 # set to the desired video duration minutes
VidCaptureStartTime = 0 # var for checking elapsed time

## saving to a usb
saveToUSB = True
##saveToUSB = False
USBfilepath = 'E:' ## set to whatever drive the device recognizes the usb as


while True:
    Now = datetime.datetime.now() # refresh current time
    
    if SetupNewVideoFile and SaveVideo:
        ## strings for file naming description
        FPSstr = str(FPS)
        sizestr = str(dispWidth) + "x" + str(dispHeight)
        VidCaptureStartTime = Now.minute # updating comparitor for starting new video file
        TS = str(Now.year) + "_" + str(Now.month)+ "_" + str(Now.day)+ "-" + str(Now.hour)+ "_" + str(Now.minute)

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        title = "Test_"+sizestr+"_"+"FPS"+FPSstr+"_" + TS + ".avi"
        if saveToUSB:
            filepath = USBfilepath + "\\Videos\\"
        else:
            filepath = os.getcwd() + "\\Videos\\"
        fullpath = filepath + title
        print(fullpath)
        VidOutput = cv2.VideoWriter(fullpath,fourcc, FPS, (dispWidth,dispHeight))

        SetupNewVideoFile = False
        print("Starting a new file save!")
        
    if abs(Now.minute - VidCaptureStartTime)%VidCaptureDuration == 0 and abs(Now.minute - VidCaptureStartTime) > 0 and not SetupNewVideoFile and SaveVideo:
        SetupNewVideoFile = True
        VidOutput.release() # end the last video so we can start a new one
        print("finished a file save!")


    ## reading the camera capture    
    ret, frame = cap.read() 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # converts image to gray scale

    cv2.imshow('frame',frame) # displays the frame
##    cv2.imshow('gray', gray)
##    print (TS)
##    cv2.rectangle(frame, (15,15), (200,200), (0,255,0),1) # B,G,R  line thickness

    if SaveVideo:
        VidOutput.write(frame) # save the frames

    ## exit and close when user presses q key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

## cleanup
cap.release()
if SaveVideo:
    VidOutput.release() # release the VidOutputput frame
cv2.destroyAllWindows()
