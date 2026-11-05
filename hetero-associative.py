import numpy as np

def bipolar_activation(value):
   result = np.zeros_like(value)
   result[value > 0] = 1
   result[value < 0] = -1
   return result

def binary_activation(value):
   return (value > 0).astype(int)


def hetero_association():
   source = np.array([
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 0, 0, 1],
       [0, 0, 1, 1]
   ])

   target = np.array([
       [0, 1],
       [0, 1],
       [1, 0],
       [1, 0]
   ])

   weights = np.zeros((4, 2))

   for source_vec, target_vec in zip(source, target):
       weights = weights + np.outer(source_vec, target_vec)

   print(weights)

   for vector in source:
       net = vector @ weights
       result = binary_activation(net)
       print(vector, "->", net, "->", result)

hetero_association()


# [[0. 2.]
#  [0. 1.]
#  [1. 0.]
#  [2. 0.]]
# [1 0 0 0] -> [0. 2.] -> [0 1]
# [1 1 0 0] -> [0. 3.] -> [0 1]
# [0 0 0 1] -> [2. 0.] -> [1 0]
# [0 0 1 1] -> [3. 0.] -> [1 0]