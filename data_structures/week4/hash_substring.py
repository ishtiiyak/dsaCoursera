# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # Using Rabin-Karp algorithm for efficient substring search
    p_len, t_len = len(pattern), len(text)
    p_hash = hash(pattern)
    current_hash = hash(text[:p_len])
    occurrences = []

    for i in range(t_len - p_len + 1):
        if current_hash == p_hash and text[i:i + p_len] == pattern:
            occurrences.append(i)
        if i < t_len - p_len:
            # Rolling hash update
            current_hash = hash(text[i + 1:i + 1 + p_len])

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
