# 1. Run DFS
# 2. Return vertices in reverse Post-order


class DFS:
    def __init__(self, graph):
        self.marked = {}
        self.reverse_post_stack = []

        for v in graph.vertices():
            if not self.marked[v]:
                self._dfs(graph, v)

    def _dfs(self, graph, v):
        self.marked[v] = True

        for u in graph.get_edges(v):
            if not self.marked[u]:
                self._dfs(graph, u)

        self.reverse_post_stack.append(v)

    def reverse_post(self):
        while self.reverse_post_stack:
            yield self.reverse_post_stack.pop()