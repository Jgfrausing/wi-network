
# To get the packages: pip3 install -r requirements.txt

import numpy as np
import scipy.linalg as la
from sklearn.cluster import KMeans
from numpy.linalg import eig
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

def printMatrix(M, name):
  print(name + ":")
  [print(row) for row in M]
  print()


eigenStuff = eig(A)
#printMatrix(eigenStuff, "EigenValues and EigenVectors")

secondSmallestEigenVector = eigenStuff[1][1]
print(secondSmallestEigenVector)

kmeans = KMeans(n_clusters=2, init=secondSmallestEigenVector)
#kmeans.cluster_centers_


print(kmeans)