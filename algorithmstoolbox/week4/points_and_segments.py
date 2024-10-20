def points_cover_optimized(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)
    events = []

    # Create events for segment starts and ends
    for start in starts:
        events.append((start, 1))  # +1 for segment start
    for end in ends:
        events.append((end + 1, -1))  # -1 for segment end (end + 1 for exclusive)

    # Sort the events
    events.sort()

    # Add points to events with an index
    for index, point in enumerate(points):
        events.append((point, 0, index))  # 0 for point

    # Sort events again
    events.sort()

    active_segments = 0

    # Process events
    for event in events:
        if len(event) == 2:  # Segment start or end
            if event[1] == 1:  # Start of segment
                active_segments += 1
            else:  # End of segment
                active_segments -= 1
        else:  # Point event
            count[event[2]] = active_segments

    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_optimized(input_starts, input_ends, input_points)
    print(*output_count)
