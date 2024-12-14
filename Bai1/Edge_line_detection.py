import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt

I=cv.imread('C:/Program Files/MATLAB/R2023a/toolbox/images/imdata/circuit.tif')
Img=I
I=cv.cvtColor(I,cv.COLOR_RGB2GRAY)

cv.imshow('Original',cv.resize(I,(0,0),fx=2,fy=2))
Edge_canny=cv.Canny(I,threshold1=30,threshold2=180,L2gradient=False)
# if gradient of a point is lower than threshold 1, it tis not edge, if it is higher than 180, that point is in edge
#depending on threshold 1 and threshold 2, the "not-sure-edge" point be considered to be an edge if it is connected to 
#"sure-edge" points
cv.imshow('Edges using canny',cv.resize(Edge_canny,(0,0),fx=2,fy=2))
Edge_Laplacian=cv.Laplacian(I,ddepth=-1,ksize=3)
Edge_Laplacian=cv.medianBlur(Edge_Laplacian,ksize=3)
cv.imshow('Edges using Laplacian',cv.resize(Edge_Laplacian,(0,0),fx=2,fy=2))


#standard houghlines
lines=cv.HoughLines(Edge_canny,1,np.pi/180,90,0,0)
# with the following arguments:
# dst: Output of the edge detector. It should be a grayscale image (although in fact it is a binary one)
# lines: A vector that will store the parameters (r,θ) of the detected lines
# rho : The resolution of the parameter r in pixels. We use 1 pixel.
# theta: The resolution of the parameter θ in radians. We use 1 degree (CV_PI/180)
# threshold: The minimum number of intersections to "*detect*" a line
# srn and stn: Default parameters to zero. Check OpenCV reference for more info.

# Draw the lines
print(lines)
print(lines.shape)
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv.line(Img, pt1, pt2, (20+i,12+i*4,25+i*8), 3, cv.LINE_AA)
        # Img
        # Point 	pt1,
        # Point 	pt2,
        # const Scalar & 	color,
        # int 	thickness = 1,
        # int 	lineType = LINE_8,
        # int 	shift = 0 

cv.imshow('Find lines',cv.resize(Img,(0,0),fx=2,fy=2))
print('the number of lines is'+str(i+1))
cv.waitKey(0)

plt.figure()
plt.subplot(121)
plt.imshow(I)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(Edge_canny)
plt.title('Edge detection using canny')
plt.xticks([])
plt.yticks([])

plt.figure()
plt.subplot(121)
plt.imshow(I)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(Edge_Laplacian)
plt.title('Edge detection using Laplacian')
plt.xticks([])
plt.yticks([])

plt.figure()
plt.subplot(121)
plt.imshow(I)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(Img)
plt.title('Find lines')
plt.xticks([])
plt.yticks([])

plt.show(block=False)
plt.pause(20)
plt.close

