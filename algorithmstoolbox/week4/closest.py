from collections import namedtuple
from itertools import combinations
from math import sqrt, inf

Point = namedtuple('Point', 'x y')

def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

def closest_pair(points):
    if len(points) <= 3:
        return minimum_distance_squared_naive(points)
    
    mid = len(points) // 2
    midpoint = points[mid]
    
    left_points = points[:mid]
    right_points = points[mid:]
    
    # Recursively find the smallest distance in both halves
    min_distance_squared = min(closest_pair(left_points), closest_pair(right_points))
    
    # Check for points in the strip within the minimum distance found
    strip = [p for p in points if (p.x - midpoint.x) ** 2 < min_distance_squared]
    
    # Check distances in the strip
    min_distance_squared = min(min_distance_squared, minimum_distance_squared_naive(strip))
    
    return min_distance_squared

def minimum_distance_squared_naive(points):
    min_distance_squared = inf

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared, distance_squared(p, q))

    return min_distance_squared

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    # Sort points by x-coordinate
    input_points.sort(key=lambda point: point.x)
    
    min_dist_squared = closest_pair(input_points)
    print("{0:.9f}".format(sqrt(min_dist_squared)))
