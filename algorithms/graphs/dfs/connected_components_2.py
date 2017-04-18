# Vertices v and u are connected if there is a path between them.
# Goal: Pre-process graph to queries of the form is v connected tp u in CONSTANT time.
#
# The relation 'is connected to' is an equivalence relation:
# - Reflexive: v is connected to v
# - Symmetric: if v is connected to u, then u is connected to v
# - Transitive: if v is connected to u and u is connected to x then v is connected to x
#
# Vertices with the same CC ids are CONNECTED
# Use DFS


class CC:
    def __init__(self, graph):
        """Find Connected Components in graph"""
        self.marked = {}
        self.cc = {}
        self.count = 0

        for v in graph.vertices():
            if not self.marked[v]:
                self._dfs(graph, v)
                self.count += 1

    def connected(self, v, u):
        """Are v and u connected"""
        return self.id(v) == self.id(u)

    def count(self):
        """number of connected components"""
        return self.count

    def id(self, v):
        """component identifier for v"""
        return self.cc[v]

    def _dfs(self, graph, v):
        self.marked[v] = True

        self.cc[v] = self.count

        for u in graph.get_edges(v):
            if not self.marked[u]:
                self._dfs(graph, u)
