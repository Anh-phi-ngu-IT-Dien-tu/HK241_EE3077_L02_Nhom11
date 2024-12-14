clc
close all
originalBW = imread('text.png');

se = strel('line',11,90);

erodedBW = imerode(originalBW,se);
figure
imshow(originalBW)
figure
imshow(erodedBW)

A = imread('coins.png');
figure
imshow(A)
se=strel('disk',6);
Aerode=imerode(A,se);
figure
montage([A,Aerode])