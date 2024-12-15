load("limitted_speed_120.mat")

%% The paths of positive image
posImages=imageDatastore(gTruth.DataSource.Source)

%% Label data
bounding_boxex=boxLabelDatastore(gTruth.LabelData)

%% Combine the image and box label datastores
positiveInstance=combine(posImages,bounding_boxex)

%% Get negative images
negativeFolder="D:\COMPUTER_VISION_TEAMWORK\Viola_Jones\Training\nonStopSigns"
negativeImages = imageDatastore(negativeFolder)

%% Training process
trainCascadeObjectDetector("detector.xml",positiveInstance,negativeFolder,FalseAlarmRate=0.01,NumCascadeStages=5);
