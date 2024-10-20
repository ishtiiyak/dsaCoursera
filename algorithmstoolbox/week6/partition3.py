def optimal_weight(W, weights):
    n = len(weights)
    # Create a 2D list to store the maximum weights
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

def partition3(A):
    total_sum = sum(A)
    
    # Check conditions for partitioning into three subsets
    if total_sum % 3 != 0 or len(A) < 3 or max(A) > total_sum // 3:
        return False

    target = total_sum // 3
    
    # Sort weights in descending order to optimize the search
    A.sort(reverse=True)

    # Create a list to store the current weights of the three partitions
    partitions = [0] * 3

    # Check if we can fill three partitions with the target sum
    part1 = optimal_weight(target, A) == target
    part2 = optimal_weight(target, A) == target
    
    return part1 and part2

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    print(1 if partition3(A) else 0)
