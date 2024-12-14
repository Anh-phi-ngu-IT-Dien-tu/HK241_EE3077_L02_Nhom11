A = imread('coins.png');
figure
imshow(A)
imwrite(A,'new.png')
% hold on
% [centers, radii, metric] = imfindcircles(A,[15 30]); % tim vong tron có ban kinh tu 15 den 30
% centersStrong5 = centers(1:5,:); 
% radiiStrong5 = radii(1:5);
% metricStrong5 = metric(1:5);
% viscircles(centersStrong5, radiiStrong5,'Color','b'); % tao vong tron
% 
% C = imread('circlesBrightDark.png'); 
% figure
% imshow(C)
% hold on
% Rmin = 30;
% Rmax = 65;
% [centersBright, radiiBright] = imfindcircles(C,[Rmin Rmax],'ObjectPolarity','bright'); %tim vong tron mau sang
% [centersDark, radiiDark] = imfindcircles(C,[Rmin Rmax],'ObjectPolarity','dark'); %tim vogn tron mau toi
% viscircles(centersBright, radiiBright,'Color','b');
% viscircles(centersDark, radiiDark,'LineStyle','--');
