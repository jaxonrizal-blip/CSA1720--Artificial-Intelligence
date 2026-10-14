
from heapq import heappush, heappop

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            target = state[i] - 1
            distance += abs(i // 3 - target // 3)
            distance += abs(i % 3 - target % 3)
    return distance

def solve(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state == goal:
            for step in path + [state]:
                print(step[:3])
                print(step[3:6])
                print(step[6:])
                print()
            print("Puzzle solved!")
            return

        if state in visited:
            continue
        visited.add(state)

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        moves = [(-1, 0), (1, 0),
                 (0, -1), (0, 1)]

        for dr, dc in moves:
            r, c = row + dr, col + dc

            if 0 <= r < 3 and 0 <= c < 3:
                new_pos = r * 3 + c
                new_state = list(state)
                new_state[zero], new_state[new_pos] = (
                    new_state[new_pos], new_state[zero])

                new_state = tuple(new_state)

                if new_state not in visited:
                    heappush(pq, (
                        g + 1 + heuristic(new_state),
                        g + 1,
                        new_state,
                        path + [state]
                    ))

    print("No solution found.")

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solve(start)
