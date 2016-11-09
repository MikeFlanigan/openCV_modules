import cv2
import numpy as np

## switching to HSV since easier to capture a constant color and only vary the saturation

camera = cv2.VideoCapture(0)
cv2.namedWindow("cam_display",cv2.WINDOW_NORMAL)

min_thresh_img = np.zeros((300,512,3), np.uint8)
max_thresh_img = np.zeros((300,512,3), np.uint8)
min_thresh_img = cv2.cvtColor(min_thresh_img, cv2.COLOR_BGR2HSV)
max_thresh_img = cv2.cvtColor(max_thresh_img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("min_thresh",cv2.WINDOW_NORMAL)
cv2.namedWindow("max_thresh",cv2.WINDOW_NORMAL)

def nothing(x): # this defined for a non action for the track bar formatting
    pass

cv2.createTrackbar('Hmi','min_thresh',0,360,nothing)
cv2.createTrackbar('Smi','min_thresh',0,100,nothing)
cv2.createTrackbar('Vmi','min_thresh',0,100,nothing)

cv2.createTrackbar('Hma','max_thresh',0,360,nothing)
cv2.createTrackbar('Sma','max_thresh',0,100,nothing)
cv2.createTrackbar('Vma','max_thresh',0,100,nothing)

while True:
    ret, frame = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    h_mi = cv2.getTrackbarPos('Hmi','min_thresh')
    s_mi = cv2.getTrackbarPos('Smi','min_thresh')
    v_mi = cv2.getTrackbarPos('Vmi','min_thresh')

    min_thresh_img[:] = [h_mi, s_mi, v_mi]
    lower_color = np.array([h_mi, s_mi, v_mi])
    
    h_ma = cv2.getTrackbarPos('Hma','max_thresh')
    s_ma = cv2.getTrackbarPos('Sma','max_thresh')
    v_ma = cv2.getTrackbarPos('Vma','max_thresh')

    max_thresh_img[:] = [h_ma, s_ma, v_ma]
    upper_color = np.array([h_ma, s_ma, v_ma])
    
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    
    cv2.imshow('min_thresh',min_thresh_img)
    cv2.imshow('max_thresh',max_thresh_img)
    cv2.imshow('cam_display',frame)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
