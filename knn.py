from math import sqrt


class Instance:
    points = []
    labeledClass = ""

    def __init__(self, points, labeledClass):
        self.points = points
        self.labeledClass = labeledClass


def knn(testPoint, trainingData, k):  # algorithm for one point
    distArr = []
    for anInstance in trainingData:  # calculate distance b/w this point and all training data
        distArr.append(
            (distance(testPoint.points, anInstance.points), anInstance.labeledClass))  # have distance and class saved
    distArr = sorted(distArr, reverse=False)  # sort distances descending
    kNN = distArr[:k]  # get k first neighbors
    map = {}
    for element in kNN:
        map[element[1]] = 0
    for element in kNN:
        map[element[1]] += 1

    predicted = max(map, key=lambda key: map[key])
    predictedFrequency = map[predicted]
    tie = [predicted]
    for element in map:
        if map[element] == predictedFrequency and element != predicted:
            tie.append(element)
    if tie.__len__() > 1:  # tie occurred, get first appearance in file
        for anInstance in trainingData:
            if anInstance.labeledClass in tie:
                predicted = anInstance.labeledClass
                break

    return predicted


def distance(pointOne, pointTwo):
    total = 0
    for i in range(0, pointOne.__len__()):
        total += ((pointTwo[i] - pointOne[i]) ** 2)
    return sqrt(total)


def output():
    trainingDataLines = [line.rstrip('\n') for line in open('TrainData.txt')]
    trainingData = []
    for i in range(0, trainingDataLines.__len__() - 1):
        tmp = trainingDataLines[i].split(",")  # file is separated w/ commas
        points = []
        for j in range(0, 8):
            points.append(float(tmp[j]))
        labeledClass = tmp[8]
        tDInstance = Instance(points, labeledClass)
        trainingData.append(tDInstance)
    testDataLines = [line.rstrip('\n') for line in open('TestData.txt')]
    testData = []
    for i in range(0, testDataLines.__len__() - 1):
        tmp = testDataLines[i].split(",")  # file is separated w/ commas
        points = []
        for j in range(0, 8):
            points.append(float(tmp[j]))
        labeledClass = tmp[8]
        tDInstance = Instance(points, labeledClass)
        testData.append(tDInstance)

    for k in range(1, 10):
        print "K: ", k
        total = 0
        correct = 0
        for testDataInstance in testData:
            total += 1
            predicted = knn(testDataInstance, trainingData, k)
            print "Predicted class: ", predicted, " Actual class: ", testDataInstance.labeledClass
            if predicted == testDataInstance.labeledClass:
                correct += 1
        print "Correct classes: ", correct
        print "Accuracy: ", float(correct) / float(total)
        print "-------------------------"


output()
