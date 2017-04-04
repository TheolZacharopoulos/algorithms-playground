class Graph:
    def __init__(self, adjacency_map=None):
        if adjacency_map is None:
            adjacency_map = {}

        self._adjacency_map = adjacency_map

    def vertices(self):
        return list(self._adjacency_map.keys())

    def edges(self):
        return self._generate_edges()

    def incident_edges(self, v):
        return self._adjacency_map[v]

    def add_vertex(self, vertex):
        if vertex not in self._adjacency_map:
            self._adjacency_map[vertex] = []

    def add_edge(self, source, destination):
        if source in self._adjacency_map:
            self._adjacency_map[source].append(destination)
        else:
            self._adjacency_map[source] = [destination]

    def _generate_edges(self):
        edges = []

        for vertex in self._adjacency_map:
            for neighbour in self._adjacency_map[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
