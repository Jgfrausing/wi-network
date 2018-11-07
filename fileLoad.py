import numpy as np
from scipy import sparse

def getSparseFriendsDefault():
    return getSparseFriends("material/friendships.txt")

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

    #matrix = sparse.csr_matrix(matrix)
    userId = {v: k for k, v in userId.items()}

    return matrix, userId


def getWordsClassesAndReviewsFromFile(filepath : str):
    reviews = []
    words = set()
    classes = []

    with open(filepath) as file_handler:
        score = 0
        review = ""
        for line in file_handler:
            if line.startswith("review/score:"):
                score = float(line.strip("review/score: "))
                if score not in classes:
                    classes.append(score)

            if line.startswith("review/summary"):
                review = line.strip("review/summary: ").rstrip("\n") + " . "

            if line.startswith("review/text"):
                review += line.strip("review/text: ").rstrip("\n")

            if line == "\n":
                reviews.append((review, score))
                for word in (review.split()):
                    if word not in words:
                        words.add(word)
                review = ""
    return words, classes, reviews
