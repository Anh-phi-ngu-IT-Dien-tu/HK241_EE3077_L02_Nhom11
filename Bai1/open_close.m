clc
close all
clear
original = imread('coins.png');
imshow(original);
se = strel('disk',25)
afterOpening = imopen(original,se)%erosion-dilation
figure
imshow(afterOpening);
figure
level=graythresh(afterOpening);
g=imbinarize(afterOpening,level);
imshow(g)

afterOpening = imclose(original,se)%dilation-erosion
figure
imshow(afterOpening);
figure
level=graythresh(afterOpening);
g=imbinarize(afterOpening,level);
imshow(g)
