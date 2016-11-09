import cv2
import numpy as np
import datetime
import os


save = True
##save = False
Now = datetime.datetime.now()
TS = str(Now.year) + "_" + str(Now.month)+ "_" + str(Now.day)+ "-" + str(Now.hour)+ "_" + str(Now.minute)


cap0 = cv2.VideoCapture(2)
cap1 = cv2.VideoCapture(0) 

# saves things
fourcc = cv2.VideoWriter_fourcc(*'XVID')
filepath = os.getcwd() + "\\Videos\\"
title0 = TS + "_Test_10in_cam0.avi"
title1 = TS + "_Test_10in_cam1.avi"
fullpath0 = filepath + title0
fullpath1 = filepath + title1
if save == True: 
    out0 = cv2.VideoWriter(fullpath0,fourcc, 20.0, (640,480))
    out1 = cv2.VideoWriter(fullpath1,fourcc, 20.0, (640,480))

while True:
    ret, cam0 = cap0.read()
    ret, cam1 = cap1.read()
    
    if save == True: 
        out0.write(cam0) # save the frame
        out1.write(cam1) # save the frame
    cv2.imshow('cam0',cam0)
    cv2.imshow('cam1',cam1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap0.release()
cap1.release()
if save == True: 
    out0.release() # release the output frame
    out1.release() # release the output frame
cv2.destroyAllWindows()
