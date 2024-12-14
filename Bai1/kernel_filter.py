import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import time

#boxfilter
I=cv.imread('D:\COMPUTER_VISION_TEAMWORK\Code_bai_1\8.-CT-Virtual-Colonography.jpg')
kernel=np.ones((9,9))/81
output=cv.filter2D(src=I,ddepth=-1,kernel=kernel)


plt.subplot(121)
plt.imshow(I)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(output)
plt.title('Averaging')
plt.xticks([])
plt.yticks([])
plt.show(block=False)
plt.pause(20)
plt.close()


