import cv2
import numpy as np

#initialcamcapture

capture=cv2.VideoCapture('videojalan.mp4')
success,img=capture.read()
cnt= 0

while success:
    sucess,img=capture.read()
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    if cnt!= 0:
        BGSub=cv2.absdiff(img1,img)
        cv2.imshow('hasil',BGSub)

    else :
        img1=img.copy()
        cnt=1

    img1=img.copy()

    if cv2.waitKey(1)>0:
        break

capture.release()
cv2.destroyAllWindows()
