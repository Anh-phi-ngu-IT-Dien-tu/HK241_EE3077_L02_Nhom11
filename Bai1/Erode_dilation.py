import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

I=cv.imread('C:/Program Files/MATLAB/R2023a/toolbox/images/imdata/text.png')
I=cv.cvtColor(I,cv.COLOR_RGB2GRAY)

cv.imshow('original image',I)

se=np.ones((11,1))

Ie=cv.erode(src=I,kernel=se)
Id=cv.dilate(src=I,kernel=se)

cv.imshow('Erode image',Ie)
cv.imshow('Dilation image',Id)

cv.waitKey(0)

