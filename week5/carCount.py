import cv2
import numpy as np



capture=cv2.VideoCapture('videojalan.mp4')
success,img=capture.read()
cnt = 0

while success:
    sucess,img=capture.read()
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    if cnt!= 0:
        BGSub=cv2.absdiff(img1,img)

        
        cv2.imshow('hasil',BGSub)
        hasil_img = BGSub
        ret,thresh_img=cv2.threshold(hasil_img,25,255,cv2.THRESH_BINARY)
        
        cv2.imshow('thresh',thresh_img)
        dilate_img=cv2.dilate(thresh_img,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)),iterations=1)
        erode_img=cv2.erode(dilate_img,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)),iterations=1)
        
        cv2.imshow('dilate', dilate_img)
        contours,hirarki=cv2.findContours(dilate_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        jumlah=0
        for c in contours :
          
            area = cv2.contourArea(c)
            if area > 200:
                x, y, w, h=cv2.boundingRect(c)
                jumlah += 1
            
                print(jumlah)
    else :
        img1=img.copy()
        cnt=1

    img1=img.copy()
    
    if cv2.waitKey(1)>0:
        break

capture.release()
cv2.destroyAllWindows()
