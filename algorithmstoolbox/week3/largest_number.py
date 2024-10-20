from functools import cmp_to_key

def compare(x, y):
    # Compare concatenated results
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def largest_number(numbers):
    numbers = list(map(str, numbers))
    # Sort numbers based on the custom comparator
    numbers.sort(key=cmp_to_key(compare))
    # Join sorted numbers into the largest number
    largest = ''.join(numbers)
    
    # Handle case where the result is multiple zeros
    return largest if largest[0] != '0' else '0'

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))
