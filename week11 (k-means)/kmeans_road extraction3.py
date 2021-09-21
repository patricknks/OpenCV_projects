import cv2 as cv
import numpy as np
cv.namedWindow('INPUT',1)
cv.namedWindow('OUTPUT',1)
vid = cv.VideoCapture('images/videojalan3.mp4')
lth = (0,0,0)
tmp = (80,320)
rsz = (320,180)
uth = (180,60,256)
tmp = np.zeros(tmp,np.float32)
while True :
    try :
        ori = vid.read()[1]
        ori = cv.resize(ori,rsz)
        cut = ori[80:180,0:320]
        res = cv.cvtColor(cut,40)
        res = cv.blur(res,(9,9))
        res = cv.GaussianBlur(res,(9,9),0)
        res = cv.medianBlur(res,9)
        res = cv.bilateralFilter(res,9,9,9)
        res = res.reshape(-1,3)
        res = np.float32(res)
        cri = (3,10,1.0)
        com,lab,cen = cv.kmeans(res,2,None,cri,1,2)
        cen = np.uint8(cen)
        res = cen[lab.flatten()]
        res = res.reshape(cut.shape)
        res = cv.inRange(res,lth,uth)
        res = np.concatenate((tmp,res))
        ker = cv.getStructuringElement(2,(15,15))
        res = cv.morphologyEx(res,2,ker)
        cv.imshow('INPUT',ori)
        cv.imshow('OUTPUT',res)
        if cv.waitKey(1) == 27 : break
    except : break
vid.release()
cv.destroyAllWindows()
