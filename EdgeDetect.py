import cv2
import numpy as np

cap = cv2.VideoCapture(1) 

while True:
    _, frame = cap.read() 

    #laplachian = cv2.Laplacian(frame, cv2.CV_64F)
    #sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    #sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    edges = cv2.Canny(frame,200,220)


    cv2.imshow('frame',frame)
    #cv2.imshow('Laplachian',laplachian)
    #cv2.imshow('sobelx',sobelx)
    #cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)

    #######################
    '''
    This section to detect edges and make them green in the original image
    '''
    # figure out the frame size from the vid capture
    # frame size is 620x480 (widthxheight) determined by brute force rect lol

##    GrnEdges = cv2.bitwise_and(frame,[0,255,0],GrnEdges,edges)

    #######################
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
