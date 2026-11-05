import numpy as np

def execute_sofm_updates():
   
    weights_base = np.array(
        [[0.3, 0.2, 0.1, 0.8, 0.4], [0.5, 0.6, 0.7, 0.9, 0.2]]
    )

    scenarios = [
        (np.array([0.2, 0.4]), 0.2, "Phase A"),
        (np.array([0.6, 0.6]), 0.1, "Phase B"),
    ]

    for sample, l_rate, phase_name in scenarios:
        current_weights = weights_base.copy()

        sq_distances = np.sum((current_weights - sample[:, None]) ** 2, axis=0)
        best_node_idx = np.argmin(sq_distances)

        current_weights[:, best_node_idx] += l_rate * (
            sample - current_weights[:, best_node_idx]
        )

        print(f"=== {phase_name} ===")
        print(f"Input: {sample} | Learning Rate: {l_rate}")
        print(f"Node Distances: {np.round(sq_distances, 4)}")
        print(f"Winning Node: Unit {best_node_idx + 1}")
        print(f"New Weights:\n{np.round(current_weights, 4)}\n")

execute_sofm_updates()


# === Phase A ===
# Input: [0.2 0.4] | Learning Rate: 0.2
# Node Distances: [0.02 0.04 0.1  0.61 0.08]
# Winning Node: Unit 1
# New Weights:
# [[0.28 0.2  0.1  0.8  0.4 ]
#  [0.48 0.6  0.7  0.9  0.2 ]]

# === Phase B ===
# Input: [0.6 0.6] | Learning Rate: 0.1
# Node Distances: [0.1  0.16 0.26 0.13 0.2 ]
# Winning Node: Unit 1
# New Weights:
# [[0.33 0.2  0.1  0.8  0.4 ]
#  [0.51 0.6  0.7  0.9  0.2 ]]
