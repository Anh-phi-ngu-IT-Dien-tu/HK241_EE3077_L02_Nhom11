from evaluate_alexnet import *
import csv

evaluate=AlexNet_Image_Classification()
txtFilepath='Counting_true_false.txt'
counting_true_top1=0
counting_true_top5=0

##Kimono evaluation
csvFilepath='Kimono_label_evaluation.csv'

with open(csvFilepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    data=[['Image number','Rank5','Rank4','Rank3','Rank2','Rank1','Label probability','Top 1 evaluation','Top 5 evaluation']]
    writer.writerows(data)

for i in range(1,21,1):
    print('\nImage kimono number '+str(i))
    data.append(i)
    imageFilepath='D:/COMPUTER_VISION_TEAMWORK/AlexNet/kimono{num}.jpg'.format(num=i)
    evaluate.choseClassId('kimono')
    evaluate.getSoftmaxResult(imageFilepath)
    evaluate.printResultTop1()
    evaluate.printResultTop5()
    evaluate.resultTop1()
    evaluate.resultTop5()
    evaluate.EvaluateTop1()
    evaluate.EvaluateTop5()

    with open(csvFilepath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        datawrite=[[i,evaluate.Rank[0],evaluate.Rank[1],evaluate.Rank[2],evaluate.Rank[3],evaluate.Rank[4],evaluate.Label_prob,evaluate.evalTop1,evaluate.evalTop5]]
        writer.writerows(datawrite)
    
    if evaluate.evalTop1==True:
        counting_true_top1=counting_true_top1+1
    if evaluate.evalTop5==True:
        counting_true_top5=counting_true_top5+1

    

file = open(txtFilepath, "w") 
string1='The number of True in Top1 evaluation of Kimono is'+str(counting_true_top1)+'\n'
string2='The number of True in Top5 evaluation of Kimono is'+str(counting_true_top5)+'\n'
file.write(string1)
file.write(string2)
counting_true_top1=0
counting_true_top5=0


##Miniskirt evaluation
csvFilepath='Miniskirt_label_evaluation.csv'

with open(csvFilepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    data=[['Image number','Rank5','Rank4','Rank3','Rank2','Rank1','Label probability','Top 1 evaluation','Top 5 evaluation']]
    writer.writerows(data)

for i in range(1,21,1):
    print('\nImage miniskirt number '+str(i))
    data.append(i)
    imageFilepath='D:/COMPUTER_VISION_TEAMWORK/AlexNet/miniskirt{num}.jpg'.format(num=i)
    evaluate.choseClassId('miniskirt')
    evaluate.getSoftmaxResult(imageFilepath)
    evaluate.printResultTop1()
    evaluate.printResultTop5()
    evaluate.resultTop1()
    evaluate.resultTop5()
    evaluate.EvaluateTop1()
    evaluate.EvaluateTop5()

    with open(csvFilepath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        datawrite=[[i,evaluate.Rank[0],evaluate.Rank[1],evaluate.Rank[2],evaluate.Rank[3],evaluate.Rank[4],evaluate.Label_prob,evaluate.evalTop1,evaluate.evalTop5]]
        writer.writerows(datawrite)

    if evaluate.evalTop1==True:
        counting_true_top1=counting_true_top1+1
    if evaluate.evalTop5==True:
        counting_true_top5=counting_true_top5+1

file = open(txtFilepath, "a") 
string1='The number of True in Top1 evaluation of miniskirt is'+str(counting_true_top1)+'\n'
string2='The number of True in Top5 evaluation of miniskirt is'+str(counting_true_top5)+'\n'
file.write(string1)
file.write(string2)
counting_true_top1=0
counting_true_top5=0

##Missile evaluation
csvFilepath='Missile_label_evaluation.csv'

with open(csvFilepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    data=[['Image number','Rank5','Rank4','Rank3','Rank2','Rank1','Label probability','Top 1 evaluation','Top 5 evaluation']]
    writer.writerows(data)

for i in range(1,21,1):
    print('\nImage missile number '+str(i))
    data.append(i)
    imageFilepath='D:/COMPUTER_VISION_TEAMWORK/AlexNet/missile{num}.jpg'.format(num=i)
    evaluate.choseClassId('missile')
    evaluate.getSoftmaxResult(imageFilepath)
    evaluate.printResultTop1()
    evaluate.printResultTop5()
    evaluate.resultTop1()
    evaluate.resultTop5()
    evaluate.EvaluateTop1()
    evaluate.EvaluateTop5()

    with open(csvFilepath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        datawrite=[[i,evaluate.Rank[0],evaluate.Rank[1],evaluate.Rank[2],evaluate.Rank[3],evaluate.Rank[4],evaluate.Label_prob,evaluate.evalTop1,evaluate.evalTop5]]
        writer.writerows(datawrite)

    if evaluate.evalTop1==True:
        counting_true_top1=counting_true_top1+1
    if evaluate.evalTop5==True:
        counting_true_top5=counting_true_top5+1

file = open(txtFilepath, "a") 
string1='The number of True in Top1 evaluation of missile is'+str(counting_true_top1)+'\n'
string2='The number of True in Top5 evaluation of missile is'+str(counting_true_top5)+'\n'
file.write(string1)
file.write(string2)
counting_true_top1=0
counting_true_top5=0

#Pizza evaluation
csvFilepath='Pizza_label_evaluation.csv'

with open(csvFilepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    data=[['Image number','Rank5','Rank4','Rank3','Rank2','Rank1','Label probability','Top 1 evaluation','Top 5 evaluation']]
    writer.writerows(data)

for i in range(1,21,1):
    print('\nImage pizza number '+str(i))
    data.append(i)
    imageFilepath='D:/COMPUTER_VISION_TEAMWORK/AlexNet/pizza{num}.jpg'.format(num=i)
    evaluate.choseClassId('pizza')
    evaluate.getSoftmaxResult(imageFilepath)
    evaluate.printResultTop1()
    evaluate.printResultTop5()
    evaluate.resultTop1()
    evaluate.resultTop5()
    evaluate.EvaluateTop1()
    evaluate.EvaluateTop5()

    with open(csvFilepath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        datawrite=[[i,evaluate.Rank[0],evaluate.Rank[1],evaluate.Rank[2],evaluate.Rank[3],evaluate.Rank[4],evaluate.Label_prob,evaluate.evalTop1,evaluate.evalTop5]]
        writer.writerows(datawrite)

    if evaluate.evalTop1==True:
        counting_true_top1=counting_true_top1+1
    if evaluate.evalTop5==True:
        counting_true_top5=counting_true_top5+1


file = open(txtFilepath, "a") 
string1='The number of True in Top1 evaluation of pizza is'+str(counting_true_top1)+'\n'
string2='The number of True in Top5 evaluation of pizza is'+str(counting_true_top5)+'\n'
file.write(string1)
file.write(string2)
counting_true_top1=0
counting_true_top5=0

##Tank evaluation
csvFilepath='Tank_label_evaluation.csv'

with open(csvFilepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    data=[['Image number','Rank5','Rank4','Rank3','Rank2','Rank1','Label probability','Top 1 evaluation','Top 5 evaluation']]
    writer.writerows(data)

for i in range(1,21,1):
    print('\nImage tank number '+str(i))
    data.append(i)
    imageFilepath='D:/COMPUTER_VISION_TEAMWORK/AlexNet/tank{num}.jpg'.format(num=i)
    evaluate.choseClassId('tank')
    evaluate.getSoftmaxResult(imageFilepath)
    evaluate.printResultTop1()
    evaluate.printResultTop5()
    evaluate.resultTop1()
    evaluate.resultTop5()
    evaluate.EvaluateTop1()
    evaluate.EvaluateTop5()

    with open(csvFilepath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        datawrite=[[i,evaluate.Rank[0],evaluate.Rank[1],evaluate.Rank[2],evaluate.Rank[3],evaluate.Rank[4],evaluate.Label_prob,evaluate.evalTop1,evaluate.evalTop5]]
        writer.writerows(datawrite)


    if evaluate.evalTop1==True:
        counting_true_top1=counting_true_top1+1
    if evaluate.evalTop5==True:
        counting_true_top5=counting_true_top5+1

file = open(txtFilepath, "a") 
string1='The number of True in Top1 evaluation of tank is'+str(counting_true_top1)+'\n'
string2='The number of True in Top5 evaluation of tank is'+str(counting_true_top5)+'\n'
file.write(string1)
file.write(string2)
counting_true_top1=0
counting_true_top5=0
