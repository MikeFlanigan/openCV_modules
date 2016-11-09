import cv2
import numpy as np

camera = cv2.VideoCapture(0)
cv2.namedWindow("cam_display",cv2.WINDOW_NORMAL)

min_thresh_img = np.zeros((300,512,3), np.uint8)
max_thresh_img = np.zeros((300,512,3), np.uint8)

cv2.namedWindow("min_thresh",cv2.WINDOW_NORMAL)
cv2.namedWindow("max_thresh",cv2.WINDOW_NORMAL)

def nothing(x): # this defined for a non action for the track bar formatting
    pass

cv2.createTrackbar('Rmi','min_thresh',0,255,nothing)
cv2.createTrackbar('Gmi','min_thresh',0,255,nothing)
cv2.createTrackbar('Bmi','min_thresh',0,255,nothing)

cv2.createTrackbar('Rma','max_thresh',0,255,nothing)
cv2.createTrackbar('Gma','max_thresh',0,255,nothing)
cv2.createTrackbar('Bma','max_thresh',0,255,nothing)

while True:
    ret, frame = camera.read()

    r_mi = cv2.getTrackbarPos('Rmi','min_thresh')
    g_mi = cv2.getTrackbarPos('Gmi','min_thresh')
    b_mi = cv2.getTrackbarPos('Bmi','min_thresh')

    min_thresh_img[:] = [b_mi, g_mi, r_mi]
    lower_color = np.array([b_mi, g_mi, r_mi])
    
    r_ma = cv2.getTrackbarPos('Rma','max_thresh')
    g_ma = cv2.getTrackbarPos('Gma','max_thresh')
    b_ma = cv2.getTrackbarPos('Bma','max_thresh')

    max_thresh_img[:] = [b_ma, g_ma, r_ma]
    upper_color = np.array([b_ma, g_ma, r_ma])
    
    mask = cv2.inRange(frame, lower_color, upper_color)
    
    
    cv2.imshow('min_thresh',min_thresh_img)
    cv2.imshow('max_thresh',max_thresh_img)
    cv2.imshow('cam_display',frame)
    cv2.imshow('mask',mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
