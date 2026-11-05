import numpy as np

def train_lvq_network():
   prototypes = np.array(
       [[0.0, 0.0, 1.0, 1.0], [1.0, 0.0, 0.0, 0.0]], dtype=float
   )

   class_labels = np.array([1, 2])
   learning_rate = 0.1

   dataset = [
       (np.array([0, 0, 0, 1]), 2),
       (np.array([1, 1, 0, 0]), 1),
       (np.array([0, 1, 1, 0]), 1),
   ]

   for epoch, (sample, true_label) in enumerate(dataset, start=1):
     
       dist_scores = np.linalg.norm(prototypes - sample, axis=1) ** 2
       bmu_idx = np.argmin(dist_scores)
       predicted_label = class_labels[bmu_idx]

       if predicted_label == true_label:
           prototypes[bmu_idx] += learning_rate * (sample - prototypes[bmu_idx])
       else:
           prototypes[bmu_idx] -= learning_rate * (sample - prototypes[bmu_idx])

       print(f"=== Iteration {epoch}: Input {sample} (Target: {true_label}) ===")
       print(f"Euclidean Distances: Class 1 = {dist_scores[0]:.2f}, Class 2 = {dist_scores[1]:.2f}")
       print(f"BMU Index: Unit {bmu_idx + 1} (Assigned Class {predicted_label})")
       print(f"Updated Weight Matrix:\n{np.round(prototypes.T, 4)}\n")

train_lvq_network()




# === Iteration 1: Input [0 0 0 1] (Target: 2) ===
# Euclidean Distances: Class 1 = 1.00, Class 2 = 2.00
# BMU Index: Unit 1 (Assigned Class 1)
# Updated Weight Matrix:
# [[0.  1. ]
#  [0.  0. ]
#  [1.1 0. ]
#  [1.  0. ]]

# === Iteration 2: Input [1 1 0 0] (Target: 1) ===
# Euclidean Distances: Class 1 = 4.21, Class 2 = 1.00
# BMU Index: Unit 2 (Assigned Class 2)
# Updated Weight Matrix:
# [[ 0.   1. ]
#  [ 0.  -0.1]
#  [ 1.1  0. ]
#  [ 1.   0. ]]

# === Iteration 3: Input [0 1 1 0] (Target: 1) ===
# Euclidean Distances: Class 1 = 2.01, Class 2 = 3.21
# BMU Index: Unit 1 (Assigned Class 1)
# Updated Weight Matrix:
# [[ 0.    1.  ]
#  [ 0.1  -0.1 ]
#  [ 1.09  0.  ]
#  [ 0.9   0.  ]]

