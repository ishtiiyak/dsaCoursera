from random import randint

def partition3(array, left, right):
    pivot = array[left]
    m1 = left  # Start of the "equal" section
    m2 = left  # End of the "equal" section

    for i in range(left, right + 1):
        if array[i] < pivot:
            array[m1], array[i] = array[i], array[m1]
            m1 += 1
            m2 += 1
        elif array[i] == pivot:
            array[m2], array[i] = array[i], array[m2]
            m2 += 1

    return m1, m2 - 1

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
