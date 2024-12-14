import os
import cv2
import matplotlib.pyplot as plt

cascPathface = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"

faceCascade=cv2.CascadeClassifier(cascPathface)

output_frames=[]

for i in range(1,21,1):
    path='Viola_Jones/{ij}.jpg'.format(ij=i)
    frame=cv2.imread(path)
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces=faceCascade.detectMultiScale(image=gray_frame,scaleFactor=1.1,minNeighbors=4,minSize=(20,20),
                                       flags=cv2.CASCADE_SCALE_IMAGE)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h),(255,0,0),thickness=10)

    cv2.imwrite('Viola_Jones/{ij}py.jpg'.format(ij=i),frame)    
    output_frames.append(frame)


for i in range(20):
    plt.figure()
    plt.imshow(output_frames[i])
    plt.title('Result')
    plt.xticks([])
    plt.yticks([])

plt.show()