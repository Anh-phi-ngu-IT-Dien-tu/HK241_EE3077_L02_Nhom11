detector = vision.CascadeObjectDetector("stopSignDetector.xml");
img = imread("stopSignTest.jpg");
bbox = step(detector,img);
detectedImg = insertObjectAnnotation(img,"rectangle",bbox,"stop sign");
figure
imshow(detectedImg)