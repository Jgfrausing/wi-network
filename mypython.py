# To get the packages: pip3 install -r requirements.txt

import numpy as np
import scipy.linalg as la
np.set_printoptions(suppress=True)

A = np.array([[1,3,4],[2,1,3],[4,1,2]])

L = np.array([[1,0,0],[2,1,0],[4,11/5,1]])
U = np.array([[1,3,4],[0,-5,-5],[0,0,-3]])
print(L.dot(U))
print(L)
print(U)