def eval(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        raise ValueError("Invalid operator")

def get_maximum_value(exp):
    n = (len(exp) + 1) // 2
    solution = [[(0, 0)] * n for _ in range(n)]

    # Function to access digits and operators
    def digits(i):
        return int(exp[2 * i])

    def op(i):
        return exp[2 * i + 1]

    # Initialize the solution for single digits
    for i in range(n):
        solution[i][i] = (digits(i), digits(i))

    # Calculate minimum and maximum values for all subexpressions
    for length in range(1, n):  # length of the current subexpression
        for i in range(n - length):
            j = i + length
            temp_min = float('inf')
            temp_max = float('-inf')

            # Iterate through all possible partitions of the subexpression
            for k in range(i, j):
                a = eval(solution[i][k][0], solution[k + 1][j][0], op(k))
                b = eval(solution[i][k][1], solution[k + 1][j][1], op(k))
                c = eval(solution[i][k][0], solution[k + 1][j][1], op(k))
                d = eval(solution[i][k][1], solution[k + 1][j][0], op(k))

                temp_min = min(temp_min, min(a, b, c, d))
                temp_max = max(temp_max, max(a, b, c, d))

            solution[i][j] = (temp_min, temp_max)

    return solution[0][n - 1][1]

if __name__ == '__main__':
    s = input().strip()
    print(get_maximum_value(s))
