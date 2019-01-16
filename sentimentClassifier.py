import re
import numpy as np
import io
import fileLoad
# Matching
pattern = "[.,!?:;]"
negation_terms = set(("never no nothing nowhere noone none not havent hasnt hadnt cant couldnt shouldnt wont wouldnt dont doesnt didnt isnt arent aint"
                 + "haven't hasn't hadn't can't couldn't shouldn't won't wouldn't don't doesn't didn't isn't aren't ain't").split())

def fix_review(reviews):
  fixed_reviews = []
  for r in reviews:
    new_words = fix_words(r[0])
    fixed_reviews.append((new_words, r[1]))
  return fixed_reviews

def fix_words(text):
  text_formated = replaced = re.sub(pattern, " . ", text)
  words = text_formated.lower().split()
  new_words = []
  negate = False
  for x in range(0, len(words)):
    w = words[x]
    if is_end_of_sentence(w):
      negate = False
      continue
    elif is_negate(w):
      negate = True
    elif negate:
      w = negate_word(w)
    new_words.append(w)
  return new_words

def negate_word(w):
  return w + "_NEG"

def is_end_of_sentence(w):
  return w == "."

def is_negate(w):
  return w in negation_terms

## p(c) = N(c)/N
def probability_per_class(classes, reviews):
  
  class_probability = {}
  class_count = len(classes)
  review_count = len(reviews)
  for c in classes:
    counts = sum([element == c for element in reviews])
    class_probability[c] = (counts + 1) / (review_count + class_count)
  return class_probability


## w(c)
def distinct_words_per_class(classes, reviews, words):
  distinct_count = {}
  for c in classes:
    for w in words:
      for tup in reviews:
        relevant_reviews = [tup[0] for tup in reviews if tup[1] == c]
        nested_words = [review for review in relevant_reviews]
        distinct_word_count = len(set([item for sublist in nested_words for item in sublist]))

        distinct_count[c] = distinct_word_count
  return distinct_count

## N(xi, c)
def word_count_per_class(classes, reviews, words, classIndex, wordIndex):
  result = np.zeros((len(words), len(classes)))

  for w in words:
    wi = wordIndex[w]
    for r in reviews:
      ci = classIndex[r[1]]
      word_occurences_in_review = sum([1 for x in r[0] if x == w])
      result[wi][ci] += word_occurences_in_review

  return result
        
def createIndexes(lst):
  index = {}
  lst = list(lst)
  for x in range(0, len(lst)):
    index[lst[x]] = x
  return index


def classify(naive_class_probabilities, distinct_words, word_class_matrix, test_review, classIndex, wordIndex):
  test_review_ = fix_words(test_review)
  
  p_per_class = np.ones((len(classIndex)))
  word_counts = len(wordIndex)
  for w in test_review_:
    wi = int(wordIndex[w])
    for c in classIndex:
      ci = int(classIndex[c])
      word_chance_for_class = (int(word_class_matrix[wi][ci]) + 1) / (int(distinct_words[c]) + word_counts)
      p_per_class[ci] *= word_chance_for_class

  naive_class_probabilities_vector = [float(x) for x in naive_class_probabilities.values()]
  return convert_to_percentage(p_per_class * naive_class_probabilities_vector)

def convert_to_percentage(vector):
  v_sum = sum(vector)
  for x in range(0, len(vector)):
    vector[x] /= v_sum
  
  return vector
