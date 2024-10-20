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

def fibonacci_sum(n):
    # Sum of the first n Fibonacci numbers is F(n + 2) - 1
    return (fibonacci_mod(n + 2, 10) - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
