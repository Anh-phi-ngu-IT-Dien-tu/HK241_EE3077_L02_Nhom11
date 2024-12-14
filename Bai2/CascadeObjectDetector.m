clc
faceDetector = vision.CascadeObjectDetector;

I = imread('visionteam.jpg');
bboxes = faceDetector(I)

IFaces = insertObjectAnnotation(I,'rectangle',bboxes,'Face');   
figure
imshow(IFaces)
title('Detected faces');

bodyDetector = vision.CascadeObjectDetector('UpperBody'); 
bodyDetector.MinSize = [60 60];
bodyDetector.MergeThreshold = 10;

I2 = imread('visionteam.jpg');
bboxBody = bodyDetector(I2);

IBody = insertObjectAnnotation(I2,'rectangle',bboxBody,'Upper Body');
figure
imshow(IBody)
title('Detected upper bodies');

% vidObj = VideoReader("WIN_20241117_18_11_11_Pro.mp4");
% while hasFrame(vidObj)
%     vidFrame = readFrame(vidObj);
%     imshow(vidFrame)
%     pause(1/60)
% end