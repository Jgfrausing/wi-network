import fileLoad
import sentimentClassifier as sc

word_class_matrix      = fileLoad.read_matrix("s_small_matrix")
naive_class_probablity = fileLoad.read_dict("s_naive_class_probability")
word_index             = fileLoad.read_dict("s_word_index")
distinct_words         = fileLoad.read_dict("s_distinct_words")
class_index            = fileLoad.read_dict("s_class_index")

probabilities = sc.word_probabilities(naive_class_probablity, distinct_words, word_class_matrix, "expensive trick questionable stopped", class_index, word_index)
prob_per_class = zip(class_index.keys(), probabilities)


for pair in sorted(prob_per_class, key=lambda x: x[1], reverse=True):
  print(pair)

