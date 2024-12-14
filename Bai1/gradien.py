import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


I=cv.imread('C:/Program Files/MATLAB/R2023a/toolbox/images/imdata/coins.png')
I=cv.cvtColor(I,cv.COLOR_RGB2GRAY)

laplacian=cv.Laplacian(src=I,ddepth=cv.CV_32F,ksize=3)

gx=cv.Sobel(src=I,ddepth=cv.CV_32F,dx=1,dy=0,ksize=3,scale=1,delta=0,borderType=cv.BORDER_DEFAULT)#vertical sobel kernel
gy=cv.Sobel(src=I,ddepth=cv.CV_32F,dx=0,dy=1,ksize=3,scale=1,delta=0,borderType=cv.BORDER_DEFAULT)#horizontal sobel kernel
mag, angle = cv.cartToPolar(gx, gy, angleInDegrees=True)

mag=cv.convertScaleAbs(mag)
angle=cv.convertScaleAbs(angle)
laplacian=cv.convertScaleAbs(laplacian)#convert back to uint8_t
gx = cv.convertScaleAbs(gx)
gy = cv.convertScaleAbs(gy)

g=cv.addWeighted(gx,0.5,gy,0.5,0)

cv.imshow('Orginal',I)
cv.imshow('Laplacian',laplacian)
cv.imshow('magnitude',mag)
cv.imshow('angle',angle)
cv.imshow('Gx',gx)
cv.imshow('Gy',gy)
cv.imshow('G',g)

cv.waitKey(0)