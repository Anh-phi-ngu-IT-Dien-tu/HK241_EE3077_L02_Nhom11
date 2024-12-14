clc
close all
clear
I=imread("coins.png");
figure
imshow(I)
[Gmag,Gdir] = imgradient(I,"prewitt");%find gradient manitude and direction using prewitt method
figure
imshowpair(Gmag,Gdir,"montage");
title("Gradient Magnitude (Left) and Gradient Direction (Right) Using Prewitt Method")
[Gmag,Gdir] = imgradient(I,"sobel");%find gradient manitude and direction using sobel method
figure
imshowpair(Gmag,Gdir,"montage");
title("Gradient Magnitude (Left) and Gradient Direction (Right) Using sobel Method")

[Gx,Gy]=imgradientxy(I,"prewitt");
figure
imshowpair(Gx,Gy,"montage")
title("Gradient x and Gradient y Using prewitt Method")
[Gx,Gy]=imgradientxy(I);
figure
imshowpair(Gx,Gy,"montage")
title("Gradient x and Gradient y Using sobel Method")