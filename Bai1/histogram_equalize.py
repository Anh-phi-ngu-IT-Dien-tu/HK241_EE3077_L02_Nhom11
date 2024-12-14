import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

I=cv.imread('C:/Program Files/MATLAB/R2023a/toolbox/images/imdata/pout.tif',cv.IMREAD_GRAYSCALE)
I = cv.resize(I, (0, 0), None, 2, 2)#multiply number of rows by 2, number og columns by 2

cv.imshow('Image',I)
J=cv.equalizeHist(I)
J_hist=cv.calcHist(J,[0],None,[256],[0,256])
cv.imshow('Equalized image',J)
Compare=np.hstack([I,J])
cv.imshow('Compare',Compare)
cv.waitKey(0)
cv.destroyAllWindows()

I_hist=cv.calcHist(I,[0],None,[256],[0,256])
x=np.empty((0))
y=np.empty((0))
for i,value in enumerate(I_hist):
    x=np.hstack([x,i])
    y=np.hstack([y,value])

plt.figure()
plt.stem(x,y)
plt.title("Original histogram")
plt.xlabel("Bins")
plt.ylabel("number of Pixels")
plt.xlim([0, 256])
plt.grid(visible=True)

x=np.empty((0))
y=np.empty((0))
for i,value in enumerate(J_hist):
    x=np.hstack([x,i])
    y=np.hstack([y,value])
plt.figure()
plt.stem(x,y)
plt.title("Equalized histogram")
plt.xlabel("Bins")
plt.ylabel("number of Pixels")
plt.xlim([0, 256])
plt.grid(visible=True)

plt.show(block=False)
plt.pause(20)
plt.close()