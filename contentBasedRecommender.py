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

# id    | term_1 | term_2 | ...
# kurt  | 1.5    | 2.3    | ... <- tf_idf values
# prod1 | 0.7    | 1.3    | ...
# prod2 | 0.3    | 2.1    | ...

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

# We should filtered his 4+ reviews, and only used those.





def pseudo_code():
    # MOVIIES (id, title, length in minutes, genres, budget $, date)
    lotr = (0, "Lord of the Rings: The King Returns", 200, ["fantasy", "drama"], 94000000, "17/12-2003")
    nights = (1, "All these Sleeping Nights", 100, ["documentary", "drama"], 100000, "04/11-2016")

    kasper1 = (_, "Batman Rings Killing Softly", 92, ["crime", "action", "romance"], 40000000, "06/05-1994")
    kasper2 = (_, "Money Wolf Never Sleeps", 101, ["mocumentary", "documentary"], 1000000, "17/01-2019")

    dist_title = "Cosine similarity"
    dist_length = "mse"
    dist_genres = "Jaccard"
    dist_budget = "mse"
    dist_date = "mse"

    dist_weight = [0.3, 0.2, 0.1, 0.2, 0.3]
    def dist(a, b):
        # distances between a and b of course.
        distances = [dist_title(a, b), dist_length(a, b), dist_genres(a, b), dist_budget(a, b), dist_date(a, b)]
        weighted_dist = np.dot(distances, dist_weight)
        return weighted_dist


    def get_recommendations(u, k):
        centroids = cluster_movies_for(u)
        movie_count = len(movies)
        predictions = np.ones(movie_count) * float('inf')
        for c in centroids:
            for i in range(movie_count):
                d = dist(c, movies[i])
                if d < predictions[i]:
                    predictions[i] = d
      return sorted_on_snd(zip(range(movie_count), predictions))[:k]
      
      

