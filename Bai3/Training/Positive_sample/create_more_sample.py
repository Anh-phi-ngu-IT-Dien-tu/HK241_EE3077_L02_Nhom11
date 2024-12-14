import os
import cv2

for i in range(1,14,1):
    path='Viola_Jones/Training/Positive_sample/data{ij}.jpg'.format(ij=i)
    frame=cv2.imread(path)
    try:
        cv2.imshow("Image",frame)
        output=cv2.GaussianBlur(src=frame,ksize=(5,5),sigmaX=1000,sigmaY=1000,borderType=cv2.BORDER_WRAP)
        cv2.imwrite('Viola_Jones/Training/Positive_sample/datamedian{ij}.jpg'.format(ij=i),output)    
    except :
        continue

for i in range(14,18,1):
    path='Viola_Jones/Training/Positive_sample/data{ij}.jpg'.format(ij=i)
    frame=cv2.imread(path)
    try:
        cv2.imshow("Image",frame)
        output=cv2.GaussianBlur(src=frame,ksize=(11,11),sigmaX=1000,sigmaY=1000,borderType=cv2.BORDER_WRAP)
        cv2.imwrite('Viola_Jones/Training/Positive_sample/datamedian{ij}.jpg'.format(ij=i),output)    
    except :
        continue

for i in range(18,24,1):
    path='Viola_Jones/Training/Positive_sample/data{ij}.jpg'.format(ij=i)
    frame=cv2.imread(path)
    try:
        cv2.imshow("Image",frame)
        output=cv2.GaussianBlur(src=frame,ksize=(3,3),sigmaX=200,sigmaY=200,borderType=cv2.BORDER_WRAP)
        cv2.imwrite('Viola_Jones/Training/Positive_sample/datamedian{ij}.jpg'.format(ij=i),output)    
    except :
        continue

for i in range(24,28,1):
    path='Viola_Jones/Training/Positive_sample/data{ij}.jpg'.format(ij=i)
    frame=cv2.imread(path)
    try:
        cv2.imshow("Image",frame)
        output=cv2.GaussianBlur(src=frame,ksize=(10,10),sigmaX=500,sigmaY=500,borderType=cv2.BORDER_WRAP)
        cv2.imwrite('Viola_Jones/Training/Positive_sample/datamedian{ij}.jpg'.format(ij=i),output)    
    except :
        continue


