import cv2
import numpy as np

img = cv2.imread('D:\MachineVison\cachinh tron.png')

#xoay anh voi goc la 90 do
#newimg = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

#cv2.imshow('anh moi',newimg)

#lay kich thuoc cua anh
(h, w,d) = img.shape # chieu cao, chieu rong , chieu sau
print("width={}, height={}, depth={}".format(w, h, d))

#xoay anh voi cac goc bat ki
center = (w // 2, h // 2) #tinh toa do tam xoay
M = cv2.getRotationMatrix2D(center, 45, 1.0) # tao ma tran xoay
rotated = cv2.warpAffine(img, M, (w,h)) #ap dung phep bien doi hinh hoc len anh
cv2.imshow('anh cu',img)
cv2.imshow('anh moi',rotated)
cv2.waitKey()
