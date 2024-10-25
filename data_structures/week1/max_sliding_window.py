from collections import deque

def max_sliding_window(sequence, m):
    dq = deque()
    maximums = []

    for i in range(len(sequence)):
        if dq and dq[0] == i - m:
            dq.popleft()

        while dq and sequence[dq[-1]] < sequence[i]:
            dq.pop()

        dq.append(i)

        if i >= m - 1:
            maximums.append(sequence[dq[0]])

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
