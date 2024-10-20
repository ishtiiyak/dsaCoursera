def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):  # Pisano period cannot be more than m * m
        previous, current = current, (previous + current) % m
        # The period starts with 0, 1
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_huge(n, m):
    n = n % pisano_period(m)  # Reduce n by the Pisano period
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
