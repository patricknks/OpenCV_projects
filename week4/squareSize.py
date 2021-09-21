import cv2 as cv2
import numpy as np

#warna background hitam
img=np.zeros((400,400),dtype=np.uint8)

#warna putih
img[50:250,50:250]=255
img[260:350,50:150]=255
img[50:150,260:350]=255
cv2.imshow('Gambar',img)
#threshold
ret,thresh_img=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
contours,hirarki=cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
color=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img=cv2.drawContours(color,contours,-1, (0,255,0),2)
jumlah=0

for c in contours :
    jumlah += 1
    x,y,w,h=cv2.boundingRect(c)
    print('w',w)
    print('h',h)
print(jumlah)
    
#show img
cv2.imshow('Hasil',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

