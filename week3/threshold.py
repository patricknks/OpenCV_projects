import cv2 
import numpy as np


img=cv2.imread('cthgambar.jpg',0)
ret, thresh1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)

cv2.imshow('display',thresh1)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
