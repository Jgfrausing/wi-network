import fileLoad
import sentimentClassifier as sc

word_class_matrix      = fileLoad.read_matrix("s_small_matrix")
naive_class_probablity = fileLoad.read_dict("s_naive_class_probability")
word_index             = fileLoad.read_dict("s_word_index")
distinct_words         = fileLoad.read_dict("s_distinct_words")
class_index            = fileLoad.read_dict("s_class_index")

probabilities = sc.classify(naive_class_probablity, distinct_words, word_class_matrix, "Terrible product. Shipping time is unreasonably long.", class_index, word_index)
prob_per_class = zip(class_index.keys(), probabilities)


for pair in sorted(prob_per_class, key=lambda x: x[1], reverse=True):
  print(pair)

# "Totally Wonderful. Very good taste."
# ('5.0', 0.9399688880120401)
# ('3.0', 0.04318694208701625)
# ('2.0', 0.008489229658219985)
# ('1.0', 0.005998535026547652)
# ('4.0', 0.0023564052161758595)

# "Terrible product. Shipping time is unreasonably long."
# ('1.0', 0.7377709191932813)
# ('5.0', 0.25590482817027105)
# ('4.0', 0.004009985962029687)
# ('3.0', 0.00172211812085812)
# ('2.0', 0.000592148553559721)