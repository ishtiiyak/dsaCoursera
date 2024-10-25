# python3
import sys


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    result = []
    # Implement this function yourself
    strs = [text]
    s = text
    for i in range(0, len(text)-1):
        s = s[-1] + s[0:-1]
        strs.append(s)
    strs.sort()
    l = len(text)
    for i in strs:
        index = i.index('$') + 1
        result.append(l-index)
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
