import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print(os.getcwd())

img = cv2.imread('soccerball.jpg',cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR  = 1
#IMREAD_UNCHANGED = -1

#image display using OpenCV
cv2.imshow('title',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('ballgray.png',img)


# image display and plotting with matplotlib
##plt.imshow(img,cmap='gray',interpolation='bicubic')
##plt.plot([50,100],[80,100],'r',linewidth=8)
##plt.show()
