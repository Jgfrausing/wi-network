import numpy as np
import statistics as stats
import math
from scipy.sparse import csc_matrix
import random

ratings = [ [5, 3, 4, 4, 0]
          , [3, 1, 2, 3, 3]
          , [4, 3, 4, 3, 5]
          , [3, 3, 1, 5, 4]
          , [1, 5, 5, 2, 1]]

ratings_ = np.transpose(ratings)

# m = matrix       a, b = indexes into the matrix
def pearson_similarity(m, a, b):
  item_count = len(m[0])

  # Indexes of items that both a and b has rated
  P = [i for (i, ra, rb) in zip(range(item_count), m[a], m[b]) if ra != 0 and rb != 0]
  
  r_a_avg = average_rating(m, a)
  r_b_avg = average_rating(m, b)
  
  numerator = 0
  denominator_a = 0
  denominator_b = 0

  for pi in P:
    r_a_p = m[a][pi]
    r_b_p = m[b][pi]

    numerator += (r_a_p - r_a_avg) * (r_b_p - r_b_avg)
    denominator_a += (r_a_p - r_a_avg) ** 2
    denominator_b += (r_b_p - r_b_avg) ** 2
  
  return numerator / (math.sqrt(denominator_a) * math.sqrt(denominator_b))

def average_rating(m, a):
  return stats.mean([ra for ra in m[a] if ra != 0])

# m = matrix    a = row (user)  p = col (item)
def user_kNN_predict(m, a, p):
  user_count = len(m)
  
  r_a_avg = average_rating(m, a)

  # :: [(index, similarity)]
  a_sim_to_others = [(b, pearson_similarity(m, a, b)) for b in range(user_count)]
  a_neighbours = [(index, sim) for (index, sim) in a_sim_to_others if index != a and sim > 0]

  # :: double
  summed_sim_to_neighbours = sum([sim for (_, sim) in a_neighbours])

  prediction = 0

  for (b, sim) in a_neighbours:

     weight = sim / summed_sim_to_neighbours
     r_b_avg = average_rating(m, b)
     r_b_p = m[b][p]

     prediction += weight *  (r_b_p - r_b_avg)
  
  # Add a's average into the prediction
  prediction += r_a_avg

  return prediction


def calc_mse_user_kNN(m, a, test_indexes):
  squared_error = 0
  for i in test_indexes:

    actual_value = m[a][i]
    predicted_value = user_kNN_predict(m, a, i)

    squared_error += (predicted_value - actual_value) ** 2

  return squared_error / len(test_indexes)

def run_user_kNN():
  print("User-based kNN")
  print(f" * MSE for kNN user_based: {calc_mse_user_kNN(ratings, 0, range(3))}")
  print(f" * Prediction for item5: {user_kNN_predict(ratings, 0, 4)}")



#########################################################


def to_sparse_array(m):
  (rows, cols) = np.shape(m)

  sparse_array = []

  for r in range(rows):
    for c in range(cols):
      val = m[r][c]
      if val != 0:
        sparse_array.append((r, c, val))
  return sparse_array


# m = matrix     k = latent factors    lr = learning rate
def funk_SVD_predict(m, k, lr, iterations):
  (rows, cols) = np.shape(m)
  A = np.random.rand(rows, k)
  B = np.random.rand(k, cols)
  
  # Here we could remove obvious structure: avg
  
  # :: [(row, col, val)]
  sparse_array = to_sparse_array(m)
  sparse_array_len = len(sparse_array)

  for i in range(iterations):
    print(f"Iteration: {i}")

    (row, col, actual_val) = sparse_array[random.randint(0, sparse_array_len - 1)]
    predicted_val = np.dot(A[row], B[:,col])

    error = actual_val - predicted_val

    A[row] = A[row] + (lr * error * B[:,col])
    B[:,col] = B[:,col] + (lr * error * A[row])


  # We would re-add the obvious structure again
  R = np.matmul(A, B)

  return (A, B, R)


#run_user_kNN()

(A, B, result) = funk_SVD_predict(ratings, 2, 0.01, 10000)

print(result)