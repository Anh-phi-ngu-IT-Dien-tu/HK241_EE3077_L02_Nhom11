clc
close all
A = imread('cameraman.tif');
filter=imboxfilt(A,11);%image, n*n average filter
Iblur = imgaussfilt(A,2);
figure
imshowpair(A,filter,"montage")
figure
montage([A,Iblur])

