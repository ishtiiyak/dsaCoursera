def optimal_summands(n):
    summands = []
    current_sum = 0
    k = 1
    
    while current_sum + k <= n:
        summands.append(k)
        current_sum += k
        k += 1
    
    # Add the remaining value to the last summand
    if current_sum < n:
        summands[-1] += (n - current_sum)
    
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
