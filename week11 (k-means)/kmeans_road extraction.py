import numpy as np
import cv2 as cv

cap = cv.VideoCapture('images/videojalan.mp4')

n=0
K = 3

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Can not receive frame. Exiting . . . ")
        break
    
    #resize original frame
    scale_percent = 30
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)   
    frame = cv.resize(frame, dim, interpolation = cv.INTER_AREA)
    #resize original frame
    frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    frame1 = frame.reshape((-1,3))
    frame1 = np.float32(frame1)

    #K-mean clustering
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret,label,center=cv.kmeans(frame1,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    labels = label.flatten()
    res = center[labels]
    res2 = res.reshape((frame.shape))

    #masking image
    masked_image = np.zeros(frame.shape)
    masked_image = masked_image.reshape((-1, 3))

    t = np.where(center==np.amin(center))
        
    cluster = t[0]
    masked_image[labels == cluster] = [255, 255, 255]

    masked_image = masked_image.reshape(frame.shape)

    #print data
    
    print("label : ")
    print(label)
    print("labels : ")
    print(labels)
    print("center : ")
    print(center) 
    
    #show image
    cv.imshow('frame',frame)
    cv.imshow('res2',res2)
    cv.imshow('mask',masked_image)
    n=n+1
    if cv.waitKey(1) > 0:
        break

cap.release()
cv.destroyAllWindows()
