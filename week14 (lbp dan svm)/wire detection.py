# Import Modules
import os
import cv2 as cv
import numpy as np
from imutils import paths
from skimage import feature
from sklearn.svm import LinearSVC
import math

# Define LBP Class
class LocalBinaryPattern :
    # Variable Initialization
    def __init__(self,points,radius) :
        self.points = points
        self.radius = radius
    # Describe LBP Feature
    def describe(self,image,ep=1e-7) :
        lbp = feature.local_binary_pattern(image,self.points,self.radius,method='uniform')
        htg = np.histogram(lbp.ravel(),bins=np.arange(0,self.points+3),range=(0,self.points+2))[0]
        htg = htg.astype('float') ; htg /= (htg.sum()+ep) ; return htg

# Learning Process
LBP = LocalBinaryPattern(10,1)
data = [] ; lab = []
for p in paths.list_images('images') :
    img = cv.imread(p)
    gry = cv.cvtColor(img,6)
    htg = LBP.describe(gry)
    lab.append(p.split(os.path.sep)[-2])
    data.append(htg)
model = LinearSVC(C=100.0,random_state=50,max_iter=50000)
model.fit(data,lab)

# Detection Process
vid = cv.VideoCapture('video_uji.mp4')
vid.set(1,0) ; size = (480,850)
roix,roiy = 5,5

while True :
    frm = vid.read()[1] ; img = frm.copy()
    for i in range(int(size[0]/roiy)) :
        for j in range(int(size[1]/roix)) :
            p1 = (j*roix,i*roiy)
            p2 = (j*roix+roix,i*roiy+roiy)
            imr = img[p1[1]:p2[1],p1[0]:p2[0]]
            imr = cv.GaussianBlur(imr,(3,3),0)
            gry = cv.cvtColor(imr,6)
            htg = LBP.describe(gry)
            out = model.predict(htg.reshape(1,-1))[0]
            if out == '1' : cv.rectangle(frm,p1,p2,(255,0,255),-1)
            # 1 = Kabel
            # 2 = Tiang
            # 3 = Jalan
            # 4 = Pohon
            # 5 = Danau
    #cv.imshow('img',img)
    frame = frm.copy()
    frame2 = frame.copy()
    ungu = np.array([255,0,255])
    fltr = cv.inRange(frame,ungu,ungu)
    
    #edges = cv.Canny(mask, 100, 400, None, 3)

    linesP = cv.HoughLinesP(fltr, 1, np.pi / 180, 100,minLineLength=50,maxLineGap=3)
        
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(img, (l[0], l[1]), (l[2], l[3]), (0,0,255), 2,cv.LINE_AA)

##    lines = cv.HoughLines(mask, 1, np.pi / 180, 150, None, 0, 0)
##        
##    if lines is not None:
##        for i in range(0, len(lines)):
##            rho = lines[i][0][0]
##            theta = lines[i][0][1]
##            a = math.cos(theta)
##            b = math.sin(theta)
##            x0 = a * rho
##            y0 = b * rho
##            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
##            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
##            cv.line(frame2, pt1, pt2, (255,0,255), 3, cv.LINE_AA)
    
    #cv.imshow('canny_edge',edges)            
    cv.imshow('fltr',fltr)
    #cv.imshow('finallll',frame2)
    cv.imshow('FINALLLLL',img)
    #cv.imshow('FRAME',frm)
    if cv.waitKey(1) == 27 : break
cv.destroyAllWindows()
