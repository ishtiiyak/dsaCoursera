# # python3
# import sys

# NA = -1

# class Node:
# 	def __init__ (self):
# 		self.next = [NA] * 4
# 		self.patternEnd = False

# def solve (text, n, patterns):
# 	result = []

# 	// write your code here

# 	return result

# text = sys.stdin.readline ().strip ()
# n = int (sys.stdin.readline ().strip ())
# patterns = []
# for i in range (n):
# 	patterns += [sys.stdin.readline ().strip ()]

# ans = solve (text, n, patterns)

# sys.stdout.write (' '.join (map (str, ans)) + '\n')

# python3
def build_trie(patterns):
    tree = {0: {}}
    cnt = 0
    for pattern in patterns:
        current_node = 0
        for char in pattern:
            if char in tree[current_node]:
                current_node = tree[current_node][char]
            else:
                cnt += 1
                tree[cnt] = {}
                tree[current_node][char] = cnt
                current_node = cnt
        # Mark the end of the pattern with a unique symbol
        tree[current_node]['$'] = cnt
    return tree

def solve(text, n, patterns):
    tree = build_trie(patterns)
    result = set()
    for i in range(len(text)):
        current_node = 0
        j = i
        while j < len(text):
            if text[j] in tree[current_node]:
                current_node = tree[current_node][text[j]]
                j += 1
                if '$' in tree[current_node]:
                    result.add(i)
                    break
            else:
                break
    return list(result)

if __name__ == "__main__":
    text = input().strip()
    n = int(input().strip())
    patterns = [input().strip() + '$' for _ in range(n)]
    ans = solve(text, n, patterns)
    print(' '.join(map(str, sorted(ans))))
