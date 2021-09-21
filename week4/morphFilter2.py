import cv2 
import numpy as np

capture=cv2.VideoCapture(0)
success,img=capture.read()

#thresholding function
while success:
    success,img=capture.read()
    
    #threshold
    ret,thresh_img=cv2.threshold(cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY),50,255,cv2.THRESH_BINARY)
    cv2.imshow("hasil threshold", thresh_img)
    dilate_img=cv2.dilate(thresh_img,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,3)),iterations=4)
    erode_img=cv2.erode(dilate_img,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,3)),iterations=4)
    
    
    cv2.imshow("dilate",dilate_img)
    cv2.imshow("erode",erode_img)
    contours,hirarki=cv2.findContours(erode_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #print(contours)
    #color=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    img=cv2.drawContours(img,contours,-1,(0,255,0),2)

    jumlah=0
    for c in contours :
        #jumlah += 1
        x, y, w, h=cv2.boundingRect(c)
        if w>20 and h>20:
            jumlah += 1
            print("w",w,"h",h)
        print(jumlah)

    #show image
    cv2.imshow("Hasil",img)
    if cv2.waitKey(1)>0:
            break
capture.release()
cv2.destroyAllWindows()
       

