import sentimentClassifier as sc
import fileLoad as fl

words = ['like', 'hate', 'smells', 'not', 'I', 'this', 'product', 'do', 'it', 'because']
words = [w.lower() for w in words]
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
          , ("I do it", True)           
          , ("I not hate it", True) 
          ]

words = words + [sc.negate_word(x) for x in words]

words, classes, reviews = fl.getWordsClassesAndReviewsFromFile("material/SmallSentimentTrainingData.txt")
print("Loaded file")

words.union(set([sc.negate_word(x) for x in words]))
print("Unioned words")

reviews_ = sc.fix_review(reviews)
print("Fixed Reviews")

wordIndex = sc.createIndexes(words)
print("Created word index")

classIndex = sc.createIndexes(classes)
print("Created class index")

naive_class_probablity = sc.probability_per_class(classes, reviews_)
print("Computed naive class probabilities")

distinct_words = sc.distinct_words_per_class(classes, reviews_, words)
print("Computed distinct words")

word_class_matrix = sc.word_count_per_class(classes, reviews_, words, classIndex, wordIndex)
print("Computed word_class matrix")

fl.save_matrix(word_class_matrix, "s_small_matrix")
fl.save_dict(distinct_words, "s_distinct_words")
fl.save_dict(naive_class_probablity, "s_naive_class_probability")
fl.save_dict(wordIndex, "s_word_index")
fl.save_dict(classIndex, "s_class_index")

print("Saved all results")