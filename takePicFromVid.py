import cv2

camname = 'Data_Alpha_FPS6_2016_12_29-15_5.avi' # 0 for webcam
cam = cap = cv2.VideoCapture(camname)

while True:
        ret, frame = cam.read()
        cv2.imshow('frame',frame)


        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '): # save pic and open new window with it
                cv2.imwrite('picture.jpg',frame)
                cv2.imshow('saved pic',frame)
        elif key == ord('q'): break # ends program


                
cam.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)

