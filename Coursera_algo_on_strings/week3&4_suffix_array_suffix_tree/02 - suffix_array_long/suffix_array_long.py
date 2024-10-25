# python3
import sys


def compute_classes(classes, order, L):
    newClasses = [None] * len(order)
    newClasses[order[0]] = 0

    for i in range(1, len(order)):
        cur = order[i]
        prev = order[i-1]

        mid = (cur + L) % len(order)
        midPrev = (prev + L) % len(order)

        if (classes[cur] != classes[prev]) or (classes[mid] != classes[midPrev]):
            newClasses[cur] = newClasses[prev] + 1
        else:
            newClasses[cur] = newClasses[prev]

    return newClasses


def compute_order(text, classes, order, L):
    counter = [0] * len(text)
    new_order = [0] * len(text)

    for c in classes:
        counter[c] += 1

    for i in range(1, len(text)):
        counter[i] += counter[i-1]

    for i in range(len(text)-1, -1, -1):
        start = (order[i] - L + len(text)) % len(text)
        cl = classes[start]

        counter[cl] -= 1
        new_order[counter[cl]] = start

    return new_order


def precompute_classes(text, order):
    classes = [None] * len(text)
    classes[order[0]] = 0

    for i in range(1, len(order)):
        classes[order[i]] = classes[order[i-1]]

        if text[order[i]] != text[order[i-1]]:
            classes[order[i]] += 1

    return classes


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    order = sorted(range(len(text)), key=lambda x: text[x])
    classes = precompute_classes(text, order)
    L = 1

    while L < len(text):
        order = compute_order(text, classes, order, L)
        classes = compute_classes(classes, order, L)
        L *= 2

    return order


if __name__ == '__main__':
    text = input  ().strip()
    print(" ".join(map(str, build_suffix_array(text))))
