import cv2 
import numpy as np

capture=cv2.VideoCapture(0)
success,img=capture.read()

#thresholding function
while success:
    success,img=capture.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imshow("gray",gray)
    if cv2.waitKey(1)>0:
            break
capture.release()
cv2.destroyAllWindows()
