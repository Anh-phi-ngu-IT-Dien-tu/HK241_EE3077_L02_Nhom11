clc
close all

I  = imread('circuit.tif');
I = imrotate(I,33,'crop');
%
figure
imshow(I)
BW = edge(I,'prewitt');
figure
imshow(BW)
[H,T,R] = hough(BW);%needed fo houghlines
figure
imshow(H,[],'XData',T,'YData',R,...
            'InitialMagnification','fit');%Hough transform diagram
xlabel('\theta'), ylabel('\rho');
axis on, axis normal, hold on;

P  = houghpeaks(H,5,'threshold',ceil(0.3*max(H(:))))%needed for houghlines% lam tron 
x = T(P(:,2)); y = R(P(:,1));
plot(x,y,'s','color','white');

lines = houghlines(BW,T,R,P,'FillGap',5,'MinLength',7);%fillgap khoang cach toi giua cac pixel de duoc xem nhu doan thang, %do dai toi thieu de duoc xem nhu duong thang
%se ra 12 hang co cung ro va theta
figure
imshow(I) 
hold on
max_len = 0;
for k = 1:length(lines)
   xy = [lines(k).point1; lines(k).point2];
   plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');

   % Plot beginnings and ends of lines
   plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
   plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');

   % Determine the endpoints of the longest line segment
   len = norm(lines(k).point1 - lines(k).point2);
   if ( len > max_len)
      max_len = len;
      xy_long = xy;
   end
end

%plot(xy_long(:,1),xy_long(:,2),'LineWidth',2,'Color','cyan');