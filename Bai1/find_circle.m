clc
close all
A = imread('coins.png');

[centers, radii, metric] = imfindcircles(A,[30 60])%radiuas from 30-60
%centersStrong5 = centers(1:5,:); 
%radiiStrong5 = radii(1:5);
%metricStrong5 = metric(1:5);
figure
imshow(A)
viscircles(centers, radii,'EdgeColor','r');

figure
A = imread('circlesBrightDark.png');
imshow(A)
[centersBright, radiiBright] = imfindcircles(A,[20 100],'ObjectPolarity','bright');%radiuas from 20-100
[centersBright1, radiiBright1] = imfindcircles(A,[20 100],'ObjectPolarity','dark');
viscircles(centersBright, radiiBright,'Color','b');
viscircles(centersBright1, radiiBright1,'Color','r');


