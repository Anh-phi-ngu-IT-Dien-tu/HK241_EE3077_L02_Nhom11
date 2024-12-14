clc
close all
I = imread('pout.tif');
J = imtranslate(I,[50, -100],'FillValues',255);
figure
imshow(I);
title('Original Image');
set(gca,'Visible','on');
figure
imshow(J);
title('Translated Image');
set(gca,'Visible','on');

