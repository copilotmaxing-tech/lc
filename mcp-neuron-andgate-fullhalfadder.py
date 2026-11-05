
# Artificial Intelligence and Soft Computing
# 1. AND Gate using McCulloch-Pitts Neuron
# 2. Half Adder
# 3. Full Adder

# -------------------------------
# 1. AND GATE USING MCP NEURON
# -------------------------------

print("\n===== AND GATE USING MCP NEURON =====")

w1 = 1
w2 = 1
threshold = 2

print("Input A | Input B | Output")
print("--------------------------")

for a in [0, 1]:
    for b in [0, 1]:

        net = (a * w1) + (b * w2)

        if net >= threshold:
            output = 1
        else:
            output = 0

        print("   ", a, "  |   ", b, "  |   ", output)


# -------------------------------
# 2. HALF ADDER
# -------------------------------

print("\n===== HALF ADDER =====")

print("Input A | Input B | Sum | Carry")
print("--------------------------------")

for a in [0, 1]:
    for b in [0, 1]:

        sum = a ^ b
        carry = a & b

        print("   ", a, "  |   ", b, "  |  ", sum, "  |   ", carry)


# -------------------------------
# 3. FULL ADDER
# -------------------------------

print("\n===== FULL ADDER =====")

print("Input A | Input B | Cin | Sum | Carry")
print("-------------------------------------")

for a in [0, 1]:
    for b in [0, 1]:
        for cin in [0, 1]:

            sum = a ^ b ^ cin

            carry = (a & b) | (b & cin) | (a & cin)

            print("   ", a, "  |   ", b, "  |  ", cin,
                  "  |  ", sum, "  |   ", carry)

print("\n===== PROGRAM COMPLETED SUCCESSFULLY =====")




# ===== AND GATE USING MCP NEURON =====
# Input A | Input B | Output
# --------------------------
#     0   |    0   |    0
#     0   |    1   |    0
#     1   |    0   |    0
#     1   |    1   |    1

# ===== HALF ADDER =====
# Input A | Input B | Sum | Carry
# --------------------------------
#     0   |    0   |   0   |    0
#     0   |    1   |   1   |    0
#     1   |    0   |   1   |    0
#     1   |    1   |   0   |    1

# ===== FULL ADDER =====
# Input A | Input B | Cin | Sum | Carry
# -------------------------------------
#     0   |    0   |   0   |   0   |    0
#     0   |    0   |   1   |   1   |    0
#     0   |    1   |   0   |   1   |    0
#     0   |    1   |   1   |   0   |    1
#     1   |    0   |   0   |   1   |    0
#     1   |    0   |   1   |   0   |    1
#     1   |    1   |   0   |   0   |    1
#     1   |    1   |   1   |   1   |    1

# ===== PROGRAM COMPLETED SUCCESSFULLY =====