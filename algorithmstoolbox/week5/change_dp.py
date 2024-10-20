def change(money):
    # Denominations available
    denominations = [4, 3, 1]
    
    # Initialize the number of coins
    num_coins = 0
    
    # Iterate through each denomination
    for coin in denominations:
        if money == 0:
            break
        num_coins += money // coin  # Use as many coins of this denomination as possible
        money %= coin  # Reduce the money by the amount used

    return num_coins

if __name__ == '__main__':
    m = int(input())
    print(change(m))
