
from collections import deque

def water_jug(a, b, target):
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            print("Solution steps:")
            for state in path:
                print(state)
            return

        states = [
            (a, y), (x, b), (0, y), (x, 0),
            (x - min(x, b-y), y + min(x, b-y)),
            (x + min(y, a-x), y - min(y, a-x))
        ]

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("Target cannot be reached")

a = int(input("Enter capacity of Jug 1: "))
b = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

if target < 0 or target > max(a, b):
    print("Invalid target amount")
else:
    water_jug(a, b, target)
