
# To get the packages: pip3 install -r requirements.txt

import numpy as np
import scipy.linalg as la
from sklearn.cluster import KMeans
import numpy.linalg as npl

np.set_printoptions(suppress=True)

A = np.array( [ [0, 1, 1, 0, 0, 0, 0, 0, 0]
              , [1, 0, 1, 0, 0, 0, 0, 0, 0]
              , [1, 1, 0, 1, 1, 0, 0, 0, 0]
              , [0, 0, 1, 0, 1, 1, 1, 0, 0]
              , [0, 0, 1, 1, 0, 1, 1, 0, 0]
              , [0, 0, 0, 1, 1, 0, 1, 1, 0]
              , [0, 0, 0, 1, 1, 1, 0, 1, 0]
              , [0, 0, 0, 0, 0, 1, 1, 0, 1]
              , [0, 0, 0, 0, 0, 0, 0, 1, 0]
              ])


def mkLaplacian(A):
  D = [sum(row) for row in A] * np.eye(A.shape[0])
  return D - A

def mkEigenDecom(L):
  return npl.eig(L)

# We need second smallest because of math
def getSecondSmallestEigenVector(eigenDecom):
  eigValues = eigenDecom[0]
  smallestIndex = 0
  secondSmallIndex = 0
  smallestValue = float('inf')
  secondSmallValue = float('inf')

  for x in range(0,len(eigValues)):
    value = eigValues[x]
    if value <= smallestValue:
      secondSmallValue = smallestValue
      secondSmallIndex = smallestIndex

      smallestValue = value
      smallestIndex = x
    elif value <= secondSmallValue:
      secondSmallValue = value
      secondSmallIndex = x

  return eigenDecom[1][:,secondSmallIndex]

def getClusterAmount(matrix):
  return 2 # dynamic

def getClusters(amount, eigenVector):
  return KMeans(n_clusters=amount).fit(eigenVector.reshape(-1, 1)).labels_


L = mkLaplacian(A)
eiDecom = mkEigenDecom(L)
getSecondSmallestEigenVector(eiDecom)