clc
close all
I = imread('eight.tif');
J = imnoise(I,'salt & pepper',0.02);
figure
montage([I,J])
K = medfilt2(J,[3,3]);
figure
imshowpair(J,K,'montage')