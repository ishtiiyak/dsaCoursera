# python3
import sys


def InverseBWT(bwt):
    # write your code here
    T = {}
    count = {}
    texts = []
    for j, i in enumerate(bwt):
        texts.append(i)
        try:
            count[i] += 1
        except:
            count[i] = 1
        T[j] = (i, count[i])
    texts.sort()
    inverse_T = {}
    inverse_count = {}
    for j, i in enumerate(texts):
        try:
            inverse_count[i] += 1
        except:
            inverse_count[i] = 1
        inverse_T[(i, inverse_count[i])] = j
    text = ""
    curr = (texts[0], 1)
    curr_index = inverse_T[curr]
    while len(text) < len(bwt):
        text += curr[0]
        curr = T[curr_index]
        curr_index = inverse_T[curr]

    return text[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
