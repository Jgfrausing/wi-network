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


def save_matrix(matrix, filename):
    mat_file = '' #.join([f"{x};" for x in [row for row in word_class_matrix]])
    for row in matrix:
        for elm in row:
            mat_file += f"{int(elm)};"
        mat_file += "\n"
    save_file(mat_file, filename)
    pass


def save_dict(dic, filename):
    ind_file = ''.join([f"{x};{dic[x]};\n" for x in dic])
    save_file(ind_file, filename)
    pass


def read_matrix(filename):
    mat_file = read_file(filename)

    rows = mat_file.split("\n")
    row_count = len(rows)-1
    col_count = len(rows[0].split(";"))-1

    matrix = np.zeros(shape=(row_count, col_count))

    for row in range(0, row_count):
        cols = rows[row].split(";")
        for col in range(0, col_count):
            matrix[row][col] = float(cols[col])

    return matrix
     
def read_dict(filename):
    dict_file = read_file(filename)

    rows = dict_file.split("\n")
    row_count = len(rows)-1
    col_count = len(rows[0].split(";"))-1

    dic = {}

    for row in range(0, row_count):
        cols = rows[row].split(";")
        dic[cols[0]] = cols[1]

    return dic

def read_file(filename):
    file = open(f"material/{filename}.csv","r") 
    return file.read() 

def save_file(str, filename):
    file = open(f"material/{filename}.csv","w") 
    file.write(str) 

