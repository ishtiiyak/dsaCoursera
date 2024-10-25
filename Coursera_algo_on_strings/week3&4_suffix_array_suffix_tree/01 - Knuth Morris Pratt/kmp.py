# python3
import sys


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    # Implement this function yourself
    text = pattern + '$' + text
    s = [0 for _ in range(len(text))]
    border = 0
    for i in range(1, len(text)):
        while border > 0 and text[i] != text[border]:
            border = s[border - 1]
        if text[i] == text[border]:
            border = border + 1
        else:
            border = 0
        s[i] = border
    l = len(pattern)
    for j, i in enumerate(s[l + 1:]):
        if i == l:
            result.append(j-l+1)
    return result


if __name__ == '__main__':
    pattern = input().strip()
    text = input().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
