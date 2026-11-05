import numpy as np

def bipolar_activation(value):
   result = np.zeros_like(value)
   result[value > 0] = 1
   result[value < 0] = -1
   return result

def binary_activation(value):
   return (value > 0).astype(int)


def bam_model():
   first_pattern = np.array(
       [1, 1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1]
   )
   second_pattern = np.array(
       [1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1]
   )

   first_target = np.array([-1, 1])
   second_target = np.array([1, 1])

   weight_matrix = (
       np.outer(first_pattern, first_target)
       + np.outer(second_pattern, second_target)
   )

   print(weight_matrix)

   patterns = [
       (first_pattern, "Pattern 1"),
       (second_pattern, "Pattern 2")
   ]

   for vector, label in patterns:
       net_output = vector @ weight_matrix
       final_output = bipolar_activation(net_output)
       print(label, "->", net_output, "->", final_output)

bam_model()


# [[ 0  2]
#  [ 0  2]
#  [ 0  2]
#  [ 0  2]
#  [ 2  0]
#  [ 2  0]
#  [ 0  2]
#  [-2  0]
#  [-2  0]
#  [ 0  2]
#  [ 0 -2]
#  [ 0 -2]
#  [ 0  2]
#  [-2  0]
#  [-2  0]]
# Pattern 1 -> [-12  18] -> [-1  1]
# Pattern 2 -> [12 18] -> [1 1]