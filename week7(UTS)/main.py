#python coba2.py --CS_GRAY --TH_YES --THRESVALUE 50 --MORPH_ERODE --BS_YES
import cv2 
import numpy as np
import sys

capture=cv2.VideoCapture('videojalan.mp4')
success,image=capture.read()

def fungsi(*argv):
    for arg in argv:
        print (arg)
cnt = 0
#fungsi(sys.argv[1:])
while success:
    th_value = int(sys.argv[4])
    success,image=capture.read()
    img = cv2.flip(image, 1)
    cv2.imshow("og", img)
    
#GRAY
    if (sys.argv[1] == '--CS_GRAY'):
        cs=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#RGB
    if (sys.argv[1] == '--CS_RGB'):
        cs=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    if (sys.argv[1] == '--CS_RGBB'):
        blue=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        cs=blue.copy()
        cs[:, :, 1] = 0
        cs[:, :, 2] = 0
    if (sys.argv[1] == '--CS_RGBG'):
        green=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        cs=green.copy()
        cs[:, :, 0] = 0
        cs[:, :, 2] = 0
    if (sys.argv[1] == '--CS_RGBR'):
        red=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        cs=red.copy()
        cs[:, :, 0] = 0
        cs[:, :, 1] = 0
#HSV
    if (sys.argv[1] == '--CS_HSV'):
        cs=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    if (sys.argv[1] == '--CS_HSVH'):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        cs = h
    if (sys.argv[1] == '--CS_HSVS'):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        cs = s
    if (sys.argv[1] == '--CS_HSVV'):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        cs = v
#CS_NO
    if (sys.argv[1] == '--CS_NO'):
        cs=img.copy()
        
#THRESHOLD
    if (sys.argv[2] == '--TH_YES'):
        ret, img=cv2.threshold(cs,th_value,255,cv2.THRESH_BINARY)
    if (sys.argv[2] == '--TH_NO'):
        img = cs.copy()

#MORPHOLOGY FILTER
    if (sys.argv[5] == '--MORPH_ERODE'):
        morph=cv2.erode(img,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)),iterations=1)
    if (sys.argv[5] == '--MORPH_DILATE'):
        morph=cv2.dilate(img,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)),iterations=1)
    if (sys.argv[5] == '--MORPH_NO'):
        morph = th.copy()

#BACKGROUND SUBSTRACTION
    if (sys.argv[6] == '--BS_YES'):
        
        if cnt!= 0:
           # print('1')
            BGSub=cv2.absdiff(img1,morph)
            cv2.imshow("SAMPAI BGSUB",BGSub)
        else:
           # print('2')
            img1=morph.copy()
            cnt=1

        img1=morph.copy()
    if (sys.argv[6] == '--BS_NO'):
        cv2.imshow("SAMPAI MORPH",morph)
    if cv2.waitKey(1)>0:
            break

capture.release()
cv2.destroyAllWindows()
