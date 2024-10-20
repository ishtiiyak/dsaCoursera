from sys import stdin

def optimal_value(capacity, weights, values):
    # Calculate the value-to-weight ratio
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(len(values))]
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item[2], reverse=True)
    
    value = 0.
    
    for val, weight, ratio in items:
        if capacity == 0:
            break
        
        # Take as much as possible from the current item
        if weight <= capacity:
            capacity -= weight
            value += val
        else:
            value += val * (capacity / weight)  # Take the fraction of the item
            capacity = 0  # The knapsack is full now
    
    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
