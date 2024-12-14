clc
close all
I = imread('pout.tif');
J = imadjust(I);%When you use this syntax, imadjust saturates the bottom 1% and the top 1% of all pixel values. 
% The function linearly maps pixel values between the saturation limits to values between 0 and 1
%almost the same like histeq
figure
imshow(I)
title('Original image')
figure
imhist(I)
title('Original image histogram')
figure
imshow(J)
title('Image with adjust function')
figure
imhist(J)
title('Image histogram with adjust function')
G=imadjust(I,[0.3 0.7]);%maps intensity values in I to new values in J such that values between 
% low_in and high_in linearly map to values between 0 and 1.
% [0.3 0.7] ->[0 1]
figure()
imshow(G)
title('Image with desired adjust function')
figure
imhist(G)
title('Image histogram with  desired adjust function')
H=imadjust(I,[0.1 0.7],[0.2 0.5]);
figure
imshow(H)
title('Image with desired adjust function 2')
figure
imhist(H)
title('Image histogram with desired adjust function 2')

mydlg = warndlg('This is a warning.', 'A Warning Dialog');
waitfor(mydlg);
disp('This prints after you close the warning dialog.');
clc
clear
close all
RGB=imread('Capture.jpg');
figure
imshow(RGB);
title('RGB image')
RGB2 = imadjust(RGB,[.2 .3 0; .6 .7 1],[]);
figure
imshow(RGB2)
imwrite(RGB2,'ghost.jpg')
