clc
close all
I=imread('coins.png');
figure
imshow(I)
figure 
imhist(I)
level = graythresh(I)%Calculate a threshold using graythresh. The threshold is normalized to the range [0, 1].
BW = imbinarize(I,level);% if pixel sensivity is >= level then pixel value=1 else pixel value=0
figure
imshowpair(I,BW,'montage')
