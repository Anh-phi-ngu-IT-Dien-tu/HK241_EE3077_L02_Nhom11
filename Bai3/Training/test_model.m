%% Load model
detector = vision.CascadeObjectDetector("detector.xml");

%% Load image
img = imread("Test_sample\z6125163709543_840db72834f5ea6ed654f961e40ddc3c.jpg");

%% Find object
bbox = step(detector,img);

%% Insert box
detectedImg = insertObjectAnnotation(img,"rectangle",bbox,"stop sign");

%% Show figure
figure
imshow(detectedImg)