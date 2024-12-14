clc 
clear all
I=imread("Capture.jpg")
I=rgb2gray(I);
H=imgaussfilt(I,10);
figure
imshowpair(I,H,'montage')
imwrite(H,'modified_image.jpg')