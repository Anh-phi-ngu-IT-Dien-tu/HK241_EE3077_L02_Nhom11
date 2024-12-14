clc
clf
clear
close all
A = imread("westconcordaerial.png");
Ref = imread("westconcordorthophoto.png");

figure
imshowpair(A,rgb2gray(A),"montage")
title("Anh bi phai mau")
figure
imshow(Ref)
title("target histogram")
B = imhistmatch(A,Ref);
figure
imshow(B)
title("Histogram Matched RGB Image")
figure
imhist(A)
figure
imhist(Ref)
figure
imhist(B)


