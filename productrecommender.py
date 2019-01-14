import fileLoad as fl

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract the data
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
    
# Combine the review for each product and each user
product_reviews_dict = {}
user_reviews_dict = {}


for x in range(0, len(text)):
    if prod[x] in product_reviews_dict:
        product_reviews_dict[prod[x]] += " " + text[x] + " . "
    else:
        product_reviews_dict[prod[x]] = text[x] + " . "

    if user[x] in user_reviews_dict:
        user_reviews_dict[user[x]] += " " + text[x] + " . "
    else:
        user_reviews_dict[user[x]] = text[x] + " . "

kurt_robair_id = "AMNTZU1YQN1TH"
kurt_robairs_reviews = ["B00004Y2UT", "B00006LVEU", "B0002E1H9W", "B0002M728Y"
  , "B0002M72JS", "B0006NDF8A", "B000EEHKVY", "B0018TIADQ", "B001FQ74FW", "B003JJQMD8"]

product_reviews = list(product_reviews_dict.values())
user_reviews = list(user_reviews_dict.values())

# A combination of text from all Kurt Robairs reviews
kurt_robairs_collected_reviews = user_reviews_dict[kurt_robair_id]

# A Matrix where each row is a vector describing a review in terms of tf_idf
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([kurt_robairs_collected_reviews] + product_reviews)

# The cosine similarity between Kurt Robairs combined reviews and all other products' combined reviews
product_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix)[0][1:]

# Zip score together with product id. Then sort desc on score.
ordered_products_with_scores = sorted(list(zip(product_reviews_dict.keys(), product_scores)), key = lambda tup : tup[1], reverse = True)

# Find products that Kurt Robairs hasn't reviewed
recommended_products = [p for p in ordered_products_with_scores if p[0] not in kurt_robairs_reviews]

# Show top 10 products with scores, recommended for Kurt Robair
for kvp in recommended_products[:10]:
    print(f"Id: {kvp[0]}, Score: {kvp[1]}")


# Kurt's Recommendations: 7 * 5.0, 3 * 3.0
# He only reviews items he like. So we can use his reviews as a basis for finding other items!
# If this wasn't the case, we would need to take other factors into account. For example the scores, useful property etc.