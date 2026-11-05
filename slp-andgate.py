def train_and_gate(X1, X2, target, learning_rate=1):
    # Initial weights and bias
    W1 = 0
    W2 = 0
    B = 0

    epoch = 0

    while True:
        epoch += 1
        changed = False

        print("\nEpoch:", epoch)
        print("X1\tX2\tT\tYin\tY\tW1\tW2\tB")

        for i in range(len(X1)):
            x1 = X1[i]
            x2 = X2[i]
            t = target[i]

            # Calculate net input
            Yin = B + W1 * x1 + W2 * x2

            # Activation function
            if Yin > 0:
                Y = 1
            elif Yin < 0:
                Y = -1
            else:
                Y = 0

            # Update weights only if output != target
            if Y != t:
                W1 = W1 + learning_rate * t * x1
                W2 = W2 + learning_rate * t * x2
                B = B + learning_rate * t

                changed = True

            print(f"{x1}\t{x2}\t{t}\t{Yin}\t{Y}\t{W1}\t{W2}\t{B}")

        # Stop when no weight changes occur
        if changed == False:
            break

    print("\nFinal Weights:")
    print("W1 =", W1)
    print("W2 =", W2)
    print("Bias =", B)

    return W1, W2, B


# AND Gate input
X1 = [1, 1, -1, -1]
X2 = [1, -1, 1, -1]

# AND Gate target output
target = [1, -1, -1, -1]

# Train perceptron
train_and_gate(X1, X2, target)








# Epoch: 1
# X1      X2      T       Yin     Y       W1      W2      B
# 1       1       1       0       0       1       1       1
# 1       -1      -1      1       1       0       2       0
# -1      1       -1      2       1       1       1       -1
# -1      -1      -1      -3      -1      1       1       -1

# Epoch: 2
# X1      X2      T       Yin     Y       W1      W2      B
# 1       1       1       1       1       1       1       -1
# 1       -1      -1      -1      -1      1       1       -1
# -1      1       -1      -1      -1      1       1       -1
# -1      -1      -1      -3      -1      1       1       -1

# Final Weights:
# W1 = 1
# W2 = 1
# Bias = -1