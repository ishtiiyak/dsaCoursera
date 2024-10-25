import sys

NA = -1

class Node:
    def __init__(self):
        self.next = [NA] * 4  # A, C, G, T
        self.patternEnd = False  # Marks end of a pattern in the trie

def letter_to_index(letter):
    """ Maps letters to indices: A -> 0, C -> 1, G -> 2, T -> 3 """
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[letter]

def build_trie(patterns):
    """ Builds a trie from the list of patterns """
    root = Node()
    trie = [root]
    for pattern in patterns:
        current_node = root
        for char in pattern:
            idx = letter_to_index(char)
            if current_node.next[idx] == NA:
                new_node = Node()
                trie.append(new_node)
                current_node.next[idx] = len(trie) - 1
            current_node = trie[current_node.next[idx]]
        current_node.patternEnd = True  # Mark end of the pattern
    return trie

def prefix_matching(text, trie, start_idx):
    """ Checks for a pattern match starting from start_idx in the text """
    current_node = trie[0]
    for i in range(start_idx, len(text)):
        char = text[i]
        idx = letter_to_index(char)
        if current_node.next[idx] != NA:
            current_node = trie[current_node.next[idx]]
            if current_node.patternEnd:
                return start_idx  # Match found starting at start_idx
        else:
            break
    return -1  # No match found starting at start_idx

def solve(text, n, patterns):
    """ Finds all starting positions in 'text' where a string in 'patterns' appears """
    result = []
    trie = build_trie(patterns)  # Build trie for all patterns
    for i in range(len(text)):
        match = prefix_matching(text, trie, i)
        if match != -1:
            result.append(match)
    return result

# Reading input and invoking solve
if __name__ == "__main__":
    input = sys.stdin.read().strip().splitlines()
    text = input[0]
    n = int(input[1])
    patterns = input[2:2 + n]
    
    ans = solve(text, n, patterns)
    sys.stdout.write(' '.join(map(str, ans)) + '\n')
