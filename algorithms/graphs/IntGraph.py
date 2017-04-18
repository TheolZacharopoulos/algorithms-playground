class Graph:
    def __init__(self, num):
        self._adjacency_map = {}
        for i in range(1, num + 1):
            self._adjacency_map[i] = []

    def connect(self, v, u):
        pass

    def vertices(self):
        return self._adjacency_map.keys()

    def get_edges(self, v):
        return self._adjacency_map[v]

    def adj(self, v):
        for u in self._adjacency_map[v]:
            yield u


class BiGraph(Graph):
    def connect(self, v, u):
        # since it is undirected
        self._adjacency_map[v].append(u)
        self._adjacency_map[u].append(v)


class DirectedGraph(Graph):
    def connect(self, v, u):
        # since it is directed
        self._adjacency_map[v].append(u)
