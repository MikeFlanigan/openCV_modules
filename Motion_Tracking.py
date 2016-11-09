import cv2
import numpy as np

# private vars
tol = 80
DEL = 1


cap = cv2.VideoCapture('Shop_Test_7_12_16.avi')
##cap = cv2.VideoCapture(0) 
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame = cap.read()
    fgmask = fgbg.apply(frame)
    edges = cv2.Canny(frame,tol-5,tol)

    if ret == False:
        print(ret)
    
    if (cv2.waitKey(50) & 0xFF == ord('q')) or ret ==False:
        break

    cv2.imshow('orig', frame)
    cv2.imshow('fg', fgmask)
    cv2.imshow('edges',edges)
    
''' Used for determining a proper edge tol value
    if tol == 255:
        DEL = -1
    elif tol == 0:
        DEL = 1

    if tol % 10 == 0: # modulus math
        print(tol)
    
    tol = tol + DEL
'''
cap.release()
cv2.destroyAllWindows()
