from collections import defaultdict, deque

class Vertex:
    def __init__(self, vertex_num, string, out_edges=None, in_edges=None):
        self.vertex_num = vertex_num
        self.string = string
        self.out_edges = out_edges if out_edges else []
        self.in_edges = in_edges if in_edges else []
        self.edge_list = []
        self.removed = False
        self.found = False
        self.visited = False
        self.temp = None  # Used in bubble handling for tracking tree nodes

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.used = False  # Tracks usage for Eulerian cycle

# Global variables
count_map = defaultdict(int)
k = 20  # Size of k-mer


def create_de_bruijn_graph(reads):
    id_map = {}
    out_edges_map = defaultdict(list)
    in_edges_map = defaultdict(list)
    unique_kmers = set()
    id_counter = 0

    for read in reads:
        for j in range(len(read) - k + 1):
            k_mer = read[j:j + k]
            a = k_mer[:-1]
            b = k_mer[1:]

            if k_mer in unique_kmers:
                count_map[k_mer] += 1
                continue

            unique_kmers.add(k_mer)
            count_map[k_mer] = 1

            if a not in id_map:
                id_map[a] = id_counter
                id_counter += 1
            if b not in id_map:
                id_map[b] = id_counter
                id_counter += 1

            if is_overlap(a, b):
                out_edges_map[a].append(id_map[b])
                in_edges_map[b].append(id_map[a])

    graph = [Vertex(i, str_val) for str_val, i in id_map.items()]

    for key, idx in id_map.items():
        graph[idx].out_edges = out_edges_map[key]
        graph[idx].in_edges = in_edges_map[key]

    return graph


def is_overlap(a, b):
    return a[1:] == b[:-1]


def tip_removal(graph):
    count = 0
    for vertex in graph:
        if vertex.removed:
            continue
        if not vertex.out_edges:
            count += in_explore(graph, vertex.vertex_num)
        elif not vertex.in_edges:
            count += out_explore(graph, vertex.vertex_num)
    return count


def in_explore(graph, vertex_idx):
    count = 0
    while graph[vertex_idx].out_edges and len(graph[vertex_idx].in_edges) == 1:
        graph[vertex_idx].removed = True
        count += 1
        prev_vertex = graph[vertex_idx].in_edges.pop()
        graph[prev_vertex].out_edges.remove(vertex_idx)
        vertex_idx = prev_vertex
    return count


def out_explore(graph, vertex_idx):
    count = 0
    while graph[vertex_idx].in_edges and len(graph[vertex_idx].out_edges) == 1:
        graph[vertex_idx].removed = True
        count += 1
        next_vertex = graph[vertex_idx].out_edges.pop()
        graph[next_vertex].in_edges.remove(vertex_idx)
        vertex_idx = next_vertex
    return count


def make_edges(graph):
    edges = []
    for vertex in graph:
        if vertex.removed:
            continue
        for adj in vertex.out_edges:
            edge = Edge(vertex.vertex_num, adj)
            vertex.edge_list.append(len(edges))
            edges.append(edge)
    return edges


def eulerian_cycle(graph, edges):
    max_genome = ""
    for vertex in graph:
        if not vertex.removed and not vertex.visited:
            cycle = []
            eulerian_explore(graph, edges, vertex.vertex_num, cycle)
            genome = reconstruct_genome(graph, cycle)
            if len(genome) > len(max_genome):
                max_genome = genome
    return max_genome


def eulerian_explore(graph, edges, vertex_idx, cycle):
    graph[vertex_idx].visited = True
    for edge_idx in graph[vertex_idx].edge_list:
        edge = edges[edge_idx]
        if not edge.used:
            edge.used = True
            eulerian_explore(graph, edges, edge.end, cycle)
    cycle.append(vertex_idx)


def reconstruct_genome(graph, cycle):
    genome = graph[cycle[-1]].string
    for vertex_idx in reversed(cycle[:-1]):
        genome += graph[vertex_idx].string[-1]
    return genome


def main():
    reads = ["<your genome read strings here>"]
    graph = create_de_bruijn_graph(reads)
    tip_removal(graph)
    edges = make_edges(graph)
    genome = eulerian_cycle(graph, edges)
    print("Reconstructed genome:", genome[:5400])


if __name__ == "__main__":
    main()
