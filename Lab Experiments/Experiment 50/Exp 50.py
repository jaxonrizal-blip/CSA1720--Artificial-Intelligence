import numpy as np
import matplotlib.pyplot as plt

# XOR Dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([[0], [1], [1], [0]])

# Neural Network: 2 Input, 4 Hidden, 1 Output
def neural_network(weights, X):
    w1 = weights[:8].reshape(2, 4)
    b1 = weights[8:12].reshape(1, 4)
    w2 = weights[12:16].reshape(4, 1)
    b2 = weights[16]

    hidden = np.tanh(np.dot(X, w1) + b1)
    output = 1 / (1 + np.exp(-np.clip(
        np.dot(hidden, w2) + b2, -500, 500
    )))

    return output

# Fitness Function
def fitness(weights):
    predictions = neural_network(weights, X)
    error = np.mean((y - predictions) ** 2)
    return 1 / (error + 0.001)

# Genetic Algorithm Settings
population_size = 100
generations = 500
mutation_rate = 0.1

# Initialize Population
population = np.random.uniform(-2, 2, (population_size, 17))

best_fitness_history = []

# Genetic Algorithm
for generation in range(generations):

    scores = np.array([fitness(ind) for ind in population])

    best_index = np.argmax(scores)
    best_fitness = scores[best_index]

    best_fitness_history.append(best_fitness)

    # Elitism
    new_population = [population[best_index].copy()]

    # Generate New Population
    while len(new_population) < population_size:

        # Select Parents
        parent1 = population[np.random.randint(population_size)]
        parent2 = population[np.random.randint(population_size)]

        # Crossover
        crossover_point = np.random.randint(1, 17)
        child = np.concatenate((
            parent1[:crossover_point],
            parent2[crossover_point:]
        ))

        # Mutation
        mutation = np.random.randn(17) * mutation_rate
        mask = np.random.rand(17) < 0.2
        child += mutation * mask

        new_population.append(child)

    population = np.array(new_population)

    if (generation + 1) % 50 == 0:
        print("Generation:", generation + 1,
              "Best Fitness:", round(best_fitness, 4))

# Best Neural Network
scores = np.array([fitness(ind) for ind in population])
best_weights = population[np.argmax(scores)]

# Predictions
predictions = neural_network(best_weights, X)

print("\nFinal XOR Results")
print("-----------------")

for i in range(len(X)):
    print(
        X[i], "Expected:", y[i][0],
        "Predicted:", round(predictions[i][0], 3),
        "Output:", int(predictions[i][0] >= 0.5)
    )

# Plot Fitness
plt.plot(best_fitness_history)
plt.title("Genetic Algorithm - Fitness Improvement")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.grid()
plt.show()

print("\nGenetic Algorithm Completed!")
