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

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    # Using the property: S(n) = F(n) * F(n + 1)
    fn = fibonacci_mod(n, 10)
    fn_plus_1 = fibonacci_mod(n + 1, 10)
    
    return (fn * fn_plus_1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
