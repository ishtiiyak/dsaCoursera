def majority_element_optimized(elements):
    candidate = None
    count = 0
    
    # Phase 1: Find a candidate
    for element in elements:
        if count == 0:
            candidate = element
        count += (1 if element == candidate else -1)
    
    # Phase 2: Verify the candidate
    if elements.count(candidate) > len(elements) // 2:
        return 1
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_optimized(input_elements))
