import sys

def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):  # Pisano period cannot be more than m * m
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_mod(n, m):
    n = n % pisano_period(m)  # Reduce n by the Pisano period
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def fibonacci_partial_sum(from_, to):
    sum_to = fibonacci_mod(to + 2, 10) - 1  # S(to)
    sum_from = fibonacci_mod(from_, 10) - 1  # S(from - 1)

    return (sum_to - sum_from) % 10

if __name__ == '__main__':
    input_data = sys.stdin.read()  # Use a different variable name
    from_, to = map(int, input_data.split())
    print(fibonacci_partial_sum(from_, to))
