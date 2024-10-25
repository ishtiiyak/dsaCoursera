# python3
import sys


def BWT(text):
    strs = [text]
    s = text
    for i in range(0, len(text)-1):
        s = s[-1] + s[0:-1]
        strs.append(s)
    strs.sort()
    bwt = ""
    for i in strs:
        bwt += i[-1]
    return bwt


if __name__ == '__main__':
    # text = sys.stdin.readline().strip()
    text = input().strip()
    print(BWT(text))
