def change(money):
    denominations = [10, 5, 1]  # Common coin denominations
    count = 0

    for coin in denominations:
        count += money // coin  # Count how many coins of this denomination
        money %= coin           # Reduce the remaining amount

    return count

if __name__ == '__main__':
    m = int(input())
    print(change(m))
