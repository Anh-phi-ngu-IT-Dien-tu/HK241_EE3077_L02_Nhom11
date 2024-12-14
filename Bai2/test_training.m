load("stopSignsAndCars.mat");
stopSigns = fullfile(toolboxdir("vision"),"visiondata",stopSignsAndCars{:,1})
imds = imageDatastore(stopSigns)
blds = boxLabelDatastore(stopSignsAndCars(:,2))
positiveInstances = combine(imds,blds)
imDir = fullfile(matlabroot,"toolbox","vision","visiondata","stopSignImages");
addpath(imDir);
negativeFolder = fullfile(matlabroot,"toolbox","vision","visiondata","nonStopSigns")
negativeImages = imageDatastore(negativeFolder);
trainCascadeObjectDetector("stopSignDetector.xml",positiveInstances,negativeFolder,FalseAlarmRate=0.01,NumCascadeStages=3);
