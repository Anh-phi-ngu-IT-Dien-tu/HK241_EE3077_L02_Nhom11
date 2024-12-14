from evaluate_alexnet import *
import csv
import numpy

evaluate=AlexNet_Image_Classification()

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


