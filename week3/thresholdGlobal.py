import cv2 
import numpy as np


img=cv2.imread('cthgambar.jpg',0)
ret, globalthresh=cv2.threshold(img,100,255,cv2.THRESH_BINARY)

cv2.imshow('hasil_threshold',globalthresh)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
