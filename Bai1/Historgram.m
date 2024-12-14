clc
clear 
close all

I=imread("pout.tif");

figure
imhist(I)
[J,T]=histeq(I);
figure
imshowpair(I,J,"montage")
figure
imhist(J)
figure
plot((0:255)/255,T);
figure
histogram(I);
figure
histogram(J);
pause(20)
close all