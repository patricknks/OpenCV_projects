import cv2 
import numpy as np

capture=cv2.VideoCapture(0)

success,img=capture.read()
while success:
    success,img=capture.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thres1=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    adaptif=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,12)
    cv2.imshow('threshold',thres1)
    cv2.imshow('adaptiv threshold',adaptif)
    cv2.imshow('original',img)
    if cv2.waitKey(1)>0:
        break
cv2.destroyAllWindows()
