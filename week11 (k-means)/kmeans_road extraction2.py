import numpy as np
import cv2 as cv

center = np.uint8([[0,0,0],
                   [255,255,255]])
kernel1 = np.ones((4,4),np.uint8)
kernel2 = np.ones((9,9),np.uint8)

cap = cv.VideoCapture('images/videojalan2.mp4');

while(True):
    ret,frame = cap.read()
    kframe = cv.resize(frame,(200,200))
    cv.imshow('frame',kframe)
    Z = kframe.reshape((-1,3))
##    print(kframe.shape)
##    print(Z.shape)
    Z = np.float32(Z)
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,10,1.0)
    K = 4
    retu,labbel,cnter = cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
##    center = np.uint8(center)
    label = labbel.flatten()
    y = np.bincount(label).argmax()
    
    for i in range(len(label)): 
        if label[i] != y:
            label[i] = 0
        else:
            label[i] = 1
##    res = center[labbel.flatten()]
    res = center[label]
    res2 = res.reshape((kframe.shape))

    r,g,b = cv.split(res2)
##    cv.imshow('r',r)
    nb_components, output, stats, centroids = cv.connectedComponentsWithStats(r, connectivity=4)
    sizes = stats[:, -1]

    max_label = 1
    max_size = sizes[1]
    for i in range(2, nb_components):
        if sizes[i] > max_size:
            max_label = i
            max_size = sizes[i]

    img2 = np.zeros(output.shape)
    img2[output == max_label] = 255

    
    img2 = cv.morphologyEx(img2, cv.MORPH_OPEN, kernel1)
    img2 = cv.morphologyEx(img2, cv.MORPH_CLOSE, kernel2)
##    img2 = cv.morphologyEx(img2, cv.MORPH_DILATE, kernel2)
    
    
    cv.imshow('kframe',img2)

    if cv.waitKey(1) >0:
        break

cap.release()
cv.destroyAllWindows()
    
##img = cv.imread('tes.jpg')
####cv.imshow('img',img)
##Z = img.reshape((-1,3))
##
##Z = np.float32(Z)
##
##criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,10,1.0)
##K = 6
##ret,labbel,center = cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
##
####center = np.uint8(center)
##label = labbel.flatten()
##y = np.bincount(labbel.flatten()).argmax()
##
##for i in range(len(label)): 
##    if label[i] != y:
##        label[i] = 0
##    else:
##        label[i] = 1
##        
##center = np.uint8([[0,0,0],
##                   [255,255,255]])
####print(center)
##res = center[label]
##res2 = res.reshape((img.shape))
##r,g,b = cv.split(res2)
##print(r.shape)
####cv.imshow('r',r)
##nb_components, output, stats, centroids = cv.connectedComponentsWithStats(r, connectivity=4)
##sizes = stats[:, -1]
##
##max_label = 1
##max_size = sizes[1]
##for i in range(2, nb_components):
##    if sizes[i] > max_size:
##        max_label = i
##        max_size = sizes[i]
##
##img2 = np.zeros(output.shape)
##img2[output == max_label] = 255
##
##kernel = np.ones((8,8),np.uint8)
##img2 = cv.morphologyEx(img2, cv.MORPH_CLOSE, kernel)
##
##cv.imshow('img',img2)
##
##cv.waitKey(0)
##cv.destroyAllWindows()

##import moviepy.editor
##from moviepy.editor import *
##video = VideoFileClip("file.mp4").subclip(103,128)
##result = CompositeVideoClip([video]) # Overlay text on video
##final = result.resize(height=360)
##final2= final.crop(x1=185,width=270)
##final2.write_videofile("cut.mp4",fps=20) # Many options...
##video = VideoFileClip("cut3.mp4")
##print(video.w)
##print(video.h)
##final = video.resize((480,640))
##final= video.crop(x1=200,width=720)
##final.write_videofile("cut3.mp4",fps=20)
