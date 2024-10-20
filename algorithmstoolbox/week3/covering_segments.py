from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # Sort segments by their end points
    segments.sort(key=lambda s: s.end)
    
    points = []
    current_point = None
    
    for segment in segments:
        # If current_point is None or segment starts after current_point
        if current_point is None or segment.start > current_point:
            current_point = segment.end
            points.append(current_point)
    
    return points

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
