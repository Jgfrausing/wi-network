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
    
