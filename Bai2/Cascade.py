import os
import cv2

"""
These are predefined model that exist when we download opencv with pip
"""
cascPathface = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
cascPatheyes = os.path.dirname(cv2.__file__) + "/data/haarcascade_eye_tree_eyeglasses.xml"

#loading the classifier with a model file xml file
faceCascade=cv2.CascadeClassifier(cascPathface)

#capture video from pc/laptop webcam
video_capture=cv2.VideoCapture(0)

print(cascPathface)

while True:
    #capture image frame from video
    ret,frames=video_capture.read()

    gray_frame=cv2.cvtColor(src=frames,code=cv2.COLOR_RGB2GRAY)

    """
    scaleFactor: resize the image so our classifier which is an 24*24 window can detect easier
    minNeighbors:Parameter specifying how many neighbours each candidate rectangle should have to retain it. 
                This parameter will affect the quality of the detected faces. Higher value results in fewer 
                detections but with higher quality. 3~6 is a good value for it.
    flags : Mode of operation
    minSize: Minimum possible object size. Objects smaller than that are ignored.
    maxSize: Maximum possible object size. Objects larger than that are ignored. 
            If maxSize == minSize model is evaluated on single scale
    """
    faces=faceCascade.detectMultiScale(image=gray_frame,scaleFactor=1.1,minNeighbors=4,minSize=(20,20),
                                       flags=cv2.CASCADE_SCALE_IMAGE)
    
    print(len(faces))
    #draw the rectangular 
    for (x,y,w,h) in faces:
        cv2.rectangle(frames, (x, y), (x + w, y + h),(0,25,122),thickness=10)
    
    cv2.imshow('Video', frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
