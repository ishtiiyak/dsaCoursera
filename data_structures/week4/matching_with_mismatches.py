# python3

import sys

def solve(k, text, pattern):
    p_len = len(pattern)
    occurrences = []
    for i in range(len(text) - p_len + 1):
        mismatches = sum(1 for a, b in zip(text[i:i + p_len], pattern) if a != b)
        if mismatches <= k:
            occurrences.append(i)
    return occurrences

for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    print(len(ans), *ans)
