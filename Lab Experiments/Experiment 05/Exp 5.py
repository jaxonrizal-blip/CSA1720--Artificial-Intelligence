
from collections import deque

def solve(M, C, B):
    start = (M, C, 1)
    goal = (0, 0, 0)
    queue = deque([(start, [])])
    visited = set()

    moves = [(m, c) for m in range(B + 1)
             for c in range(B + 1)
             if 1 <= m + c <= B]

    def valid(m, c):
        return (0 <= m <= M and 0 <= c <= C and
                (m == 0 or m >= c) and
                (M-m == 0 or M-m >= C-c))

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)
        path = path + [state]

        if state == goal:
            print("Solution steps:")
            for s in path:
                print(s)
            return

        m, c, boat = state

        for dm, dc in moves:
            if boat == 1:
                new = (m-dm, c-dc, 0)
            else:
                new = (m+dm, c+dc, 1)

            if valid(new[0], new[1]):
                queue.append((new, path))

    print("No solution exists")

M = int(input("Enter number of missionaries: "))
C = int(input("Enter number of cannibals: "))
B = int(input("Enter boat capacity: "))

solve(M, C, B)
