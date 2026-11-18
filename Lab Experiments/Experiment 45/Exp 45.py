import random
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define possible states
states = ["Sunny", "Cloudy", "Rainy"]

# Step 2: Define transition probability matrix
transition_matrix = np.array([
    [0.6, 0.3, 0.1],
    [0.2, 0.5, 0.3],
    [0.1, 0.3, 0.6]
])

# Step 3: Display transition matrix
print("Transition Probability Matrix:")
print(transition_matrix)

# Step 4: Predict next event
def predict_next(current_state):
    index = states.index(current_state)

    next_state = random.choices(
        states,
        weights=transition_matrix[index],
        k=1
    )

    return next_state[0]

# Step 5: Generate event sequence
current_state = "Sunny"
sequence = [current_state]

for i in range(10):
    current_state = predict_next(current_state)
    sequence.append(current_state)

# Step 6: Display predicted sequence
print("\nPredicted Event Sequence:")

for i, event in enumerate(sequence):
    print("Step", i + 1, ":", event)

# Step 7: Calculate event frequency
print("\nEvent Frequencies:")

for state in states:
    count = sequence.count(state)
    print(state, ":", count)

# Step 8: Visualize sequence
colors = {
    "Sunny": "orange",
    "Cloudy": "gray",
    "Rainy": "blue"
}

plt.figure(figsize=(9, 4))

for i, event in enumerate(sequence):
    plt.scatter(
        i, 1,
        color=colors[event],
        s=150,
        label=event if event not in sequence[:i] else ""
    )
    plt.text(i, 1.08, event, ha="center")

plt.title("Markov Chain Event Prediction")
plt.xlabel("Time Steps")
plt.yticks([])
plt.legend()
plt.grid(axis="x")
plt.show()

print("\nMarkov Chain Prediction Completed!")
