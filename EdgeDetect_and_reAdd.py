import cv2
import numpy as np

cap = cv2.VideoCapture(0) 

while True:
    _, webcam = cap.read()
    cv2.imshow('webcam',webcam)

    edges = cv2.Canny(webcam,200,220)
    cv2.imshow('edges',edges)

    # rows,cols,channels = webcam.shape
    grn_image = np.zeros(webcam.shape, np.uint8)
    grn_image[:]=(0,255,0) 
    
    edge_grn = cv2.bitwise_and(grn_image,grn_image, mask = edges)
    cv2.imshow('edges_grn',edge_grn)


    


    webcam_color_edges = cv2.bitwise_and(webcam,webcam, mask = edges)
    cv2.imshow('webcam_color_edges',webcam_color_edges)
    
    webcam_no_edges = cv2.subtract(webcam,webcam_color_edges)
    cv2.imshow('webcam with edges removed',webcam_no_edges)


    webcam_grn_edges = cv2.add(edge_grn,webcam_no_edges)
    cv2.imshow('webcam_grn_edges',webcam_grn_edges)
    
    
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
