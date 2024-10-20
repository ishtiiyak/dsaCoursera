def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous, current = 0, 1

    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10

    return current


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
