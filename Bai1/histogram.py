import cv2 as cv
import numpy as np
import matplotlib.pyplot  as plt 
import time

img=cv.imread('D:\COMPUTER_VISION_TEAMWORK\Code_bai_1\Capture.jpg',cv.IMREAD_GRAYSCALE)
print(img.shape)
cv.imshow('Image',img)

cv.waitKey(0)
cv.destroyAllWindows()


hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("number of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.grid(visible=True)
plt.show(block=False)
plt.pause(20)
plt.close()

