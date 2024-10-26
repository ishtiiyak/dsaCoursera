class DeBruijnGraph:
    def __init__(self, k, t):
        self.k = k
        self.t = t
        self.v = 0
        self.edges = []
        self.edge_set = set()
        self.vertices = []
        self.prefix_map = {}
        self.vertex_map = {}
        self.adj_list = []

    def add_read(self, read):
        for i in range(len(read) - self.k + 1):
            kmer = read[i:i + self.k]
            if kmer not in self.edge_set:
                self.edge_set.add(kmer)
                self.edges.append(kmer)

    def build_de_bruijn(self):
        for edge in self.edges:
            pre = edge[:-1]
            suf = edge[1:]

            if pre not in self.vertex_map:
                self.vertices.append(pre)
                self.vertex_map[pre] = self.v
                self.v += 1

            if suf not in self.vertex_map:
                self.vertices.append(suf)
                self.vertex_map[suf] = self.v
                self.v += 1

        self.adj_list = [[] for _ in range(self.v)]

        for edge in self.edges:
            pre = edge[:-1]
            suf = edge[1:]
            from_vertex_index = self.vertex_map[pre]
            to_vertex_index = self.vertex_map[suf]
            self.adj_list[from_vertex_index].append(to_vertex_index)

    def count_bubbles(self):
        count = 0
        for i in range(len(self.adj_list)):
            if len(self.adj_list[i]) >= 2:
                count += self.count_bubbles_from_source(i, self.t)
        return count

    def get_non_overlapping_paths(self, path, visited, all_paths, all_sets, l):
        if len(path) == l:
            all_paths.append(list(path))
            all_sets.append(set(visited))
            return

        s = path[-1]

        if len(self.adj_list[s]) == 0:
            all_paths.append(list(path))
            all_sets.append(set(visited))
            return

        for v in self.adj_list[s]:
            if v not in visited:
                visited.add(v)
                path.append(v)
                self.get_non_overlapping_paths(path, visited, all_paths, all_sets, l)
                path.pop()
                visited.remove(v)

    def get_path_string(self, left_path, right_path, merge):
        ret = ','.join(map(str, left_path[:left_path.index(merge) + 1])) + ";"
        ret += ','.join(map(str, right_path[:right_path.index(merge) + 1]))
        return ret

    def count_bubbles_from_left_right_paths(self, left_set, right_set, left_paths, right_paths):
        merge_paths = set()
        for i, s in enumerate(left_set):
            for p in right_paths:
                for v in p:
                    if v in s:
                        path_string = self.get_path_string(left_paths[i], p, v)
                        merge_paths.add(path_string)
                        break
        return len(merge_paths)

    def count_bubbles_from_source(self, s, t):
        count = 0
        n_path = len(self.adj_list[s])
        for i in range(n_path - 1):
            for j in range(i + 1, n_path):
                left_paths, right_paths = [], []
                left_set, right_set = [], []
                
                path, visited = [self.adj_list[s][i]], {self.adj_list[s][i]}
                self.get_non_overlapping_paths(path, visited, left_paths, left_set, t)
                
                path, visited = [self.adj_list[s][j]], {self.adj_list[s][j]}
                self.get_non_overlapping_paths(path, visited, right_paths, right_set, t)
                
                count += self.count_bubbles_from_left_right_paths(left_set, right_set, left_paths, right_paths)
        
        return count


if __name__ == "__main__":
    k = int(input("Enter k: "))
    t = int(input("Enter t: "))
    graph = DeBruijnGraph(k, t)
    
    print("Enter reads (type 'END' to stop):")
    while True:
        read = input()
        if read == "END":
            break
        graph.add_read(read)
    
    graph.build_de_bruijn()
    print("Number of bubbles:", graph.count_bubbles())
