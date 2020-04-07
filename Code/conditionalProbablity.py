import math
import numpy as np
import csv
csv.field_size_limit(1000000000)

GREEN = {}
YELLOW = {}
ORANGE = {}


def generateCoVarMatrix(color):
    rows = color['CoVar_Mat'][1: -1].split(']')
    CoVarMatrix = np.array([rows[0][1:].split(','), rows[1][3:].split(','), rows[2][3:].split(',')], dtype=float)
    return CoVarMatrix


def generateMeanMatrix(color):
    return np.array([[color['B_Mean']], [color['G_Mean']], [color['R_Mean']]], dtype=float)


def generateProb(givenInt, coVarMat, meanPt):
    Det_CoVarMatrix = np.linalg.det(coVarMat)
    constant = 1 / (((2 * 3.14) ** 3) * Det_CoVarMatrix) ** (0.5)

    inv_CoVarMatrix = np.linalg.inv(coVarMat)
    ptMinMean = givenInt - meanPt
    e = np.matmul(np.matmul(np.transpose(ptMinMean), inv_CoVarMatrix), ptMinMean) / (-2)
    return constant * math.exp(e)


reader = csv.reader(open('green.csv', 'r'))
for row in reader:
    if row == []:
        continue
    else:
        k, v = row
        GREEN[k] = v

reader = csv.reader(open('yellow.csv', 'r'))
for row in reader:
    if row == []:
        continue
    else:
        k, v = row
        YELLOW[k] = v

reader = csv.reader(open('orange.csv', 'r'))
for row in reader:
    if row == []:
        continue
    else:
        k, v = row
        ORANGE[k] = v

givenPt = np.array([[133], [230], [200]], dtype=float)

CoVarMatrix_Green = generateCoVarMatrix(GREEN)
meanPt_Green = generateMeanMatrix(GREEN)
print("probability that the intensity is green: ", generateProb(givenPt, CoVarMatrix_Green, meanPt_Green))

CoVarMatrix_Yellow = generateCoVarMatrix(YELLOW)
meanPt_Yellow = generateMeanMatrix(YELLOW)
print("probability that the intensity is yellow: ", generateProb(givenPt, CoVarMatrix_Yellow, meanPt_Yellow))

CoVarMatrix_Orange = generateCoVarMatrix(ORANGE)
meanPt_Orange = generateMeanMatrix(ORANGE)
print("probability that the intensity is orange: ", generateProb(givenPt, CoVarMatrix_Orange, meanPt_Orange))
