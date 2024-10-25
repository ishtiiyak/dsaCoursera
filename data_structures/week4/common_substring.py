# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def solve(s, t):
    ans = Answer(0, 0, 0)
    len_s, len_t = len(s), len(t)
    dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]
    
    for i in range(1, len_s + 1):
        for j in range(1, len_t + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > ans.len:
                    ans = Answer(i - dp[i][j], j - dp[i][j], dp[i][j])
    return ans

for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)
