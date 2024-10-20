def optimal_weight(W, weights):
    n = len(weights)
    # Create a 2D list (table) to store the maximum weights
    values = [[0] * (W + 1) for _ in range(n + 1)]

    # Fill the table according to the dynamic programming approach
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if j >= weights[i - 1]:
                values[i][j] = max(weights[i - 1] + values[i - 1][j - weights[i - 1]],
                                   values[i - 1][j])
            else:
                values[i][j] = values[i - 1][j]

    return values[n][W]

if __name__ == '__main__':
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))
    print(optimal_weight(W, weights))
