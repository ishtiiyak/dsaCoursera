def build_heap(data):
    """Build a min-heap from ``data`` inplace using sift-down.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []

    # Helper function to sift down the element at index i
    def sift_down(i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(data) and data[left] < data[min_index]:
            min_index = left
        if right < len(data) and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append((i, min_index))
            sift_down(min_index)

    # Build the heap from the last non-leaf node down to the root
    for i in range(len(data) // 2 - 1, -1, -1):
        sift_down(i)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
