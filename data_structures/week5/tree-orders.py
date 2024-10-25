#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)    # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.right = [0 for _ in range(self.n)]
        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        self._inOrder(0)  # Start with the root node (index 0)
        return self.result

    def _inOrder(self, index):
        if index == -1:  # Base case: no node
            return
        self._inOrder(self.left[index])  # Traverse left subtree
        self.result.append(self.key[index])  # Visit node
        self._inOrder(self.right[index])  # Traverse right subtree

    def preOrder(self):
        self.result = []
        self._preOrder(0)  # Start with the root node (index 0)
        return self.result

    def _preOrder(self, index):
        if index == -1:  # Base case: no node
            return
        self.result.append(self.key[index])  # Visit node
        self._preOrder(self.left[index])  # Traverse left subtree
        self._preOrder(self.right[index])  # Traverse right subtree

    def postOrder(self):
        self.result = []
        self._postOrder(0)  # Start with the root node (index 0)
        return self.result

    def _postOrder(self, index):
        if index == -1:  # Base case: no node
            return
        self._postOrder(self.left[index])  # Traverse left subtree
        self._postOrder(self.right[index])  # Traverse right subtree
        self.result.append(self.key[index])  # Visit node

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
