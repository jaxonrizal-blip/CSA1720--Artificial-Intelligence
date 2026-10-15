
def minimax(depth, node, maximizing, values):
    if depth == 2:
        return values[node]

    if maximizing:
        best = float("-inf")
        for i in range(2):
            value = minimax(depth + 1, node * 2 + i,
                            False, values)
            best = max(best, value)
        return best

    else:
        best = float("inf")
        for i in range(2):
            value = minimax(depth + 1, node * 2 + i,
                            True, values)
            best = min(best, value)
        return best

values = list(map(int, input(
    "Enter 4 leaf node values: ").split()))

if len(values) == 4:
    result = minimax(0, 0, True, values)
    print("Optimal value:", result)
else:
    print("Please enter exactly 4 values")
