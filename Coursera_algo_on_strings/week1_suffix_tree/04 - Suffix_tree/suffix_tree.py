def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
    tree = {0: {}}  # root node
    node_count = 0

    # Construct suffix tree
    for i in range(len(text)):
        current_node = 0
        for j in range(i, len(text)):
            current_char = text[j]
            if current_char in tree[current_node]:
                current_node = tree[current_node][current_char]
            else:
                node_count += 1
                tree[current_node][current_char] = node_count
                tree[node_count] = {}
                current_node = node_count

    # Collect edge labels
    def collect_labels(node, current_label):
        for char, child_node in tree[node].items():
            new_label = current_label + char
            result.append(new_label)
            collect_labels(child_node, new_label)

    # Initiate label collection starting from the root node
    collect_labels(0, "")
    return result


if __name__ == '__main__':
    text = input().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
