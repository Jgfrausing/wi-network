import fileLoad as fl

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

reviews = fl.read_json('material/instruments.json')

text = []
user = []
prod = []
scor = []

for review in reviews:
    text.append(review['reviewText'])
    user.append(review['reviewerID'])
    prod.append(review['asin'])
    scor.append(review['overall'])
    

productDict = {}
userDict = {}

for x in range(0, len(text)):
    if prod[x] in productDict:
        productDict[prod[x]] += " " + text[x] + " . "
    else:
        productDict[prod[x]] = text[x] + " . "

    if user[x] in userDict:
        userDict[user[x]] += " " + text[x] + " . "
    else:
        userDict[user[x]] = text[x] + " . "



productReviews = {"a" : "godt medium super trommer stikker", "b" : "virkelig guitar special godt medium guitar"}
userReviews = {"user1" : "godt medium super trommer stikker", "user2" : "virkelig guitar special godt medium guitar"}



kurtRobairId = "AMNTZU1YQN1TH"
kurtRobairsReviews = ["B00004Y2UT", "B00006LVEU", "B0002E1H9W", "B0002M728Y"
  , "B0002M72JS", "B0006NDF8A", "B000EEHKVY", "B0018TIADQ", "B001FQ74FW", "B003JJQMD8"]

productList = list(productDict.values())
userList = list(userDict.values())
user = userDict[kurtRobairId]


tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([user] + productList)
#print(tfidf_matrix.shape)

recommendedProducts = cosine_similarity(tfidf_matrix[0], tfidf_matrix)[0][1:]

orderedRecommendations = sorted(list(zip(productDict.keys(), recommendedProducts)), key = lambda tup : tup[1], reverse = True)
print(orderedRecommendations)
'''
print(f"MAX SCORE: {max(recommendedProducts)}")
print(f"MIN SCORE: {min(recommendedProducts)}")


for review in kurtRobairsReviews:
  print(review)
  print(zipped[review])
'''