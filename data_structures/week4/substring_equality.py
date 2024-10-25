# python3

import sys
import hashlib

class Solver:
    def __init__(self, s):
        self.s = s
        self.prefix_hashes = self._compute_prefix_hashes(s)
        self.base = 257
        self.mod = 10**9 + 7

    def _compute_prefix_hashes(self, s):
        prefix_hashes = [0] * (len(s) + 1)
        for i in range(len(s)):
            prefix_hashes[i + 1] = (prefix_hashes[i] * self.base + ord(s[i])) % self.mod
        return prefix_hashes

    def _get_substring_hash(self, start, length):
        hash_value = (self.prefix_hashes[start + length] -
                      self.prefix_hashes[start] * pow(self.base, length, self.mod)) % self.mod
        return hash_value

    def ask(self, a, b, l):
        return self._get_substring_hash(a, l) == self._get_substring_hash(b, l)

s = sys.stdin.readline().strip()
q = int(sys.stdin.readline())
solver = Solver(s)
for _ in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
