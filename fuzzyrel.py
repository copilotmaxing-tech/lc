import numpy as np


values = [2, 4, 6, 8, 10]


set_A = np.array([1, 0.65, 0.5, 0.35, 0])
set_B = np.array([0, 0.35, 0.5, 0.65, 1])


def complement(arr):
   return 1 - arr


operations = [
   ("(a) A union B", np.maximum(set_A, set_B)),
   ("(b) A intersection B", np.minimum(set_A, set_B)),
   ("(c) A'", complement(set_A)),
   ("(d) B'", complement(set_B)),
   ("(e) A' intersection B'",
    np.minimum(complement(set_A), complement(set_B))),
   ("(f) A' union B'",
    np.maximum(complement(set_A), complement(set_B))),
   ("(g) (A union B)'",
    complement(np.maximum(set_A, set_B))),
   ("(h) (A intersection B)'",
    complement(np.minimum(set_A, set_B))),
   ("(i) A union A'",
    np.maximum(set_A, complement(set_A))),
   ("(j) A intersection A'",
    np.minimum(set_A, complement(set_A))),
   ("(k) B union B'",
    np.maximum(set_B, complement(set_B))),
   ("(l) B intersection B'",
    np.minimum(set_B, complement(set_B)))
]


print("x =", values)


for label, answer in operations:
   print(f"{label:22}", np.round(answer, 2).tolist())





universe = [0, 1, 2, 5, 7, 9, 10]

S_set = np.array([1.0, 1.0, 0.8, 0.2, 0.1, 0.0, 0.0])
C_set = np.array([0.0, 0.0, 0.0, 0.5, 0.7, 0.8, 1.0])

algebraic_sum = S_set + C_set - (S_set * C_set)
algebraic_product = S_set * C_set

bounded_sum = np.minimum(1, S_set + C_set)
bounded_difference = np.maximum(0, S_set + C_set - 1)

output = [
   ("Algebraic Sum", algebraic_sum),
   ("Algebraic Product", algebraic_product),
   ("Bounded Sum", bounded_sum),
   ("Bounded Difference", bounded_difference)
]

print("x        ", universe)

for operation, result in output:
   print(f"{operation:20}", np.round(result, 2).tolist())






# Q2: Cartesian product using minimum
set_A = np.array([0.5, 0.2, 0.9])
set_B = np.array([1.0, 0.5, 1.0])


relation = np.minimum.outer(set_A, set_B)


print("Q2 R =\n", relation)







# Q3: Max-min and max-product composition
first_relation = np.array([
   [0.1, 0.2, 0.3],
   [0.4, 0.5, 0.6]
])

second_relation = np.array([
   [0.8, 0.1],
   [0.6, 0.9],
   [0.4, 1.0]
])

# Expand dimensions so corresponding elements can be compared
min_values = np.minimum(
   first_relation[:, :, np.newaxis],
   second_relation[np.newaxis, :, :]
)

max_min_result = np.max(min_values, axis=1)

# Max-product composition
product_values = (
   first_relation[:, :, np.newaxis] *
   second_relation[np.newaxis, :, :]
)

max_product_result = np.max(product_values, axis=1)

print("Q3 T (max-min) =\n", max_min_result)
print("Q3 T (max-product) =\n", np.round(max_product_result, 2))

