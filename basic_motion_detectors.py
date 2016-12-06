import cv2
import numpy as np
import timeit

# intitialize variables
Pause = False
FirstFrame = None
bg_avg = None

## ---- USER CONTROLS --------------------
cap = cv2.VideoCapture('./Videos/dist_vid_nicks.avi')
##cap = cv2.VideoCapture(0)

disp_w = int(640/1.2)
disp_h = int(480/1.2)

dynamic_bg = True
memory_strength = .8 # smaller remembers old frames longer, larger weighs new frames heavier, eg. forgetting movement faster

blur_kernel = 9 # kernal size for removing noise from the image, must be odd and positive

noise_kernel = 19

intenstity_thresh = 15 # changes of less than this intensity are ignored
change_set_to = 255 # pixel intensity that detected change areas are set to
## ---- END OF; USER CONTROLS ------------


cv2.namedWindow('image_orig',cv2.WINDOW_NORMAL)
cv2.resizeWindow("image_orig",disp_w,disp_h)
cv2.namedWindow('image_orig_blur',cv2.WINDOW_NORMAL)
cv2.resizeWindow("image_orig_blur",disp_w,disp_h)
cv2.namedWindow('image_MOG2',cv2.WINDOW_NORMAL)
cv2.resizeWindow("image_MOG2",disp_w,disp_h)
cv2.namedWindow('image_PYI',cv2.WINDOW_NORMAL)
cv2.resizeWindow("image_PYI",disp_w,disp_h)

fgbg = cv2.createBackgroundSubtractorMOG2()
i=0
while True:
    i+=1
    ret,frame = cap.read() 
    start_time = timeit.default_timer() # begin timer

    if ret:
        # showing blur effects on original image
        blurred = cv2.GaussianBlur(frame, (blur_kernel, blur_kernel),0,0)
        
        # preprocessing for both detectors
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (blur_kernel, blur_kernel),0,0) # last two vars are the std dev in x and y, as 0 they are calculated from the kernal size

        ## --- cv detection function ---------
        mog_mask = fgbg.apply(gray)
        flag, mog_mask = cv2.threshold(mog_mask, intenstity_thresh, change_set_to, cv2.THRESH_BINARY)
##        mog_mask = cv2.morphologyEx(mog_mask, cv2.MORPH_OPEN, (noise_kernel,noise_kernel)) # elimenating small noise
##        mog_mask = cv2.morphologyEx(mog_mask, cv2.MORPH_CLOSE, (noise_kernel,noise_kernel)) # filling in small holes
        ## --- end of; cv detection function --

        ## --- simple pyi detection function ---
        ## initializing bg frame
        if not dynamic_bg:
            if FirstFrame == None and i == 10:
                FirstFrame = gray
        else:
            if bg_avg == None:
                bg_avg = gray.copy().astype(np.float)
        ## subtracting bg and fg to determine motion
        if not dynamic_bg and FirstFrame != None:
            frameDelta = cv2.absdiff(gray,FirstFrame)
        elif dynamic_bg and bg_avg != None:
            cv2.accumulateWeighted(gray, bg_avg, memory_strength)
            frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(bg_avg))
        
        try:
            flag, pyi_mask = cv2.threshold(frameDelta, intenstity_thresh, change_set_to, cv2.THRESH_BINARY)
        except NameError:
            print('name undefined')
            pass # lazy fix
        ## --- end of; simple pyi detection function ---


    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or ret == False:
        break
    elif key == ord(' '): Pause = True

    cv2.imshow('image_orig', frame)
    cv2.imshow('image_orig_blur', blurred)
    cv2.imshow('image_MOG2', mog_mask)
    if ret and (FirstFrame != None or bg_avg != None):
        cv2.imshow('image_PYI', pyi_mask)

    if Pause:
        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord(' '):
                Pause = False
                break
    elapsed = timeit.default_timer() - start_time # end timer 
    print('elapsed time for 1 frame: ',elapsed)

cap.release()
cv2.destroyAllWindows()
