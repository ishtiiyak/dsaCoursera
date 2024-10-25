import sys, threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        heights = [0] * self.n

        def node_height(node):
            if heights[node] != 0:
                return heights[node]
            if self.parent[node] == -1:
                heights[node] = 1
            else:
                heights[node] = 1 + node_height(self.parent[node])
            return heights[node]

        max_height = 0
        for vertex in range(self.n):
            max_height = max(max_height, node_height(vertex))

        return max_height

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
