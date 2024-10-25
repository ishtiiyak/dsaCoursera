# python3
import sys


def PreprocessBWT(bwt):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
      * starts - for each character C in bwt, starts[C] is the first position 
          of this character in the sorted array of 
          all characters of the text.
      * occ_count_before - for each character C in bwt and each position P in bwt,
          occ_count_before[C][P] is the number of occurrences of character C in bwt
          from position 0 to position P inclusive.
    """
    # Implement this function yourself
    sorted_chars = [i for i in bwt]
    sorted_chars.sort()
    starts = {}
    for j, i in enumerate(sorted_chars):
        if i in starts:
            continue
        else:
            starts[i] = j
    counts = {}
    for i in starts:
        counts[i] = [0 for i in range(len(bwt))]
    for j, i in enumerate(bwt):
        for k in starts:
            if i == k:
                if j-1 >= 0:
                    counts[k][j] = counts[k][j - 1] + 1
                else:
                    counts[k][j] = 1
            else:
                if j-1 >= 0:
                    counts[k][j] = counts[k][j - 1]
                else:
                    counts[k][j] = 0
    print(starts, counts)
    return starts, counts


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and occ_counts_before.
    """
    # Implement this function yourself

    top = 0
    bottom = len(bwt) - 1
    while top <= bottom:
        if pattern != "":
            symbol = pattern[-1]
            pattern = pattern[0:-1]
            if symbol in bwt[top: bottom + 1]:
                if top-1 >= 0:
                    top = starts[symbol] + occ_counts_before[symbol][top]
                else:
                    top = starts[symbol]
                try:
                    bottom = starts[symbol] + \
                        occ_counts_before[symbol][bottom + 1] - 1
                except:
                    bottom = starts[symbol] + \
                        occ_counts_before[symbol][bottom] - 1
            else:
                return 0
        else:
            return bottom - top + 1

    return 0


if __name__ == '__main__':
    bwt = input().strip()
    pattern_count = int(input())
    patterns = list(input().split())
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).
    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(CountOccurrences(
            pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
