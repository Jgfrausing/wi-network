import re

words = ['like', 'hate', 'smells', 'not', 'I', 'this', 'product', 'do', 'it', 'because'] 

classes = [True, False]

reviews = [ ("I like this product", True)
                    , ("I hate this product", False)
                    , ("this product smells", False)
                    , ("this product do it because it smells", True)
                    , ("I do not like it", False)
                    , ("I like it", True)
                    , ("I like it because it smells", True)
                    , ("this product smells like this", False)
                    , ("hate hate hate this product", False)
                    , ("like smells this product", False)
                    , ("I do this product because it smells", True)
                    , ("I do like hate this product", False)
                    , ("hate it because I like this product", False)
                    , ("I do not like this product", False)
                    , ("I do not like smells", False)
                    , ("hate it", False)
                    , ("I like like like this product", True)
                    , ("I like this product like it", True)
                    , ("hate it smells", False)
                    , ("I do it", True) ]

def probability_per_class(classes, reviews):
  class_counts = {}
  review_count = len(reviews)
  for c in classes:
    counts = sum([element == c for element in reviews])
    class_counts[c] = counts / review_count
  return class_counts

def probability_of_words_class(classes, reviews, words):
    count = {}
    word_count = len(words)
    for c in classes:
        for r in [x[1] == c for x in reviews]:
            counts = 0
            for w in words:
                counts += sum([x == w for x in r[0].split()])
            ## TODO: this does not work - should return dict<class, distinct words>
            
            
ps = probability_per_class(classes, reviews)
pw = probability_per_class(classes, words)
print(ps)
print(pw)
  
def word_probabilities(classes, words, reviews):
  word_probabilities = {}
  ps = probability_per_class(classes, reviews)
  pw = probability_per_class(classes, words)
  for c in classes:
    for w in words:
      for tup in reviews:
        count = sum([x == w for x in tup[0].split()])