import fileLoad as fl

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

print(len(userDict))
print(list(userDict.values())[0])
print(list(productDict.values())[0])