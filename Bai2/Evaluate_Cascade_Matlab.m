close all
clc
clear 
faceDetector = vision.CascadeObjectDetector;


k=0;
for i=1:20
    path =num2str(i)+".jpg";
    I = imread(path);
    bboxes = faceDetector(I);
    if(~isnan(bboxes))
        k=k+1;
    end
    IFaces = insertObjectAnnotation(I,'rectangle',bboxes,'Face');   
    figure
    imshow(IFaces);
    imwrite(IFaces,num2str(i)+"mat.jpg")
end


