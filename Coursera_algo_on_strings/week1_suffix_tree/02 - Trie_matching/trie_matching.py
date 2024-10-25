# python3
import sys


def build_trie(patterns):
    tree = dict()
    cnt = 0
    tree[0] = dict()
    for pattern in patterns:
        x = 0
        for i in pattern:
            if i in tree[x]:
                x = tree[x][i]
                continue
            else:
                cnt += 1
                tree[cnt] = {}
                tree[x][i] = cnt
                x = cnt
    return tree


def solve(text, n, patterns):
    tree = build_trie(patterns)
    result = []
    for i in range(len(text)):
        x = 0
        j = i
        flag = True
        while j < len(text) and tree[x] != {}:
            try:
                x = tree[x][text[j]]
                j += 1
            except:
                flag = False
                break
        if flag and len(tree[x]) == 0:
            result.append(i)
    return result


text = input().strip()
n = int(input().strip())
patterns = []
for i in range(n):
    patterns.append(input().strip())
ans = solve(text, n, patterns)
print(' '.join(map(str, ans)))
