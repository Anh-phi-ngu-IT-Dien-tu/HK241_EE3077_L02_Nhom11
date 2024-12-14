clc
close all
I=imread('snowflakes.png');
Kernel= [1 1 1; -1 -5 1; -1 -1 1];
figure
imshow(I)
J=ordfilt2(I,5,Kernel);
figure
imshowpair(I,J,'montage')
title('Filter with defined kernel')
true(5)
