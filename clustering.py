# To get the packages: pip3 install -r requirements.txt

import numpy as np
from sklearn.cluster import KMeans
import numpy.linalg as npl
import fileLoad

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

Asmall = np.array( [ [0, 1, 1, 0, 0, 0]
                   , [1, 0, 1, 0, 0, 0]
                   , [1, 1, 0, 1, 0, 0]
                   , [0, 0, 1, 0, 1, 1]
                   , [0, 0, 0, 1, 0, 1]
                   , [0, 0, 0, 1, 1, 0]
                   ])

def mkLaplacian(A):
  L = A * -1
  D = [sum(row) for row in A]
  for x in range(0, len(D)):
    L[x,x] = D[x] + A[x,x]
  return L

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
  return 5 # dynamic

def getClusters(amount, eigenVector):
  kmeans = KMeans(n_clusters=amount)
  transposed = eigenVector.reshape(-1,1)

  return kmeans.fit(transposed.real).labels_

def runSmallExample(): # from Lecture 7, slide 28
  L = mkLaplacian(Asmall)
  print(L)
  eiDecom = mkEigenDecom(L)
  print(eiDecom)
  sSEV = getSecondSmallestEigenVector(eiDecom)
  print(sSEV)
  clusters = getClusters(2, sSEV)  
  print(clusters)

def run():
  print("Loading network...")
  A, _ = fileLoad.getSparseFriendsDefault()
  print("Done")
  print("Laplacian... ")
  L = mkLaplacian(A)
  print("Done")
  print("Getting eigendecomposition...")
  eiDecom = mkEigenDecom(L)
  print("Done")
  print("Getting second smallest eigen vector...")
  sSEV = getSecondSmallestEigenVector(eiDecom)
  print("Done")
  print("\"Computing\" cluster amounts...")
  clustAmount = getClusterAmount(sSEV)
  print("Done")
  print("Getting clusters...")
  clusters = getClusters(clustAmount, sSEV)
  print(clusters)

  print("Writing clusters to file: 'material/clusteringResults.txt'...")
  with open('material/clusteringResults.txt', 'w') as f:
    for item in clusters:
      f.write("%s\n" % item)

  print("Done")



runSmallExample()
# The small graph
#   1 \      / 5
#   |  3 - 4   |
#   2 /      \ 6
# 
# sSEV: [ 0.46470513  0.46470513  0.26095647 -0.26095647 -0.46470513 -0.46470513]
# Splits: [1 1 1 0 0 0]


#run()

