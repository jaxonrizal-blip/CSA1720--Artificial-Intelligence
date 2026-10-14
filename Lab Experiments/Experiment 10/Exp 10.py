
import heapq

graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    graph[node] = {}
    edges = input("Enter neighbors and costs (B:2 C:3): ").split()

    for edge in edges:
        neighbor, cost = edge.split(":")
        graph[node][neighbor] = int(cost)

heuristic = {}
for node in graph:
    heuristic[node] = int(input("Enter heuristic for " + node + ": "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

pq = [(heuristic[start], 0, start, [start])]
best_cost = {start: 0}

while pq:
    f, g, node, path = heapq.heappop(pq)

    if g != best_cost.get(node):
        continue

    if node == goal:
        print("Shortest path:", " -> ".join(path))
        print("Total cost:", g)
        break

    for neighbor, cost in graph[node].items():
        new_g = g + cost

        if new_g < best_cost.get(neighbor, float("inf")):
            best_cost[neighbor] = new_g
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(
                pq, (new_f, new_g, neighbor, path + [neighbor])
            )
else:
    print("No path found")
