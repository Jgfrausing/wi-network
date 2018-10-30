import numpy as np
from scipy import sparse

def getSparseFriends():
    getSparseFriends("material/friendships.txt")

def getSparseFriends(file):
    file = open(file, "r")

    lines = file.readlines()
    friendships = {}
    user = ""
    userId = {}

    idCount = 0
    for line in lines:        
        if line.startswith("user:"):
            user = line.replace("user: ", "").lower().strip()
            if user not in userId:
                userId[user] = idCount
                idCount += 1
        elif line.startswith("friends:"):
            friendships[user] = line.replace("friends:", "").lower().split()
            for friend in friendships[user]:
                if friend not in userId:
                    userId[friend] = idCount
                    idCount += 1

    n = len(userId)
    matrix = np.zeros((n, n), dtype=int)

    for key, value in friendships.items():
        for friend in value:
            matrix[userId[key], userId[friend]] = 1
            spar2[userId[key], userId[friend]] = 1

    matrix = sparse.csr_matrix(matrix)

    return matrix, userId
