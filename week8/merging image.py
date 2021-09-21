import cv2
import numpy as np

img1=cv2.imread('Map1.jpg',0)
img2=cv2.imread('Map2.jpg',0)
i=0
j=0
h, w = img1.shape
for j in range(0,w-101, 50):
    for i in range(0,h-101, 50):
        template=img1[i:i+100,j:j+100].copy()
        res = cv2.matchTemplate(img2,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(res)
        loc = np.where( res >= threshold)
        if max_val > threshold:
            print(max_val,'\n')
            print(max_loc,'\n')
            cv2.rectangle(img2, max_loc, (max_loc[0] + 100, max_loc[1] + 100), (0,0,255), 1)
            cv2.rectangle(img1, (j,i), (j+100,i+100), (0,0,255), 1)


cv2.imshow('Display1',img1)
cv2.imshow('Display2',img2)
cv2.waitKey(0)
