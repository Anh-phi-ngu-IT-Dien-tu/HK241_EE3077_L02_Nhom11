clc
close all
I=imread("circuit.tif");

figure
imshow(I)

E=edge(I,'canny');
figure
imshowpair(I,E,'montage')

[H,T,R] = hough(E,'RhoResolution',0.5,'Theta',-90:0.5:89);
G=imadjust(rescale(H));
figure
imshow(G)
figure
imshow(G,'XData',T,'YData',R,...
      'InitialMagnification','fit');
axis on, axis normal, hold on;
colormap(gca,hot);

RGB = imread('gantrycrane.png');
figure
imshow(RGB)
I  = im2gray(RGB);
BW = edge(I,'canny');
figure
imshow(BW)
[H,T,R] = hough(BW,'Theta',44:0.5:46);
figure
imshow(imadjust(rescale(H)),'XData',T,'YData',R,...
   'InitialMagnification','fit');
title('Limited Theta Range Hough Transform of Gantrycrane Image');
xlabel('\theta')
ylabel('\rho');
axis on, axis normal;
colormap(gca,hot)


