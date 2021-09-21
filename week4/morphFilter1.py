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
    erode_img=cv2.erode(thresh_img,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)),iterations=4)
    dilate_img=cv2.dilate(erode_img,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)),iterations=4)
    
    cv2.imshow("dilate",dilate_img)
    cv2.imshow("erode",erode_img)
    contours,hirarki=cv2.findContours(erode_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #color=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    img=cv2.drawContours(img,contours,-1,(0,255,0),2)

    #show image
    cv2.imshow("Hasil",img)
    if cv2.waitKey(1)>0:
            break


capture.release()
cv2.destroyAllWindows()
       

