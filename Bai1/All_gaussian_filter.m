clc
close all
I=imread("Capture.jpg");
I=rgb2gray(I);
figure
imshow(I)
I=imnoise(I,"gaussian")
figure
imshow(I)
J=imgaussfilt(I);% using gaussian filter with standard deviation=0.5
figure
montage([I,J])
title('Standard deviation=0.5')
H=imgaussfilt(I,10);
figure
montage([I,H])
title('Standard deviation=10')