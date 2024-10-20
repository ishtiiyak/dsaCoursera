from sys import stdin

def min_refills(distance, tank, stops):
    # Include the start point (0) and the destination
    stops = [0] + stops + [distance]
    num_refills = 0
    current_location = 0
    current_index = 0
    n = len(stops)

    while current_index < n - 1:  # while we haven't reached the destination
        last_refill = current_index
        
        # Move to the farthest stop reachable with the current fuel
        while (current_index < n - 1 and 
               stops[current_index + 1] - stops[last_refill] <= tank):
            current_index += 1
        
        # If no further stop can be reached, we need to refill
        if current_index == last_refill:
            return -1  # Cannot reach the next stop
        
        # If we haven't reached the last stop yet, increment refills
        if current_index < n - 1:
            num_refills += 1
            
    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
