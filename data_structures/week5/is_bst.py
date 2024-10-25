class Node:
    def __init__(self, key=0, left=-1, right=-1):
        self.key = key
        self.left = left
        self.right = right

def inorder_traversal(tree, root, result):
    if root == -1:
        return
    inorder_traversal(tree, tree[root].left, result)
    result.append(tree[root].key)
    inorder_traversal(tree, tree[root].right, result)

def in_order(tree):
    result = []
    inorder_traversal(tree, 0, result)  # Start with the root index 0
    return result

def is_binary_search_tree(tree):
    if len(tree) > 1:
        v = in_order(tree)
        for i in range(1, len(v)):
            if v[i] < v[i - 1]:
                return False
    return True

def main():
    nodes = int(input().strip())
    tree = []

    for _ in range(nodes):
        key, left, right = map(int, input().strip().split())
        tree.append(Node(key, left, right))

    if is_binary_search_tree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

if __name__ == "__main__":
    main()
