clc
close all
clear
BW = imread('text.png');
se = strel('line',11,90);
BW2 = imdilate(BW,se);
imshow(BW), title('Original')
figure 
imshow(BW2)
title('Dilated')

A = imread('coins.png');
figure
imshow(A)
se=strel('disk',6);
Aerode=imdilate(A,se);
figure
montage([A,Aerode])