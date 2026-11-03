import random

# Objective function
def fitness(x):
    return x ** 2

# Generate initial population
population = [random.randint(0, 31) for _ in range(6)]

# Genetic Algorithm
for generation in range(20):

    # Selection
    population.sort(key=fitness, reverse=True)
    parents = population[:3]

    # Crossover
    offspring = []
    for i in range(3):
        p1 = random.choice(parents)
        p2 = random.choice(parents)

        child = (p1 + p2) // 2
        offspring.append(child)

    # Mutation
    for i in range(len(offspring)):
        if random.random() < 0.2:
            offspring[i] = random.randint(0, 31)

    # Update population
    population = parents + offspring

# Display result
best = max(population, key=fitness)

print("Best Solution:", best)
print("Maximum Fitness:", fitness(best))
