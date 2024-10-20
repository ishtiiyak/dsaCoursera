def edit_distance(first_string, second_string):
    m = len(first_string)
    n = len(second_string)

    # Create a (m+1) x (n+1) matrix to store results of subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the first column and first row
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from first_string
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters into first_string

    # Fill the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                               dp[i][j - 1] + 1,    # Insertion
                               dp[i - 1][j - 1] + 1)  # Substitution

    return dp[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
