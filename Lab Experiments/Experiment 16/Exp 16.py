import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# User input
x1 = float(input("Enter first input (0 or 1): "))
x2 = float(input("Enter second input (0 or 1): "))

# Weights and bias for AND gate
w1 = 10
w2 = 10
bias = -15

# Feed forward calculation
net = (x1 * w1) + (x2 * w2) + bias
output = sigmoid(net)

# Display result
print("Network Output:", round(output, 4))

if output >= 0.5:
    print("Predicted Output: 1")
else:
    print("Predicted Output: 0")
