# This example is taken from "Machine Learning in Action,Ch02"

from numpy import *
import operator

def createDataSet():
  group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
  labels = ['A','A','B','B']
  return group, labels

# Function: classify0:
# For every point in our dataset:
#  Calculate the distance between inX and the current point
#  Sort the distances in increasing order
#  Take k items with lowest distances to inX
#  Find the majority class among these items
#  Return themajority class as the prediction for the class of inX
# Inputs:
#  inX: input vector to classify
#  dataSet: full matrix of training examples
#  labels: vector or labels
#  k: number of nearest neighbors to use in voting

def classify0(inX, dataSet, labels, k):
  dataSetSize = dataSet.shape[0]  # returns the number of measurements (observations)
  # Perform Euclidean distance calculation
  diffMat = tile(inX, (dataSetSize,1)) - dataSet
  sqDiffMat = diffMat**2
  sqDistances = sqDiffMat.sum(axis=1)
  distances = sqDistances**0.5
  # Get list of sorted indices
  sortedDistIndices = distances.argsort()
  # Voting with lowest k distances
  classCount={}
  for i in range(k):
    voteIlabel = labels[sortedDistIndices[i]]  
    classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
  sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
  return sortedClassCount[0][0]

# Process tab delimited text from file into a matrix
def file2matrix(filename):
  fr = open(filename)
  # Get number of lines (observations) in file
  numberOfLines = len(fr.readlines())
  # Create matrix to return
  returnMat = zeros((numberOfLines,3))
  classLabelVector = []
  fr = open(filename)
  index = 0
  for line in fr.readlines():
    line = line.strip()
    listFromLine = line.split('\t')
    returnMat[index,:] = listFromLine[0:3]
    classLabelVector.append(int(listFromLine[-1]))
    index += 1
  return returnMat, classLabelVector

# Normalizing a data set
# use formula newValue = (oldValue-min)/(max - min)
# on a columna basis
def autoNorm(dataSet):
  minVals = dataSet.min(0)   # min and max per column
  maxVals = dataSet.max(0)
  ranges = maxVals - minVals
  normDataSet = zeros(shape(dataSet))
  m = dataSet.shape[0]       # find the number of rows
  normDataSet = dataSet - tile(minVals, (m,1))
  normDataSet = normDataSet/tile(ranges, (m,1))
  return normDataSet, ranges, minVals
 
