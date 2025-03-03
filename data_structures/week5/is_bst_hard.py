class Node:
    def __init__(self, key=0, left=-1, right=-1):
        self.key = key
        self.left = left
        self.right = right

def inorder_traversal(tree, root, result):
    if root == -1:
        return
    inorder_traversal(tree, tree[root].left, result)
    result.append(tree[root].key)  # Append the key, not the index
    inorder_traversal(tree, tree[root].right, result)

def in_order(tree):
    result = []
    inorder_traversal(tree, 0, result)  # Start with the root index 0
    return result

def is_binary_search_tree(tree):
    if len(tree) > 1:
        v = in_order(tree)

        for i in range(len(v) - 1):
            # Check if current key is greater than the next key
            if v[i + 1] < v[i]: 
                return False
            
            # Check if there are equal keys and left child points to the parent
            if v[i] == v[i + 1] and tree[v[i + 1]].left == i:
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
