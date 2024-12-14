import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

I=cv.imread('C:/Program Files/MATLAB/R2023a/toolbox/images/imdata/coins.png')
I=cv.cvtColor(I,cv.COLOR_RGB2GRAY)

se=cv.getStructuringElement(shape=cv.MOTION_EUCLIDEAN,ksize=(20,20))
opening = cv.morphologyEx(src=I, op=cv.MORPH_OPEN, kernel=se, iterations=1) 
closing=cv.morphologyEx(src=I,op= cv.MORPH_CLOSE, kernel=se,iterations=1)

cv.imshow('original image',I)
cv.imshow('opening image',opening)
cv.imshow('closing image',closing)

cv.waitKey(0)
