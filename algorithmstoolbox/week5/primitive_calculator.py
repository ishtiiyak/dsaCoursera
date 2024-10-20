def compute_operations(n):
    # Initialize the array to store the minimum number of operations
    operations = [0] * (n + 1)
    # To store the previous number for path reconstruction
    previous = [0] * (n + 1)

    for i in range(2, n + 1):
        # Start with the operation of subtracting 1
        operations[i] = operations[i - 1] + 1
        previous[i] = i - 1

        # If divisible by 2, check if this option is better
        if i % 2 == 0 and operations[i] > operations[i // 2] + 1:
            operations[i] = operations[i // 2] + 1
            previous[i] = i // 2

        # If divisible by 3, check if this option is better
        if i % 3 == 0 and operations[i] > operations[i // 3] + 1:
            operations[i] = operations[i // 3] + 1
            previous[i] = i // 3

    # Reconstruct the sequence of operations
    sequence = []
    while n > 0:
        sequence.append(n)
        n = previous[n]

    return sequence[::-1]  # Return the sequence in correct order

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
