import cv2
import numpy as np
import datetime as dt

# Experiments and options

CV_read_experiment = True # just reading frames from a camera
CV_change_detect_experiment = True # a simple gray + blur + change detection
CV_show_experiment = True # showing the outputs in a window

# the average FPS can get skewed to look better than it really was
# due to a few very fast outlier loop times
drop_outlier_times = True 
plot_per_loop_times = True

program_run_time = 10 # seconds to run for
################################
# Setup

if CV_read_experiment or CV_show_experiment:
    using_CV = True
else:
    using_CV = False

if using_CV:
    cap = cv2.VideoCapture(0)

if CV_show_experiment:
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame',640,480)

last_frame = None
thresh_frame = None

start = dt.datetime.now()
stop = dt.datetime.now()
elapsed = start - stop

FPS_list = []

start_prog = dt.datetime.now()
try:
    print('Running experiment...')
    while True:
        start = dt.datetime.now()
        #########################
        # Experiments

        if using_CV:
            ret, frame = cap.read()

        if CV_change_detect_experiment:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
            if last_frame is not None:
                frame_delta = cv2.absdiff(last_frame, gray_frame)
                thresh_frame = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
            last_frame = gray_frame

        if CV_show_experiment:
            if not CV_change_detect_experiment:
                cv2.imshow('frame',frame)
            else:
                if thresh_frame is not None:
                    cv2.imshow('frame',thresh_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # End Experiments
        ########################
        stop = dt.datetime.now()
        elapsed = stop - start  

        if elapsed.microseconds > 0:
            inst_FPS = 1000.0/(elapsed.microseconds/1000.0)
        else:
            inst_FPS = 999

        # Debugging prints
##        print('microseconds elapsed: ',elapsed.microseconds)
##        print('Instantaneous FPS: ', inst_FPS)

        # List for storing each loop's FPS count
        # appending to lists can be slow, but for 5 seconds at full speed
        # it's basically unmeasureable
        if inst_FPS < 900:
            FPS_list.append(inst_FPS)

        if (dt.datetime.now() - start_prog).seconds >= program_run_time:
            print(' ')
            print('Experiment finished. Ran ',program_run_time,' seconds.')
            break
except KeyboardInterrupt:
    print('User stopped program.')
    pass

print(' ')
FPS_array = np.asarray(FPS_list) # useful

if drop_outlier_times:
    median = np.median(FPS_array)
    bounds = median*0.25 # count values within 25% of the median
    indices = np.where(FPS_array <= median + bounds)[0]
    print('Dropped ',len(indices),' outliers.')
    print('Percent loops that were evaluated: ',np.round(len(indices)/len(FPS_array)*100,2),'%')

print(' ')
print('Average FPS: ', FPS_array[indices].mean())

if using_CV:
    cap.release()
    cv2.destroyAllWindows()

if plot_per_loop_times:
    import matplotlib.pyplot as plt
    if drop_outlier_times:
        plt.plot(FPS_list, 'ro',Markersize=5)
        plt.plot(indices, FPS_array[indices],'ko')
        plt.legend(['Outliers','Inliers'])
    else:
        plt.plot(FPS_list, 'ko')
    plt.xlabel('Frame')
    plt.ylabel('FPS speed')
    plt.show()


