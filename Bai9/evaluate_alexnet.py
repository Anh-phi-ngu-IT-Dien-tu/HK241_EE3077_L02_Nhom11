from PIL import Image
from torchvision import transforms
import torch
import requests
import time

class AlexNet_Image_Classification():
    def __init__(self):
        "loading the model"
        self.model = torch.hub.load('pytorch/vision:v0.10.0', 'alexnet', pretrained=True)
        self.model.eval()
        self.probabilities=[]
        self.class_id=0
        self.Rank=[]
        self.Label_prob=0
        self.evalTop1=False
        self.evalTop5=False
        #move model to graphics card
        if torch.cuda.is_available():
            self.model.to('cuda')

    def getSoftmaxResult(self,path):

        "preprocess the image"
        start=time.time()
        input_image = Image.open(path)
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

        input_tensor = preprocess(input_image)
        ## create 224*224*3 batch to fit the input of alexnet
        input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model


        # move the input and model to GPU for speed if available
        if torch.cuda.is_available():
            input_batch = input_batch.to('cuda')
            

        with torch.no_grad():
            output = self.model(input_batch)
        # Tensor of shape 1000, with confidence scores over ImageNet's 1000 classes

        # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
        self.probabilities = torch.nn.functional.softmax(output[0], dim=0)
        end=time.time()
        print('time comsumption='+str(end-start))

    def choseClassId(self,object):
        """we need the output after softmax phase"""

        url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"

        # Send a GET request to download the class labels
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Convert the response text directly into a list of class labels
        class_labels = [line.strip() for line in response.text.splitlines()]
        self.class_id=class_labels.index(object)

    def EvaluateTop1(self):
        temp=self.probabilities
        m=max(temp)
        for i,j in enumerate(self.probabilities):
            if float(j) == m:
                res=i
                break

        if res == self.class_id:
            self.evalTop1=True
        else:
            self.evalTop1=False
    
    def EvaluateTop5(self):
        temp=self.probabilities
        max=sorted(range(len(temp)), key=lambda x: temp[x])
        res=max[-5:]
        
        for i,j in enumerate(res):
            if j==self.class_id:
                self.evalTop5=True
                return
            else:
                continue
        self.evalTop5=False        
    
    def resultTop1(self):
        temp=self.probabilities
        result=temp[self.class_id]
        self.Label_prob=result
    
    def resultTop5(self):
        temp=self.probabilities
        max=sorted(range(len(temp)), key=lambda x: temp[x])
        res=max[-5:]
        val=[]
        for i,j in enumerate(res):
            val.append(float(self.probabilities[j]))
        self.Rank=val

    def printResultTop1(self):
        temp=self.probabilities
        m=max(temp)
        for i,j in enumerate(self.probabilities):
            if float(j) == m:
                res=i
                break
        print('The components with id='+str(self.class_id)+' has a probability of '+str(self.probabilities[self.class_id]))
        print('The maximum value has id='+str(res)+' with a probability of '+str(float(self.probabilities[res])))

    def printResultTop5(self):
        temp=self.probabilities
        max=sorted(range(len(temp)), key=lambda x: temp[x])
        res=max[-5:]
        val=[]
        for i,j in enumerate(res):
            val.append(float(self.probabilities[j]))
        print('The components with id='+str(self.class_id)+' has a probability of '+str(float(self.probabilities[self.class_id])))
        print('The values in top 5 have ids='+str(res)+' has a probability of '+str(val))


    
        



    
