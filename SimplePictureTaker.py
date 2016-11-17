import cv2
import time

time.sleep(5) # delay time

cam = cap = cv2.VideoCapture(0)

ret, frame = cam.read()
cv2.imshow('frame',frame)
cv2.imwrite('picture.jpg',frame)
while True:
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cam.release()
cv2.destroyAllWindows()
