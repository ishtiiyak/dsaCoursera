class TrieNode:
    def __init__(self):
        self.children = {}

def build_trie(patterns):
    trie = [TrieNode()]
    for pattern in patterns:
        current_node = 0
        for char in pattern:
            if char in trie[current_node].children:
                current_node = trie[current_node].children[char]
            else:
                new_node = len(trie)
                trie[current_node].children[char] = new_node
                trie.append(TrieNode())
                current_node = new_node
    return trie

def main():
    n = int(input())
    patterns = [input().strip() for _ in range(n)]

    trie = build_trie(patterns)

    for i, node in enumerate(trie):
        for char, child_node in node.children.items():
            print(f"{i}->{child_node}:{char}")

if __name__ == "__main__":
    main()
