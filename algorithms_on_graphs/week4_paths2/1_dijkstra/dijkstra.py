import sys
import heapq

def distance(adj, cost, s, t):
    # Initialize distances with a large value
    inf = float('inf')
    dist = [inf] * len(adj)
    dist[s] = 0
    # Priority queue to keep track of minimum distance nodes
    priority_queue = [(0, s)]  # (distance, node)

    while priority_queue:
        d, u = heapq.heappop(priority_queue)
        
        # If the extracted node has a distance greater than the recorded distance, skip it
        if d > dist[u]:
            continue

        # Explore neighbors
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                heapq.heappush(priority_queue, (dist[v], v))

    # Return -1 if target is unreachable, otherwise return shortest distance
    return -1 if dist[t] == inf else dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
