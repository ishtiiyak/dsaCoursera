from sys import stdin

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        self.key = key
        self.sum = sum
        self.left = left
        self.right = right
        self.parent = parent

def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
        v.right.parent = v

def smallRotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v

def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        smallRotation(v.parent)  # Zig-zig
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        smallRotation(v.parent)  # Zig-zig
        smallRotation(v)
    else:
        smallRotation(v)  # Zig-zag
        smallRotation(v)

def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            smallRotation(v)
            break
        bigRotation(v)
    return v

def find(root, key):
    v = root
    last = root
    next = None
    while v is not None:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)

def split(root, key):
    result, root = find(root, key)
    if result is None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right

# Global root of the splay tree
root = None

def insert(x):
    global root
    left, right = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)

def erase(x):
    global root
    left, right = split(root, x)
    middle, right = split(right, x + 1)
    # If middle is not None, it means we found the node to delete
    if middle is not None:
        root = merge(left, right)  # Reconstruct the tree without the middle

def search(x):
    global root
    result, root = find(root, x)
    return result is not None and result.key == x

def sum(fr, to):
    global root
    left, middle = split(root, fr)
    middle, right = split(middle, to + 1)
    ans = 0
    if middle is not None:
        ans = middle.sum  # Get the sum of the middle segment
    root = merge(merge(left, middle), right)  # Restore the tree
    return ans

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for _ in range(n):
    line = stdin.readline().strip().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
