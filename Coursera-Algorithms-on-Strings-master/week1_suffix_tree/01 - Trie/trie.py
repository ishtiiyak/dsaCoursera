# Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


def build_trie(patterns):
    tree = dict()
    # write your code here
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


if __name__ == '__main__':
    n = int(input())
    patterns = []
    for i in range(n):
        patterns.append(input())
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
