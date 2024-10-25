import sys

def reach(adj, s):
    # Function to check if nodes are reachable
    visited = [0] * len(adj)
    def explore(v):
        visited[v] = 1
        for n in adj[v]:
            if visited[n] == 0:
                explore(n)
    explore(s)
    return visited

def shortest_paths(adj, cost, s, distance, reachable, shortest):
    # Set reachability of all nodes
    reach_ = reach(adj, s)
    for i in range(len(reachable)):
        reachable[i] = reach_[i]

    # Initialize distances and previous node tracking
    distance[s] = 0
    prev = [-1] * len(adj)

    # Bellman-Ford algorithm to update distances
    for i in range(len(adj)):
        updated = False
        for u in range(len(adj)):
            for index, v in enumerate(adj[u]):
                if distance[u] != 10**19 and distance[v] > distance[u] + cost[u][index]:
                    distance[v] = distance[u] + cost[u][index]
                    prev[v] = u
                    updated = True
                    # On last iteration, mark nodes involved in a negative cycle
                    if i == len(adj) - 1:
                        reach_cycle = reach(adj, v)
                        for j in range(len(shortest)):
                            if reach_cycle[j] == 1:
                                shortest[j] = 0
        if not updated:
            break  # No more updates needed

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
    s = data[0] - 1

    # Initialize distance, reachable, and shortest arrays
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n

    # Run shortest paths algorithm
    shortest_paths(adj, cost, s, distance, reachable, shortest)

    # Output results
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
