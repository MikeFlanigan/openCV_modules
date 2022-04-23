import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
# cap = cv2.VideoCapture('Thunderstorm_boats.mp4')
cap = cv2.VideoCapture('Nighttime motorboat flyby.mp4')

n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # total number of frames
print('frames: ',n_frames)

# Check if camera opened successfully
if (cap.isOpened()== False): 
    print("Error opening video stream or file")

f_count = 0
# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # keep track of how many frames have been loaded
    f_count += 1 

    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame',frame)

        # Press Q on keyboard to    exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        pass 

    # Break the loop
    else: 
        break

print(f_count," frames")

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()