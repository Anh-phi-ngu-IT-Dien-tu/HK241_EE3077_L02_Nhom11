%% Load model
detector = vision.CascadeObjectDetector("detector.xml");


for i=1:20
%% Load image
path="Test_sample\"+num2str(i)+".jpg"
img = imread(path);

%% Find object
bbox = step(detector,img);

%% Insert box
detectedImg = insertObjectAnnotation(img,"rectangle",bbox,"stop sign");

%% Show figure
figure
imshow(detectedImg)

imwrite(detectedImg,"Result\"+num2str(i)+"mat.jpg")

end