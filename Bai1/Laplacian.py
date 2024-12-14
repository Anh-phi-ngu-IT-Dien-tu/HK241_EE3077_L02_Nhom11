import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from add_noise import *

I=cv.imread('C:/Program Files/MATLAB/R2023a/toolbox/images/imdata/pout.tif')
I_salt_peper=add_salt_and_pepper_noise(I,0.1)
I_median_filter=cv.medianBlur(I_salt_peper,3)#kernel 5*5
I_laplacian=cv.Laplacian(I_median_filter,ddepth=-1,ksize=3)#kernel 3*3, use for line detection

plt.figure()
plt.subplot(121)
plt.imshow(I)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(I_salt_peper)
plt.title('Add noise')
plt.xticks([])
plt.yticks([])

plt.figure()
plt.subplot(121)
plt.imshow(I_salt_peper)
plt.title('Add noise')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(I_median_filter)
plt.title('Median filter')
plt.xticks([])
plt.yticks([])

plt.figure()
plt.subplot(121)
plt.imshow(I_median_filter)
plt.title('Median filter')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(I_laplacian)
plt.title('Laplacian')
plt.xticks([])
plt.yticks([])

plt.show()
