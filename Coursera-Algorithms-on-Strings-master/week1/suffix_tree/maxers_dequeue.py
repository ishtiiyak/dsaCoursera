# python3
import sys

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.children = []

def build_suffix_tree(text):
    n = len(text)
    root = Node(None, None)
    
    for i in range(n):
        current_node = root
        j = i
        while j < n:
            found = False
            for child in current_node.children:
                if text[child.start] == text[j]:  # Match found
                    k = child.start
                    while k < child.end and j < n and text[k] == text[j]:
                        k += 1
                        j += 1
                    if k == child.end:
                        current_node = child
                    else:
                        # Split node
                        mid_node = Node(child.start, k)
                        mid_node.children.append(Node(j, n))  # New child for the remaining suffix
                        child.start = k
                        mid_node.children.append(child)
                        current_node.children.remove(child)
                        current_node.children.append(mid_node)
                    found = True
                    break
            if not found:
                current_node.children.append(Node(j, n))
                break
    return root

def collect_suffixes(node, text):
    suffixes = []
    stack = [(node, "")]
    while stack:
        node, path = stack.pop()
        if node.start is not None:
            path += text[node.start:node.end]
        if not node.children:
            suffixes.append(path)
        for child in node.children:
            stack.append((child, path))
    return suffixes

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    suffix_tree = build_suffix_tree(text)
    suffixes = collect_suffixes(suffix_tree, text)
    print("\n".join(suffixes))
