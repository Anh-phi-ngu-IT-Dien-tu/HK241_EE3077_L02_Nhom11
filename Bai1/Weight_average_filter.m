clc
close all
A = imread('cameraman.tif');
A = double(A);
localSums = imboxfilt(A, 11, 'NormalizationFactor',1);
figure
imshowpair(A,localSums,'montage')
figure
histogram(localSums)
figure
histogram(A)