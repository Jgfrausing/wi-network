import fileLoad
import sentimentClassifier as sc

word_class_matrix      = fileLoad.read_matrix("small_matrix")
naive_class_probablity = fileLoad.read_dict("naive_class_probability")
word_index             = fileLoad.read_dict("word_index")
distinct_words         = fileLoad.read_dict("distinct_words")
class_index            = fileLoad.read_dict("class_index")

probability = sc.word_probabilities(naive_class_probablity, distinct_words, word_class_matrix, "I not hate it", class_index, word_index)
print(list(class_index.keys()))
print(probability)
