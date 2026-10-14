
from itertools import permutations

n = int(input("Enter number of cities: "))

cost = []
print("Enter cost matrix row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

start = int(input("Enter starting city (0 to n-1): "))

cities = [i for i in range(n) if i != start]
min_cost = float("inf")
best_path = []

for p in permutations(cities):
    path = [start] + list(p) + [start]
    total = 0

    for i in range(n):
        total += cost[path[i]][path[i + 1]]

    if total < min_cost:
        min_cost = total
        best_path = path

print("Minimum cost:", min_cost)
print("Best path:", " -> ".join(map(str, best_path)))
