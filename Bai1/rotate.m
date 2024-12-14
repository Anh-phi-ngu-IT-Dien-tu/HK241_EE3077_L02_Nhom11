I = fitsread('solarspectra.fts');
I = rescale(I);
figure
imshow(I)
title('Original Image')
J = imrotate(I,-30,"bilinear",'loose');figure
imshow(J)
title('Rotated Image')