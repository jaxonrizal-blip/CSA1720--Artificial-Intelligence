
colors = input("Enter colors separated by space: ").split()
n = int(input("Enter number of regions: "))

graph = {}

for i in range(n):
    region = input("Enter region name: ")
    neighbors = input(
        "Enter neighboring regions separated by space: "
    ).split()
    graph[region] = neighbors

coloring = {}

def solve(regions, index):
    if index == len(regions):
        return True

    region = regions[index]

    for color in colors:
        safe = True

        for neighbor in graph[region]:
            if coloring.get(neighbor) == color:
                safe = False
                break

        if safe:
            coloring[region] = color

            if solve(regions, index + 1):
                return True

            del coloring[region]

    return False

regions = list(graph.keys())

if solve(regions, 0):
    print("\nMap Coloring Solution:")
    for region in regions:
        print(region, ":", coloring[region])
else:
    print("No solution exists")
