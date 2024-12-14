import cv2 as cv
from skimage import exposure 
from skimage.exposure import match_histograms 
import numpy as np
import matplotlib.pyplot as plt

A=cv.imread('C:/Program Files/MATLAB/R2023a/toolbox/images/imdata/westconcordaerial.png')
ref=cv.imread('C:/Program Files/MATLAB/R2023a/toolbox/images/imdata/westconcordorthophoto.png')

cv.imshow('Original image',A)
cv.imshow('Reference imafe',ref)

A=cv.cvtColor(A,cv.COLOR_RGB2GRAY)

matched=match_histograms(A, ref,multichannel=True)

cv.imshow('matched',matched)

cv.waitKey(0)
cv.destroyAllWindows()