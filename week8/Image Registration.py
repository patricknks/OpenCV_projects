import cv2
import numpy as np
from matplotlib import pyplot as plt

gbrkiri = cv2.imread('gambarkiri.jpg',0)
gbrkanan = cv2.imread('gambarkanan.jpg',0)
i = 0
j = 0
h, w = gbrkiri.shape

for j in range(0, w-101, 50):
    for i in range(0, w-101, 50):
        template = gbrkanan[i:i+100,j:j+100].copy()
        res = cv2.matchTemplate(gbrkiri,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.55
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        loc = np.where( res >= threshold)
        if max_val > 0.8:
            print(max_val)
            print(max_loc)
            cv2.rectangle(gbrkanan, max_loc, (max_loc[0] + 100, max_loc[1] + 100), (0,0,255),1)
            #cv2.rectangle(gbrkiri, (j,i), (j+100,i+100), (0,0,255), 1)
            cv2.rectangle(gbrkiri, (j,i), (j+100,i+100), (0,0,255), 1)

#cv2.imshow('res.png',img_rgb)
cv2.imshow('gambar', gbrkiri)
cv2.imshow('test', gbrkanan)
cv2.waitKey(0)
cv2.destroyAllWindows()
