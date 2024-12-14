import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


I=cv.imread('C:/Program Files/MATLAB/R2023a/toolbox/images/imdata/pout.tif')
I=cv.cvtColor(I,cv.COLOR_RGB2GRAY)
cv.imshow('Original',I)

#simple thresholding
ret,thresh=cv.threshold(src=I,thresh=122,maxval=255,type=cv.THRESH_BINARY)
print(ret)
cv.imshow('Thresholding level 122',thresh)


#otsu thresholding
otsu_threshold, image_result = cv.threshold(I, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
print(otsu_threshold)
cv.imshow('Otsu thresholding',image_result)
cv.waitKey(0)

