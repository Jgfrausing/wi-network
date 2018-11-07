import re
import numpy as np
import io
import fileLoad

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

def distinct_words_per_class(classes, reviews):
  # this has been thoroughly tested. Trust me, I'm an engineer
  count = {}
  for c in classes:
    for w in words:
      for tup in reviews:
        count = sum([x == w for x in tup[0].split()])
        relevant_reviews = [tup[0] for tup in reviews if tup[1] == c]
        nested_words = [review.split() for review in relevant_reviews]
        distinct_word_count = len(set([item for sublist in nested_words for item in sublist]))
        count[c] = distinct_word_count
  return count

def word_count_per_class(classes, review, words, classIndex, wordIndex):
  # this has also been thorougly tested. Like really really much.
  result = np.zeros((len(words), len(classes)))

  for w in words:
    wi = wordIndex[w]
    for r in reviews:
      ci = classIndex[r[1]]
      word_occurences_in_review = sum([1 for x in r[0].split() if x == w])
      result[wi][ci] += word_occurences_in_review

  return result
        
def createIndexes(lst):
  index = {}
  for x in range(0, len(lst)):
    index[lst[x]] = x
  return index


def word_probabilities(naive_class_probablity, distinct_words, word_class_matrix, test_review, classIndex, wordIndex):
  naive_class_probablity = probability_per_class(classes, reviews)
  distinct_words = distinct_words_per_class(classes, reviews)
  word_class_matrix = word_count_per_class(classes, reviews, words, classIndex, wordIndex)

  p_per_class = np.ones((len(classes)))

  for w in test_review.split():
    wi = wordIndex[w]
    for c in classes:
      ci = classIndex[c]
      word_chance_for_class = word_class_matrix[wi][ci] / distinct_words[c]
      p_per_class[ci] *= word_chance_for_class
  return p_per_class
