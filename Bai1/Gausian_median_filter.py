import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from add_noise import *
import time


I=cv.imread('C:/Program Files/MATLAB/R2023a/toolbox/images/imdata/pout.tif')
I_gaussian_noise=add_gaussian_noise(I,0.5)
I_salt_and_pepper=add_salt_and_pepper_noise(I,0.1)
output=cv.GaussianBlur(src=I_gaussian_noise,ksize=(5,5),sigmaX=100,sigmaY=100,borderType=cv.BORDER_WRAP)
# input image, kernel size, standard deviation x, standard deviation for y,

plt.figure()
plt.subplot(121)
plt.imshow(I)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(I_gaussian_noise)
plt.title('Gausian noise')
plt.xticks([])
plt.yticks([])

plt.figure()
plt.subplot(121)
plt.imshow(I)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(I_salt_and_pepper)
plt.title('Salt and pepper nosie')
plt.xticks([])
plt.yticks([])

plt.figure()
plt.subplot(121)
plt.imshow(I_gaussian_noise)
plt.title('Nosie')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(output)
plt.title('Gausian filter')
plt.xticks([])
plt.yticks([])

output=cv.medianBlur(I_salt_and_pepper,5)#median blur with kernel 5*5

plt.figure()
plt.subplot(121)
plt.imshow(I_salt_and_pepper)
plt.title('Salt and pepper nosie')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(output)
plt.title('Median filter')
plt.xticks([])
plt.yticks([])

plt.show(block=False)
plt.pause(10)
plt.close()
