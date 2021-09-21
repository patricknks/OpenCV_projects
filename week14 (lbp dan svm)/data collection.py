# Import Modules
import os
import cv2 as cv
import numpy as np
from imutils import paths
from skimage import feature
from sklearn.svm import LinearSVC

# Collect Images for Learning
vid = cv.VideoCapture('video_uji.mp4')
cv.namedWindow('ROI',0)
cv.namedWindow('FRAME',0)
cv.resizeWindow('ROI',500,500)
roix,roiy = 10,10
d1,d2 = 'images/1/','images/2/'
d3,d4 = 'images/3/','images/4/'
d5,d6 = 'images/5/','images/6/'
n1,n2,n3,n4,n5 = 0,0,0,0,0
vid.set(1,200) ; size = (480,850)
frm = vid.read()[1]
for i in range(int(size[0]/roiy)) :
    for j in range(int(size[1]/roix)) :
        p1 = (j*roix,i*roiy)
        p2 = (j*roix+roix,i*roiy+roiy)
        tmp = frm.copy()
        n = n1+n2+n3+n4+n5
        # 1 = Kabel
        # 2 = Tiang
        # 3 = Jalan
        # 4 = Pohon
        # 5 = Danau
        img = frm[p1[1]:p2[1],p1[0]:p2[0]]
        cv.rectangle(tmp,p1,p2,(0,255,0),1)
        cv.putText(tmp,str(n),(10,250),0,10,(0,255,0),1)
        cv.imshow('FRAME',tmp) ; cv.imshow('ROI',img)
        k = cv.waitKey(0)
        if   k == 27 : break
        elif k == 49 : n1 += 1 ; cv.imwrite(d1+str(n1)+'.jpg',img)
        elif k == 50 : n2 += 1 ; cv.imwrite(d2+str(n2)+'.jpg',img)
        elif k == 51 : n3 += 1 ; cv.imwrite(d3+str(n3)+'.jpg',img)
        elif k == 52 : n4 += 1 ; cv.imwrite(d4+str(n4)+'.jpg',img)
        elif k == 53 : n5 += 1 ; cv.imwrite(d5+str(n5)+'.jpg',img)
    if cv.waitKey(0) == 27 : break
cv.destroyAllWindows()
