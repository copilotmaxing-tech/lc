import numpy as np

def bipolar_activation(value):
   result = np.zeros_like(value)
   result[value > 0] = 1
   result[value < 0] = -1
   return result

def binary_activation(value):
   return (value > 0).astype(int)

def auto_association():
   pattern = np.array([-1, 1, 1, 1])
   weight_matrix = np.outer(pattern, pattern)

   print(weight_matrix)

   input_patterns = [
       [-1, 1, 1, 1],
       [0, 1, 1, 1],
       [-1, 1, 0, 1],
       [-1, -1, 1, 1],
       [0, 0, 1, 1],
       [-1, -1, -1, 1]
   ]

   for item in input_patterns:
       item = np.array(item)
       net_value = item @ weight_matrix
       output = bipolar_activation(net_value)

       print(item, "->", net_value, "->", output)

auto_association()


# [[ 1 -1 -1 -1]
#  [-1  1  1  1]
#  [-1  1  1  1]
#  [-1  1  1  1]]
# [-1  1  1  1] -> [-4  4  4  4] -> [-1  1  1  1]
# [0 1 1 1] -> [-3  3  3  3] -> [-1  1  1  1]
# [-1  1  0  1] -> [-3  3  3  3] -> [-1  1  1  1]
# [-1 -1  1  1] -> [-2  2  2  2] -> [-1  1  1  1]
# [0 0 1 1] -> [-2  2  2  2] -> [-1  1  1  1]
# [-1 -1 -1  1] -> [0 0 0 0] -> [0 0 0 0]